"""
1. Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку определенных 
данных из файлов info_1.txt, info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV. 
Для этого:
Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и считывание данных.
В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь значения 
параметров «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». 
Значения каждого параметра поместить в соответствующий список. 
Должно получиться четыре списка — например, os_prod_list, os_name_list, os_code_list, os_type_list. 
В этой же функции создать главный список для хранения данных отчета — например, main_data — и поместить в него 
названия столбцов отчета в виде списка: «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». 
Значения для этих столбцов также оформить в виде списка и поместить в файл main_data (также для каждого файла);
Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой функции реализовать получение 
данных через вызов функции get_data(), а также сохранение подготовленных данных в соответствующий CSV-файл;
Проверить работу программы через вызов функции write_to_csv(). 
"""
import chardet
import re
import csv


files = ['info_1.txt', 'info_2.txt', 'info_3.txt']

# поскольку при просмотре файла внутри IDE возникли непонятные символы 
# вместо человекочитаемых строк, я перекодировал файлы в кодировку utf-8
def encode_files(files):
    for file in files:
        with open(f'thema2\{file}', 'rb') as f:
            content = f.read()
            encoding = chardet.detect(content)['encoding']
            decoded_content = content.decode(encoding)
        with open(f'thema2/{file}', 'w', encoding='utf-8', newline='') as f:
            f.write(decoded_content)

#encode_files(files)


# вариант №1
def get_all(files):
    os_prod_reg = re.compile(r'Изготовитель системы:\s*(.*)')
    os_name = re.compile(r'Название ОС:\s*(.*)')
    os_code = re.compile(r'Код продукта:\s*(.*)')
    os_type = re.compile(r'Тип системы:\s*(.*)')
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    headers = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
    for file in files:
         with open(f'thema2/{file}', encoding='utf-8') as f:
             data = f.read()
             os_prod_list.append(os_prod_reg.findall(data)[0])
             os_name_list.append(os_name.findall(data)[0])
             os_code_list.append(os_code.findall(data)[0])
             os_type_list.append(os_type.findall(data)[0])
    
    main_data = [headers, os_prod_list, os_name_list, os_code_list, os_type_list]
    return main_data


csv_data = get_all(files)
#print(csv_data)

def write_to_csv(csv_data, filename):
    with open(filename, 'w', newline='') as f:
        f_writer = csv.writer(f)
        for row in csv_data:
            f_writer.writerow(row)

write_to_csv(csv_data, 'thema2/csv_file.csv')

with open('thema2/csv_file.csv') as f:
    print(f.read())


# вариант №2
def get_all2(file):
    os_prod_reg = re.compile(r'Изготовитель системы:\s*(.*)')
    os_name = re.compile(r'Название ОС:\s*(.*)')
    os_code = re.compile(r'Код продукта:\s*(.*)')
    os_type = re.compile(r'Тип системы:\s*(.*)')
    with open(f'thema2/{file}', encoding='utf-8') as f:
        data = f.read()
        os_prod = os_prod_reg.findall(data)
        os_name = os_name.findall(data)
        os_code = os_code.findall(data)
        os_type = os_type.findall(data)
    return [os_prod[0], os_name[0], os_code[0], os_type[0]]


def write_to_csv2(csv_data, filename):
    headers = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
    data = [headers] + csv_data
    with open(filename, 'w', newline='') as f:
        f_writer = csv.writer(f)
        f_writer.writerows(data)


csv_data2 = [get_all2(file) for file in files]
write_to_csv2(csv_data2, 'thema2/csv_file2.csv')
with open('thema2/csv_file2.csv') as f:
    print(f.read())



# вариант №3
def get_all3(files):
    os_prod_reg = re.compile(r'Изготовитель системы:\s*(.*)')
    os_name = re.compile(r'Название ОС:\s*(.*)')
    os_code = re.compile(r'Код продукта:\s*(.*)')
    os_type = re.compile(r'Тип системы:\s*(.*)')
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    lst = []
    for file in files:
         with open(f'thema2/{file}', encoding='utf-8') as f:
             data = f.read()
             os_prod_list.append(os_prod_reg.findall(data)[0])
             os_name_list.append(os_name.findall(data)[0])
             os_code_list.append(os_code.findall(data)[0])
             os_type_list.append(os_type.findall(data)[0])
    for i in range(len(os_prod_list)):
        lst.append([os_prod_list[i], 
                    os_name_list[i], 
                    os_code_list[i],  
                    os_type_list[i]])
    return lst


csv_data3 = get_all3(files)
#print(csv_data3)

def write_to_csv3(csv_data, filename):
    headers = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
    data = [headers] + csv_data
    with open(filename, 'w', newline='') as f:
        f_writer = csv.writer(f)
        f_writer.writerows(data)

write_to_csv3(csv_data3, 'thema2/csv_file3.csv')
with open('thema2/csv_file2.csv') as f:
    print(f.read())







