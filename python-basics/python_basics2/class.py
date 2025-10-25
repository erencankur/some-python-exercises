# class
#bn: fonksiyonlarda belirli fonksiyonalite ifade eden kodlari bir araya getirmeyi görmüstük +
#bn: class mantiginda hem fonksiyalite hem de veriyi bir arada tutma yoluna bakacagiz
#bn: class'in içerisindeki veri (data) lara attribute, fonksiyonlara method diyecegiz.
#bn: diyelim ki bir is yeri çalisanlari kodumuzda ifade etmek istiyoruz +
#bn: her çalişanin farkli farkli özellikleri (attribute)'lari ve yaptiklari seyler (methodlari) olacak
#bn: fonksiyon tanimlarken def kullaniyorduk, class yaratirken class ile tanimlayacagiz
#bn: class'in içerisinde method yaratirken, classtan yaratilan objeyi methodlar ilk arguman olarak alirlar

#pn: ATTRIBUTE
class Employee:
    pass
e = Employee()
e.a = 4 #gn: e objesine a attribute'u ekledik
print(e.a) # 4

#bn: tek tek belirtmek yerine en basta olugtururken de attribete lari verebiliriz
class Employee:
    def __init__(self, name, last, age, pay):
        self.name = name
        self.last = last
        self.age = age
        self.pay = pay

emp_1 = Employee("Ferdi", "Kadioglu", "24", 1907)
print(emp_1.name) # Ferdi

#pn: method
class Employee:
    def __init__(self, name, last, age, pay):
        self.name = name
        self.last = last
        self.age = age
        self.pay = pay

    def fullname(self):
        print(f"{self.name} {self.last}")
    
emp_1 = Employee("Ferdi", "Kadioglu", "24", 1907)
emp_1.fullname() # Ferdi Kadioglu
Employee.fullname(emp_1) # Ferdi Kadioglu

#pn: CLASS VARIABLE
#bn: Instance Variable: Class'tan yaratilan objelerin kendilerine özgü degiskenleri. Üstteki örnekteki name, last, age, pay gibi
#bn: Class Variable: Class'tan yaratilan tüm objelerde paylasilan degiskenler
#bn: Instance variable her obje için farkli olabilir, ama class variable hepsi için ayni olmak zorunda
class Employee:

    raise_percent=1.05

    def __init__(self, name, last, age, pay):
        self.name = name
        self.last = last
        self.age = age
        self.pay = pay

    def apply_raise(self):
        self.pay *= self.raise_percent

emp_1 = Employee("Ferdi", "Kadioglu", "24", 1907)
print(emp_1.raise_percent) # 1.05
print(emp_1.pay) # 1907
emp_1.apply_raise() #gn: zam uygulandi
print(emp_1.pay) # 2002.3500000000001

#bn: emp_1.raise_percent -> ilk olarak bu instance'a bakar, eger bulamazsa class variable olarak var mi diye bakar
#bn: objenin attribute'larini döndürür
print(emp_1.__dict__) # {'name': 'Ferdi', 'last': 'Kadioglu', 'age': '24', 'pay': 2002.3500000000001}
print(Employee.__dict__)

#
emp_1.raise_percent = 2.5 #gn: sadece 1. çalişanin zam oranini değiştirir
Employee.raise_percent = 2.5 #gn: her çalişanin zam oranini değiştirir

# kaç tane çalisan oldugunu class variable'i olarak tutma
class Employee:

    raise_percent = 1.05
    num_emp = 0

    def __init__(self, name, last, age, pay):
        self.name = name
        self.last = last
        self.age = age
        self.pay = pay
        Employee.num_emp += 1

    def apply_raise(self):
        self.pay *= self.raise_percent

print(Employee.num_emp) # 0
emp_1 = Employee("Ferdi", "Kadioglu", "24", 1907)
emp_1 = Employee("Osayi", "Samuel", "21", 6161)
print(Employee.num_emp) # 2

