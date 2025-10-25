l = [1, 2]
for _ in range(100):
    newNumber = l[-1] + l[-2]
    l.append(newNumber)
    if newNumber >= 4000000:
        break

result = 0
for i in l:
    if i % 2 == 0:
        result += i

print("Fibonacci: ", l)
print("Sum: ", result)