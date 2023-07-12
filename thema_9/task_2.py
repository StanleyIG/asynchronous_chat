"""
2. Написать функцию host_range_ping() для перебора ip-адресов из заданного диапазона.
Меняться должен только последний октет каждого адреса.
По результатам проверки должно выводиться соответствующее сообщение.
"""
from ipaddress import ip_address
import subprocess
import chardet
import re


def host_range_ping(ARGS):
    not_available = re.compile(r'Заданная сеть недоступна')
    for addr in ARGS:
        try:
            ipv4 = str(ip_address(addr))
            args = ['ping', ipv4]
        except ValueError:
            args = ['ping', addr]
        PING = subprocess.Popen(args, stdout=subprocess.PIPE)
        DATA = PING.communicate()
        RESULT = chardet.detect(DATA[0])
        OUT = DATA[0].decode(RESULT['encoding'])
        if re.search(not_available, OUT):
            print(f'{addr}: Узел не доступен')
        else:
            print(f'{addr}: Узел доступен')

args = ['192.168.35.5', '192.168.75.10', 'yandex.ru', 'vk.com', 'hh.ru', '192.168.73.10']
#host_range_ping(args)
