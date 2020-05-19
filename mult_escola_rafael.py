def multiplication(top_number_initial, bottom_number_initial):
    result_list = check_signal(top_number_initial, bottom_number_initial)
    top_number = result_list[0]
    bottom_number = result_list[1]

    bottom_number = bottom_number[::-1]
    multiplied = []
    for x in bottom_number:
        multiplied.append(multiplying_logic(top_number, x))
    result = adding_zeros(multiplied)

    result = sum_logic(result)

    if result_list[2] == '+':
        # Sending for formatting.
        # formatting_content(top_number_initial, bottom_number_initial, multiplied, str(result))
        return str(result)
    else:
        result_string = f'{result_list[2]}{str(result)}'
        # Sending for formatting.
        # formatting_content(top_number_initial, bottom_number_initial, multiplied, result_string)
        return result_string


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


def inverting_number_of_list(list_of_numbers):
    x = []
    for numbers in list_of_numbers:
        x.append(int(numbers))

    x = sorted(x, reverse=True)
    new_list = []
    for numbers in x:
        new_list.append(str(numbers)[::-1])
    return new_list


def formatting_content(x, y, list_for_add, result):
    list_1 = sorted([x, y], reverse=True)
    result_length = len(result)
    # Getting the length from each number from list_1, after sorted reverse.
    length_x = len(list_1[0])
    length_y = len(list_1[1])

    # Getting the difference.
    length = length_x - length_y

    print(' ' * (result_length - length_x), list_1[0])
    print('x', f'{list_1[1]}'.rjust(result_length-1))
    print('-' * (result_length + 1))

    for index in range(len(list_for_add)):
        print(f'{list_for_add[index]} {(" "*index)}'.rjust(result_length+2))

    print('-' * (result_length + 1))
    print('', result)


if __name__ == '__main__':
    multiplication('999999999999999', '8888888888888')
    print('')
    print('')
    print('')
    multiplication('-98765', '-12345')
    print('')
    print('')
    print('')
    multiplication('594', '-3242343')
    # multiplication('59454545454545', '32423433454')
