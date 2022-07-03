hour, min = input().split()
hour = int(hour)
min = int(min)

if min < 45:
    if hour > 0:
        hour -= 1
    elif hour == 0:
        hour += 23
    min = 60 - (45 - min)
    print(hour, min)
else:
    min -= 45
    print(hour, min)