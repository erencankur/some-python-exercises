# fonksiyonlar, kodumuzda abstraction (soyutlama) ve decomposition (problemi küçük parçalara ayirma) (modülerlik) yapmamizi saglar.
def square(x):
    return x * 2
print(square(3)) # 9
a = square(4)
print(a) # 16

def cube(x):
    result = x ** 3
    return result
print(cube(2)) # 8

a = cube(square(2))
print(a) # 64

#bn: fonksiyonun hiçbir inputu olmayabilir
def weird():
    return 5
print(weird()) # 5

#bn: fonksiyonlar return'e geldikten sonrasina bakmiyor, return ün sagina yazilan degeri veriyor ve fonksiyondan çikiyor
def f(x):
    res = x ** 2
    for _ in range (10):
        res += 20
        return res
        print("hey")
print(f(10)) # 120

def f(x):
    res = x ** 2
    for _ in range (10):
        res += 20
    return res
print(f(10)) # 300

def f(x):
    l = []
    res = x * x
    for i in range (10):
        res += 20
        l.append (res)
    return l
print(f(10)) # [120, 140, 160, 180, 200, 220, 240, 260, 280, 300]

# void functions (değer döndürmeyen fonksiyonlar)
def square(x):
    print(x, "in/ün/un karesi:", x ** 2) #gn: x'in karesini değer olarak vermiyor, sadece ekrana bastirttirir
square(3) # 3 in/ün/un karesi: 9
print(square(3)) # None

#bn: hem bir deger bastirip hem de ayni anda o degğri döndürebilir
def square(x):
    res = x ** 2
    print(x, "in/ün/un karesi:", x ** 2)
    return res
square(3) # 3 in/ün/un karesi: 9
print(square(3)) # 9

# birden fazla parametre içeren fonksiyonlar
def power (x, y) :
    return x ** y
print(power(2,3)) # 8

# birden fazla değer döndüren fonksiyonlar
#bn: sonucu tuple olarak döndürür
def f(x):
    return 2*x, 10*x
print(f(10)) # (20, 100)
print(type(f(10))) # tuple


#bn: bu iki değeri farkli değişkenlere eşitleyebilirim
def f(x):
    return 2*x, 10*x
a, b = f(10)
print(a) # 20
print(b) # 100
print(type(a)) # int

def f(x, y):
    return 2*x*y, (10*x)**y
a, b = f(10, 2)
print(a) # 40
print(b) # 10000

# predefined parameters
#bn: aksini belirtilmez ise fonksiyon, predefined degerleri kullanir
#bn: predefined olarak verecegimiz degerleri en sona yazmaliyiz yoksa hata aliriz
def hello(end, start = "Hello"):
    print(start + " " + end)
hello("Osman") # Hello Osman
hello("Osman", start = "Selam") # Selam Osman
hello("Osman", "Selam") # Selam Osman

def power(x, y=1) :
    return x ** y
print(power(3)) # 3
print(power(3,2)) # 9

def f(x, y=1, z=2) :
    return x + y + z
print(f(2)) # 5
print(f(2,3)) # 7
print(f(2,3,4)) # 9

# argümanlarin degerlerinin güncellenip güncellenmedigi durumlar
#bn: integer ve floatlarin degerleri degismez
a = 2
b = 3.5
def f(x):
    x = 4
    return x
print(f(a)) # 4
print(a) # 2
print(f(b)) # 4
print(b) # 3.5

#bn: listlerin değerleri değişir, void function olsa bile
l = [1,2,3]
def f(x):
    x[0] = "a"
    return x
print(f(l)) # ['a', 2, 3]
print(l)    # ['a', 2, 3]

l = [1,2,3]
def f(x):
    x[0] = "a"
print(f(l)) # None
print(l)    # ['a', 2, 3]

# first class function
#bn: Python'da fonksiyonlar, first class function'dır
#bn: fonksiyonlar diger veri tipleri gibi manipüle edilebilir ve baska fonksiyonlara argüman olarak verilebilir.
#bn: bir fonksiyon başka bir degiskene atanabilir
def kare(x):
    return x ** 2
a = kare
print(a(3)) # 9

#bn: bir fonksiyon baska bir fonksiyona argüman olarak verilebilir
def f2(x, f):
    return f(x) + 4
print(f2(3, kare)) # 13

def f3(x):
    return x**5
print(f2(2, f3)) # 36

# fonksiyonları obje olarak kullanma
l=[1, 2, 3, 4]
def apply(l,f):
    for i in range(len(l)):
        l[i]=f(l[i])

def square(x):
    return x**2

print(apply(l, square)) # None
print(l) # [1, 4, 9, 16]

# fonksiyonlar listesini belirli bir degere uygulama
def cube(x):
    return x**3

def apply_funcs(f_list, x):
    l=[]
    for f in f_list:
        l.append(f(x))
    return l
print(apply_funcs([square, cube], 5)) # [25, 125]