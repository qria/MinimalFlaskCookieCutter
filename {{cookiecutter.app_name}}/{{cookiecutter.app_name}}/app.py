import os

from flask import Flask, render_template
from jinja2 import StrictUndefined
from sentry_sdk import init as sentry_init
from sentry_sdk.integrations.flask import FlaskIntegration

from .extensions import db, migrate


app = Flask(__name__)
app.config.from_object("{{cookiecutter.app_name}}.config")

if app.config.get("JINJA_STRICT_UNDEFINED"):
    # Detect undefined jinja variables
    app.jinja_env.undefined = StrictUndefined

# Initialize Extensions
db.init_app(app)
migrate.init_app(app, db)

SENTRY_API_KEY = os.environ.get("SENTRY_API_KEY")
if SENTRY_API_KEY:
    sentry_init(SENTRY_API_KEY, integrations=[FlaskIntegration()])


@app.route("/")
def index() -> str:
    return render_template("index.html")
