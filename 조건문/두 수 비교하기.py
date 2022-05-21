#int형으로 받아야하므로 map()안에 넣어주면 input, split모두 int형으로 바꿀 수 있음
firstNum,secondNum = map(int, input().split())

if firstNum > secondNum:
    print('>')
elif firstNum < secondNum:
    print('<')
else:
    print('==')