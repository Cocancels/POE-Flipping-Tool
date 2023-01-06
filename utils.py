import requests

def get_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print('Error: ' + str(response.status_code))
        return None

def get_item_type_data(type):
    url = 'https://poe.ninja/api/data/itemoverview?league=Sanctum&type=' + type
    data = get_data(url)
    return data['lines']

def get_item_data(type, name):
    items = get_item_type_data(type)

    for item in items:
        if item['name'] == name:
            return item

def get_chaos_item_price(type, name):
    item = get_item_data(type, name)
    return item['chaosValue']

def get_divine_item_price(type, name):
    item = get_item_data(type, name)
    return round(item['divineValue'], 2)