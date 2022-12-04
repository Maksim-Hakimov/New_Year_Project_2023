import json


def load_json():
    """
    Загрузка json
    """
    with open('data/123.json', 'r', encoding='UTF-8') as name_json:
        return json.load(name_json)


def create_dict(user, text):
    """
    Создает словарь из json. Получает новые значения и добавляет их в созданный словарь
    """
    dict_one = load_json()

    len_dict = len(dict_one) + 1

    all_dict = {'pk': len_dict, 'user': user, 'text': text}
    dict_one.append(all_dict)

    wright_json(dict_one)
    return


def wright_json(dict_one):
    """
    Перезаписывает json
    """
    with open('data/123.json', 'w', encoding='UTF-8') as name_json:
        json.dump(dict_one, name_json, ensure_ascii=False)
    return
