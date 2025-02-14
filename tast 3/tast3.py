import json

def load_j(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def save_j(data):
    with open('report.json', 'w') as file:
        json.dump(data, file)

def values(tests, values_dict):
    if isinstance(tests, list):
        for item in tests:
            values(item, values_dict)
    elif isinstance(tests, dict):
        if 'id' in tests and tests['id'] in values_dict:
            tests['value'] = values_dict[tests['id']]
        for key, value in tests.items():
            if isinstance(value, (dict, list)):
                values(value, values_dict)

def test3():
    values_data = load_j('values.json')  # Чтение values.json
    tests_data = load_j('tests.json')    # Чтение tests.json

    values_dict = {item['id']: item['value'] for item in values_data['values']}

    values(tests_data, values_dict)

    save_j(tests_data)

test3()