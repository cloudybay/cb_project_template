# -*- coding: utf-8 -*-

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases


DATABASES = {
}


"""
DB_YEAR_FROM = 2014
DB_YEAR_TO = 2025
DB_PATTERN = 'wra_%d'

for year in range(DB_YEAR_FROM, DB_YEAR_TO):
    DATABASES.update({
        "%d"%year: {
            "ENGINE": "django.db.backends.mysql",
            "NAME": DB_PATTERN % year,
            "HOST": "",
            "USER": "",
            "PASSWORD": "",
            "PORT": "",
        }
    })
"""


def GET_DATABASES(params, databases=None):
    if databases is None:
        databases = DATABASES

    for k in databases.keys():
        v = databases[k]
        if isinstance(v, dict):
            GET_DATABASES(params, v)
        elif k in params:
            databases[k] = params[k]

    return databases
