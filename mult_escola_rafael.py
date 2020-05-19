def multiplication(top_number, bottom_number):
    result_list = check_signal(top_number, bottom_number)
    top_number = result_list[0]
    bottom_number = result_list[1]

    bottom_number = bottom_number[::-1]
    multiplied = []
    for x in bottom_number:
        multiplied.append(multiplying_logic(top_number, x))
    result = adding_zeros(multiplied)

    x = True
    while x:
        result = sum_logic(result)
        if len(result) == 1:
            x = False
    if result_list[2] == '+':
        # Sending for formatting.
        formatting_content(top_number, bottom_number, multiplied, result[0])
        return result[0]
    else:
        result_string = f'{result_list[2]}{result[0]}'
        # Sending for formatting.
        formatting_content(top_number, bottom_number, multiplied, result_string)
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


def formatting_content(x,y, list_for_add, result):
    list_1 = sorted([x, y[:: -1]], reverse=True)
    result_length = len(result)

    # Getting the length from each number from list_1, after sorted reverse.
    length_x = len(list_1[0])
    length_y = len(list_1[1])

    # Getting the difference.
    length = length_x - length_y

    print(' '*((result_length - length_x)-1), list_1[0])
    print('x', ' '*((result_length - length_y)-3), list_1[1])
    print('-'*result_length)

    

    print(result)


if __name__ == '__main__':
    multiplication('100', '2000')
