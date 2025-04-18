
def get_mask_card_number(card_number: str) -> str:
    """Возвращаем замаскированный номер карты"""
    len_number = 16
    if len(card_number) == len_number:
        return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    else:
        return "Вы ввели некорректные данные"


def get_mask_account(account_number: str) -> str:
    """Возвращаем замаскированный номер счета"""
    len_acc_num = 20
    if len(account_number) == len_acc_num:
        return f"**{account_number[-4:]}"
    else:
        return "Вы ввели некорректные данные"


