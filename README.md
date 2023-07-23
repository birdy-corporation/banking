# Some commands

```bash
# Docker login via PAT
echo $DOCKER_PAT | docker login -u ribeiromauro --password-stdin

# Create the new docker image
docker build -t banking:latest .

# To update requirements via bazel
# and make sure that the venv is up-to-date
bazel run //:py_transitive_requirements.update && pip install -r requirements_lock.txt

```
