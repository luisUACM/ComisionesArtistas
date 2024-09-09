from flask import Flask

def init_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True

    with app.app_context():
        #  =========================================================
        #   
        #   Aquí importar todos los archivos que usen el objeto app
        #   
        #  =========================================================
        from .routes import routes
        return app