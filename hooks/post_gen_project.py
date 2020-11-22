import random
import string


# Generates Flask's `SECRET_KEY` configuration
# Use `SystemRandom` because `SECRET_KEY` should not be predicted
secret_key = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(32))

with open('../{{cookiecutter.app_name}}/{{cookiecutter.app_name}}/config/default.py', 'w') as f:
    f.write(f'SECRET_KEY = "{secret_key}"\n')
