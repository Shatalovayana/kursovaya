from src.functions import *
import pytest


@pytest.fixture
def test_data():
    return {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    }


def test_load_operations():
    load_data = load_operations('operations.json')
    assert load_data is not None


def test_executed_operations():
    executed_list = executed_operations(load_operations('operations.json'))
    assert type(executed_list) is list


def test_get_card_number_from(test_data):
    assert get_card_number_from(test_data) == "Maestro 1596 83** **** 5199"


def test_get_card_number_to(test_data):
    assert get_card_number_to(test_data) == "Счет **9589"


def test_date_operations(test_data):
    date = date_operations(test_data)
    assert type(date) is str
