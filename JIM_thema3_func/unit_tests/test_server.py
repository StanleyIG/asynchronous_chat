from server import process_client_message
import unittest
from common.variables import*



class TestServer(unittest.TestCase):

    err_dict = {
        RESPONSE: 400,
        ERROR: 'Bad Request'
        }

    ok_dict = {RESPONSE: 200}

    def test_no_action(self):
        """Оошибка если нет действия"""
        self.assertEqual(process_client_message(
            {TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}}),
            self.err_dict
        )

    def test_wrong_action(self):
        """ошибка если неизвестное действие"""
        self.assertEqual(process_client_message(
            {ACTION: 'Wrong', TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}}),
            self.err_dict
        )

    def test_no_time(self):
        """ошибка если нет поля времени"""
        self.assertEqual(process_client_message(
            {ACTION: PRESENCE, USER: {ACCOUNT_NAME: 'Guest'}}),
            self.err_dict
        )

    def test_no_user(self):
        """ошибка если нет поля пользхователя"""
        self.assertEqual(process_client_message(
            {ACTION: PRESENCE, TIME: 1.1}),
            self.err_dict
        )

    def test_ok_check(self):
        self.assertEqual(process_client_message(
            {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}}),
            self.ok_dict
        )




