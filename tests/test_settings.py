SECRET_KEY = 'fake-key'
INSTALLED_APPS = [
    "tests",
    "mindwiki",
]
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
    },
}
