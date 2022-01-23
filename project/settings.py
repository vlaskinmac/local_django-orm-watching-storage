import os

import dj_database_url

from environs import Env
from dotenv import load_dotenv


load_dotenv()


env = Env()
env.read_env()

# DATABASES = os.getenv("DATABASES")

DATABASES = env.dj_db_url("DATABASES")
DATABASES['default'] = dj_database_url.config(
    default=f'postgres://{os.getenv("USER")}:'
            f'{os.getenv("PASSWORD")}@{os.getenv("HOST")}:{os.getenv("PORT")}/{os.getenv("NAME")}'
)


DEBUG = env.bool('DEBUG')

INSTALLED_APPS = ['datacenter']

SECRET_KEY = env("SECRET_KEY")

ROOT_URLCONF = "project.urls"

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")


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


