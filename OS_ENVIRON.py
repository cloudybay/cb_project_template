import os
import sys


# set project home path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)
os.environ["BASE_DIR"] = BASE_DIR


# env for django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "etc.settings")

# path for project config
from etc.settings import CONF_DIR
_CONF = os.path.join(BASE_DIR, 'etc', 'conf', CONF_DIR)
os.environ.setdefault("CONF", _CONF)

# env for cb log
_LOG_DIR = os.path.join(BASE_DIR, 'logfiles')
os.environ.setdefault('LOG_CONFIG', os.path.join(_CONF, 'log.conf'))
os.environ.setdefault('LOG_DIR', _LOG_DIR)
os.environ.setdefault('COLLECTIVE_DIR', _LOG_DIR)

##
# env for cb util
##
#os.environ.setdefault('IMPORT', os.path.join(BASE_DIR, 'data/import'))
#os.environ.setdefault('ARCHIVE', os.path.join(BASE_DIR, 'data/archive'))
#os.environ.setdefault('SIGNAL', os.path.join(BASE_DIR, 'data/signal'))
#os.environ.setdefault('DISPATCH', os.path.join(BASE_DIR, 'data/dispatch'))
