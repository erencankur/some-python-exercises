import numpy as np

x = np.array([1, 2, 3, 4]) # [1 2 3 4]
type(x) # numpy.ndarray

x = np.array([1, 2, 3, "a"]) # ['1' '2' '3' 'a'] #bn: array'de string olduğu için hepsini stringe çevirdi
type(x) # numpy.ndarray

x = np.array([1, 2, 3, 4.99]) #bn: hepsi float olur
x = np.array([1, 2, 3, 4.99, "a"]) #bn: hepsi string olur

x = np.array ([1, 2, 3, 4.99], dtype = "int32") #bn: hepsi integer olur => 4.99 = 4
x = np. array ([1, 2, 3, 4.99], dtype = "str") #bn: hepsi string olur
#rn: "4.99" str -> float -> int yapmak gerekir yoksa hata verir

np.zeros(10) # [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
np.zeros(10, dtype = float) # [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
np.zeros(10, dtype = int) # [0 0 0 0 0 0 0 0 0 0]
np.zeros(10, dtype = str) # ['' '' '' '' '' '' '' '' '' '']

np.zeros((3, 4)) # [[0. 0. 0. 0.] \n [0. 0. 0. 0.] \n [0. 0. 0. 0.]]
np.zeros([3, 4]) # [[0. 0. 0. 0.] \n [0. 0. 0. 0.] \n [0. 0. 0. 0.]]
np.zeros([3, 4, 5]) # 3 kere np.zeros((4, 5)) oluşturur
np.zeros([3, 4, 5, 6]) # 3 kere 4 kerelik np.zeros((5, 6)) oluşturur

np.full((3, 4), 5) # [[5 5 5 5] \n [5 5 5 5] \n [5 5 5 5]]
np.full((3, 4), "a") # [[a a a a] \n [a a a a] \n [a a a a]]

np.arange(3, 12) # [ 3  4  5  6  7  8  9 10 11]
np.arange(3, 12, 2) # [ 3  5  7  9 11]
np.arange(12, 3, -2) # [12 10  8  6  4]

np.linspace(1, 2) #bn: 1 ve 2'yi dahil edecek şekilde eşit aralıklara böler, default olarak 50 parçaya böler
np.linspace(1, 2, 3) # [1.  1.5 2. ]
np.linspace(1, 2, 3, endpoint = False) # [1.  1.33 1.66 ] #bn: son elemanı dahil etmez

np.random.normal(0, 1, (4, 5)) #bn: (ortalama, standart sapma, array boyutu)
np.random.normal(5, 100, (4, 5))

np.random.randint(1, 10, (3, 4)) #bn: (kaçtan, kaça(son sayı hariç), array boyutu(default olarak 1))
np.random.randint(1, 10)
np.random.randint(1, 10, (3, 4, 5))

d = {}
for _ in range(20000):
    val = np.random.randint(1, 11)
    if val not in d:
        d[val] = 1
    else:
        d[val] += 1
print(d) #bn: 1'den 10'a kadar olan sayıları 20000 kez rastgele çağırır ve görülme sıklığını yazdırır

np.eye(3, 4) #bn: boyutunu belirlediğin şekilde identity (birim) matrix oluşturur
np.eye(4, 4)
np.eye(4) #bn: (4, 4)'e eşit

a = [1, 2, 3]
b = [2, 4, 8]
a + b # [1, 2, 3, 2, 4, 8]
[2, 4, 8] * 3 # [2, 4, 8, 2, 4, 8, 2, 4, 8]
#rn: pythonda listelerde (a * b) işlemi tanımlı olmadığı için yapılamaz ama numpy sayesinde yapabılabilir
a = np.array([1, 2, 3])
b = np.array([2, 4, 8])
a + b # [ 3  6 11]
a * b # [ 2  8 24] #bn: eleman sayısı aynı olmalı
a * 3 # [3 6 9]

x = np.zeros((2, 5, 4))
x.shape # (2, 5, 4)
x.ndim # 3 #bn: parantez içinde kaç tane sayı olduğunu belirtir
x.size # 40 #bn: kaç eleman olduğunu belirtir
x.dtype # float64