#pn: CLASS METHOD
#bn: @classmethod, decorator methodu ilk argüman olarak instance almak yerine class'i alacak sekilde günceller
class Employee:

    raise_percent = 1.05
    num_emp = 0

    def __init__(self, name, last, age, pay):
        self.name = name
        self.last = last
        self.age = age
        self.pay = pay
        Employee.num_emp += 1

    def apply_raise(self):
        self.pay *= self.raise_percent

    @classmethod
    def set_raise(cls, amount): #gn: parantez içindeki ilk eleman ne yazarsan yaz Employee'yi temsil eder
        cls.raise_percent = amount

emp_1 = Employee("Ferdi", "Kadioglu", "24", 1000)
emp_2 = Employee("Osayi", "Samuel", "21", 5000)
print(emp_1.raise_percent) # 1.05
Employee.set_raise(1.6)
print(emp_1.raise_percent) # 1.6
emp_2.set_raise(2.2)
print(emp_1.raise_percent) # 2.2

# alternative constructor
#bn: class'i olustururken input olarak str verilir ve bundan name, age gibi bilgiler çikarilmasi lazimsa aşağidaki gibi yaplablr
emp_1_str = "Ferdi-Kadioglu-24-1000"
name, last, age, pay = emp_1_str.split("-")
emp_1 = Employee(name, last, age, pay)
print(emp_1.name) # Ferdi

#bn: daha iyi bir yöntem
class Employee:

    raise_percent = 1.05
    num_emp = 0

    def __init__(self, name, last, age, pay):
        self.name = name
        self.last = last
        self.age = age
        self.pay = pay
        Employee.num_emp += 1

    def apply_raise(self):
        self.pay *= self.raise_percent

    @classmethod
    def set_raise(cls, amount): #gn: parantez içindeki ilk eleman ne yazarsan yaz Employee'yi temsil eder
        cls.raise_percent = amount

    @classmethod
    def from_string(cls, emp_str): #gn: parantez içindeki ilk eleman ne yazarsan yaz Employee'yi temsil eder
        name, last, age, pay = emp_1_str.split("-")
        return cls(name, last, int(age), float(pay)) #gn: yeni çalişan yaratacak ve döndürecek

emp_1_str = "Ferdi-Kadioglu-24-1000"
emp_1 = Employee.from_string(emp_1_str)
print(emp_1.pay) # 1000.0

#pn: STATIC METHOD
#bn: Regular method'lar (ilk ), class'in instance'ini (olusturulan objeyi) methodlara otomatikmen argüman olarak verir (self olarak)
#bn: Class methodlari, ise class'i otomatikmen argüman olarak verir
#bn: Static methodlar otomatik olarak bir sey vermeyen methodlar olacak.
#bn: Instance veya class'a methodun icerisinde erisim olmuyorsa static olarak tanimlamak daha iyi olabilir
class Employee:

    raise_percent = 1.05
    num_emp = 0

    def __init__(self, name, last, age, pay):
        self.name = name
        self.last = last
        self.age = age
        self.pay = pay
        Employee.num_emp += 1

    def apply_raise(self):
        self.pay *= self.raise_percent

    @classmethod
    def set_raise(cls, amount): #gn: parantez içindeki ilk eleman ne yazarsan yaz Employee'yi temsil eder
        cls.raise_percent = amount

    @classmethod
    def from_string(cls, emp_str): #gn: parantez içindeki ilk eleman ne yazarsan yaz Employee'yi temsil eder
        name, last, age, pay = emp_1_str.split("-")
        return cls(name, last, int(age), float(pay)) #gn: yeni çalişan yaratacak ve döndürecek
    
    @staticmethod
    def holiday_print(day):
        if day == "weekend":
            print("This is an off day")
        else:
            print("This is not an off day")

Employee.holiday_print("weekend") # This is an off day
emp_1 = Employee("Ferdi", "Kadioglu", "24", 1907)
emp_1.holiday_print("working day") # This is not an off day

