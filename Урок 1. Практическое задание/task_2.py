"""
Задание 2.

Каждое из слов «class», «function», «method» записать в байтовом формате
без преобразования в последовательность кодов
не используя!!! методы encode и decode)
и определить тип, содержимое и длину соответствующих переменных.

Подсказки:
--- b'class' - используйте маркировку b''
--- используйте списки и циклы, не дублируйте функции
"""

def to_bytes(lst):
    res = []
    for item in lst:
        byte_string = b''
        for i in item:
            byte_string += bytes([ord(i)])
        res.append(byte_string)
        print(f' содержимое: {byte_string}, тип: {type(byte_string)},'
              f' длина: {len(byte_string)}')
    return res



def to_bytes2(lst):
    res = []
    for i in lst:
        byte_string = bytes(i, 'utf-8')
        res.append(byte_string)
        print(f' содержимое: {byte_string}, тип: {type(byte_string)},'
              f' длина: {len(byte_string)}')
    return res

some_lst = ['class', 'function', 'method']
print(to_bytes(some_lst))
print(to_bytes2(some_lst))


