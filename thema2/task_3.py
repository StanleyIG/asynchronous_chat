"""
Написать скрипт, автоматизирующий сохранение данных в файле YAML-формата. Для этого:
Подготовить данные для записи в виде словаря, в котором первому ключу соответствует 
список, второму — целое число, третьему — вложенный словарь, где значение каждого ключа — это целое 
число с юникод-символом, отсутствующим в кодировке ASCII (например, €);
Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml. 
При этом обеспечить стилизацию файла с помощью параметра default_flow_style, а также установить 
возможность работы с юникодом: allow_unicode = True;
Реализовать считывание данных из созданного файла и проверить, совпадают ли они с исходными.
"""
import random
import chardet
import yaml


# Функция для проверки, является ли число символом ASCII
def is_ascii(num):
    return num < 128


def yaml_data():
    symbol_list = []
    value_list = [[], 5, {}]
    for i in range(3):
        while True:
            num = random.randint(0, 255)
            if not is_ascii(num):
                byte_str = bytes.fromhex(hex(num)[2:])
                detect = chardet.detect(byte_str)['encoding']
                if detect is not None:
                    decode_str = byte_str.decode(detect)
                    byte_str_utf8 = decode_str.encode('utf-8')
                    str_utf8 = byte_str_utf8.decode('utf-8')
                    if str_utf8 not in [x[0] for x in symbol_list]:
                        symbol_list.append((str_utf8, value_list[i]))
                        break
                
    return symbol_list

res = yaml_data()
#print(res)


def write_yaml_data(key_value_list):
    data = {}
    for key, value in key_value_list:
        data[key] = value
    with open('thema2/data_read.yaml', 'w', encoding='utf-8') as y_f:
        yaml.dump(data, y_f, default_flow_style=False, allow_unicode=True)
    print(data)
        
#write_yaml_data(res)

with open('thema2/data_read.yaml', encoding='utf-8') as y_f:
    data = yaml.load(y_f, Loader=yaml.FullLoader)
    #print(data)


# вариант №2
def yaml_data2():
    hex_list = []
    value_list = [[], 5, {}]
    for i in range(3):
        while True:
            num = random.randint(0, 255)
            hex_num = hex(num)
            if not is_ascii(num) and hex_num not in hex_list:
                hex_list.append((hex_num, value_list[i]))
                break

    return hex_list

write_yaml_data(yaml_data2())






