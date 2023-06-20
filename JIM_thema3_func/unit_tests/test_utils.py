import unittest
from unittest.mock import MagicMock, patch
from common.variables import*
from socket import socket, AF_INET, SOCK_STREAM
from common.utils import get_message, send_message
from client import create_presence, process_ans
from server import process_client_message
from client import create_presence
from server import process_client_message
import json

from unittest.mock import patch, MagicMock
from server import main
from common.variables import *
import sys


class TestUtils(unittest.TestCase):
    
    client_mesage = {ACTION: PRESENCE, TIME: 1.1,  USER: {ACCOUNT_NAME: 'Guest'}}

    def test_client_data_get_message(self):
        """тест проверяет выходные данные от клиента"""

        # создаю заглушку для сокета
        sock = MagicMock()
        # Устанавливаю возвращаемое значение для recv
        js_message = json.dumps(create_presence())
        encoded_message = js_message.encode(ENCODING)
        sock.recv.return_value = encoded_message
        # Вызываю функцию get_message
        result = get_message(sock)
        result[TIME] = 1.1
        # Проверяю, что результат соответствует ожидаемому словарю
        self.assertEqual(result, self.client_mesage)
        # Проверяею, что recv был вызван с правильным аргументом
        sock.recv.assert_called_once_with(MAX_PACKAGE_LENGTH)

    
    def test_client_type_get_message(self):
        """тест проверяет тип выходных данных от клиента"""

        # Создаем заглушку для сокета
        sock = MagicMock()
        # Устанавливаю возвращаемое значение для recv
        js_message = json.dumps(create_presence())
        encoded_message = js_message.encode(ENCODING)
        sock.recv.return_value = encoded_message
        # Вызываю функцию get_message
        result = get_message(sock)
        result[TIME] = 1.1
        # Проверяю, что результат соответствует ожидаемому словарю
        self.assertIsInstance(result, dict)
        # Проверяею, что recv был вызван с правильным аргументом
        sock.recv.assert_called_once_with(MAX_PACKAGE_LENGTH)


    def test_server_data_get_message(self):
        """тест проверяет выходные данные от сервера"""

        # Создаем заглушку для сокета
        sock = MagicMock()
        # Устанавливаю возвращаемое значение для recv
        js_message = json.dumps(process_client_message(self.client_mesage))
        encoded_message = js_message.encode(ENCODING)
        sock.recv.return_value = encoded_message
        # Вызываю функцию get_message
        result = get_message(sock)
        # Проверяю, что результат соответствует ожидаемому словарю
        self.assertEqual(result, {RESPONSE: 200})
        # Проверяею, что recv был вызван с правильным аргументом
        sock.recv.assert_called_once_with(MAX_PACKAGE_LENGTH)


    def test_server_type_get_message(self):
        """тест проверяет тип выходных данных от сервера"""

       # Создаю заглушку для сокета
        sock = MagicMock()
        # Устанавливаю возвращаемое значение для recv
        js_message = json.dumps(process_client_message(self.client_mesage))
        encoded_message = js_message.encode(ENCODING)
        sock.recv.return_value = encoded_message
        # Вызываю функцию get_message
        result = get_message(sock)
        # Проверяю, что результат соответствует ожидаемому словарю
        self.assertIsInstance(result, dict)
        # Проверяею, что recv был вызван с правильным аргументом
        sock.recv.assert_called_once_with(MAX_PACKAGE_LENGTH)


    def test_invalid_data_get_message(self):
        """Проверяю, что ValueError вызывается при получении недопустимых данных"""

        sock = MagicMock()
        # Устанавливаю возвращаемое значение для recv как недопустимые данные
        sock.recv.return_value = b'some str'
        # вызывается функция get_message и подтверждается, что она вызывает ValueError
        self.assertRaises(ValueError, get_message, sock)

    
    def test_data_send_message(self):
        """тест проверяет выходные данные функцию send_mesage()"""
        # Создаю заглушку для сокета
        sock = MagicMock()
        # Вызываю функцию send_message
        send_message(sock, self.client_mesage)
        # Проверяю, что send был вызван с правильным аргументом
        js_byte_message = json.dumps(self.client_mesage)
        sock.send.assert_called_once_with(js_byte_message.encode(ENCODING))


