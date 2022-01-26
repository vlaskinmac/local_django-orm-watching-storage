import os

from environs import Env

env = Env()

env.read_env()

DATABASES = {'default': env.dj_db_url('DATABASE_URL')}

DEBUG = env.bool('DEBUG', default=False)

INSTALLED_APPS = ['datacenter']

SECRET_KEY = env('SECRET_KEY')

ROOT_URLCONF = 'project.urls'

ALLOWED_HOSTS = env('ALLOWED_HOSTS')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]

USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True