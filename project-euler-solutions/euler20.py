def fact(n):
    r = 1
    for i in range(1, n+1):
        r *= i

    r2 = 0
    for i in range(len(str(r))):
        r2 += int(str(r)[i])

    print(r2)

fact(100)