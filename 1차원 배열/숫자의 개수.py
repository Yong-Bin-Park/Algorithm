mul_list = []
new_list = []

A = int(input())
B = int(input())
C = int(input())

mul = A * B * C

while True:   # 먼저 곱한 값을 하나씩 잘라서 배열에 넣는다.
    result = mul % 10
    mul_list.append(result)
    tmp = mul // 10
    mul = tmp
    if mul < 10:
        mul_list.append(mul)
        break

for i in range(10):   # 그 배열에서 0부터 몇개인지 찾아서 새로운 배열에 넣는다.
    new_count = mul_list.count(i)
    new_list.append(new_count)
    print(new_list.pop(0))