import inflect
p = inflect.engine()

number = []
for i in range(1,1001):
    if len(number) < 1001:
        num = p.number_to_words(i).replace(" ","")
        number.append(num.replace("-",""))
        
result = 0
for i in number:
    result += int(len(i))

#bn: Burada Inflect kutuphanesini kullaniyoruz. Yazdigimiz sayiyi bize string halinde kelime halini donduruyor
#bn: Dondurdugu zaman bosluk ve "-" oluyor bu yuzden de 2 defa replace islemine tabi tutuyoruz. Son olarak tum sayilarin kelime halini elde ettikten sonra bunlarin karakter toplamini bir dongu yardimi ile buluyoruz. 