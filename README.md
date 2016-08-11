# Clothe Me

Clothe Me is a fictional store with database models designed specifically for
a talk that digs into customising SQL in Django.

## Get up and running:

You should already have postgres installed and your database created.

- Ensure python 3.4 is installed (some deps don't work with python 3.5)
- `cp clotheme/clotheme/_secrets.py clotheme/clotheme/secrets.py` and edit

```
mkvirtualenv -p python34 customsql
pip install -r requirements.txt
pip install --pre RISE
jt -t grade3 -T
jupyter-nbextension install rise --py --sys-prefix
jupyter nbextension enable rise --py --sys-prefix

cd clotheme
./manage.py migrate
./manage.py test  # make sure everything is working
./manage.py shell_plus --notebook  # start the notebook
```
