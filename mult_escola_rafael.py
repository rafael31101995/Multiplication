import unittest


def multiplica(multiplicador, multiplicando):
    def multiplication(multiplicador, multiplicando):
        answer = ''
        for x in reversed(range(0, len(multiplicador))):
            result = int(multiplicador[x:x + 1]) * int(multiplicando[:1])
            answer = answer + str(result)
            print(answer)


class Test_multiplication(unittest.TestCase):
    def setUp(self):
        pass

    def test_multiplica(self):
        self.assertEqual(multiplica('999999999999999', '8888888888888'), '8888888888887991111111111112')
        self.assertEqual(multiplica('999999999999999', '0'), '0')
        self.assertEqual(multiplica('-1', '1'), '-1')
        self.assertEqual(multiplica('100', '2000'), '2000')
