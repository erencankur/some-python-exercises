import numpy as np
from tensorflow.keras.models import Sequential # type: ignore
from tensorflow.keras.layers import Input, Dense # type: ignore
from tensorflow.keras.optimizers import SGD # type: ignore

x = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])

model = Sequential()
model.add(Input(shape=(2,)))  # Giriş katmanını tanımla, burada shape=(2,) girişlerin boyutunu belirler
model.add(Dense(units=4, activation="relu"))  # Gizli katman (4 nöron)
model.add(Dense(units=1, activation="sigmoid"))  # Çıkış katmanı (1 nöron)

model.compile(optimizer=SGD(learning_rate=0.1), loss='binary_crossentropy', metrics=['accuracy'])

model.fit(x, y, epochs=5000, verbose=0)  # 5000 iterasyon boyunca eğit

predictions = model.predict(x)

print("Girdi: \n", x)
print("Gerçek Çikiş: \n", y)
print("Tahminler: \n", predictions)