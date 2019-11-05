def factorial(numStr):
    num = int(numStr)
    answer = 1
    for i in range(1, num+1):
        answer *= i
    return answer


def toBinary(numStr):
    num = int(numStr)
    answer = ""
    while num > 0:
        r = num % 2
        answer += str(r)
        num = num // 2
    answer = answer[::-1]
    return answer


def toDec(numStr):
    numStr = str(numStr)
    answer = 0
    position = 1
    for i in range(len(numStr)):
        if numStr[-1-i] == '1':
            answer += position
        position *= 2
    return answer
