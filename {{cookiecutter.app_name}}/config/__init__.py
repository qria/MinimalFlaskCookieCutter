""":mod:`{{cookiecutter.app_name}}.config` --- Configuration Object
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module wraps around configuration loading logic, because:

1. we want to maintain same loading logic in flask and celery

1. celery config only accepts a single configuration object.

"""

import os

from .default import *  # noqa

# Overwrite flask's `ENV` configuration
# Note that flask's original default value for this is "production".
ENV = os.environ.get("FLASK_ENV", "development")

# Load environment dependent configuration
if ENV == "production":
    from .production import *  # noqa
elif ENV == "development":
    from .development import *  # noqa
elif ENV == "test":
    from .test import *  # noqa
else:
    raise Exception("Unsupported Environment.")

if ENV != "test":
    # Load local configuration
    try:
        from .local import *  # noqa
    except ImportError:
        pass
