digits = int(input("number of digits: "))
largest = 0
for i in range(10 ** (digits-1), 10 ** digits):
    for j in range(i, 10 ** digits):
        x = i * j
        if (str(x) == str(x)[::-1]) and (x > largest):
            largest = x
            a = i
            b = j
print(a, "*", b, "=", largest)