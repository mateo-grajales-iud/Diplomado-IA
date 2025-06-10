from ...config import Config

class FormFields:

    def __init__(self):
        self.title = "SmartEats: Usando GenAI para mejorar la alimentación"
        self.role = "Eres un nutricionista experto en dietas y amplios conocimientos de cocina nacional e internacional"
        self.show_role = Config.DEBUG_ROLE_FIELD