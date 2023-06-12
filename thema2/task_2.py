"""
Есть файл orders в формате JSON с информацией о заказах. Написать скрипт, автоматизирующий его заполнение данными. 
Для этого:
Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item), количество (quantity), цена (price), покупатель (buyer), дата (date). 
Функция должна предусматривать запись данных в виде словаря в файл orders.json. 
При записи данных указать величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.
"""
import json
from datetime import datetime


# вариант №1
def write_order_to_json(item, quantity, price, buyer, date):
    filename = 'thema2/orders.json'
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
        data['orders'].extend([item, quantity, price, buyer, date])


    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

write_order_to_json(1, 57, 10767.37, 'Иван', datetime.now().strftime("%d.%m.%Y"))


# вариант №2
def write_order_to_json2(item, quantity, price, buyer, date):
    filename = 'thema2/orders2.json'
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
        data['orders'].append({'item': item, 'quantity': quantity, 'price': price, 'buyer': buyer, 'date': date})
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

write_order_to_json2(1, 57, 10767.37, 'Иван', datetime.now().strftime("%d.%m.%Y"))

# вариант №3
def write_order_to_json3(**kwargs):
    filename = 'thema2/orders2.json'
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
        data['orders'].append(kwargs)


    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

write_order_to_json3(item=1, quantity=57, price=10767.37, buyer='Иван', date=datetime.now().strftime("%d.%m.%Y"))



        
