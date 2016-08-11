SECRET_KEY = 'PUT A SECRET STRING HERE'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'clotheme',
        'USER': 'clotheme',
        'PASSWORD': 'PUT YOUR DB PASSWORD HERE',
        'HOST': 'localhost',
        'PORT': '5432',
        'CONN_MAX_AGE': 300
    }
}