a = np.arange(1, 11) # [ 1  2  3  4  5  6  7  8  9 10]
a.shape # (10,)
a.reshape(2, 5) # [[ 1  2  3  4  5] \n [ 6  7  8  9 10]] #bn: array'i güncellemez ve eleman sayısı tutmazsa error verir
a.reshape(-1, 2) #bn: -1 burada eleman sayısına göre değişkenlik gösterir: -1, 2'yi 10'a tamamlamak için 5 değerini alır
a[np.newaxis, :] # [[ 1  2  3  4  5  6  7  8  9 10]] #bn: 1 row, 10 column olacak şekilde dönüştürür
a[np.newaxis, :].shape # (1, 10)
a[:, np.newaxis] # [[ 1] \n [ 2] \n [ 3] ... \n [10]] #bn: 1 column, 10 row olacak şekilde dönüştürür
a[:, np.newaxis].shape
a[:, None] #bn: np.newaxis yerine None da yazılabilir, aynı görevi görür

a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
np.concatenate([a, b]) # [1 2 3 4 5 6 7 8] #bn: a ve b güncellenmez
b = [5, 6, 7, 8.44]
np.concatenate([a, b]) # [1.   2.   3.   4.   5.   6.   7.   8.44]
b = [5, 6, 7, "8"]
np.concatenate([a, b]) # ['1' '2' '3' '4' '5' '6' '7' '8']

c = np.array([[1, 2, 3], [4, 5, 6]]) # [[1 2 3] \n [4 5 6]]
d = np.array([[7, 8, 9], [10, 11, 12]]) # [[ 7  8  9] \n [10 11 12]]
np.concatenate([c, d]) # [[ 1  2  3] \n [ 4  5  6] \n [ 7  8  9] \n [10 11 12]] #bn: dikey olarak ekledi
np.concatenate([c, d], axis = 1) # [[ 1  2  3  7  8  9] \n [ 4  5  6 10 11 12]] #bn: yatay olarak ekledi
#rn: axis = 0 -> dikey, axis = 1 -> yatay (default olarak 0 değerini alır)

a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
np.stack([a,b]) # [[1 2 3 4] \n [5 6 7 8]]
np.stack([a,b], axis = 1) # [[1 5] \n [2 6] \n [3 7] \n [4 8]]
#rn: concatenate() methodu dizileri belirtilen eksende birleştirir
#rn: stack() methodu dizileri yeni bir eksende birleştirir ve sonuç olarak bir yığın oluşturur

l = [10, 20, 30, 40, 50, 60, 70, 80]
np.split(l, [2, 6]) # [array([10, 20]), array([30, 40, 50, 60]), array([70, 80])]
np.split(l, [3, 5]) # [array([10, 20, 30]), array([40, 50]), array([60, 70, 80])]
a = np.array([10, 20, 30, 40, 50, 60, 70, 80])
np.split(a, [3, 5]) # [array([10, 20, 30]), array([40, 50]), array([60, 70, 80])]

a, b = (l, 10)
print(a) # [10, 20, 30, 40, 50, 60, 70, 80]
print(b) # 10
x, y, z = np.split(l, [2,6])
print(x) # [10 20]
print(y) # [30 40 50 60]
print(z) # [70 80]

a = np.arange(12).reshape(4,3)
np.vsplit(a, [2]) # [array([[0, 1, 2], [3, 4, 5]]), array([[ 6,  7,  8], [ 9, 10, 11]])]
np.hsplit(a, [2]) # [array([[ 0,  1], [ 3,  4], [ 6,  7], [ 9, 10]]), array([[ 2], [ 5], [ 8], [11]])]

a = np.array([20, 32, 5, 30, 10])
print(np.sort(a)) # [ 5 10 20 30 32]
print(a) # [20 32  5 30 10]
a.sort()
print(a) # [ 5 10 20 30 32]
#rn: np.sort(a) array'i güncellemez, a.sort() array'i günceller

a = np.array([3, 1, 6, 5, 4, 2])
np.argsort(a) # [1 5 0 4 3 2] #bn: array'in elemanlarının sıralanmış halinin index sıralamasını döndürür
print(a) # [3 1 6 5 4 2]

