def multiplication(top_number_initial, bottom_number_initial):
    result_list = check_signal(top_number_initial, bottom_number_initial)
    # Getting float_point

    float_index = check_float_index(result_list[0]) + check_float_index(result_list[1])

    top_number = result_list[0].replace('.', '')
    bottom_number = result_list[1].replace('.', '')

    bottom_number = bottom_number[::-1]
    multiplied = []
    for x in bottom_number:
        multiplied.append(multiplying_logic(top_number, x))
    result = adding_zeros(multiplied)

    result = sum_logic(result)
    result_2 = str(result)
    new_result = ''
    for index, number in enumerate(result_2[::-1]):
        if index == float_index and float_index != 0:
            new_result += '.'
            new_result += number
        else:
            new_result += number

    if result_list[2] == '+':
        # Sending for formatting.
        formatting_content(top_number_initial, bottom_number_initial, multiplied, new_result[::-1])
        return str(result)
    else:
        result_string = f'{result_list[2]}{str(result)}'
        # Sending for formatting.
        formatting_content(top_number_initial, bottom_number_initial, multiplied, new_result[::-1])
        return result_string


def multiplying_logic(top_number, bottom_number):
    answer = ''
    value = ''
    for x in reversed(range(0, len(top_number))):
        if value.isalnum():
            sum_value = int(value)
        else:
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


def sum_logic(initial_list):
    another_list = []
    for number in initial_list:
        another_list.append(int(number))
    result = 0
    for index in reversed(range(0, len(another_list))):
        result += another_list[index]

    return result


# This function, add zeros to the end of each number.
def adding_zeros(values):
    prepare_to_sum = []
    for index, value in enumerate(values):
        if index >= 1:
            adding_zero = index * '0'
            value = value + adding_zero
            prepare_to_sum.append(value)
        else:
            prepare_to_sum.append(value)
    return prepare_to_sum


def check_signal(x, y):
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


def check_float_index(string_number):
    if '.' in string_number[::-1]:
        return string_number[::-1].index('.')
    else:
        return 0


def formatting_content(x, y, list_for_add, result):
    list_1 = sorted([x, y], reverse=True)
    result_length = len(result)
    # Getting the length from each number from list_1, after sorted reverse.
    length_x = len(list_1[0])
    length_y = len(list_1[1])

    # Getting the difference.
    length = length_x - length_y

    print(' ' * (result_length - length_x), list_1[0])
    print('x', f'{list_1[1]}'.rjust(result_length - 1))
    print('-' * (result_length + 1))

    for index in range(len(list_for_add)):
        print(f'{list_for_add[index]} {(" " * index)}'.rjust(result_length + 2))

    print('-' * (result_length + 1))
    print('', result)


if __name__ == '__main__':
    multiplication('2.5', '2.5')
    print('')
    print('')
    print('')

    multiplication('-98765', '-12345')
    print('')
    print('')
    print('')

    multiplication('20.2', '2.2')
    print('')
    print('')
    print('')

    '''
    multiplication('-98765', '-12345')
    print('')
    print('')
    print('')

    multiplication('594', '-3242343')
    print('')
    print('')
    print('')
    '''

    # multiplication('2', '2.5')
    # multiplication('59454545454545', '32423433454')
