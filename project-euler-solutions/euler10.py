limit = 2000000
is_prime = [True] * (limit + 1)  #bn: Asalları takip eden bir liste oluştur
is_prime[0] = is_prime[1] = False  #bn: 0 ve 1 asal değildir

# Eleme işlemi
for i in range(2, int(limit**0.5) + 1):  #bn: Yalnızca kareköküne kadar döngü yap
    if is_prime[i]:  #bn: Eğer i asalsa, onun katları asal olamaz
        for j in range(i * i, limit + 1, i):  #bn: i'nin kuvvetlerini işaretle
            is_prime[j] = False

prime_sum = 0
for i in range(len(is_prime)):
    if is_prime[i]:
        prime_sum += i
print(prime_sum)