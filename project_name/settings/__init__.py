import os
import sys
import traceback

from .settings import *

OPERATION_MODE = os.environ.get("OPERATION_MODE", None)
if OPERATION_MODE:
    try:
        extend_settings_name = "conf.%s.django_settings" % OPERATION_MODE
        django_settings = __import__(
            "conf.%s.django_settings" % OPERATION_MODE,
            fromlist=['*']
        )
        if "__all__" in django_settings.__dict__:
            names = django_settings.__dict__["__all__"]
        else:
            # otherwise we import all names that don't begin with _
            names = [x for x in django_settings.__dict__ if not x.startswith("_")]
            # names = [x for x in djanto_settings.__dict__]
        for name in names:
            globals()[name] = getattr(django_settings, name)

    except Exception:
        traceback.print_exc(file=sys.stdout)
