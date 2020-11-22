import os

SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URL"]

# MUST set this if this is a public repository!
if os.environ.get("SECRET_KEY"):
    SECRET_KEY = os.environ["SECRET_KEY"]

if os.environ.get("SENTRY_API_KEY"):
    SENTRY_API_KEY = os.environ["SENTRY_API_KEY"]
