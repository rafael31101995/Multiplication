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


if __name__ == '__main__':
    multiplication('99999', '123')