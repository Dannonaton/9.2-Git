from typing import Union
from datetime import datetime
from masks import get_mask_account
from masks import get_mask_card_number



def mask_account_card(type_and_number: Union[str]) -> Union[str]:
    """Функция, которая маскирует номер счета или карты"""

    text_result = ""
    digit_result = ""
    digit_count = 0

    for el in type_and_number:
        if el.isalpha() or " ":
            text_result += el
        elif el.isdigit():
            digit_result += el
            digit_count += 1
    if digit_count > 16:
        return f"{text_result} {get_mask_account(digit_result)}"
    else:
        return f"{text_result} {get_mask_card_number(digit_result)}"


def get_date(user_date: Union[str]) -> str:
    """Функция получения даты в определенном формате и возвращения в формате ДД.ММ.ГГГГ
    с использованием Метода strptime() и strftime()"""

    date_format = datetime.strptime(user_date, "%Y-%m-%dT%H:%M:%S.%f")
    new_date = date_format.strftime("%d.%m.%Y")
    return new_date

print(get_date("2024-03-11T02:26:18.671407"))