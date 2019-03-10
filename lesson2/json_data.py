import json
import os


def write_orders_to_json(tmp_item, tmp_quantity, tmp_price, tmp_buyer, tmp_date):
    try:
        data = json.load(open(os.path.join('json', 'orders.json')))
    except:
        data = []

    dict_to_json = {
        'item': tmp_item,
        'quantity': tmp_quantity,
        'price': tmp_price,
        'buyer': tmp_buyer,
        'date': tmp_date
    }

    data.append(dict_to_json)

    with open(os.path.join('json', 'orders.json'), 'w') as json_data:
        json.dump(data, json_data, indent=4)


write_orders_to_json('apple', '4', '100', 'John', '01/03/2019')
write_orders_to_json('car', '1', '5', 'Jack', '08/03/2019')
