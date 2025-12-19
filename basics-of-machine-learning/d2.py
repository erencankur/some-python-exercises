import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

# -----------------------------
# 1. Basit veri seti
# -----------------------------
# Boy (cm), Kilo (kg)
X = np.array([
    [150, 50], [160, 55], [170, 65],  # Sınıf 0
    [180, 80], [190, 85], [200, 90]   # Sınıf 1
])
y = np.array([0, 0, 0, 1, 1, 1])

# Eğitim ve test ayrımı
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# -----------------------------
# 2. Ölçekleme yok (Raw data)
# -----------------------------
knn_raw = KNeighborsClassifier(n_neighbors=3)
knn_raw.fit(X_train, y_train)

# -----------------------------
# 3. Ölçekleme var
# -----------------------------
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

knn_scaled = KNeighborsClassifier(n_neighbors=3)
knn_scaled.fit(X_train_scaled, y_train)

# -----------------------------
# 4. Görselleştirme Fonksiyonu
# -----------------------------
def plot_decision_boundary(knn, X, y, scaled=False):
    plt.figure(figsize=(6,5))
    
    # Eksen aralığı
    x_min, x_max = X[:,0].min()-5, X[:,0].max()+5
    y_min, y_max = X[:,1].min()-5, X[:,1].max()+5
    
    # Meshgrid oluştur
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 200),
                         np.linspace(y_min, y_max, 200))
    
    grid = np.c_[xx.ravel(), yy.ravel()]
    if scaled:
        grid = scaler.transform(grid)
    
    Z = knn.predict(grid)
    Z = Z.reshape(xx.shape)
    
    plt.contourf(xx, yy, Z, alpha=0.3, cmap=plt.cm.coolwarm)
    plt.scatter(X[:,0], X[:,1], c=y, s=100, edgecolor='k', cmap=plt.cm.coolwarm)
    title = "KNN Karar Sınırı - " + ("Ölçeklenmiş Veri" if scaled else "Ham Veri")
    plt.title(title)
    plt.xlabel("Boy (cm)")
    plt.ylabel("Kilo (kg)")
    plt.show()

# -----------------------------
# 5. Karar Sınırlarını Çiz
# -----------------------------
plot_decision_boundary(knn_raw, X_train, y_train, scaled=False)
plot_decision_boundary(knn_scaled, X_train, y_train, scaled=True)