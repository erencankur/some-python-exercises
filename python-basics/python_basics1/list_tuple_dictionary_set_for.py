# list mantiği
notlar = [25, 40, 80, 55, 72]
print(len(notlar)) # 5
notlar[1] -= 1
for i in range(len(notlar)):
    notlar[i] += i+1
print(notlar) # [26, 41, 83, 59, 77]
print(notlar[2:4]) # [83, 59]

# listedeki elemanlari değiştirme
#bn: listeye eklenen ve çikarilan elemanlarin sayisi birbirine eşit olmak zorunda değildir
#bn: sadece bir tane eleman eklenilecekse köşeli parantez kullanmak ZORUNLUDUR
#bn: birden fazla eleman eklenilecekse köşeli parantez kullanmak ZORUNLU DEĞILDIR
notlar = [25, 40, 80, 55, 72]
notlar[2:4] = 10, 14
notlar[2:4] = [10, 14] # üsttekiyle ayni
print(notlar) # [25, 40, 10, 14, 72]


notlar[2:4] = [12]
print(notlar) # [25, 40, 12, 72]

notlar[:] = []
print(notlar) # [] = liste boşaltildi

notlar[:] = 1, 2, 5
print(notlar) # [1, 2, 5]

# listenin sonuna sadece bir tane eleman ekleme #yn: append()
l=[19,0]
l.append(7)
print(l) # [19, 0, 7]

# listenin sonuna birden fazla eleman ekleme #yn: extend()
l.extend([19, 14, 16])
print(l) # [19, 0, 7, 19, 14, 16]

# listede istediğin yere eleman ekleme #yn: insert()
#bn: geldiği indexteki eleman ve sağindaki elemanlar birer eleman sağa kayar 
l.insert(0, 20)
print(l) # [20, 19, 0, 7, 19, 14, 16] #gn: 20'yi 0. indexe koydu, sağindaki elemanlar birer eleman sağa kaydi
l.insert(3, 14)
print(l) # [20, 19, 0, 14, 7, 12, 14, 16] #gn: 14'ü 3. indexe koydu, sağindaki elemanlar birer eleman sağa kaydi

# girilen değerdeki ilk elemani listeden silme #yn: remove()
l.remove(14)
print(l) # [20, 19, 0, 7, 19, 14, 16] #gn: ilk 14 yazan elemani sildi

#rn: girilien değerde bir sayi yoksa error verir, bunu try-except ile çözebiliriz
try:
    l.remove (33)
except ValueError:
    pass
print(l) # [20, 19, 0, 7, 19, 14, 16] #gn: girilen değerde bir eleman olmadiği için listede değişiklik olmadi

# girilen indexteki elemani silme ve o indexteki elemanin değerini döndürme #yn: pop()
print(l.pop(2)) # 0
print(l) # [20, 19, 7, 19, 14, 16]

# girilen değerin listede kaç defa göründügü #yn: cost()
print(l.count(19)) # 2
print(l.count(12)) # 0

# liste kopyalama #yn: copy()
#bn:    l2=l           yaparsak l'de değişiklik yaptiğimizda l2'de de ayni değişiklikler OLUR
#bn:    l3=l.copy()    yaparsak l'de değişiklik yaptiğimizda l3'de değişiklik OLMAZ
l2=l
l3=l.copy()
l.append(111)
print(l)  # [20, 19, 7, 19, 14, 16, 111]
print(l2) # [20, 19, 7, 19, 14, 16, 111]
print(l3) # [20, 19, 7, 19, 14, 16]

# listeleri birleştirme (concatenation) #yn: +
l = l2 + l3
print(l) # [20, 19, 7, 19, 14, 16, 111, 20, 19, 7, 19, 14, 16]

# girilen değerdeki ilk elemanin indexini bulma #yn: index()
print(l.index(16)) # 5
#bn: listede olmayan değerler için error verir

