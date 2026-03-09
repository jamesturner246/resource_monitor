# TLDR Setup

At any point once the server is started, see a summary of resource allocations by
pointing a web browser at `http://127.0.0.1:8000/`.

```bash
# Set up a django env.
python -m venv .venv
. .venv/bin/activate
pip install -U pip
pip install django==5.2

# Set up the local SQLite DB.
python manage.py makemigrations
python manage.py migrate

# Start a local test server.
python manage.py runserver

# Add some resources.
curl -k -X POST "http://127.0.0.1:8000/add_resource/" -d "name=resource_one"
curl -k -X POST "http://127.0.0.1:8000/add_resource/" -d "name=resource_two"

# Take control.
curl -k -X POST "http://127.0.0.1:8000/take_resource/" -d "name=resource_one"
curl -k -X POST "http://127.0.0.1:8000/take_resource/" -d "name=resource_two"

# Release one.
curl -k -X POST "http://127.0.0.1:8000/release_resource/" -d "name=resource_one"
```
