#!/usr/bin/env python
import os
import sys


# set project home path
HOME = os.path.dirname(os.path.abspath(__file__))
if HOME not in sys.path:
    sys.path.append(HOME)
os.environ.setdefault("HOME", HOME)


# env for django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{ project_name }}.settings")

# path for project config
_CONF = os.path.join(HOME, 'conf')
os.environ.setdefault("CONF", _CONF)

# env for cb log
_LOG_DIR = os.path.join(HOME, 'logfiles')
os.environ.setdefault('LOG_CONFIG', os.path.join(_CONF, 'log.conf'))
os.environ.setdefault('LOG_DIR', _LOG_DIR)
os.environ.setdefault('COLLECTIVE_DIR', _LOG_DIR)

##
# env for cb util
##
#os.environ.setdefault('IMPORT', os.path.join(HOME, 'data/import'))
#os.environ.setdefault('ARCHIVE', os.path.join(HOME, 'data/archive'))
#os.environ.setdefault('SIGNAL', os.path.join(HOME, 'data/signal'))
#os.environ.setdefault('DISPATCH', os.path.join(HOME, 'data/dispatch'))