# listeyi ters çevirmek #yn: reverse()
#bn: l'yi günceller (inplace)
l.reverse()
print(l) # [16, 14, 19, 7, 19, 20, 111, 16, 14, 19, 7, 19, 20]
#bn: l'nin güncellenmesi istenmiyorsa slicing yapabilabilir
l2=l[::-1] #gn: l2 listesi, l'nin tersine eşitlendi ancak bu olurken l listesinde bir değişiklik olmadi
print(l) # [16, 14, 19, 7, 19, 20, 111, 16, 14, 19, 7, 19, 20]
print(l2) # [20, 19, 7, 19, 14, 16, 111, 20, 19, 7, 19, 14, 16]

# orijinal listeyi GÜNCELLEMEDEN listenin elemanlarini küçükten büyüğe doğru siralama #yn: sorted()
l2=sorted(l)
print(l) # [16, 14, 19, 7, 19, 20, 111, 16, 14, 19, 7, 19, 20]
print(l2) # [7, 7, 14, 14, 16, 16, 19, 19, 19, 19, 20, 20, 111]

# orijinal listeyi GÜNCELLEYEREK (inplace) listenin elemanlarini küçükten büyüğe doğru siralama #yn: sort()
l.sort()
print(l) # [7, 7, 14, 14, 16, 16, 19, 19, 19, 19, 20, 20, 111]
#bn: sorted() ile sort()'un kullanim şekilleri farkli, dikkat et

# farkli type'tan elemanlari beraber siralama
#rn: farkli type'tan elemanlar beraber siralanmaya çalişilirsa error verir, hepsini string yapmak gerekir
l2=["a", "2,5", "b", "1", "f", "3"]
print(sorted(l2)) # ['1', '2,5', '3', 'a', 'b', 'f']

# listenin içindeki listeleri siralama
#bn: sirayla listenin içindeki listelerin ilk sayilarina, ikinci sayilarina, ... bakar
l3=[[1,44,44],[1,2.5,3],[1,44,33]]
print(sorted(l3)) # [[1, 2.5, 3], [1, 44, 33], [1, 44, 44]]

# listenin içindeki listeden eleman seçme
print(l3[0][1]) # 44
print(l3[2][2]) # 33
print(l3[1][1]) # 2.5

#pn: TUPLE
#bn: değiştirilemeyen listelerdir
t=(1, 2, 3)
l=[1, 2, 3]
print(type(t)) # tuple
print(type(l)) # list

# değeri girilen elemanin list'te veya tuple'da olup olmadiğini bulma #yn: in
t=(10, 20, 30)
l=[15, 25, 35]
print(20 in t) # True
print(20 in l) # False

#pn: DICTIONARY
#bn: dictionary yapisinin elemanlarina erismek için belirli key'ler kullanilir ve bunlar da value'lar verir
#bn: dictionary'ler süslü parantez {} ile belirtilir
#bn: dictionary'nin formu {key1: value1, keya: valuea...} seklinde olur
#bn: dictionary'lerin elemanlarina ulasmak için belirlenen key'ler köşeli parantez [] ile kullanilir
#bn: dictionary'lerin key'leri IMMUTABLE bir yapida olur, value'lar ise MUTABLE da IMMUTABLE da olabilir
    #bn: bu yüzden key, list yapisinda olamaz ama tuple yapisinda olabilir
notlar = {"Hasan": 80, "Osman": 72, "Niyazi": 95}
print(len(notlar)) # 3
print(notlar) # {'Hasan': 80, 'Osman': 72, 'Niyazi': 95}
print(notlar["Osman"]) # 72
notlar["Osman"] += 5
print(notlar["Osman"]) # 77

# dictionary içinde dictionary
ogrenciler = {"Oosterwolde": {"not": 80, "ogrenci_no":703}, "Osayi": {"not": 72, "ogrenci_no": 408}}
print(len(ogrenciler)) # 2
print(ogrenciler) # {'Oosterwolde': {'not': 80, 'ogrenci_no': 703}, 'Osayi': {'not': 72, 'ogrenci_no': 408}}
print(len(ogrenciler["Osayi"])) # 2
print(ogrenciler["Osayi"]) # {'not': 72, 'ogrenci_no': 408}
print(ogrenciler["Osayi"]["not"]) # 72
ogrenciler["Osayi"]["not"] -= 8
print(ogrenciler["Osayi"]["not"]) # 64

