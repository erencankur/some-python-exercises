sum = 0
for i in range(1,101):
    sum += i
sum **= 2

square = 0
for i in range(1,101):
    square += i**2

print(sum - square)