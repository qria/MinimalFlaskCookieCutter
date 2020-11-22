DEBUG = True

# jijna templates are cached by default
TEMPLATES_AUTO_RELOAD = True

# undefined jinja variables silently fails by default
# we don't want that behaviour, at least in development
JINJA_STRICT_UNDEFINED = True

SQLALCHEMY_DATABASE_URI = "postgres://localhost:5432/{{cookiecutter.app_name}}"
