# closure'u hatırlatan bazı örnekler
def ilk_func(msg):
    print(msg)    
 
ilk_func("Merhaba")
 
ikinci = ilk_func
ikinci("Merhaba")
 
print(id(ilk_func))
print(id(ikinci))

def arttir(x):
    return x + 1
 
def azalt(x):
    return x - 1
 
def islem(func, x):
    result = func(x)
    return result
 
print(islem(arttir, 4))
print(islem(azalt, 4))

def cagrilan():
    def donen():
        print("Merhaba")
    return donen
 
yeni = cagrilan()
yeni()

# decorator
#bn: decorator, bir fonksiyonu alıp yeni fonksiyonellikler ekler ve döndürür.
#bn: orijinal fonksiyonu değiştirmez
def fonksiyon():
    print("Ana fonksiyon")

def decorator_ornek(func):
    def ic_fonksiyon():
        print("Decorate durum")
        return func()
    return ic_fonksiyon

fonksiyon() # Ana fonksiyon
nesne = decorator_ornek(fonksiyon)
nesne() # Decorate durum \n Ana fonksiyon

#
def print_func():
    print("hey")

def decorator_func(func) :
    def wrapper_func():
        print(f"the name of the function is {func.__name__}")
        return func()
    return wrapper_func

decorated_print = decorator_func(print_func)
decorated_print() # the name of the function is print_func \n hey

#bn: @func
#bn: @func yapinca aslinda fonksiyonumuzu func'a input olarak veriyoruz
@decorator_func #gn: şununla ayni => print_func = decorator_func(print_func)
def print_func():
    print("hey")

print_func() # the name of the function is print_func \n hey

#
def func(name, number):
    print(f"Name: {name}, number: {number}")
func("jack", 102) # Name: jack, number: 102

#
def decorator_func(func):
    def wrapper_func(*args):
        print(f"the name of the function is {func.__name__}")
        return func(*args)
    return wrapper_func

@decorator_func #func = decorator_func(func)
def func(name, number):
    print(f"Name: {name}, number: {number}")

func("Jack", 102)

#
def akilli_bolme(func):
    def inner(a,b):
        print("Bölme işlemi: ", a, "and" , b)
        if b == 0:
            print("Hoooppp, böyle bir bölme olmaz.")
            return
        return func(a,b)
    return inner
 
@akilli_bolme
def bol(a,b):
    return a/b
 
print(bol(2,5))
print(bol(0,5))
print(bol(2,0))