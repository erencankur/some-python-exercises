import numpy as np
import matplotlib.pyplot as plt

numpyDizisi1 = np.linspace(1,10,20)
numpyDizisi2 = numpyDizisi1 ** 3

benimFigure = plt.figure()
figureAxes = benimFigure.add_axes([0.2,0.2,0.6,0.6])
figureAxes.plot(numpyDizisi1, numpyDizisi2, "g")
figureAxes.set_xlabel("X ekseni veri ismi")
figureAxes.set_ylabel("Y ekseni veri ismi")
figureAxes.set_title("Grafik Basligi")

plt.show()