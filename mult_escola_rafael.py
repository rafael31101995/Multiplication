import unittest


def multiplication(top_number, bottom_number):
    result_list = check_if_is_negative(top_number, bottom_number)
    top_number = result_list[0]
    bottom_number = result_list[1]

    mm = bottom_number[::-1]
    multiplied = []
    for x in mm:
        multiplied.append(multiplying_logic(top_number, x))
    result = adjusting_list(multiplied)
    x = True
    while x:
        result = making_sum(result)
        if len(result) == 1:
            x = False
    if result_list[2] == '+':
        return result[0]
    else:
        result_string = f'{result_list[2]}{result[0]}'
        return result_string


def check_if_is_negative(x, y):
    signal = []
    string_signal = '+'
    if x[0:1] == '-':
        x = x.replace('-', '')
        signal.append('negative')
    if y[0:1] == '-':
        y = y.replace('-', '')
        signal.append('negative')

    if len(signal) > 1:
        string_signal = '+'
    elif len(signal) == 1:
        string_signal = '-'

    result_list = [x, y, string_signal]
    return result_list


def multiplying_logic(top_number, bottom_number):
    answer = ''
    value = ''
    for x in reversed(range(0, len(top_number))):
        try:
            sum_value = int(value)
        except:
            sum_value = 0

        result = (int(top_number[x:x + 1]) * int(bottom_number)) + sum_value
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
        else:
            prepare_to_sum.append(value)
    return prepare_to_sum


def making_sum(initial_list):
    x = inverting_number_of_list(initial_list)

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

    another_list.append(result_string[:: -1])
    for index, value in enumerate(x):
        if index >= 2:
            another_list.append(value[:: -1])
        else:
            pass
    return another_list


def inverting_number_of_list(list_of_numbers):
    x = []
    for numbers in list_of_numbers:
        x.append(int(numbers))

    x = sorted(x, reverse=True)
    new_list = []
    for numbers in x:
        new_list.append(str(numbers)[::-1])
    return new_list


class Test_multiplication(unittest.TestCase):
    def setUp(self):
        pass

    def test_multiplication(self):
        self.assertEqual(multiplication('999999999999999', '8888888888888'), '8888888888887991111111111112')
        self.assertEqual(multiplication('999999999999999', '0'), '0')
        self.assertEqual(multiplication('-1', '1'), '-1')
        self.assertEqual(multiplication('-1', '-1'), '1')
        self.assertEqual(multiplication('100', '2000'), '200000')
