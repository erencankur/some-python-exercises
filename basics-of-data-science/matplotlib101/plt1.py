import numpy as np
import matplotlib.pyplot as plt

#pn: 1
yasListesi = [10,20,30,30,30,40,50,60,70,75]
kiloListesi = [20,60,80,85,86,87,70,90,95,90]

numpyYasListesi = np.array(yasListesi)
numpyKiloListesi = np.array(kiloListesi)

plt.plot(numpyYasListesi, numpyKiloListesi, "g") #bn: buradaki "g" rengi belirler, "r" yazilsaydi kirmizi olurdu
plt.xlabel("Yaş")
plt.ylabel("Kilo")
plt.title("Yaşa Göre Kilo Dağilimi")

plt.show()