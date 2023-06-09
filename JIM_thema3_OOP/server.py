from socket import socket, AF_INET, SOCK_STREAM
import sys
import json
from common.variables import *
from common.utils import MessageUtils


class Server:
    def __init__(self, listen_address, listen_port):
        self.listen_address = listen_address
        self.listen_port = listen_port
        self.transport = socket(AF_INET, SOCK_STREAM)
        self.message_utils_object = MessageUtils()


    def process_client_message(self, message):
        """
        Обработка сообщений от клиентов, принимает словарь -
        сообщение от клиента, апрверяет корретность,
        возвращает словарь-ответ для клиента

        :param message:
        :return:
        """
        if ACTION in message and message['action'] == PRESENCE and TIME in message \
                and USER in message and ACCOUNT_NAME in message[USER]:
            return {RESPONSE: 200}
        return {
            RESPONSE: 400,
            ERROR: 'Bad Request'
        }

    def start(self):
        try:
            self.transport.bind((self.listen_address, self.listen_port))
        except OSError as e:
            print(f'Ошибка запуска сервера: {e.strerror}')
            sys.exit(1)

        self.transport.listen(MAX_CONNECTIONS)

        while True:
            client, client_address = self.transport.accept()
            try:
                message_from_client = self.message_utils_object.get_message(client)
                print(message_from_client)
                response = self.process_client_message(message_from_client)
                self.message_utils_object.send_message(client, response)
                client.close()
            except (ValueError, json.JSONDecodeError):
                print('Принято некорретное сообщение от клиента')
                client.close()


def main():
    """
    Загрузка параметров командной строки, если нет параметров, то задаём
    значения по умолчанию.
    Сначала обрабатываем порт:
    server.py -p 8079 -a 192.168.0.102
    :return:
    """

    try:
        if '-p' in sys.argv:
            listen_port = int(sys.argv[sys.argv.index('-p') + 1])
        else:
            listen_port = DEFAULT_PORT
        if listen_port < 1024 or listen_port > 65535:
            raise ValueError
    except IndexError:
        print('После параметра "-p" необходимо указать номер порта.')
        sys.exit(1)
    except ValueError:
        print('В качестве порта может быть указано только число в диапазоне от 1024 до 65535.')
        sys.exit(1)

    # Обработка адреса
    try:
        if '-a' in sys.argv:
            listen_address = sys.argv[sys.argv.index('-a') + 1]
        else:
            listen_address = DEFAULT_IP_ADDRESS

    except IndexError:
        print('После параметра "-a" необходимо указать адрес, который будет слушать сервер.')
        sys.exit(1)

    server = Server(listen_address, listen_port)
    server.start()


if __name__ == '__main__':
    main()