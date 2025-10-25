import numpy as np
import pandas as pd

benimSozlugum = {"Atil" : 50, "Zeynep" : 40, "Mehmet" : 30}
pd.Series(benimSozlugum)
    # Atil      50
    # Zeynep    40
    # Mehmet    30
    # dtype: int64
type(pd.Series(benimSozlugum)) # pandas.core.series.Series
benimYaslarim = [50,40,30]
benimIsimlerim = ["Atil", "Zeynep", "Mehmet"]
print(pd.Series(benimYaslarim))
    # 0    50
    # 1    40
    # 2    30
    # dtype: int64
print(pd.Series(benimYaslarim, benimIsimlerim)) #bn: (data, index)
    # Atil      50
    # Zeynep    40
    # Mehmet    30
    # dtype: int64
yarismaSonucu1 = pd.Series([10,5,1], ["Atil", "Zeynep", "Mehmet"])
print(yarismaSonucu1)
    # Atil      10
    # Zeynep     5
    # Mehmet     1
    # dtype: int64
yarismaSonucu2 = pd.Series([20,7,3], ["Atil", "Zeynep", "Mehmet"])
sonSonuc = yarismaSonucu1 + yarismaSonucu2
print(sonSonuc)
    # Atil      30
    # Zeynep    12
    # Mehmet     4
    # dtype: int64

#pn: data frames
data = np.random.randn(4,3)
dataFrame = pd.DataFrame(data)
print(dataFrame)
    #           0         1         2
    # 0 -0.467911 -0.264289 -1.252211
    # 1 -0.052579  0.316859  0.370436
    # 2 -1.835895  0.057670 -0.333379
    # 3  1.020873 -0.103743  0.492394
dataFrame[0]
    #           0
    # 0 -0.467911
    # 1 -0.052579
    # 2 -1.835895
    # 3  1.020873
yeniDataFrame = pd.DataFrame(data, index = ["Atil", "Zeynep", "Atlas", "Mehmet"], columns = ["Maas", "Yas", "Calisma Saati"] )
print(yeniDataFrame)
    #             Maas       Yas  Calisma Saati
    # Atil   -0.467911 -0.264289      -1.252211
    # Zeynep -0.052579  0.316859       0.370436
    # Atlas  -1.835895  0.057670      -0.333379
    # Mehmet  1.020873 -0.103743       0.492394
yeniDataFrame["Yas"]
    #              Yas
    # Atil   -0.264289
    # Zeynep  0.316859
    # Atlas   0.057670
    # Mehmet -0.103743
yeniDataFrame[["Maas", "Yas"]]
    #             Maas       Yas
    # Atil   -0.467911 -0.264289
    # Zeynep -0.052579  0.316859
    # Atlas  -1.835895  0.057670
    # Mehmet  1.020873 -0.103743
yeniDataFrame.loc["Atil"] #bn: loc = location
    # Maas            -0.568391
    # Yas              0.206041
    # Calisma Saati   -0.108835
    # Name: Atil, dtype: float64
yeniDataFrame.iloc[0] #bn: iloc = index location
    # Maas            -0.568391
    # Yas              0.206041
    # Calisma Saati   -0.108835
    # Name: Atil, dtype: float64

yeniDataFrame["Emeklilik Yasi"] = yeniDataFrame["Yas"] + yeniDataFrame["Yas"]
print(yeniDataFrame)
    #             Maas       Yas  Calisma Saati  Emeklilik Yasi
    # Atil   -1.609368 -0.195783      -0.329359       -0.391566
    # Zeynep  0.595303 -0.962818       1.069219       -1.925636
    # Atlas   1.290365  0.130179      -1.011957        0.260358
    # Mehmet  2.773297  1.040159       0.845653        2.080318
yeniDataFrame.drop("Emeklilik Yasi", axis = 1)
yeniDataFrame.drop("Mehmet") #bn: default olarak axis = 0'dır
yeniDataFrame.drop("Emeklilik Yasi", axis = 1, inplace = True) #bn: inplace = True yapılırsa tablonun kendisi değişir

