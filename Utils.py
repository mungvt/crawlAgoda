import json


def write_json(data, filename='data_agoda.json'):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)