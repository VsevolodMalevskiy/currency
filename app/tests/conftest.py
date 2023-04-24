import pytest
from rest_framework.test import APIClient
# from django.core.management import call_command


@pytest.fixture(autouse=True, scope="function")  # позволяет во всех тестах иметь доступ к базе данных
def enable_db_access_for_all_tests(db):
    """
    give access to database for all tests
    """


# создается собственная фикстура, чтобы не писать в api.py client = APIClient()
@pytest.fixture()
def api_client():
    client = APIClient()
    yield client


# @pytest.fixture(autouse=True, scope="session")
# def load_fixtures(django_db_setup, django_db_blocker):
#     with django_db_blocker.unblock():
#         fixtures = (
#             'sources_.json',
#             'rates_.json',
#         )
#         for fixture in fixtures:
#             call_command('loaddata', f'app/tests/fixtures/{fixture}')
