def number_of_divisors(x):
    divider = 0
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            divider += 1
    return divider * 2

n = 1
while True:
    triangle_number = 0
    for i in range(1,n+1):
        triangle_number += i
    if number_of_divisors(triangle_number) > 500:
        print(triangle_number)
        break
    n += 1

#bn: Kareköküne kadar kontrol ediyoruz çünkü bir sayının çarpanları simetriktir. Örneğin, 36 sayısının çarpanları (1, 36), (2, 18), (3, 12), (4, 9), (6, 6) şeklindedir. Bu çarpanlardan sonra simetri tekrar eder. Yani, 36’nın karekökü olan 6’ya kadar tüm bölenleri bulduğumuz zaman geri kalan bölenleri de bulmuş oluruz.