import sys

import django
from django.conf import settings
from django.test.utils import get_runner
from django.test.runner import DiscoverRunner

from dotenv import load_dotenv
load_dotenv()


class NoDbTestRunner(DiscoverRunner):
    """ A test runner to test without database creation """

    def setup_databases(self, **kwargs):
        """ Override the database creation defined in parent class """
        pass

    def teardown_databases(self, old_config, **kwargs):
        """ Override the database teardown defined in parent class """
        pass


if __name__ == "__main__":
    django.setup()
    TestRunner = get_runner(settings)
    test_runner = TestRunner(keepdb=True)
    failures = test_runner.run_tests(["{{ project_name }}"])
    sys.exit(bool(failures))