yeniDataFrame.loc["Atil"]["Yas"] # -0.773094045142
yeniDataFrame.loc["Atil", "Yas"] # -0.773094045142 #bn: aynı şeyler

yeniDataFrame < 0
booleanFrame = yeniDataFrame < 0
    #          Maas    Yas  Calisma Saati
    # Atil    False  False          False
    # Zeynep  False   True           True
    # Atlas    True   True           True
    # Mehmet  False   True          False

yeniDataFrame[yeniDataFrame < 0]
yeniDataFrame[booleanFrame]
    #             Maas       Yas  Calisma Saati
    # Atil         NaN       NaN            NaN
    # Zeynep       NaN -0.131829      -0.747064
    # Atlas  -0.803672 -0.704673      -0.115712
    # Mehmet       NaN -0.106896            NaN

yeniDataFrame[yeniDataFrame["Yas"] > 0]
    #             Maas       Yas  Calisma Saati
    # Atil    0.236734  0.151291       0.316493
    # Zeynep  0.180505  0.016685       0.579658

#pn: index değiştirme
yeniDataFrame.reset_index()
    #     index      Maas       Yas  Calisma Saati
    # 0    Atil  0.842543  1.397256       1.335398
    # 1  Zeynep -0.394533  0.464110       2.155803
    # 2   Atlas -0.180676  0.787892      -2.383061
    # 3  Mehmet  0.087507  0.405483       0.819365
yeniIndeksListesi = ["Ati", "Zey", "Atl", "Meh"]
yeniDataFrame["Yeni Indeks"] = yeniIndeksListesi
print(yeniDataFrame)
    #             Maas       Yas  Calisma Saati Yeni Indeks
    # Atil    0.344273  0.644897       0.140474         Ati
    # Zeynep -0.891998 -0.126491       2.487790         Zey
    # Atlas   1.170073 -1.424402      -0.845918         Atl
    # Mehmet  2.140990  0.240173      -1.251919         Meh
yeniDataFrame.set_index("Yeni Indeks")
    #                  Maas       Yas  Calisma Saati
    # Yeni Indeks                                   
    # Ati          0.091655  0.426988       0.975148
    # Zey         -0.692806  1.763691      -0.943947
    # Atl          0.726343 -0.415165      -0.695891
    # Meh          0.333853  2.235088       0.498339
yeniDataFrame.set_index("Yeni Indeks", inplace = True)
print(yeniDataFrame)
    #                  Maas       Yas  Calisma Saati
    # Yeni Indeks                                   
    # Ati          0.091655  0.426988       0.975148
    # Zey         -0.692806  1.763691      -0.943947
    # Atl          0.726343 -0.415165      -0.695891
    # Meh          0.333853  2.235088       0.498339
yeniDataFrame.loc["Ati"]
    # Maas             0.199949
    # Yas             -0.782983
    # Calisma Saati   -0.610033
    # Name: Ati, dtype: float64

#pn: multi index
ilkIndeksler = ["Simpson", "Simpson", "Simpson", "South Park", "South Park", "South Park"]
icIndeksler =["Homer", "Bart", "Marge", "Cartman", "Kenny", "Kely" ]
birlesmisIndeks = list(zip(ilkIndeksler, icIndeksler))
print(birlesmisIndeks) # [('Simpson', 'Homer'), ('Simpson', 'Bart'), ('Simpson', 'Marge'), ('South Park', 'CartmanKenny'), ('South Park', 'Kely')]
birlesmisIndeks = pd.MultiIndex.from_tuples(birlesmisIndeks)
print(birlesmisIndeks)
    # MultiIndex([(   'Simpson',        'Homer'),
    #             (   'Simpson',         'Bart'),
    #             (   'Simpson',        'Marge'),
    #             ('South Park', 'CartmanKenny'),
    #             ('South Park',         'Kely')],
    #            )
