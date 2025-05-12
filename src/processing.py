from typing import Dict, List


def filter_by_state(transactions: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """Фильтрует заданный список словарей по ключу"""
    results = []
    for t in transactions:
        if t["state"] == state:
            results.append(t)
    return results


def sort_by_date(transactions: List[Dict], reverse: bool = True) -> List[Dict]:
    """Сортирует заданный список словарей по дате"""
    return sorted(transactions, reverse=reverse, key=lambda t: t["date"])


print(
    filter_by_state(
        [
            {"id": 41428829, "state": "Canceled", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        ]
    )
)
print(
    sort_by_date(
        [
            {"id": 41428829, "state": "Canceled", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        ]
    )
)
