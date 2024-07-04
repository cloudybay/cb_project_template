import os
import logging
import logging.config
import json
import traceback
import pytz
from datetime import datetime


class JsonFormatter(logging.Formatter):
    def __init__(self, fmt=None, datefmt=None, tz=None):
        super().__init__(fmt, datefmt)
        self.tz = tz

    def format(self, record):
        log_record = {
            'level': record.levelname,
            'time': self.formatTime(record),
            'lineno': record.lineno,
            'path': record.pathname,
            'process': record.process,
            'message': record.getMessage(),
        }
        if record.exc_info:
            log_record['exception'] = ''.join(traceback.format_exception(*record.exc_info))
        return json.dumps(log_record, ensure_ascii=False)

    def formatTime(self, record ):
        dt = datetime.fromtimestamp(record.created, self.tz)
        if self.datefmt:
            return dt.strftime(self.datefmt)
        else:
            return dt.isoformat()


class TimeZoneFormatter(logging.Formatter):
    def __init__(self, fmt=None, datefmt=None, tz=None):
        super().__init__(fmt, datefmt)
        self.tz = tz

    def formatTime(self, record, datefmt=None):
        dt = datetime.fromtimestamp(record.created, self.tz)
        if datefmt:
            return dt.strftime(datefmt)
        else:
            return dt.isoformat()


LOGGING_CONF = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'json': {
            '()': 'setup_logging.JsonFormatter',
            'datefmt': '%Y-%m-%dT%H:%M:%S.%f%z',
            'tz': pytz.timezone('Asia/Taipei')
        },
    },
    'filters': {
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'json',
        },
    },
    'loggers': {
        'cb': {
            'level': 'INFO',
            'handlers': ['console'],
            'propagate': False,
        }
    }
}


class ConfigError(Exception):
    def __init__(self, levels, msg):
        super().__init__(f"{'/'.join(levels)}: {msg}")


def load(config_file):
    conf_path = os.path.join(os.environ['BASE_DIR'], 'conf')
    if not os.path.isabs(config_file):
        operation_mode = os.environ['OPERATION_MODE']
        potential_path = os.path.join(conf_path, operation_mode, config_file)
        if os.path.exists(potential_path):
            config_file = potential_path
        else:
            config_file = os.path.join(conf_path, config_file)

    config = {}
    try:
        with open(config_file) as f:
            exec(f.read(), {}, config)
        return config
    except Exception as e:
        raise ConfigError(['ExecError'], f"Error during importing config: {config_file}") from e

partial_conf = load('logging.conf')


for key in LOGGING_CONF:
    if conf := partial_conf.get(key):
        LOGGING_CONF[key].update(conf)


logging.config.dictConfig(LOGGING_CONF)

logger = logging.getLogger('cb')
