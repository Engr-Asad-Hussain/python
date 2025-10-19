from app import create_app
from config import Config, Dev, Prod

config = Prod() if Config.APP_DEBUG is True else Dev()
app, celery = create_app(config)


if __name__ == "__main__":
    app.run(host=Config.APP_HOST, port=Config.APP_PORT, debug=Config.APP_DEBUG)
