num = int(input())
count = 0
new = num

while True:
    front = new // 10 #앞에자리
    back = new % 10 #뒤에자리
    sum = (front + back) % 10 
    new = (back * 10) + sum
    count += 1
    if(num == new):
        break
print(count)