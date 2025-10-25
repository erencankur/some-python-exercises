import numpy as np
import matplotlib.pyplot as plt

#gn: scatter
numpyDizisi1 = np.linspace(0,10,20) 
numpyDizisi2 = numpyDizisi1 ** 2

plt.scatter(numpyDizisi1, numpyDizisi2)

plt.show()

#gn: histogram
yeniDizi = np.random.randint(0,100,50)
plt.hist(yeniDizi)

plt.show()

#gn:boxplot
yeniDizi = np.random.randint(0,100,50)
plt.boxplot(yeniDizi)

plt.show()