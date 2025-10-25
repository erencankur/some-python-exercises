# parantez kullanilirsa daha okunulur olur
# ister parantez kullan, ister kullanma
print(not 5 == 5) # False
print(not (5 == 5)) # üsttekinin aynisi
print(5 != 5 and 3 >= 2) # False
print((5 != 5) and (3 >= 2))
print(5 != 5 or 3 >= 2) # True
print((5 != 5) or (3 >= 2))

#
x = int(input("Bir sayi girin: "))
if (x % 3 == 0) and (x % 2 == 0):
    print("Sayi 2 ve 3'e bölünüyor")
elif (x % 3 == 0) or (x % 2 == 0):
    print("Sayi 2 ve 3'ten sadece birine bölünüyor")
else:
    print("Sayi 2 veya 3'ten herhangi birine bölünmüyor")
print("EN BUYUK FENER") # if bloklarindan bağimsiz

#
cevap = input("x in degeri 2 olsun mu?/ne/h: ")
x = 2 if cevap == "e" else 0
print("x=" + str(x))

cvp = input("y in degeri 2 olsun mu?/ne/h: ")
condition = cvp == "e"
y = 2 if condition else 0
print("y=" + str(y)) # üsttekinin aynisi