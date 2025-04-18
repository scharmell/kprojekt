def get_date(date: str) -> str:
    """ Функция работы с данными """
    year = date[:4]
    month = date[5:7]
    day = date[8:10]
    return f"{day}.{month}.{year}"


