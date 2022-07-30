num_list = []
for i in range(9):  #9개 정수 받기
    num = int(input())
    num_list.append(num)
    
print(max(num_list))
print(num_list.index(max(num_list))+1)

#백준에서는 틀리게 나옴 -> 답은 나옴 
# for j in range(9): #최댓값 찾기
#     if num_list[j] < num_list[j-1]:
#         max_num = num_list[j-1]
    
# for k in range(9): #최댓값 위치 찾기
#     count += 1
#     if num_list[k] == max_num:
#         break
