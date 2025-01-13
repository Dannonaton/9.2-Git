from typing import Union
from datetime import datetime
from masks import get_mask_account
from masks import get_mask_card_number



def mask_account_card():
    pass


def get_date(user_date: Union[str]) -> str:
    """Функция получения даты в определенном формате и возвращения в формате ДД.ММ.ГГГГ
    с использованием Метода strptime() и strftime()"""

    date_format = datetime.strptime(user_date, "%Y-%m-%dT%H:%M:%S.%f")
    new_date = date_format.strftime("%d.%m.%Y")
    return new_date

print(get_date("2024-03-11T02:26:18.671407"))