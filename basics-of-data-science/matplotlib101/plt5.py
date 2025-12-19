import numpy as np
import matplotlib.pyplot as plt

numpyArray1 = np.linspace(0,10,20) 
numpyArray2 = numpyArray1 ** 3

figure2 = plt.figure()
eksen1 = figure2.add_axes([0.11, 0.11, 0.7, 0.7])
eksen2 = figure2.add_axes([0.3, 0.3, 0.3, 0.3])

eksen1.plot(numpyArray1, numpyArray2, "g")
eksen1.set_xlabel("X Ekseni")
eksen1.set_ylabel("Y Ekseni")
eksen1.set_title("Ana Grafik Basligi")

eksen2.plot(numpyArray2, numpyArray1, "b")
eksen2.set_xlabel("X Ekseni")
eksen2.set_ylabel("Y Ekseni")
eksen2.set_title("Kücük Grafik Basligi")

plt.show()