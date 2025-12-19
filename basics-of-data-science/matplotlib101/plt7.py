import numpy as np
import matplotlib.pyplot as plt

numpyDizisi1 = np.linspace(0,10,20) 
numpyDizisi2 = numpyDizisi1 ** 3

yeniFigure = plt.figure()
yeniEksen = yeniFigure.add_axes([0.1, 0.1, 0.8, 0.8])
yeniEksen.plot(numpyDizisi1, numpyDizisi2, label = "numpyDizisi ** 3 ")
yeniEksen.plot(numpyDizisi1, numpyDizisi1 ** 2, label = "numpyDizisi ** 2 ")
yeniEksen.legend()

yeniFigure.savefig("plt101figure.png", dpi = 200)

plt.show()