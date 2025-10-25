# closure
#bn: outer fonksiyonu çagirdiktan sona bile inner function'in outer function scope'una erisebilmesi
#bn: closure, bir fonksiyonun içinde tanımlanmış fonksiyonun, dışındaki fonksiyonun içinde tanımlanmış değişkenlere +
#bn: dıştaki fonksiyon çağrılmış olsa da erişebilmesidir.
def outer():
    msg = "Hey"
    def inner():
        print(msg)
    return inner()
outer() # Hey

#bn: bu örnek daha önce yaptiklarimizdan farkli degil
#bn: inner function, enclosing scope'a erisip msg degiskenini bastirabildi
def outer():
    msg = "Hey"
    def inner():
        print(msg)
    return inner
f = outer()
print(f) # <function outer.<locals>.inner at 0x104f08280>
#gn: simdi outer function'i çagirmis olduk ve bize içinde tanimlanan inner function'i obje olarak döndürmüs oldu
#gn: function call yapmadigim sürece obje olarak kalacak
f() # Hey

#bn: burada outer function gagrilmis olsa da onun scope'unda tanimlanan degiskene hala erisebiliyoruz
def outer(msg):
    msg = msg
    def inner():
        print(msg)
    return inner
hey_f = outer ("hey")
hey_f() # hey
messi_f = outer ("messi")
messi_f() # messi

#pn: closure'a yeni bir örnek
#bn: 1. closure olmadan
def yaz_msg(msg):
# Dış bir değişken,

    def yaz():
    # İçteki fonksiyondan bu değişkene ulaşılıyor.
        print(msg)

    yaz()

yaz_msg("Merhaba") # Merhaba

#bn: 2. closure ile
def yaz_msg(msg):
 
    def yaz():
        print(msg)
    
    return yaz
 
diger = yaz_msg("Merhaba")
diger() # Merhaba

#pn: esnekliğe bir örnek
def carpma_yap(n):
    def carp(x):
        return x * n
    return carp
 
kere3 = carpma_yap(3)
kere5 = carpma_yap(5)
 
print(kere3(9)) # 27
print(kere5(3)) # 15
print(kere5(kere3(2))) # 30 