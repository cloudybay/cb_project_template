from dev import *


from database import GET_DATABASES
DATABASES = GET_DATABASES(DB_PARAMS)


class APP_SETTINGS(object):
    """
    This is an empty class is used to defined a self settings for current application.
    Check the example:
        http://svn.cb/__dev/examples/app_settings/__init__.py
    """
