num = int(input())
result = []
for i in range(num):
    word = input()
    first = word[0]
    last = word[-1]
    result.append(first+last)

for j in result:
    print(j)