import json
import pkg_resources
import random
import re
import string
import urllib.request


app_name = "{{cookiecutter.app_name}}"

# Generates Flask's `SECRET_KEY` configuration
# Use `SystemRandom` because `SECRET_KEY` should not be predicted
secret_key = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(32))

with open(f'../{app_name}/{app_name}/config/default.py', 'w') as f:
    f.write(f'SECRET_KEY = "{secret_key}"\n')


# Pin requirements
def get_recent_version(pkg_name):
    """Crawl pypi website to get the most recent version"""
    url = f'https://pypi.org/pypi/{pkg_name}/json'
    releases = json.loads(urllib.request.urlopen(url).read())['releases']
    return sorted(releases, key=pkg_resources.parse_version, reverse=True)[0]

def pin_requirements(requirement_filename):
    """Opens requirements file and pin them with `~=` operator"""
    with open(requirement_filename) as f:
        requirements_txt = f.read()

    pinned_requirements = []

    for row in requirements_txt.split('\n'):
        if not row or row.startswith('-'):
            # Pass up instructions and empty lines
            pinned_requirements.append(row)
            continue

        # this regex is not comprehensive and might need to be fixed
        # as we include more libraries in requirements.txt
        library_name = re.match(r'([\w-]+)(\[\w+\])?', row).group(1)  # remove options from row
        recent_version = get_recent_version(library_name.strip())
        pinned_requirements.append(f'{row} ~= {recent_version}')

    pinned_requirements_txt = '\n'.join(pinned_requirements)
    with open(requirement_filename, 'w+') as f:
        f.write(pinned_requirements_txt)

pin_requirements(fr'../{app_name}/requirements.txt')
pin_requirements(fr'../{app_name}/dev-requirements.txt')

print("Project setup is complete! Now use these commands to setup devlopment environment:")
print()
print(f"cd {app_name}")
print(f"mkvirtualenv -a $(pwd) -p $(pyenv which python) {app_name}")
print(f"workon {app_name}")
print("pip install -r dev-requirements.txt")
print("git init")
print("pre-commit install")
