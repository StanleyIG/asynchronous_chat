"""
1. Написать функцию host_ping(), в которой с помощью утилиты ping
будет проверяться доступность сетевых узлов.
Аргументом функции является список, в котором каждый сетевой узел
должен быть представлен именем хоста или ip-адресом.
В функции необходимо перебирать ip-адреса и проверять
их доступность с выводом соответствующего сообщения
(«Узел доступен», «Узел недоступен»). При этом ip-адрес
сетевого узла должен создаваться с помощью функции ip_address().
"""
from ipaddress import ip_address
import subprocess
import chardet
import re

# вариант №1
def host_ping(ARGS):
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
host_ping(args)



# вариант №2
def ping(ARGS):
    PING = subprocess.Popen(ARGS, stdout=subprocess.PIPE)
    for line in PING.stdout:
        result = chardet.detect(line)
        line = line.decode(result['encoding']).encode('utf-8')
        if 'Заданная сеть недоступна' in line.decode('utf-8'):
            #print(f'{ARGS[1]}: Узел не доступен')
            return False
    return True

def host_ping2(ip_addr):
    total = 0
    for addr in ip_addr:
        try:
            ipv4 = str(ip_address(addr))
            args = ['ping', ipv4]
        except ValueError:
            args = ['ping', addr]
        total += 1
        if ping(args):
            print(f'{addr}: Узел доступен')
        else:
            print(f'{addr}: Узел не доступен')
        

#host_ping2(['192.168.35.5', '192.168.75.10', 'yandex.ru', 'vk.com', 'hh.ru', '192.168.73.10'])

#if __name__ == '__main__':
#    import sys
#    host_ping(sys.argv[1:])










