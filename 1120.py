# provavelmente tem algum jeito bem melhor de resolver isso

while True:
    wrongNum, typedNum = input().split()
    if wrongNum == '0' and typedNum == '0':
        break
    finalResult = ''
    for number in typedNum:
        if number != wrongNum:
            finalResult += number
    flag = False
    if finalResult == '':
        finalResult = '0'
    else:
        for number in finalResult:
            if number != '0':
                flag = True
                break
    if not flag:
        finalResult = '0'
    else:
        finalResult = finalResult.lstrip('0')
    print(finalResult)