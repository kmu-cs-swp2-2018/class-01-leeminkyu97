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


def toRoman(numStr):
    romanList = [('D', 500), ('CD', 400), ('C', 100), ('L', 50),
                 ('XL', 40), ('X', 10), ('V', 5), ('IV', 4), ('I', 1)]
    num = int(numStr)
    count = 0
    answer = ''
    while num > 0:
        if num - romanList[count][1] >= 0:
            answer += romanList[count][0]
            num -= romanList[count][1]
        else:
            count += 1
    return answer


def romanToDec(numStr):
    answer = 0
    romanDict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i in range(0, len(numStr)):
        if i == 0 or romanDict[numStr[i]] <= romanDict[numStr[i - 1]]:
            answer += romanDict[numStr[i]]
        else:
            answer += romanDict[numStr[i]] - 2 * romanDict[numStr[i - 1]]
    return answer