benimCizgiFilmListem = [[40, "A"], [10, "B"], [30, "C"], [9, "D"], [10, "E"], [11, "F"]]
cizgiFilmNumpyDizisi = np.array(benimCizgiFilmListem)
cizgiFilmDataFrame = pd.DataFrame(cizgiFilmNumpyDizisi, index = birlesmisIndeks, columns = ["Yas", "Meslek"])
print(cizgiFilmDataFrame)
    #                    Yas Meslek
    # Simpson    Homer    40      A
    #            Bart     10      B
    #            Marge    30      C
    # South Park Cartman   9      D
    #            Kenny    10      E
    #            Kely     11      F
cizgiFilmDataFrame.loc["Simpson"]
    #       Yas Meslek
    # Homer  40      A
    # Bart   10      B
    # Marge  30      C
cizgiFilmDataFrame.loc["Simpson"].loc["Homer"]
    # Yas       40
    # Meslek     A
    # Name: Homer, dtype: object
cizgiFilmDataFrame.index.names = ["Film Adi", "Isim"]
print(cizgiFilmDataFrame)
    #                    Yas Meslek
    # Film Adi   Isim              
    # Simpson    Homer    40      A
    #            Bart     10      B
    #            Marge    30      C
    # South Park Cartman   9      D
    #            Kenny    10      E
    #            Kely     11      F

#pn: operasyonlar - eksik veriler
sozlukVerisi = {"Istanbul":[30, 29, np.nan], "Ankara":[20, np.nan, 25], "Izmir":[40, 39, 38]}
havaDurumuDataFrame = pd.DataFrame(sozlukVerisi)
print(havaDurumuDataFrame)
    #    Istanbul  Ankara  Izmir
    # 0      30.0    20.0     40
    # 1      29.0     NaN     39
    # 2       NaN    25.0     38
havaDurumuDataFrame.dropna()
    #    Istanbul  Ankara  Izmir
    # 0      30.0    20.0     40
havaDurumuDataFrame.dropna(axis = 1) #bn: default olarak axis = 0'dır
    #    Izmir
    # 0     40
    # 2     38
    # 1     39

yeniVeri = {"Istanbul":[30, 29, np.nan], "Ankara":[20, np.nan, 25], "Izmir":[40, 39, 38], "Antalya":[45, np.nan, np.nan]}
yeniDataFrame = pd.DataFrame(yeniVeri)
yeniDataFrame.dropna(axis=1,thresh=2)
    #    Istanbul  Ankara  Izmir
    # 0      30.0    20.0     40
    # 1      29.0     NaN     39
    # 2       NaN    25.0     38
yeniDataFrame.fillna(20)
    #    Istanbul  Ankara  Izmir  Antalya
    # 0      30.0    20.0     40     45.0
    # 1      29.0    20.0     39     20.0
    # 2      20.0    25.0     38     20.0

#pn: gruplandırma
maasSozlugu = {"Departman" : ["Yazilim", "Yazilim", "Pazarlama", "Pazarlama" , "Hukuk", "Hukuk"],
              "Calisan Ismi" : ["Ahmet", "Mehmet", "Atil", "Burak", "Zeynep", "Fatma" ] ,
              "Maas" : [100,150,200,300,400,500]
              }
maasDataFrame = pd.DataFrame(maasSozlugu)
print(maasDataFrame)
    #    Departman Calisan Ismi  Maas
    # 0    Yazilim        Ahmet   100
    # 1    Yazilim       Mehmet   150
    # 2  Pazarlama         Atil   200
    # 3  Pazarlama        Burak   300
    # 4      Hukuk       Zeynep   400
    # 5      Hukuk        Fatma   500

grupObjesi = maasDataFrame.groupby("Departman")
grupObjesi.count()
    #            Calisan Ismi  Maas
    # Departman                    
    # Hukuk                 2     2
    # Pazarlama             2     2
    # Yazilim               2     2
