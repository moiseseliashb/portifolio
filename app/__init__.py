
import os

from dotenv import load_dotenv
from flask import Flask


def create_app():
    load_dotenv()

    app = Flask(
        __name__,
        static_folder="../public/static",
        static_url_path="/static",
    )

    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
    app.config["DEBUG"] = (
        os.getenv("FLASK_DEBUG", "0").lower()
        in ("1", "true", "yes")
    )

    if not app.config["SECRET_KEY"]:
        raise RuntimeError(
            "A variável SECRET_KEY não está configurada."
        )

    from app.routes import main
    app.register_blueprint(main)

    return app
