# 입력
# 첫째 줄에 상근이가 칠판에 적은 두 수 A와 B가 주어진다. 두 수는 같지 않은 세 자리 수이며, 0이 포함되어 있지 않다.

# 출력
# 첫째 줄에 상수의 대답을 출력한다.

first, second = input().split()

reversed_first = first[::-1]
reversed_second = second[::-1]

if int(reversed_first) > int(reversed_second):
    print(reversed_first)
else:
    print(reversed_second)