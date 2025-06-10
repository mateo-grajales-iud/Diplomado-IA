import uuid
from datetime import datetime

from flask import Flask, g
from app.config import Config
from app.routes.main_routes import main_routes
from app.routes.api_routes import api_routes
from app.services import QueryServices
from app.services.StoreServices.QueryStorageCache import QueryStorageCache
from app.test_utils.DummySeeder import dummyRequest
from app.services.WorkerServices import Worker
from app.services.WriterServices import PromptWriterDefault
from app.services.AIServices import PromptSender
from dotenv import load_dotenv
import os

def create_app():
    app = Flask(__name__)
    loadEnv(app)
    app.config.from_object(Config)

    app.before_request(assign_request_id)

    app.register_blueprint(main_routes)
    app.register_blueprint(api_routes)
    
    setResultStorage(app)

    if os.environ.get('WERKZEUG_RUN_MAIN') == 'true':
        Worker.StartPendingWorker(app, PromptWriterDefault.writePrompt)
        Worker.StartPromptWorker(app, PromptSender.sendPrompt)
    return app

def assign_request_id():
    g.request_id = str(uuid.uuid4())

def setResultStorage(app):
    if app.config["RESULT_STORAGE"] == "CACHE":
        QueryServices.RESULT_STORAGE = QueryStorageCache()
    if app.config["SEED_DUMMY_DATA"] == "True":
        for i in range(10):
            QueryServices.RESULT_STORAGE.storeQuery({ "request" : dummyRequest(), "status": "PENDING", "status_time" : datetime.now().strftime("%Y-%m-%d %H:%M:%S")})

def loadEnv(app):
    load_dotenv()
    app.config['FLASK_ENV'] = os.getenv('FLASK_ENV')
    app.config['DEBUG'] = os.getenv('DEBUG')
    app.config['RESULT_STORAGE'] = os.getenv('RESULT_STORAGE')
    app.config['SEED_DUMMY_DATA'] = os.getenv('SEED_DUMMY_DATA')
    app.config['GEMINI_2_FLASH_API_KEY'] = os.getenv('GEMINI_2_FLASH_API_KEY')