#pn: INHERITANCE
#bn: Inheritance, belirtilen baska classlardaki method ve attribute'lara erişmeyi sağlar
#bn: Hangi class'tan inherit etmek istedigimizi parantezin icine yaziyoruz
#bn: Inherit ettigimiz class'a parent/super class, inherit edene de child/subclass deniyor
#bn: IT'nin içine hiçbir şey yazmilmazsa bile Employee'nin özelliklerine erişimi var
#bn: aranan şey IT'nin içerisinde bulunamazsa inherit ettigi yere gidip bakar
#bn: IT nin içerisinde __init__ methodu olmadiği için gidip Employee class'ina bakar
#bn: IT'nin raise_percent ini degistirmek, inherit ettigi yerinkini degistirmez
#bn: subclass'ta yaptigimiz degisiklik parent class'i etkilemez
#bn: Subclass, superclass'tan dallandiği için onun tüm attribute'larina ve methodlarina erişebilir.

class Employee:

    raise_percent = 1.05
    num_emp = 0

    def __init__(self, name, last, age, pay):
        self.name = name
        self.last = last
        self.age = age
        self.pay = pay
        Employee.num_emp += 1

    def apply_raise(self):
        self.pay *= self.raise_percent

emp_1 = Employee("Ferdi", "Kadioglu", "24", 1000)
emp_2 = Employee("Osayi", "Samuel", "21", 5000)

class IT(Employee):
    pass

it_1 = IT("Ferdi", "Kadioglu", "24", 1000)
print(it_1.__dict__) # {'name': 'Ferdi', 'last': 'Kadioglu', 'age': '24', 'pay': 1000}
print(it_1.pay) # 1000
it_1.apply_raise()
print(it_1.pay) # 1050.0

#
class Employee:

    raise_percent = 1.05
    num_emp = 0

    def __init__(self, name, last, age, pay):
        self.name = name
        self.last = last
        self.age = age
        self.pay = pay
        Employee.num_emp += 1

    def apply_raise(self):
        self.pay *= self.raise_percent

emp_1 = Employee("Ferdi", "Kadioglu", "24", 1000)
emp_2 = Employee("Osayi", "Samuel", "21", 5000)

class IT(Employee):
    raise_percent = 1.2 #gn: IT'dekilerin yüzdelik maas degisimini farkli bir deger olarak belirledik

it_1 = IT("Ferdi", "Kadioglu", "24", 1000)
print(it_1.pay) # 1000
it_1.apply_raise()
print(it_1.pay) # 1200.0
print(IT.raise_percent) # 1.2
print(Employee.raise_percent) # 1.05

# Diyelim ki IT'cilere yeni bir özellik olarak hangi programlama dili bildiklerini de eklemek istiyorum
class IT(Employee):
    raise_percent = 1.2
    def __init__(self, name, last, age, pay, language):
        self.name = name
        self.last = last
        self.age = age
        self.pay = pay
        self.language = language

it_1 = IT("Ferdi", "Kadioglu", "24", 1000, "python")
print(it_1.language) # python

#bn: bunun yerine şöyle de yapilabilir
class IT(Employee):
    raise_percent = 1.2
    def __init__(self, name, last, age, pay, language):
        super().__init__(name, last, age, pay)
        self.language = language

it_1 = IT("Ferdi", "Kadioglu", "24", 1000, "python")
print(it_1.name) #Ferdi
print(it_1.language) # python

class IK(Employee):
    raise_percent = 1.3
    def __init__(self, name, last, age, pay, experience):
        super().__init__(name, last, age, pay)
        self.experience = experience

    def print_experience(self):
        print(f"This employee has {self.experience} years of experience")

ik_1 = IK("Osayi", "Samuel", "21", 5000, 12)
ik_1.print_experience() # This employee has 12 years of experience

#
print(isinstance(ik_1, IK)) # True
print(isinstance(ik_1, Employee)) # True
print(issubclass (IK, Employee)) # True
print(issubclass (IT, Employee)) # True
print(issubclass (IT, IK)) # False

