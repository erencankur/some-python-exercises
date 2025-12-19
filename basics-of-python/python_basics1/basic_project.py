# Bir listeyi düzleştiren (flatten) fonksiyon yazın
# input: [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]
# output: [1, 'a','cat', 2, 3, 'dog', 4, 5]
#bn: isinstance(), bir değişkenin türünün belirtilen olup olmadığını tespit etmeye yarar.
#bn: parantez içinde belirtilen ilk değer değişkenimizdir, ikinci belirtilen ise türdür.
#bn: değişken belirttiğimiz türde ise True, aksi takdirde False döner.
#yn: isisntance()

l1 = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]

def flatten(l):
    l2 = []
    for item in l:
        if isinstance(item, list):
            l2.extend(flatten(item))
        else:
            l2.append(item)
    return l2

print(flatten(l1))

# Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın
# Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün.
# input: [[1, 2], [3, 4], [5, 6, 7]]
# output: [[[7, 6, 5], [4, 3], [2, 1]]

l1 = [[1, 2], [3, 4], [5, 6, 7]]

def reverse(l):
    l2 = l1[::-1] # l2 = [[5, 6, 7], [3, 4], [1, 2]]
    l3 = []
    def reverse2(m):
        for item in m:
            l3.append(item[::-1])
        print(l3)
    reverse2(l2)

reverse(l1)