def factorial(x):
    f = 1
    for i in range(1, x+1):
        f *= i
    return f

result = factorial(40) / (factorial(20) * factorial(20))
print(result)