def geo_logs_list(geo_list):
    geo_logs_filter = []
    for visit in geo_list:
        for countries in visit.values():
            if 'Россия' in countries:
                geo_logs_filter.append(visit)
    return geo_logs_filter


def ids_new_list(ids_dict):
    ids_new = []
    for value in ids_dict.values():
        ids_new += value
    return list(set(ids_new))


def max_element(element_dict):
    for elements in element_dict.keys():
        if element_dict[elements] == max(element_dict.values()):
            return elements


if __name__ == '__main__':
    geo_logs = [
        {'visit1': ['Москва', 'Россия']},
        {'visit2': ['Дели', 'Индия']},
        {'visit3': ['Владимир', 'Россия']},
        {'visit4': ['Лиссабон', 'Португалия']},
        {'visit5': ['Париж', 'Франция']},
        {'visit6': ['Лиссабон', 'Португалия']},
        {'visit7': ['Тула', 'Россия']},
        {'visit8': ['Тула', 'Россия']},
        {'visit9': ['Курск', 'Россия']},
        {'visit10': ['Архангельск', 'Россия']}
    ]
    ids = {'user1': [213, 213, 213, 15, 213],
           'user2': [54, 54, 119, 119, 119],
           'user3': [213, 98, 98, 35]}

    stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
    print(geo_logs_list(geo_logs))
    print(ids_new_list(ids))
    print(max_element(stats))