# {{cookiecutter.app_name}}

## Requirements

- python 3.8
- postgresql 10+

## Install

```bash
pip install -r dev-requirements.txt
pre-commit install  # To install pre commit check hooks
```

## Deployment

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

Push the button above to deploy to heroku. If your app is private, this button does not work and you'll need to set it up [manually]. You may erase app.json after deployment.

For manual setup you'll need to:

- Set the following environment variables in heroku settings

    - `FLASK_APP` to `{{cookiecutter.app_name}}/app.py`
    - `FLASK_ENV` to `production`
    - `SECRET_KEY` to random string

- Add following extensions

    - [heroku-postgres]
    - [logentries]
        - Note this free version only allows **1 week** of history

Enable [Heroku automatic deployment][heroku] to automatically deploy the master branch.

[manually]: https://dashboard.heroku.com/new-app?org=personal-apps
[heroku]: https://devcenter.heroku.com/articles/github-integration#automatic-deploys
[heroku-postgres]: https://elements.heroku.com/addons/heroku-postgresql
[logentries]: https://elements.heroku.com/addons/logentries