# while
x=0
toplam=0
while x<=100:
    toplam+=x
    x+=1
print(toplam) # 5050

# for, in, range
toplam=0
for y in range(101):
    toplam+=y
print(toplam) # 5050

for c in "hey":
    print(c)
#h
#e
#y

z=1
for _ in range(5):
    z*=4
print(z) # 4 üssü 5 = 4 ** 5

# break -> break komutu ile karşilaşildiği zaman sonlandırılır.
j = 0
while j < 10:
    print (j)
    j += 1
    if j == 3:
        break # 0 1 2 (3'e gelince döngü sonlandırılır)

# continue -> continue komutu ile karşilaşildiği zaman döngünün bir sonraki iterasyonuna geçilir.
for i in range(10):
    if i == 3:
        continue
    print(i) # 3 hariç diğer sayilarin çiktisini verir