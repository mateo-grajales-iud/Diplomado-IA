from app import create_app

app = create_app()

print("name: " + __name__)

if __name__ == "__main__":
    app.run(debug=True)