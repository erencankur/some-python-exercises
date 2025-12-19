import numpy as np
import matplotlib.pyplot as plt

numpyDizisi1 = np.linspace(1,10,20) #bn: 0 ile 10(dahil) arasini 20 eşit parçaya böler
print(numpyDizisi1) # [ 0.          0.52631579  1.05263158  1.57894737  2.10526316  2.63157895
                    #   3.15789474  3.68421053  4.21052632  4.73684211  5.26315789  5.78947368
                    #   6.31578947  6.84210526  7.36842105  7.89473684  8.42105263  8.94736842
                    #   9.47368421 10.        ]
numpyDizisi2 = numpyDizisi1 ** 3
plt.figure() #bn: yeni bir grafik penceresi oluşturur
plt.plot(numpyDizisi1, numpyDizisi2, "r*-") #bn: "--" yazinca çizgi çizgi yapar, "*-" yapinca her veriyi * ile işaretler

plt.show()