new_list = []
num = int(input())
score = list(map(int,input().split()))

for i in range(num):
    new_score = (score[i]/max(score))*100
    new_list.append(new_score)

print(sum(new_list)/num)

#점수를 입력받은 후
#최고점을 찾은 후 점수/M*100 으로 취해준 후
#새로운 값으로 평균 구하기