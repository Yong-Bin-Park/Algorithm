import sys
num = int(sys.stdin.readline())

for i in range(num):
    firstNum, secondNum = map(int, sys.stdin.readline().split())
    print(firstNum+secondNum)