from api.app import create_app

app = create_app()

print(app.config)