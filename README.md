# Clothe Me

Clothe Me is a fictional store with database models designed specifically for
a talk that digs into customising SQL in Django.

## Get up and running:

You should already have postgres installed and your database created.

- Ensure python 3.4 is installed if you want to use Jupyter-Themes, otherwise 3.5
- `cp clotheme/clotheme/_secrets.py clotheme/clotheme/secrets.py` and edit

```
mkvirtualenv -p python34 customsql
pip install -r requirements.txt
```

If you want to run the presentation with reveal.js:

```
pip install --pre RISE
jupyter-nbextension install rise --py --sys-prefix
jupyter nbextension enable rise --py --sys-prefix
```

Create the models and launch the notebook:

```
cd clotheme
./manage.py migrate
./manage.py test  # make sure everything is working
./manage.py shell_plus --notebook  # start the notebook
```
