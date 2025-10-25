import numpy as np
import matplotlib.pyplot as plt

numpyDizisi1 = np.linspace(0,10,20) 
numpyDizisi2 = numpyDizisi1 ** 2

(benimFigure, benimEksen) = plt.subplots()
benimEksen.plot(numpyDizisi1, numpyDizisi1 + 1, color = "#3A95A8", alpha = 0.3, linestyle = "-.")
benimEksen.plot(numpyDizisi1, numpyDizisi1 + 2, color = "blue", linewidth = 5.0, linestyle = ":")
benimEksen.plot(numpyDizisi1, numpyDizisi1 + 3, color = "yellow", linewidth = 5.0, linestyle = "--")
benimEksen.plot(numpyDizisi1, numpyDizisi1 + 4, color = "#000000", linestyle = "--", marker = "+")
benimEksen.plot(numpyDizisi1, numpyDizisi1 + 5, color = "#000000", linestyle = "--", marker = "o", markerfacecolor = "red")
benimEksen.plot(numpyDizisi1, numpyDizisi1 + 6, color = "#FFFFFF", linestyle = "--", marker = "o", markersize = 8, markerfacecolor = "green")

plt.show()