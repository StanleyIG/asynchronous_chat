from common.variables import *
import json


class MessageUtils:

    def get_message(self, sock):
        """
        Утилита при1ма и декодирования сообщения
        принимает байты выдаёт словарь, если принято
        что-то другое выдаёт ошибку значения
        :return:
        """
        encoding_response = sock.recv(MAX_PACKAGE_LENGTH)
        if isinstance(encoding_response, bytes):
            json_response = encoding_response.decode(ENCODING)
            response = json.loads(json_response)
            if isinstance(response, dict):
                return response
            raise ValueError
        raise ValueError

    def send_message(self, sock, message):
        """
        Утилита кодирования и отправки сообщения.
        Принимает словарь и отправляет его
        :param message:
        :return:
        """
        js_message = json.dumps(message)
        encoded_message = js_message.encode(ENCODING)
        sock.send(encoded_message)