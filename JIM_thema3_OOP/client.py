from socket import socket, AF_INET, SOCK_STREAM
import sys
import json
from common.variables import *
from datetime import datetime
from common.utils import MessageUtils


class Client:
    def __init__(self, server_address, server_port):
        self.server_address = server_address
        self.server_port = server_port
        self.transport = socket(AF_INET, SOCK_STREAM)
        self.message_utils_object = MessageUtils()

    def create_presence(self, account_name='Guest'):
        out = {
            ACTION: PRESENCE,
            TIME: datetime.now().strftime("%d.%m.%Y %H:%M:%S"),
            USER: {
                ACCOUNT_NAME: account_name
            }
        }
        return out

    def process_ans(self, message):
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

    def start(self):
        try:
            self.transport.connect((self.server_address, self.server_port))
            message_to_server = self.create_presence('Test User')
            self.message_utils_object.send_message(self.transport, message_to_server)
            try:
                answer = self.process_ans(self.message_utils_object.get_message(self.transport))
                print(answer)
            except (ValueError, json.JSONDecodeError):
                print('Не удалось декодировать сообщение сервера')
        except ConnectionRefusedError:
            print(f'Не удалось подключиться к серверу {self.server_address}:{self.server_port}')
            sys.exit(1)


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

    client = Client(server_address, server_port)
    client.start()


if __name__ == '__main__':
    main()