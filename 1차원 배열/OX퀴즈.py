quiz_list = []
new_list = []
result_list = []
count = 0
result = 0
num = int(input())
for i in range(num):
    quiz = input()
    quiz_list.append(quiz)

for j in quiz_list:
    new_list.append(list(j))
    for k in new_list:
        for j in k:
            if j == 'O':
                count += 1
            elif j == 'X':
                for _ in range(1,count+1):
                    result += _
                count = 0
        for _ in range(1,count+1):
            result += _    
        result_list.append(result)
        result = 0
        count = 0
                      
for i in result_list[-num:]:
    print(i)