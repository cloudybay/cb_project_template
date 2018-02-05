import os
from .settings import *


def load_config(confile):
    _config_file = os.path.join(os.environ.get('CONF'), confile)
    _config = {}
    if os.path.exists(_config_file):
        try:
            execfile(_config_file, {}, _config)
        except NameError:
            with open(_config_file, 'r') as f:
                exec(f.read(), {}, _config)
    return _config


def extend_settings(settingsfile):
    _config = load_config(settingsfile)
    for key in _config.keys():
        exec("%s = _config['%s']" % (key, key))


extend_settings('django.settings')
