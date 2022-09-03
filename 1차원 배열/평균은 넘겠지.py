num = int(input())
score = []
for i in range(num):
    score.append(list(map(int,input().split())))

avg_list = []
count = 0    
for i in score:
    avg = sum(i[1:]) / i[0]
    for j in i[1:]:
        if j > avg:
            count += 1
    avg_2 = count / i[0] * 100
    avg_list.append(avg_2)
    count = 0
    
for i in avg_list:
    print(f'{i:.3f}%')