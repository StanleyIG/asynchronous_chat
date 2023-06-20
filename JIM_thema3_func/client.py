from socket import socket, AF_INET, SOCK_STREAM
import sys
import json
from common.variables import *
from common.utils import get_message, send_message
from datetime import datetime


def create_presence(account_name='Guest'):
    out = {
        ACTION: PRESENCE,
        TIME: datetime.now().strftime("%d.%m.%Y %H:%M:%S"),
        USER: {
            ACCOUNT_NAME: account_name
        }
    }
    return out


def process_ans(message):
    """
    Функция разбирает ответ сервера
    :param message:
    :return:
    """

    if RESPONSE in message:
        if message[RESPONSE] == 200:
            return '200 : OK'
        return f'400 : {message[ERROR]}'
    raise ValueError



def main():
    """Загрузка параметров командной строки"""
    # client.py 192.168.57.33 8079
    # server.py -p 8079 -a 192.168.57.33
    try:
        server_address = sys.argv[1]
        server_port = int(sys.argv[2])
        if server_port < 1024 or server_port > 65535:
            raise ValueError
    except IndexError:
        server_address = DEFAULT_IP_ADDRESS
        server_port = DEFAULT_PORT
    except ValueError:
        print('В качестве порта может быть указанно тольео число в диапазоне от 1024 до 65535.')
        sys.exit(1)


    # инициализация сокета и обмен
    transport = socket(AF_INET, SOCK_STREAM)
    transport.connect((server_address, server_port))
    message_to_server = create_presence('Test User')
    send_message(transport, message_to_server)
    try:
        answer = process_ans(get_message(transport))
        print(answer)
    except (ValueError, json.JSONDecodeError):
        print('Не удалось декодировать сообщение сервера')

    

if __name__== '__main__':
    main()