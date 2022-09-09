def self_num():
    new_list = []
    i = 1
    new = 0
    while i <= 10000:
        num = list(str(i))  #문자열로 만든 후 쪼개서 리스트화
        num_list = list(map(int, num))  #숫자를 문자열로 쪼갠 것들을 정수형으로 변환
        new  = i + sum(num_list)
        new_list.append(new)
        i += 1
    return new_list

new_list = self_num()
for i in range(1,10001):
    if i not in new_list:
        print(i)