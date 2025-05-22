import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "value, account_card",
    [
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("0", " Вы ввели некорректные данные"),
    ],
)
def test_mask_account_card(value, account_card):
    assert mask_account_card(value) == account_card


@pytest.mark.parametrize("value, date", [("2024-03-11T02:26:18.671407", "11.03.2024")])
def test_get_date(value, date):
    assert get_date(value) == date
