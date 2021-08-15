from .environment import env

SECRET_KEY = env('SECRET_KEY')

ALLOWED_HOSTS = list(map(str.strip, env("SITE_DOMAIN").split(',')))

DATABASES = {
    "default": {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env("POSTGRES_DB"),
        'USER': env("POSTGRES_USER"),
        'PASSWORD': env("POSTGRES_PASSWORD"),
        'HOST' : 'localhost',
        'PORT' : '5432',
    }
}

