firstNum,secondNum = map(int, input('두 개의 정수를 입력하세요.').split())

if firstNum > secondNum:
    print('>')
elif firstNum < secondNum:
    print('<')
else:
    print('==')