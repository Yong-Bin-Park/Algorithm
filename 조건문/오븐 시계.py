hour, min = input().split()
cook_min = int(input())
hour = int(hour)
min = int(min)

plus_hour = cook_min / 60
plus_hour = int(plus_hour)
cook_min %= 60
hour = hour + plus_hour
min = min + cook_min

if min >= 60:
    hour += 1
    min -= 60
if hour >= 24:
    hour -= 24
    
print(hour,min)