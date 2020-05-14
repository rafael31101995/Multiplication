import unittest


def multiplication(multiplicador, multiplicando):
    mm = multiplicando[::-1]
    for x in mm:
        print(logic_of_multipling(multiplicador, x))


def logic_of_multipling(multiplicador, multiplicando):
    answer = ''
    value = ''
    sum_value = 0
    for x in reversed(range(0, len(multiplicador))):
        try:
            sum_value = int(value)
        except:
            sum_value = 0

        result = (int(multiplicador[x:x + 1]) * int(multiplicando)) + sum_value
        if result >= 10:
            value = str(result)[0:1]
            answer = answer + str(result)[1:2]
        else:
            value = ''
            answer = answer + str(result)
    answer = answer + value
    return answer[:: -1]


class Test_multiplication(unittest.TestCase):
    def setUp(self):
        pass

    def test_multiplica(self):
        self.assertEqual(multiplica('999999999999999', '8888888888888'), '8888888888887991111111111112')
        self.assertEqual(multiplica('999999999999999', '0'), '0')
        self.assertEqual(multiplica('-1', '1'), '-1')
        self.assertEqual(multiplica('100', '2000'), '2000')
