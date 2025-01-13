bank_card_number = input("Введите номер карты: ")
bank_account_number = input("Введите номер счёта: ")


def get_mask_card_number(card_number: str) -> str:
    """Функция для маскировки номера карты"""

    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"


def get_mask_account(account_number: str) -> str:
    """Функция для маскировки номера счёта"""

    return f"**{account_number[-4:]}"


print(get_mask_card_number(bank_card_number))
print(get_mask_account(bank_account_number))
