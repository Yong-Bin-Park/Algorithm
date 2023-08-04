num = int(input())
result = num // 4
long_list = []
for i in range(result):
    i = "long"
    long_list.append(i)
long_list.append("int")
for j in long_list:
    print(j, end=' ')