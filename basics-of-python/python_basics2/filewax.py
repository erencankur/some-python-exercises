
#bn: encoding = "utf-8" -> türkçe karakterler için
#bn: mode = "w" -> dosyadaki yazıları siler ve yeni yazı ekler
#bn: mode = "a" -> dosyadaki yazıların devamına yeni yazı ekler
#bn: mode = "x" -> varolan bir dosya açılmaya çalışılırsa hata verir
#bn: mode = "r" -> varolan dosyayı okumaya yarar (direkt "r" olarak da yazılabilir)

file = open ("file.txt", mode = "a", encoding = "utf-8")
file.write("en büyük fener1")
file.close()


file = open ("file.txt", mode = "r", encoding = "utf-8")
print(file.read()) #en büyük fener1en büyük fener1en büyük fener1...
file.close()

#bn: with open ... as ... kodu ile dosya açılır ve kodun içindeki işlemler bittikten sonra dosya kapatılır

with open("fff.txt", "w" ,encoding = "utf-8") as fff:
    fff.write("Hi, I am a professional e-commerce and programming Instructor")
    fff.write("I have more than 18 courses and I am teaching over 100.000 students around the World.")
    fff.write("I am passionate about teaching and I think the best way to learn something is to teach it.")

with open("fff.txt", "r" ,encoding = "utf-8") as fff:
    fff.seek(25)
    print(fff.read(37))
    print(fff.tell()) #62