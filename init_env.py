import os
import sys
try:
    from dotenv import dotenv_values, find_dotenv, set_key
except ImportError:
    print("No module named 'dotenv'")
    print("Run 'pip install git+https://github.com/cloudybay/python-dotenv@master' to install it.")
    sys.exit(1)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DOTENV_FILE = '.env'
EXAMPLE_DOTENV = '.env.example'


def __check_git_pre_commit(home):
    _p_sample = os.path.join(home, '.git/hooks/pre-commit.sample')
    _p_commit = os.path.join(home, '.git/hooks/pre-commit')
    if os.path.exists(_p_sample):
        if not os.path.exists(_p_commit):
            import shutil
            shutil.move(_p_sample, _p_commit)


def init_dotenv():
    src_envs = dotenv_values(EXAMPLE_DOTENV)
    if not src_envs:
        print(f'No such {EXAMPLE_DOTENV} file found.')
        sys.exit(1)

    target_dotenv_file = find_dotenv(DOTENV_FILE)
    if not target_dotenv_file:
        open(os.path.join(BASE_DIR, DOTENV_FILE), 'w').close()
        target_dotenv_file = find_dotenv(DOTENV_FILE)

    target_envs = dotenv_values(target_dotenv_file)
    src_envs['BASE_DIR'] = BASE_DIR
    for env_key, value in src_envs.items():
        if env_key not in target_envs:
            set_key(target_dotenv_file, env_key, value, quote_mode="never")


if __name__ == '__main__':
    __check_git_pre_commit(BASE_DIR)
    init_dotenv()
