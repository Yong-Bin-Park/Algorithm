num = int(input())
result = []

for i in range(num):
    firstNum, secondNum = map(int, input().split())
    sum = firstNum + secondNum
    result.append(sum)

for i in range(num):
    print(result.pop(0))