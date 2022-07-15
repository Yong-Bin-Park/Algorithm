fnum, snum, tnum = map(int, input().split())

if fnum == snum == tnum:
    result = 10000 + fnum * 1000
    print(result)
elif fnum == snum != tnum:
    result = 1000 + fnum * 100
    print(result)
elif fnum == tnum != snum:
    result = 1000 + fnum * 100
    print(result)
elif fnum != snum == tnum:
    result = 1000 + snum * 100
    print(result)
elif fnum != snum != tnum:
    if fnum > snum:
        if fnum > tnum:
            result = fnum * 100
        else:
            result = tnum * 100
        print(result)
    else:
        if snum > tnum:
            result = snum * 100
        else:
            result = tnum * 100
        print(result)