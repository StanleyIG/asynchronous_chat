"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""

"""Модуль modules"""

import subprocess
import chardet



def ping(ARGS):
    YA_PING = subprocess.Popen(ARGS, stdout=subprocess.PIPE)
    for line in YA_PING.stdout:
        result = chardet.detect(line)
        line = line.decode(result['encoding']).encode('utf-8')
        print(line.decode('utf-8'))


ARGS = ['ping', 'yandex.ru']
ARGS2 = ['ping', 'youtube.com']
print('Yandex')
print(ping(ARGS))
print('Youtube')
print(ping(ARGS2))
