from src import init_app

#El objeto app contiene muchas funciones utiles para usar el framework de Flask
app = init_app()

if __name__ == "__main__":
    app.run(host='0.0.0.0')