grupObjesi.mean("Maas")
    #             Maas
    # Departman       
    # Hukuk      450.0
    # Pazarlama  250.0
    # Yazilim    125.0
grupObjesi.max()
    #           Calisan Ismi  Maas
    # Departman                   
    # Hukuk            Fatma   400
    # Pazarlama         Atil   200
    # Yazilim          Ahmet   100
grupObjesi.min()
    #           Calisan Ismi  Maas
    # Departman                   
    # Hukuk            Fatma   400
    # Pazarlama         Atil   200
    # Yazilim          Ahmet   100
print(grupObjesi.describe())
    #            Maas                                                     
    #           count   mean        std    min    25%    50%    75%    max
    # Departman                                                           
    # Hukuk       2.0  450.0  70.710678  400.0  425.0  450.0  475.0  500.0
    # Pazarlama   2.0  250.0  70.710678  200.0  225.0  250.0  275.0  300.0
    # Yazilim     2.0  125.0  35.355339  100.0  112.5  125.0  137.5  150.0

#pn: concat - concatenation
sozluk1 = {"Isim" : ["Ahmet", "Mehmet", "Zeynep", "Atil"],
           "Spor" : ["Kosu", "Yüzme", "Kosu" , "Basketbol"],
           "Kalori" : [100,200,300,400]}
DataFrame1 = pd.DataFrame(sozluk1, index=[0,1,2,3])
print(DataFrame1)
    #      Isim       Spor  Kalori
    # 0   Ahmet       Kosu     100
    # 1  Mehmet      Yüzme     200
    # 2  Zeynep       Kosu     300
    # 3    Atil  Basketbol     400
sozluk2 = {"Isim" : ["Osman", "Levent", "Atlas", "Fatma"],
           "Spor" : ["Kosu", "Yüzme", "Kosu" , "Basketbol"],
           "Kalori" : [200,100,50,300]}
DataFrame2 = pd.DataFrame(sozluk2, index=[4,5,6,7])
print(DataFrame2)
    #      Isim       Spor  Kalori
    # 4   Osman       Kosu     200
    # 5  Levent      Yüzme     100
    # 6   Atlas       Kosu      50
    # 7   Fatma  Basketbol     300
sozluk3 = {"Isim" : ["Ayse", "Mahmut", "Duygu", "Nur"],
           "Spor" : ["Kosu", "Yüzme", "Badminton" , "Tenis"],
           "Kalori" : [300,400,500,250]}
DataFrame3 = pd.DataFrame(sozluk3, index=[8,9,10,11])
print(DataFrame3)
    #       Isim       Spor  Kalori
    # 8     Ayse       Kosu     300
    # 9   Mahmut      Yüzme     400
    # 10   Duygu  Badminton     500
    # 11     Nur      Tenis     250
pd.concat([DataFrame1, DataFrame2, DataFrame3])
    #       Isim       Spor  Kalori
    # 0    Ahmet       Kosu     100
    # 1   Mehmet      Yüzme     200
    # 2   Zeynep       Kosu     300
    # 3     Atil  Basketbol     400
    # 4    Osman       Kosu     200
    # 5   Levent      Yüzme     100
    # 6    Atlas       Kosu      50
    # 7    Fatma  Basketbol     300
    # 8     Ayse       Kosu     300
    # 9   Mahmut      Yüzme     400
    # 10   Duygu  Badminton     500
    # 11     Nur      Tenis     250

#pn: merge
mergeSozluk1 = {"Isim" : ["Ahmet" , "Mehmet", "Zeynep", "Atil"],
                "Spor" : ["Kosu", "Yüzme", "Kosu" , "Basketbol"]}
mergeDataFrame1 = pd.DataFrame(mergeSozluk1)
print(mergeDataFrame1)
    #      Isim       Spor
    # 0   Ahmet       Kosu
    # 1  Mehmet      Yüzme
    # 2  Zeynep       Kosu
    # 3    Atil  Basketbol
