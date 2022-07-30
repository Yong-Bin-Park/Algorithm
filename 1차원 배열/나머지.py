num_list = []
new_list = []
count = 0
for i in range(10):
    num = int(input())
    num_list.append(num)
    
    new_num = num_list[i] % 42
    new_list.append(new_num)

new_list = set(new_list)  #중복을 허용하지 않는 자료형 set으로 변환
count_list = list(new_list)  #중복제거 후 다시 리스트형으로 변환
print(len(count_list))