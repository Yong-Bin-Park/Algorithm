# 입력
# 첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다. 
# 각 테스트 케이스는 반복 횟수 R(1 ≤ R ≤ 8), 문자열 S가 공백으로 구분되어 주어진다. S의 길이는 적어도 1이며, 20글자를 넘지 않는다. 

# 출력
# 각 테스트 케이스에 대해 P를 출력한다.

num = int(input())
result_list = []
for i in range(num):
    x, word = input().split()
    tmp = ''
    for j in list(word):
        tmp += j*int(x)
    result_list.append(tmp)

for k in result_list:
    print(k)