# dictionary'de eleman ekleme
notlar["Ferdi"] = 7
print(notlar) # {'Hasan': 80, 'Osman': 77, 'Niyazi': 95, 'Ferdi': 7}

# dictionary'de eleman silme #yn: del
del notlar["Niyazi"]
print(notlar)  # {'Hasan': 80, 'Osman': 77, 'Ferdi': 7}

# boş dictionary yaratma
d = {}
print(d) # {}

# bir değerin dictionary'nin key'lerinden biri olup olmadigini sorgulama
#bn: dictionary'de sorgulama yapmak, list ve tuple'larda sorgulama yapmaktan daha hizlidir
print("Ferdi" in notlar) # True
print("Mehmet" in notlar) # False

#pn: SET
#bn: set'leri kümeler olarak düşünebiliriz
#bn: sadece özgün (unique) değerleri tutar
#bn: içerisinde bir eleman var mi yok mu, baska bir setle hangi elemanlari farkli gibi islemleri yapabilir
#bn: dictionary'ler gibi eleman sorgusu yapmak hizlidir
#bn: dictionary'lerde key-value çift olarak bulundugu için ayni uzunluktaki bir set'ten daha fazla yer kaplar
#bn: set'ler mutable'dir
#bn: set'ler sirali değildir
#bn: set'ler indexlenemez
s2 = {1,6,4,2,1,4,5,3}
print(s2) # {1, 2, 3, 4, 5, 6}

# boş set yaratma
s = set()
print(s) # set()
print(type(s)) # set

# listedeki elemanlarla et oluşturma
l = [1,2,3,4,1,2]
s = set(l)
print(s) # {1, 2, 3, 4}
print(len(l)) # 6
print(len(s)) # 4

# set'e eleman ekleme #yn: add()
s.add(9)
print(s) # {1, 2, 3, 4, 9}
s.add(4)
print(s) #{1, 2, 3, 4, 9} #gn: girilen sayi zaten set'te varsa set değişmez, ayrica error da vermez

# set'ten eleman silme #yn: remove(), discard()
s.remove(1)
print(s) # {2, 3, 4, 9} #gn: girilen değerdeki tüm elemanlari siler
#rn: olmayan bir sayi girilirse error verir, bu sorunu çözmek için discard() kullanilir
s.discard(7)
print(s) # {2, 3, 4, 9}
s.add(7)
print(s) # {2, 3, 4, 7, 9}
s.discard(7)
print(s) # {2, 3, 4, 9}

#pn: SETLERDE KÜME MANTIĞI
# iki kümenin farkini alma (difference) #yn: difference(), -
#bn: (s1 - s2) => s1'in s2'den farkli elemanlari
s1 = set ([1,5,10])
s2 = set ([2,5,3])
print(s1.difference(s2)) # {1, 10}
print(s1 - s2) # {1, 10}

# iki kümenin birleşimini alma (union) #yn: union()
#bn: (s1 u s2) => s1 ile s2'nin tüm elemanlari
s1 = set ([1,5,10])
s2 = set ([2,5,3])
print(s1.union(s2)) # {1, 2, 3, 5, 10}

# iki kümenin kesişimini alma (intersection) #yn: intersection(), &, intersection_update()
#bn: (s1 n s2) = s1 - (s1 - s2) => s1 ile s2'nin ortak elemanlari
s1 = set ([1,5,10])
s2 = set ([2,5,3])
print(s1.intersection(s2)) # {5}
print(s1 & s2) # {5}
#bn: intersection_update() komutuyla kesişim yapilarak s1'in degerini s1 ile s2'nin kesişimine günceller
s1.intersection_update(s2)
print(s1) # {5} #gn: s1 = s1.intersection(s2) olur

