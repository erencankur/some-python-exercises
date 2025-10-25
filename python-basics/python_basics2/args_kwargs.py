# *args
#bn: degisken sayili parametre vermenin bir yoludur.
#bn: list/tuple objelerini unpack yapar ama dictionary objelerini yapmaz
#bn: sınırsız sayıda parametreli fonksiyon oluşturmak için parametrenin önüne * koyulur
def rakamlari_goster(*rakamlar):
    print(rakamlar)
 
rakamlari_goster(1,2,3,4) # (1, 2, 3, 4)
rakamlari_goster(15,'burak') # (15, 'burak')

#bn: eğer *args kullanmazsak liste veya benzeri bir şey kullanmamız gerekir
def sum(n):
    print(n) # [1, 2, 3, 4]
    print(type(n)) # list
    res = 0
    for e in n:
        res += e
    return res
numbers = [1, 2, 3, 4]
print(sum(numbers)) # 10
#rn: print(sum(1, 2, 3, 4)) gibi fonksiyonlarda birden fazla parametre kullanırsak error verir, bunun çözümü *args kullanmaktır

#bn: *args kullanırsak liste yapmak yerine elemanları tek tek girebiliriz
def sum(*n):
    print(n) # (1, 2, 3, 4)
    print(type(n)) # tuple
    res = 0
    for e in n:
        res += e
    return res
print(sum(1, 2, 3, 4)) # 10
#rn: print(sum(numbers)) error verir
#bn: ancak *args'ta da liste falan girmek yerine eleman girmek gerekir

def sum_2(*args) :
    res = 0
    print(args) # ([1, 2],)
    print(type(args)) # tuple
    print(len(args)) # 1
    for e in args:
        for j in e:
            res += j
    return res
print(sum_2([1, 2])) # 3

# **kwargs
#bn: fonksiyona degisken sayida keyword argument verilebilmesini sağlar
def fonksiyon1(**parametre):
    print(parametre)
 
fonksiyon1(deger1='Burak', deger2=20) # {'deger1': 'Burak', 'deger2': 20}
fonksiyon1(deger1='Burak', deger2=20, deger3=True, deger4=15.2) # {'deger1': 'Burak', 'deger2': 20, 'deger3': True, 'deger4': 15.2}

def students(**kwargs):
    for v in kwargs.values():
        print(v)
students(name = "Jake", student_number = "401")
# Jake
# 401

def students(**students):
    print(students)
    for v in students:
        print(v)
students(name = "Jake", student_number = "401")
# {'name': 'Jake', 'student_number': '401'}
# name
# student_number

# *args and **kwargs together
#bn: önce *args, sonra **kwargs yazılır
def weird(*args,**kwargs) :
    res = 0
    for e in args:
        res += e
    print(res)
    for k,v in kwargs.items() :
        print(k,":", v)
    return res
weird(1, 2, 3, name="Ferdi", student_number=1907)
# 6
# name : Ferdi
# student_number : 1907

# Unpacking
l=[1, 2, 3, 4]
print(l) # [1, 2, 3, 4]
print(*l) # 1 2 3 4

l1=[1, 2, 3, 4]
l2=[1, 14]
print(l1, l2) # [1, 2, 3, 4] [1, 14]
print(*l1, *l2) # 1 2 3 4 1 14

d1 = {"name": "Jake", "number": 402}
d2 = {"last_name": "Sky", "grade": 74}
merged_d = {**d1, **d2}
print(merged_d) # {'name': 'Jake', 'number': 402, 'last_name': 'Sky', 'grade': 74}

#bn: dictionary'lerde en son ekleneni ekler
d1 = {"name": "Jake", "number": 402}
d2 = {"name": "Sky", "grade": 74}
d3 = {"name": "B", "grade": 45}
merged_d = {**d1, **d2, **d3}
print(merged_d) # {'name': 'B', 'number': 402, 'grade': 45}

str_list = [*"hey this is a string"]
print(str_list) # ['h', 'e', 'y', ' ', 't', 'h', 'i', 's', ' ', 'i', 's', ' ', 'a', ' ', 's', 't', 'r', 'i', 'n', 'g']
str_list = [*"hey"]
print(str_list) # ['h', 'e', 'y']