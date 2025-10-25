import numpy as np
import matplotlib.pyplot as plt

numpyDizisi1 = np.linspace(0,10,20) 
numpyDizisi2 = numpyDizisi1 ** 3

(benimFigure, benimEksenler) = plt.subplots(nrows=1,ncols=2)
#bn: benimFigure: Grafik alaninin tümünü temsil eden Figure objesidir
#bn: benimEksenler: Bu grafik alani içindeki eksenleri (subplots) temsil eden bir numpy.ndarray dizisidir ve
    #bn: ve her bir elemani bir Axes objesidir. Bu örnekte, ncols=2 olduğu için benimEksenler dizisinde 2 eksen bulunur
print(type(benimFigure)) # matplotlib.figure.Figure
print(type(benimEksenler)) # numpy.ndarray
print(benimFigure) # Figure(1280x960)
print(benimEksenler) # [<Axes: > <Axes: >]

for eksen in benimEksenler: #bn: benimEksenler dizisindeki her bir eksen (subplot) üzerinde iterasyon yapar
    eksen.plot(numpyDizisi1, numpyDizisi2, "g")
    eksen.set_xlabel("X Ekseni")

plt.tight_layout() #bn: grafiklerin ve eksenlerin düzgün bir şekilde yerleştirilmesini sağlar, böylece grafikler birbirine çok yakın durmaz ve daha okunaklı olur
plt.show()