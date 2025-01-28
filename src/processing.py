new_dictionary = []


def filter_by_state(dictionary: list, state: str = 'EXECUTED') -> list:
    """ Функция, для сортировки по ключу """
    for i in dictionary:
        if i["state"] == state:
            new_dictionary.append(i)
    return new_dictionary


def sort_by_date(sort_time: list, reverse: bool = True) -> list:
    """ Функция, для сортировки списка по дате """
    return sorted(sort_time, key=lambda x: x["date"], reverse=reverse)


print(filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                       {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                       {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                       {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))