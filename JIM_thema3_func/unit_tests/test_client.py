import unittest
from common.variables import*
from client import create_presence, process_ans


class TestClient(unittest.TestCase):

    def test_def_peresence(self):
        """Тест конкретного зароса"""
        test = create_presence()
        test[TIME] = 1.1

        self.assertEqual(test,  {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}})

    def test_200_ans(self):
        """Тест корректного разбора ответа 200"""
        self.assertEqual(process_ans({RESPONSE: 200}), '200 : OK')

    def test_400_ans(self):
        """Тест корректного разбора ответа 400"""
        self.assertEqual(process_ans({RESPONSE: 400, ERROR: 'Bad Request'}),
                         '400 : Bad Request')
        
    def test_no_response(self):
        """Тест исключения без поля RESPONSE"""
        self.assertRaises(ValueError, process_ans, {ERROR: 'Bad Request'})