#pn: MAGIC METHODS
#bn: Magic Method'lari kullanarak bazi built-in davranislari degistirilebilir
#bn: Magic Method'lar __ ile çevrilidir. Bunlara dunder method da denir

#yn: __init__()
#bn: emp_1 = Employee("Ferdi", "Kadioglu", "24", 1000) gibi class'dan obje olusturma kisminda çağrilir
#bn: Class(......) formatinda input olarak verilenleri kendine arguman olarak alir
class Employee:

    raise_percent = 1.05
    num_emp = 0

    def __init__(self, name, last, age, pay): #gn: buradaki __init__() bir magic method'dur
        self.name = name
        self.last = last
        self.age = age
        self.pay = pay
        Employee.num_emp += 1

    def apply_raise(self):
        self.pay *= self.raise_percent

emp_1 = Employee("Ferdi", "Kadioglu", "24", 1000)

#yn: __str__()
#bn: objenin okunabilir bir tanimini oluşturmaya yarar
class Employee:

    raise_percent = 1.05
    num_emp = 0

    def __init__(self, name, last, age, pay):
        self.name = name
        self.last = last
        self.age = age
        self.pay = pay
        Employee.num_emp += 1

    def apply_raise(self):
        self.pay *= self.raise_percent

    def __str__(self):
        return f"Employee(name={self.name}, last={self.last}, age={self.age}, pay={self.pay})"

emp_1 = Employee("Ferdi", "Kadioglu", "24", 1000)
print(emp_1) # Employee(name=Ferdi, last=Kadioglu, age=24, pay=1000)

#yn: __add__()
class Employee:

    raise_percent = 1.05
    num_emp = 0

    def __init__(self, name, last, age, pay):
        self.name = name
        self.last = last
        self.age = age
        self.pay = pay
        Employee.num_emp += 1

    def apply_raise(self):
        self.pay *= self.raise_percent

    def __str__(self):
        return f"Employee(name={self.name}, last={self.last}, age={self.age}, pay={self.pay})"
    
    def __add__(self, other):
        return self.pay + other.pay

emp_1 = Employee("Ferdi", "Kadioglu", "24", 1000)
emp_2 = Employee("Osayi", "Samuel", "21", 5000)
print(emp_1 + emp_2) # 6000

#yn: __len__()
class Employee:

    raise_percent = 1.05
    num_emp = 0

    def __init__(self, name, last, age, pay):
        self.name = name
        self.last = last
        self.age = age
        self.pay = pay
        Employee.num_emp += 1

    def apply_raise(self):
        self.pay *= self.raise_percent

    def __str__(self):
        return f"Employee(name={self.name}, last={self.last}, age={self.age}, pay={self.pay})"
    
    def __add__(self, other):
        return self.pay + other.pay
    
    def __len__(self):
        return len(self.name)

emp_1 = Employee("Ferdi", "Kadioglu", "24", 1000)
print(len(emp_1)) # 5

###
class Student:
    class StudentInformation:
        def __init__(self, name, surname, age, number):
            self.name = name
            self.surname = surname
            self.age = age
            self.number = number

        def __str__(self):
            return "\nStudent:\nname = {}\nsurname = {}\nage = {}\nnumber = {}".format(self.name, self.surname, self.age, self.number)

    class Notes:
        def __init__(self, quiz1, quiz2, quiz3, final):
            self.quiz1 = quiz1
            self.quiz2 = quiz2
            self.quiz3 = quiz3
            self.final = final

        def __str__(self):
            return "\nStudent's Notes:\nquiz1 = {}\nquiz2 = {}\nquiz3 = {}\nfinal = {}".format(self.quiz1, self.quiz2, self.quiz3, self.final)

student1 = Student.StudentInformation("Hasan", "Yerebatan", 20, 714)
student1.notes = Student.Notes(80, 85, 75, 70)

print(student1)
print(student1.notes)