limit = 100000
is_prime = [True] * (limit + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(limit**0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, limit + 1, i):
            is_prime[j] = False

l = []
for i in range(len(is_prime)):
    if is_prime[i]:
        l.append(i)
print(l)