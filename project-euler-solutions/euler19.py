from datetime import datetime

start_date = datetime(1901, 1, 1)
end_date = datetime(2000, 12, 31)
current_date = start_date
sunday_count = 0

while current_date <= end_date:
    if current_date.weekday() == 6: #bn: weekday() metodu; Pazartesi’yi 0, Salı’yı 1, …, Pazar’ı 6 olarak döndürür
        sunday_count += 1
    next_month = current_date.month % 12 + 1 #bn: next_month, mevcut aydan bir sonraki ayı hesaplar, (current_date.month % 12 + 1) ifadesi ile Aralık ayı sonrası Ocak ayına geçiş sağlanır
    next_year = current_date.year + (current_date.month // 12) #bn: next_year, yıl değişimini kontrol eder ve gerektiğinde yılı arttırır
    current_date = datetime(next_year, next_month, 1) #bn: current_date yeni ayın ilk gününe ayarlanır

print(sunday_count)