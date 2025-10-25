import numpy as np
import matplotlib.pyplot as plt

numpyDizisi1 = np.linspace(1,10,20)
numpyDizisi2 = numpyDizisi1 ** 3
plt.subplot(1,2,1) #bn: 1 satir ve 2 kolon olacak, su an 1. grafik ciziliyor
plt.plot(numpyDizisi1 ,numpyDizisi2, "y*-")
plt.subplot(1,2,2) #bn: 1 satir ve 2 kolon olacak, su an 2. grafik ciziliyor
plt.plot(numpyDizisi2, numpyDizisi1, "b--")

plt.show()