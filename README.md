# Minimal Flask CookieCutter

## Rationale

I've been making a lot of quick project recently and found myself to be
repeating a lot of initial setups.

So I've compiled all the things for myself to quickly bootstrap to my style.

It contains the minimal of configuration to achieve the complete settings from development settings to deployment.

## Features

- Minimal Flask + SQLAlchemy
- Configuration object setup
    - Read config/__init\__.py for the rationale
    - Some reasonable default configurations are set
- [Black] & flake8 based autolint with precommit hooks
- Heroku
- Requirements Pinning

Note that python3.8 is assumed.


[Black]: https://github.com/psf/black