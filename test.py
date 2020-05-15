def multiplication(multiplicador, multiplicando):
    mm = multiplicando[::-1]
    multiplied = []
    for x in mm:
        multiplied.append(logic_of_multipling(multiplicador, x))

    making_sum(multiplied)


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
def making_sum(values):
    prepare_to_sum = []
    for index, value in enumerate(values):
        if index >= 1:
            adding_zero = index * '0'
            value = value + adding_zero
            prepare_to_sum.append(value)

    for index, value in enumerate(prepare_to_sum):
        


if __name__ == '__main__':
    multiplication('9990', '120')
