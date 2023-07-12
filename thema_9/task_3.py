"""
Написать функцию host_range_ping_tab(), возможности которой основаны на функции из примера 2.
Но в данном случае результат должен быть итоговым по всем ip-адресам, представленным в табличном формате
(использовать модуль tabulate). Таблица должна состоять из двух колонок
"""

from ipaddress import ip_address
import subprocess
import chardet
import re
from tabulate import tabulate


def host_range_ping_tab(ARGS):
    not_available = re.compile(r'Заданная сеть недоступна')
    avaible_lst = []
    not_available_lst = []
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
            not_available_lst.append(addr)
        else:
            avaible_lst.append(addr)
    
    ip_dict = {'Доступные': avaible_lst,
               'Недоступные': not_available_lst}
    
    return tabulate(ip_dict, headers='keys', tablefmt="pipe")

args = ['192.168.35.5', '192.168.75.10', 'yandex.ru', 'vk.com', 'hh.ru', '192.168.73.10']
print(host_range_ping_tab(args))