# generators
#bn: Generator'lar bütün cevabi hafizada tutmazlar, biz sordukça degerleri döndürürler
#bn: Generator'lar iterator'dir, next ile sonraki degerlerine erisebiliriz

#gn: fonksiyon kullanarak
def square(l):
    res = []
    for e in l:
        res.append(e*e)
    return res

l = [1, 2, 3]
print(square(l)) # [1, 4, 9]

#gn: generator kullanarak
def square_generator(l) :
    for e in l:
        yield e*e

l= [1,2,3]
g = square_generator(l)
print(next(g)) # 1
print(next(g)) # 4
print(next(g)) # 9
#gn: bir daha next(g) yazarsam exhaust olur (StopIteration verir)

#bn: bastan baslamak istiyorsam bir daha yaratmam gerekir
g = square_generator(l)
for res in g:
    print(res) # 1 \n 2 \n 3

#pn: list comprehension olusturur gibi generator olusturma
#gn: klasik hareketimiz
l = [x*x for x in [1,2,3,4,5]]
print(l) # [1, 4, 9, 16, 25]

#gn: generoter kullanarak
g = (x*x for x in [1,2,3,4,5])
print(next(g)) # 1
print(next(g)) # 4

for e in g:
    print(e) # 9 \n 16 \n 25 #gn: önceden next(g) yazdığım için kaldığı yerden devam etti, istersen bi yeniden başlativer

#pn: generator'i list'e dönüstürme
g = (x*x for x in [1,2,3,4,5])
print(list(g)) # [1, 4, 9, 16, 25]

l = [1,2,3,4,5,6]
g = square_generator(l)
print(list(g)) # [1, 4, 9, 16, 25, 36]

#pn: generators
#bn: kisa yoldan iterator yaratmamiza olanak saglar
#bn: generator'lar istenildiginde elemanlari döndürdükleri için hafiza sorununa çözüm olur
#bn: list(generator) yaptığımız zaman bu özelliğini kaybeder

#pn: generator exercises
# range() benzeri fonksiyon olusturma
#bn: yield'a gelince generator durur, next(g) yapınca yield'dan sonrasını çalıştırır
def range_generator (start, end, step) :
    current = start
    while current < end:
        yield current
        print("x")
        current += step

r = range_generator(1, 20, 3)

print(next(r)) # 1
print(next(r)) # x \n 4
print(next(r)) # x \n 7
print(next(r)) # x \n 10
print(next(r)) # x \n 13
print(next(r)) # x \n 16
print(next(r)) # x \n 19
#gn: bir daha next(g) yazarsam exhaust olur (StopIteration verir)