# iki kümenin farkinin birleşimini alma (symmetric difference) #yn: symmetric_difference()
#bn: (s1 - s2) u (s2 - s1) = (s1 u s2) - (s1 n s2 ) => s1 ve s2'nin birbirinden farkli elemanlari
s1 = set ([1,5,10])
s2 = set ([2,5,3])
print(s1.symmetric_difference(s2)) # {1, 2, 3, 10}

# iki kümenin kesişimini sorgulama (dis joint) #yn: isdisjoint()
#bn: (s1 n s2) = 0 => boş küme olup olmadiğini kontrol eder
#bn: True = boş küme (kesişmiyorlar) / False = boş küme değil (kesişiyorlar)
s1 = set ([1,5,10])
s2 = set ([2,5,3])
s3 = set ([4,6])
print(s1.isdisjoint(s2)) # False
print(s1.isdisjoint(s3)) # True
print(len(s1.intersection(s3)) == 0) # True #gn: s1.isdisjoint(s2) <- AYNI ŞEYLER -> len(s1.intersection(s2)) == 0

# alt küme sorgulama (subset) #yn: issubset()
#bn: s1'in s2'nin alt kümesi olup olmadigini kontrol eder
s1 = set ([1,5,10])
s2 = set ([2,5,3])
s3 = set ([2,5])
print(s1.issubset(s2)) # False
print(s3.issubset(s2)) # True

# üst küme sorgulama (superset) #yn: issuperset()
#bn: s1'in s2'nin üst kümesi olup olmadigini kontrol eder
s1 = set ([1,5,10])
s2 = set ([2,5,3])
s3 = set ([2,5])
print(s1.issuperset(s2)) # False
print(s2.issuperset(s3)) # True

#pn: NON-SCALAR VERI TIPLERINDE FOR
notlar = [90,72,81,77]
t = 0
for i in notlar:
    print(i)
    t += i
print("toplam", t) # toplam 320
ortalama = t / len(notlar)
print("ortalama", ortalama) # 80.0
ortalama 

#gn: ^ AYNI ŞEYLER v

notlar = [90,72,81,77]
t = 0
for i in range(len(notlar)):
    print(notlar[i])
    t += notlar[i]
print("toplam", t) # toplam 320
ortalama = t / len(notlar)
print("ortalama", ortalama) # 80.0
ortalama 

# eleman değiştirme ve continue kullanimi
for i in range(len(notlar)):
    if i == 1:
        continue
    notlar[i] += 5
print(notlar) # [95, 72, 86, 82]

# break kullanimi
l = [2,3,40,100,10,1]
x = 100
for e in range(len(l)):
    print(l[e])
    if l[e] == x:
        print ("Buldum!!")
        break

# dictionary'lerde iterasyon #yn: values(), items()
l = {"student_1": [90,89], "student_2": [80,83], "student_3": [72,74]}
for i in l:
    print(i) # studen_1 studen_2 studen_3

for i in l:
    print(l[i]) # [90, 89], [80, 83], [72, 74]

#gn: ^ AYNI ŞEYLER v

for i in l.values():
    print(i) # [90, 89], [80, 83], [72, 74]

for i,j in l.items():
    print ("key degeri:", i, "value degeri:", j) # key degeri: student_1 value degeri: [90, 89]...

#pn: SPLIT VE JOIN
# belirli bir bölme kriterine göre string'in alt parçalarini listenin elemanlari olarak dönüştürme #yn: split()
#bn: split()'in içine neye göre bölecegimizi yazariz, hiç bir sey yazmazsak default olarak boşluğa göre böler
s = "merhaba nasilsin?"
print(s.split("a")) # ['merh', 'b', ' n', 'silsin?']
s = "elma armut kel mahmut"
print(s.split(" ")) # ['elma', 'armut', 'kel', 'mahmut']
print(s.split())    # ['elma', 'armut', 'kel', 'mahmut']
s = "sari,lacivert,yeşil,beyaz,kirmizi"
print(s.split(",")) # ['sari', 'lacivert', 'yeşil', 'beyaz', 'kirmizi']
ss = s.split(",")
print(ss)           # ['sari', 'lacivert', 'yeşil', 'beyaz', 'kirmizi']

