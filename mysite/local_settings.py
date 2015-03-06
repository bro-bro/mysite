import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DEBUG = True

TEMPLATE_DEBUG = True
TEMPLATE_DIRS = {
    '/home/molkopeace//faceface/bin/mysite/templates'
}



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static/")
SOCIAL_AUTH_RAISE_EXCEPTIONS = False

SOCIAL_AUTH_FACEBOOK_KEY = '1549363238682841'
SOCIAL_AUTH_FACEBOOK_SECRET = 'da06ad7d8c50b31d8d60d590867333d7'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "/home/molkopeace/faceface/bin/mysite/static"),
    )

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
TEMPLATE_CONTEXT_PROCESSORS = (
	'django.contrib.auth.context_processors.auth',
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',

)


