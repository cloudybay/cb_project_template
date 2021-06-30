import sys
from dotenv import load_dotenv


if __name__ == "__main__":
    load_dotenv()

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
