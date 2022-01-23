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


# TODO .env файл выглядит так:

# DATABASES = {'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'HOST': 'checkpoint.devman.org',
#         'PORT': '5434',
#         'NAME': 'checkpoint',
#         'USER': 'guard',
#         'PASSWORD': 'osim5',
#     }
# }
#
# NAME= 'checkpoint'
# USER= 'guard'
# PASSWORD='osim5'
# HOST='checkpoint.devman.org'
# PORT='5434'
#
# DEBUG=True
#
# ALLOWED_HOSTS = [
# 'localhost:8000',
# '0.0.0.0:8000',
# ]
#
# SECRET_KEY=b'\x00\xe4\xf0\x92OhW_q\xcaE$\xd31\xe6\x92\nd[\xf1\x8e\xb2\xcd\xc2T\xd6\xb7\xd3ns\x17l'