mergeSozluk2 = {"Isim" : ["Ahmet" , "Mehmet", "Zeynep", "Atil"],
                "Kalori" : ["100", "200", "150" , "250"]}
mergeDataFrame2 = pd.DataFrame(mergeSozluk2)
print(mergeDataFrame2)
    #      Isim Kalori
    # 0   Ahmet    100
    # 1  Mehmet    200
    # 2  Zeynep    150
    # 3    Atil    250
print(pd.merge(mergeDataFrame1, mergeDataFrame2, on = "Isim"))
    #      Isim       Spor Kalori
    # 0   Ahmet       Kosu    100
    # 1  Mehmet      Yüzme    200
    # 2  Zeynep       Kosu    150
    # 3    Atil  Basketbol    250

#pn: ileri seviye operasyonlar
maasSozluk = {"Isim" : ["Atil", "Zeynep", "Mehmet", "Ahmet"],
              "Departman": ["Yazilim", "Satis" , "Pazarlama", "Yazilim" ],
              "Maas" : [200,300,400,500]}
maasDataFrame = pd.DataFrame(maasSozluk)
print(maasDataFrame)
    #      Isim  Departman  Maas
    # 0    Atil    Yazilim   200
    # 1  Zeynep      Satis   300
    # 2  Mehmet  Pazarlama   400
    # 3   Ahmet    Yazilim   500
maasDataFrame["Departman"]
    # 0      Yazilim
    # 1        Satis
    # 2    Pazarlama
    # 3      Yazilim
maasDataFrame["Departman"].unique()
    # Name: Departman, dtype: object
    # ['Yazilim' 'Satis' 'Pazarlama']
maasDataFrame["Departman"].nunique()
    # 3
maasDataFrame["Departman"].value_counts()
    # Departman
    # Yazilim      2
    # Satis        1
    # Pazarlama    1
    # Name: count, dtype: int64
def bruttenNete(maas) :
    return maas * 0.66
maasDataFrame["Maas"].apply(bruttenNete)
    # 0    132.0
    # 1    198.0
    # 2    264.0
    # 3    330.0
    # Name: Maas, dtype: float64
maasDataFrame.isnull()
    #     Isim  Departman   Maas
    # 0  False      False  False
    # 1  False      False  False
    # 2  False      False  False
    # 3  False      False  False
yeniBirVeri = {"Karakter Sinifi" : ["South Park", "South Park", "Simpson", "Simpson", "Simpson"],
               "Karakter Ismi" : ["Cartman", "Kenny", "Homer", "Bart", "Bart"],
               "Karakter Yas" : [9,10,50,20,10]}
karakterDF = pd.DataFrame(yeniBirVeri)
print(karakterDF)
    #   Karakter Sinifi Karakter Ismi  Karakter Yas
    # 0      South Park       Cartman             9
    # 1      South Park         Kenny            10
    # 2         Simpson         Homer            50
    # 3         Simpson          Bart            20
    # 4         Simpson          Bart            10
karakterDF.pivot_table(values = "Karakter Yas", index = ["Karakter Sinifi", "Karakter Ismi"])
    #                                Karakter Yas
    # Karakter Sinifi Karakter Ismi              
    # Simpson         Bart                   15.0
    #                 Homer                  50.0
    # South Park      Cartman                 9.0
    #                 Kenny                  10.0
karakterDF.pivot_table(values = "Karakter Yas", index = ["Karakter Sinifi", "Karakter Ismi"], aggfunc=np.sum)
    #                                Karakter Yas
    # Karakter Sinifi Karakter Ismi              
    # Simpson         Bart                     30
    #                 Homer                    50
    # South Park      Cartman                   9
    #                 Kenny                    10

#pn: excelle çalışma
dataFrame = pd.read_excel("bisiklet_fiyatlari.xlsx")
dataFrame.head() #bn: ilk 5 veriyi alir