def collatz(x):
    if x % 2 == 0:
        return x // 2
    else:
        return 3 * x + 1

def steps(x):
    step = 1
    sequence = []
    while x != 1:
        sequence.append(x)
        x = collatz(x)
        step += 1
    sequence.append(1)
    return step, sequence

max_steps = 0
biggest_number = 0
sequence_max = []

for x in range(1,1000001):
    n, sequence = steps(x)
    if n > max_steps:
        max_steps = n
        biggest_number = x
        sequence_max = sequence

print("the starting number that produces the longest chain: ", biggest_number)
print("number of steps: ", max_steps)
result = " -> ".join(map(str, sequence_max))
print(result)