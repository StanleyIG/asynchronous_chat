"""
Задание 3.

Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе с помощью маркировки b'' (без encode decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
--- обязательно!!! усложните задачу, "отловив" исключение,
придумайте как это сделать
"""
import re

def detect(lst):
    erorrs = []
    exeption = None
    for i in lst:
        try:
            res = bytes(i, 'ASCII')
            print(res)
        except UnicodeEncodeError as UE:
            erorrs.append(i)
            exeption = UE
    if erorrs:
        print(f'ошибка кодировки {exeption}, элементы: {", ".join(erorrs)}')
        return erorrs



some_lst = ['attribute', 'класс', 'функция', 'type']
errors = detect(some_lst)
print(errors)


