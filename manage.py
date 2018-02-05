#!/usr/bin/env python
import os
import sys


def __check_git_pre_commit(home):
    _p_sample = os.path.join(home, '.git/hooks/pre-commit.sample')
    _p_commit = os.path.join(home, '.git/hooks/pre-commit')
    if os.path.exists(_p_sample):
        if not os.path.exists(_p_commit):
            import shutil
            shutil.move(_p_sample, _p_commit)


if __name__ == "__main__":
    __check_git_pre_commit(os.path.dirname(os.path.abspath(__file__)))

    import env
    os.environ.setdefault('COLLECTIVE_NAME', 'manage')

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
