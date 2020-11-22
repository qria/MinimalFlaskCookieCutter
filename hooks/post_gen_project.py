import random
import string


app_name = "{{cookiecutter.app_name}}"

# Generates Flask's `SECRET_KEY` configuration
# Use `SystemRandom` because `SECRET_KEY` should not be predicted
secret_key = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(32))

with open(f'../{{app_name}}/{{app_name}}/config/default.py', 'w') as f:
    f.write(f'SECRET_KEY = "{secret_key}"\n')


print("Project setup is complete! Now use these commands to setup devlopment environment:")
print()
print(f"mkvirtualenv -a $(pwd) -p $(pyenv which python) {{app_name}}")
print(f"workon {{app_name}}")
print("pip install -r dev-requirements.txt")
print("git init")
print("pre-commit install")
