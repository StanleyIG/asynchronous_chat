"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""
import chardet


def converter(lst):
    initial_type = None
    final_type = None
    for i in range(len(lst)):
        initial_type = type(lst[i])
        if isinstance(lst[i], bytes):
            detect = chardet.detect(lst[i])
            lst[i] = lst[i].decode(detect['encoding'])
            final_type = type(lst[i])

        else:
            if isinstance(lst[i], str):
                lst[i] = lst[i].encode('utf-8')
                final_type = type(lst[i])

    return lst, initial_type, final_type

def converter2(lst):
    for i in range(len(lst)):
        if isinstance(lst[i], str):
            lst[i] = lst[i].encode('utf-8')
        elif isinstance(lst[i], bytes):
            lst[i] = lst[i].decode('utf-8')
    return lst

# converter3 возвращает новый список с новым id
def converter3(lst):
    new_lst = []
    for i in lst:
        if isinstance(i, str):
            new_lst.append(i.encode('utf-8'))
        elif isinstance(i, bytes):
            new_lst.append(i.decode('utf-8'))
    return new_lst

some_lst = ['разработка', 'администрирование', 'protocol', 'standard']
ls = [b'616263', b'34534654']
ls2 = ['string1', 'string2']
ls3 = ['string1', 'string2']
new_ls, initial_type, final_type = converter(ls)
print(f'id: {id(ls)}')
print('bytes to str')
print(f'значения: {new_ls}, начальный тип: {initial_type}, преобразован в {final_type}')
print(f'id: {id(new_ls)}')
new_ls2, initial_type2, final_type2 = converter(ls2)
print('string to bytes')
print(f'значения: {new_ls2}, начальный тип: {initial_type2}, преобразован в {final_type2}')
print()
print('converter2')
print('bytes to str')
_bytes = converter2(ls3)
print(converter2(_bytes))
print('string to bytes')
print(converter2(some_lst))
print(converter2(ls3))
print()
for_converter3 = ['разработка', 'администрирование', 'protocol', 'standard']
print('converter3')
print('to_bytes')
print(f'id до конвертации: {id(for_converter3)}')
converter3_bytes = converter3(for_converter3)
print(converter3_bytes)
print(f'id после конвертации: {id(converter3_bytes)}')
print('to_string')
_string = converter3(converter3_bytes)
print(_string)
print(f'id: {id(_string)}')