# listenin elemanlari arasina belirtilen yapiyi koyup string'e dönüstürme #yn: join()
#bn: "patern".join(list)
l = ["limon", "portakal", "elma"]
print(l)            # ['limon', 'portakal', 'elma']
print(", ".join(l)) # limon, portakal, elma

#pn: LIST COMPREHENSIONS
#bn: 1'den 10 a kadar olan sayilarin karelerinden bir liste olusturmak istenirse şöyle yapilabilir
squares = []
for i in range (1,11):
    squares.append(i*i)
print(squares) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#bn: bunun aynisi list comprehension kullanarak da yapilabilir
squares = [i * i for i in range(1,11)]
print(squares) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# list comprehension ve fonksiyon mantiğini birleştirme
def square(x):
    return x * x
squares = [square(x) for x in range(1,11)]
print(squares) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# list comprehension'larda conditional yapilari kullanma
odd_squares = []
for x in squares:
    if x % 2 == 1:
        odd_squares.append(x)
print(odd_squares) # [1, 9, 25, 49, 81]

odd_squares = [x for x in squares if x % 2 == 1]
print(odd_squares) # [1, 9, 25, 49, 81]

def square(x):
    return x * x
odd_squares = [square(x) for x in range(1,11) if (x ** 2) % 2 == 1]
print(odd_squares) # [1, 9, 25, 49, 81]

weird_squares = [x if x % 2 == 0 else -1 for x in squares]
print(weird_squares) # [-1, 4, -1, 16, -1, 36, -1, 64, -1, 100]

def is_even (x):
    if x % 2 == 0:
        return True
    if x % 2 == 1:
        return False
ultra_weird_squares = [x if x % 2 == 0 else -1 for x in squares if is_even(x)]
print(ultra_weird_squares) # [4, 16, 36, 64, 100]

# set comprehension
numbers = [1,2,3,4,5,6,7,1,2]
set_numbers = {x for x in numbers if x in [1,2,3,14,15,1,2]}
print(set_numbers) # {1, 2, 3}

# dictionary comprehension
square_dict = {e: (e * e) for e in range (1,11)}
print(square_dict) # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
print(square_dict[5]) # 25

# nested list comprehension
m = [[j for j in range(5)] for i in range(3)]
print(m) # [[0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4]]
print(len(m)) # 3
for n in m:
    print(n) # alt alta, tablo gibi çikti verir

m = [["x" for _ in range(5)] for _ in range(3)]
for row in m:
    print(row) # x'lerden oluşan bir tablo çiktisi verir

m = [[10, 11, 12], [13, 14], [15, 16, 17, 18]]
for l in m:
    print(l) # [10, 11, 12] \n [13, 14] \n [15, 16, 17, 18]

m = [[10, 11, 12], [13, 14], [15, 16, 17, 18]]
new_m = []
for l in m:
    for e in l:
        new_m.append(e)
        print(e) # 10 \n 11 \n 12 \n 13 \n ... #gn: her elemani alt alta yazar
print(new_m) # [10, 11, 12, 13, 14, 15, 16, 17, 18] #gn: her elemani içeren yeni bir liste oluşturulur

#gn: ^ AYNI ŞEYLER v

#bn: matrixi List comprehension ile flat etmek 
m = [[10, 11, 12], [13, 14], [15, 16, 17, 18]]
flatten_m = [e for l in m for e in l]
print(flatten_m) # [10, 11, 12, 13, 14, 15, 16, 17, 18] #gn: her elemani içeren yeni bir liste oluşturulur

flatten_m = [e for l in m for e in l if e % 2 == 0]
print(flatten_m) # [10, 12, 14, 16, 18] #gn: her çift sayi olan elemani içeren yeni bir liste oluşturulur

m = [[[ 25, 36, 62],[ 28, 38, 64],[ 30, 40, 67]],[[ 1, 27, 56],[ 1, 25, 55],[ 2, 21, 51]]]
flatten_m = [i for l in m for e in l for i in e]
print(flatten_m) # [25, 36, 62, 28, 38, 64, 30, 40, 67, 1, 27, 56, 1, 25, 55, 2, 21, 51]

