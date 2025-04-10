import os
import logging
import logging.config
import json
import traceback
from zoneinfo import ZoneInfo
from datetime import datetime


class JsonFormatter(logging.Formatter):
    def __init__(self, fmt=None, datefmt=None, tz=None):
        super().__init__(fmt, datefmt)
        self.tz = tz

    def format(self, record):
        log_record = {
            "level": record.levelname,
            "time": self.formatTime(record),
            "lineno": record.lineno,
            "path": record.pathname,
            "process": record.process,
            "message": record.getMessage(),
            "username": record.username if hasattr(record, "username") else None,
            "uid": record.uid if hasattr(record, "uid") else None,
            "gid": record.gid if hasattr(record, "gid") else None,
        }
        if record.exc_info:
            log_record["exception"] = "".join(traceback.format_exception(*record.exc_info))
        return json.dumps(log_record, ensure_ascii=False)

    def formatTime(self, record):
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


class UserInfoFilter(logging.Filter):
    def filter(self, record):
        record.uid = os.getuid()
        record.gid = os.getgid()
        return True


LOGGING_CONF = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "json": {
            "()": JsonFormatter,
            "datefmt": "%Y-%m-%dT%H:%M:%S.%f%z",
            "tz": ZoneInfo(os.environ["TIME_ZONE"])
        },
        "verbose": {
            "()": TimeZoneFormatter,
            "format": "[%(asctime)s %(pathname)s:%(lineno)d (%(process)d) %(levelname)s] %(message)s",
            "tz": ZoneInfo(os.environ["TIME_ZONE"])
        }
    },
    "filters": {
        "user_info": {
            "()": UserInfoFilter,
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "json",
        },
        "file": {
            "class": "logging.FileHandler",
            "filename": os.path.join(os.environ["BASE_DIR"], "logfiles", "verbose.log"),
            "formatter": "verbose",
        },
    },
    "loggers": {
        "prod": {
            "level": "INFO",
            "handlers": ["console"],
            "filters": ["user_info"],
            "propagate": False,
        },
        "stagging": {
            "level": "DEBUG",
            "handlers": ["console"],
            "filters": ["user_info"],
            "propagate": False,
        },
        "dev": {
            "level": "DEBUG",
            "handlers": ["console", "file"],
            "filters": ["user_info"],
            "propagate": False,
        },
    }
}

logging.config.dictConfig(LOGGING_CONF)


_current_logger_name = None
def getLogger(logger_name=None):
    global _current_logger_name

    if logger_name is None:
        if _current_logger_name is None:
            return logging.getLogger(os.environ["DEFAULT_LOGGER"])
        else:
            return logging.getLogger(_current_logger_name)
    _current_logger_name = logger_name
    return logging.getLogger(logger_name)
