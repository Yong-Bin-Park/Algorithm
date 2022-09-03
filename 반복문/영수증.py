total_price = int(input())
num = int(input())

sum = 0
for i in range(num):
    price, num_p = map(int,input().split())
    tmp = price * num_p
    sum += tmp
    
if total_price == sum:
    print('Yes')
else:
    print('No')
