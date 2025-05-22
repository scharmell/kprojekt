import pytest


@pytest.fixture
def card_number():
    return "1111 22** **** 4444"


@pytest.fixture
def account_number():
    return "**5555"


@pytest.fixture
def card_widget():
    return "Visa Platinum 8990922113665229"


@pytest.fixture
def account_widget():
    return "Счет 73654108430135874305"