a = np.arange(12).reshape(4,3)
a[1, 2] = 55
print(a) # [[ 0  1  2] \n [ 3  4 55] \n [ 6  7  8] \n [ 9 10 11]]
a[2] # [6 7 8]
a[1:2] # [[ 3  4 55] \n [ 6  7  8]]
a[::2] # [[0 1 2] \n [6 7 8]]
a[:, 2] # [ 2 55  8 11]
a[1, 1:3] # [ 4 55]
print(a[1:3 ,1:3]) # [[ 4 55] \n [ 7  8]]
#rn: np.arange(12) 0'dan 11'e kadardır, keşke np.arange(1,13) yazsaydım 1'den 12'ye kadar olurdu

#pn: fancy indexing
x = np.arange(1, 15)
idxs = [4, 5, 7, 1]
x[idxs] # [ 5  6  8 2]

a = np.arange(12).reshape(3, 4)
a[0:2, 1] # [1 5]
a[0:2, 1:3] # [[1 2] \n [5 6]]
a[0, [1,3]] # [[1, 3]]
a[0:, [1,3]] # [[ 1  3] \n [ 5  7] \n [ 9 11]]

a = np.arange(20).reshape(4,5)
idx1 = [1,3,2]
idx2 = [3,0,2]
a[idx1,idx2] # [ 8 15 12] #bn: sırayla kesişimlerini alır: 1,3 - 3,0 - 2,2

x = np.arange(14)
x[[1,2,3]] = 20
print(x) # [ 0 20 20 20  4  5  6  7  8  9 10 11 12 13]
x[[1,2,3]] = [100, 200, 300]
print(x) # [  0 100 200 300   4   5   6   7   8   9  10  11  12  13]

#pn: subarray
a = np.arange(1,21).reshape(4,5)
b = a[:2, :3]
c = a[:2, :3].copy()
c[0, 0] = 100
print(c) # [[100   2   3]
         #  [  6   7   8]]
print(b) # [[1 2 3]
         #  [6 7 8]]
print(a) # değişmez
b[0, 0] = 100
print(b) # [[100   2   3]
         #  [  6   7   8]]
print(a) # [[100   2   3   4   5]
         #  [  6   7   8   9  10]
         #  [ 11  12  13  14  15]
         #  [ 16  17  18  19  20]]

#pn: conditional indexing
a = np.arange(1, 10) # [1 2 3 4 5 6 7 8 9]
a < 5 # [ True  True  True  True False False False False False] #bn: eşitliğe uyan elemanlarda True döndürür
a[a < 5] # [1 2 3 4] #bn: eşitliğe uyan elemanları döndürür
b = np. array ([2, 3, 3, 4, 5, 61, 7, 8, 11])
a == b # [False False  True  True  True False  True  True False] #bn: eşit elemanlarda True döndürür
a[a == b] # [3 4 5 7 8] #bn: eşit olan değerleri döndürür, a[a == b] ve b[a == b] aynı şeydir
a[(a<3) | (a>5)] # [1 2 6 7 8 9] #bn: | = or
a[(a<3) & (a>5)] # [] #bn: & = and
a[ ~(a<3) | (a>5)] # [3 4 5 6 7 8 9] #bn: ~ = not
a[ ~( (a<3) | (a>5) ) ] # [3 4 5]

a = np.arange(1,21).reshape(4,5)
a < 7 # [[ True  True  True  True  True]
      #  [ True False False False False]
      #  [False False False False False]
      #  [False False False False False]]
a[a < 7] # [1 2 3 4 5 6]

#pn: sum
a = np.arange(1,21).reshape(4,5)
np.sum(a) # 210
np.sum(a < 5) # 4 #bn: eşitliğe uyan eleman sayısını verir
np.sum(a[a < 5]) # 10 #bn: eşitliğe uyan elemanların toplamını verir
np.sum(a, axis = 0) # [34 38 42 46 50]
np.sum(a, axis = 1) # [15 40 65 90]

#pn: all ve any
a = np.arange(20).reshape(4,5)
a > -1 # [[ True  True  True  True  True]
       #  [ True  True  True  True  True]
       #  [ True  True  True  True  True]
       #  [ True  True  True  True  True]]
np.all(a > -1) # True
np.all(a > 5) # False
np.all(a > 5, axis = 1) # [False, False, True, True]
np.all(a > 5, axis = 0) # [False, False, False, False, False]

np.any(a > -1) # True
np.any(a > 5) # True
np.any(a > 5, axis = 1) # [False  True  True  True]
np.any(a > 5, axis = 0) # [ True  True  True  True  True]