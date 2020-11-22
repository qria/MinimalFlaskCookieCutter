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

Enable [Heroku automatic deployment][heroku] to automatically deploy the master branch.


[heroku]: https://devcenter.heroku.com/articles/github-integration#automatic-deploys