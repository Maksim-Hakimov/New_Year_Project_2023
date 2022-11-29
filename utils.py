import json


def load_json():
    with open('data/123.json', 'r', encoding='UTF-8') as name_json:
        return json.load(name_json)


def create_dict(user, text):
    dict_one = load_json()

    all_dict = {'user': user, 'text': text}
    dict_one.append(all_dict)

    wright_json(dict_one)
    return


def wright_json(dict_one):
    with open('data/123.json', 'w', encoding='UTF-8') as name_json:
        json.dump(dict_one, name_json, ensure_ascii=False)
    return
