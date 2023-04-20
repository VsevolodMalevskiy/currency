import pytest


@pytest.fixture(autouse=True, scope="function")  # позволяет во всех тестах иметь доступ к базе данных
def enable_db_access_for_all_tests(db):
    """
    give access to database for all tests
    """
