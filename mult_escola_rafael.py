import unittest


def multiplication(multiplicador, multiplicando):
    mm = multiplicando[::-1]
    multiplied = []
    for x in mm:
        multiplied.append(logic_of_multipling(multiplicador, x))
    print(multiplied)
    result = adjusting_list(multiplied)
    print(result)
    making_sum(result)


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


# This function, add zeros to the end of each number.
def adjusting_list(values):
    prepare_to_sum = []
    for index, value in enumerate(values):
        if index >= 1:
            adding_zero = index * '0'
            value = value + adding_zero
            prepare_to_sum.append(value)
    return prepare_to_sum


def making_sum(lista):
    new_list = []
    for value in lista:
        new_list.append(value[::-1])

    x = sorted(new_list)

    result = 0
    ll = 0
    result_string = ''
    another_list = []
    for index, value1 in enumerate(x[0]):
        try:
            result = (int(value1) + int(x[1][index:index + 1]) + ll)
            if result > 9:
                ll = int(str(result)[0:1])
                result = int(str(result)[1:2])
            else:
                ll = 0
        except:
            result = int(value1) + ll
            ll = 0
        result_string += str(result)
        result = ''

    another_list.append(result_string)
    for index, value in enumerate(x):
        if index >= 2:
            another_list.append(value)
        else:
            pass
    print(another_list)


class Test_multiplication(unittest.TestCase):
    def setUp(self):
        pass

    def test_multiplica(self):
        self.assertEqual(multiplication('999999999999999', '8888888888888'), '8888888888887991111111111112')
        self.assertEqual(multiplication('999999999999999', '0'), '0')
        self.assertEqual(multiplication('-1', '1'), '-1')
        self.assertEqual(multiplication('100', '2000'), '2000')
