#
print(float(5)) # 5.0
print(int(5.4)) # 5
aa = 5
bb = 5.4
print(float(aa)) # 5.0
print(int(bb)) # 5

#
aaa = "5"
bbb = "5.4"
print(aaa) # 5 (type = string)
print(float(aaa)) # 5.0 (type = float)
print(bbb) # 5.4 (type = string)
print(int(float(bbb))) # 5 (type = int)
# print(int(bbb)) = hata verir, direkt int'e çevirilemez
aaa = int(aaa)
print(type(aaa)) # int
print(aaa) # 5

#
x = input("Bir sayi girin: ")
print(type(x)) # str (string)
y = int(input("Bir sayi girin: "))
print(type(y)) # int (integer)

#
name = input("İsim giriniz: ")
surname = input("Soyisim giriniz: ")
print(name + " " + surname)

# 1.25 değerini girersek sirayla şu işlemler gerçekleşiyor => 1.25(str) -> 1.25(float) -> 1(int) -> 1 * 4 = 4(int)
h = int(float(input("Ondalik bir sayi giriniz: ")))
sonuc = h * 4
print(sonuc) 

# önemli bir istisna
print(0.3 * 3 + 0.1) # 0.999...

# underscore placeholders
#bn: sayılarda daha kolay bir okunulabilirlik için _ kullanılabilir
num1 = 90_000_000_000
num2 = 90000000000
if num1 == num2:
    print("same numbers")

num3 = 0.12_13_14
num4 = 0.121314
if num3 == num4:
    print("same numbers")

# f-string
#bn: degiskenlerin degerlerini direkt olarak string'lerin içine koymak isteyebiliriz.
#bn: f-string de yaptigimiz tek sey aslinda degiskenlerin degerlerini veya hesaplamalarin sonucunu string'in icine gömmek.
#bn: f"..." diye görecegimiz yapiya String Interpolation denir
x = 2
print("x'in degeri" + " " + str(x)) # x'in degeri 2
print(f"x'in degeri {x}")           # x'in degeri 2

#bn: süslü parantezin içi hesaplanir ve string'in içine gömülür
print(f"x'in degerinin iki fazlasi {x+2}") # x'in degerinin iki fazlasi 4 #gn: x+2'nin değeri string'in içine gömüldü

isim = input("isim: ")
print(f"verilen isim {isim}") # verilen isim eren

#bn: {}'in içine fonksiyon, liste, dictionary falan filan da yazilabilir
print(f"verilen isim {isim.capitalize()}") # verilen isim Eren

def square(x):
    return x**2
x = 12
print(f"{x} sayisinin karesi {square(x)}") # 12 sayisinin karesi 144