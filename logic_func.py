import json

#clean json
def clean_json(py_json):
    py_json = py_json
    for dict_data in py_json:
        for key in list(dict_data.keys()):
            if dict_data[key] == "":
                del dict_data[key]
    return py_json

def save_json(json_data, name):
    with open(f'files/{name}.json', 'w', encoding='utf-8') as f:
        json.dump(json_data, f, ensure_ascii=False, indent=4)

