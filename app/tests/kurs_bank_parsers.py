from unittest.mock import MagicMock

from currency.models import Rate
from currency.tasks import parse_privatbank, parse_monobank

from app.tests.fixtures.constants_kurs_parsers import PRIVAT_DATA, MONO_DATA


def test_monobank_parser(mocker):
    initial_count = Rate.objects.all().count()

    request_get_mock = mocker.patch(
        'requests.get',
        return_value=MagicMock(
            json=lambda: MONO_DATA
        )
    )

    parse_monobank()
    assert Rate.objects.all().count() == initial_count + 2

    parse_monobank()
    assert Rate.objects.all().count() == initial_count + 2

    assert request_get_mock.call_count == 2


# mocker - для имитации наличия данных (mocker.patch - имитация запроса requests.get("https://api.privatbank.ua/....")
def test_privatbank_parser(mocker):
    # подсчет количества записией в базе (на начало теста их 0)
    initial_count = Rate.objects.all().count()

    request_get_mock = mocker.patch(
        'requests.get',
        return_value=MagicMock(
            json=lambda: PRIVAT_DATA  # в параметр jason обфзательно передавать функцию,не массив, поэтому ставим lambda
        )
    )

    # проверка на добавление курсов EUR и USD
    parse_privatbank()
    assert Rate.objects.all().count() == initial_count + 2

    # проверка на блокировку записи одинаковых данных курса валют
    parse_privatbank()
    assert Rate.objects.all().count() == initial_count + 2
    # прверка сколько раз вызывалась функция request_get_mock
    assert request_get_mock.call_count == 2
