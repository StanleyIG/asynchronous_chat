


class Test:
    def __init__(self):
        self.start_str = 'Запуск декоратора'
        self.end_str = 'Завершение декоратора'

    @classmethod
    def show(cls):
        return 'Какая-то функциональность метода класса'
    

TEST_OBJ = Test()
print(TEST_OBJ.show())
print(Test.show())