#pn: VARIABLE UNPACKING
(x, y, z) = (1, 2, 3)
print(x, y, z) # 1 2 3
#bn: kullanmayacağin bir veri varsa _ kullanabilirsin
(x, _) = (1, 2)
print(x) # 1 

# eleman sayilari eşit değilse #yn: *
#bn: * kullanirsan tek değer bile olsa liste olur
(x, y, *z) = (1, 2, 3, 4, 5)
print(x, y, z) # 1 2 [3, 4, 5] #gn: istenilen indexteki ve sağindaki elemanlari z'ye eşitledi
print(type(x)) # int
print(type(z)) # list
(x, y, *_) = (1, 2, 3, 4, 5) #gn: ilk iki elemani kullan, gerisini boşver misali
(x, y, *z, t) = (1, 2, 3, 4, 5, 6, 7) #gn: ilk iki elemani ve son elemani kullan, aradakileri z'ye eşitle
print(x, y, z, t) # 1 2 [3, 4, 5, 6] 7

#pn: ENUMERATE
l = [(1,2), (10,20)]
for e in l:
    print(e) # (1, 2) \n (10, 20)
for e in l:
    a, b = e
    print (a)
    print (b)
    print("***") # 1 \n 2 \n *** \n 10 \n 20 \n ***

#gn: ^ AYNI ŞEYLER v

for a, b in l:
    print("tuple' in ilk eleman", a)
    print("tuple 'in ikinci elemani", b)
    print("---")

# aynı anda hem indexi hem de elemanı bulma #yn: enumerate
#bn: enumerate() bize (index, element) olarak verecek
adlar = ['Tyler', 'Blake', 'Cory', 'Cameron']
for e in adlar:
    print(e) #gn: elemanları alt alta yazar

for i, e in enumerate(adlar):
    print(i, "indexindeki eleman:", e) #gn: index numarasını ve elemanları yazar

for i, e in enumerate(adlar, start = 12):
    print(i, "lokasyonundaki eleman:", e) #gn: start yazarak index numarası yerine istediğim sayıdan başlattım

# farkli yapilarin icinde paralel iterasyon yapma #yn: zip()
ogrenciler = ["ogrenci_1", "ogrenci_2", "ogrenci_3"]
notlar = [90,80,72]
for i in range(len(ogrenciler)):
    s = ogrenciler[i]
    g = notlar[i]
    print(s, g) #gn: tek tek öğrencileri ve aldıkları notları yazar

#gn: ^ AYNI ŞEYLER v

for s, g in zip(ogrenciler, notlar):
    print(s, g) #gn: tek tek öğrencileri ve aldıkları notları yazar

# örnek çalışma
satis = [3500.00, 76300.00, 67200.00]
maliyet = [56700.00, 21900.00, 12100.00]
for i in range(len(maliyet)) :
    s = satis[i]
    c = maliyet[i]
    kar = s - c
    print(f"Total profit: {kar}") #gn: tek tek kar miktarını yazar

satis = [3500.00, 76300.00, 67200.00]
maliyet = [56700.00, 21900.00, 12100.00]
for s, c in zip(satis, maliyet) :
    kar = s - c
    print(f'Total profit: {kar}')

# zip() ile dictionary yaratma
keys = ["isim", "soyad", "ulke", "is"]
values = ["Eren", "Cankur", "Türkiye", "Software Engineer"]
d = {}
for i in range(len(keys)):
    k = keys[i]
    v = values[i]
    d[k] = v
print(d) # {'isim': 'Eren', 'soyad': 'Cankur', 'ulke': 'Türkiye', 'is': 'Software Engineer'}

#gn: ^ AYNI ŞEYLER v

d = {}
for k, v in zip(keys, values):
    d[k] = v
print(d) # {'isim': 'Eren', 'soyad': 'Cankur', 'ulke': 'Türkiye', 'is': 'Software Engineer'}