""":mod:`{{cookiecutter.app_name}}.extensions`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Extensions are created here with Application Factory Pattern to avoid
circular definition.

See: https://flask.palletsprojects.com/en/1.1.x/patterns/appfactories/#factories-extensions  # noqa

"""

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

migrate: Migrate = Migrate()
db: SQLAlchemy = SQLAlchemy()
