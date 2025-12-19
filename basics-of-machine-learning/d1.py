import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Örnek veri
data = {
    'A': [1, 2, 3, 4, 5],
    'B': [2, 8, 3, 7, 10],
    'C': [5, 14, 3, 20, 1],
    'D': [16, 4, 23, 12, 1]
}

x_train = pd.DataFrame(data)

# Korelasyon matrisi
corr_matrix = x_train.corr()

# Isı haritası (renk geçişli)
plt.figure(figsize=(6, 4))
sns.heatmap(corr_matrix, annot=True, cmap="RdYlBu_r", vmin=-1, vmax=1, center=0)
plt.title("Renk Geçişli Korelasyon Matrisi Heatmap")
plt.show()