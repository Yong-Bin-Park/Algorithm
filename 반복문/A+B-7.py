num = int(input())

for i in range(1,num+1):
    firstNum, secondNum = map(int, input().split())
    print('Case #'+str(i)+':',firstNum+secondNum)