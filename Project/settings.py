from pathlib import Path
from decouple import config
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2m&e=73x6p_a@3rz8$&ohdp8*ox+d#9ek1^$a*5ddf@ee6e-k%'
# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = False

# DEBUG = True

ALLOWED_HOSTS = ['www.silvestrecode.shop', 'silvestrecode.shop', ]

# ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'OnePage',  # Seu app principal
    'widget_tweaks',  # Adicional para customização de formulários no template
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'Project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Ou inclua caminhos adicionais se precisar
        'APP_DIRS': True,  # Isso deve ser True para procurar templates dentro dos apps
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Project.wsgi.application'

ASGI_APPLICATION = 'meuprojeto.asgi.application'


STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DATABASE_NAME'),
        'USER': config('DATABASE_USER'),
        'PASSWORD': config('DATABASE_PASSWORD'),
        'HOST': config('DATABASE_HOST'),
        'PORT': config('DATABASE_PORT'),
    }
}


# # DATABASES configuration for local SQLite database
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',  # O arquivo de banco de dados será armazenado aqui
#     }
#  }

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


STATIC_URL = '/static/'

STATIC_ROOT = '/var/www/silvestrecode/Meusite/static'

MEDIA_URL = '/media/'

MEDIA_ROOT = '/var/www/silvestrecode/Meusite/media'


# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'static'),  # Adicione aqui o diretório que contém seus arquivos estáticos
# ]

# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # Para coletar arquivos estáticos


# STATIC_URL = '/static/'

# # Adicionando a configuração para os arquivos estáticos
# STATICFILES_DIRS = [
#     BASE_DIR / 'static',  # Aponta para a pasta static na raiz do projeto
# ]

# STATIC_ROOT = BASE_DIR / 'staticfiles'

# MEDIA_URL = '/media/'  # URL base para servir arquivos de mídia
# MEDIA_ROOT = BASE_DIR / 'media'  # Diretório onde os arquivos de mídia serão salvos


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

