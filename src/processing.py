new_dictionary = []


def filter_by_state(dictionary: list) -> list:
    """ Функция, для сортировки по ключу """
    for i in dictionary:
        if i["state"] == "EXECUTED":
            new_dictionary.append(i)
    return new_dictionary


def sort_by_date(sort_time: list, reverse: bool = True) -> list:
    """ Функция, для сортировки списка по дате """
    return sorted(sort_time, key=lambda x: x["date"], reverse=reverse)
