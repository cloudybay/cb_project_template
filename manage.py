#!/usr/bin/env python
import os
import sys


if __name__ == "__main__":
    import OS_ENVIRON
    os.environ.setdefault('COLLECTIVE_NAME', 'manage')

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

