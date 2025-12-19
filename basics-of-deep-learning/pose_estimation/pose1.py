import os
import json
import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models # type: ignore
from tensorflow.keras.models import load_model # type: ignore

# Veri Yolu
dataset_path = "./dataset/"  # Dataset klasörünüzün yolu
images_path = os.path.join(dataset_path, "images/")  # Resimlerin olduğu klasör
annotations_path = os.path.join(dataset_path, "annotations.json")  # Etiket dosyasının yolu

# COCO Dataset Formatında Etiketleri Yükleme
with open(annotations_path, "r") as f:
    annotations = json.load(f)

# Veri Hazırlama
train_images = []
train_labels = []

for ann in annotations['annotations']:
    # Resim yolu
    image_id = ann['image_id']
    image_file = os.path.join(images_path, f"{image_id}.jpg")
    image = cv2.imread(image_file)

    if image is None:
        continue

    # Resmi yeniden boyutlandır ve normalize et
    resized_image = cv2.resize(image, (224, 224))
    train_images.append(resized_image)

    # Koordinatları işleme ve normalizasyon
    keypoints = ann['keypoints']  # x, y, visibility (x, y koordinatları ve görünürlük bilgisi)
    keypoints = np.array(keypoints).reshape(-1, 3)  # Her bir nokta (x, y, v) şeklinde
    normalized_keypoints = keypoints[:, :2] / np.array([image.shape[1], image.shape[0]])  # x, y'yi normalize et
    train_labels.append(normalized_keypoints.flatten())  # x, y'yi düzleştir

# Veriyi Numpy Dizisine Çevir
train_images = np.array(train_images)
train_labels = np.array(train_labels)

# Veriyi Kontrol Et
print(f"Toplam resim sayisi: {train_images.shape[0]}")
print(f"Bir resmin boyutu: {train_images.shape[1:]}")
print(f"Bir etiketin boyutu: {train_labels.shape[1]}")

# Model Oluşturma
num_landmarks = 17  # COCO'da 17 anahtar nokta bulunuyor (x, y koordinatları)
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(num_landmarks * 2)  # Her noktanın x ve y koordinatı
])

# Model Derleme
model.compile(optimizer='adam', loss='mse', metrics=['accuracy'])

# Modeli Eğitme
model.fit(train_images, train_labels, epochs=10, batch_size=32, validation_split=0.2)

model.save("/Users/erencankur/Documents/Software/101/Python101/Py_Deep_Learning/pose_estimation/pose.keras")

### Gerçek Zamanlı Poz Tahmini ###

model = load_model("/Users/erencankur/Documents/Software/101/Python101/Py_Deep_Learning/pose_estimation/pose.keras")

# Kameradan Gelen Görüntüler ile Modeli Kullanma
camera = cv2.VideoCapture(0)

while True:
    success, frame = camera.read()
    if not success:
        break

    # Çerçeveyi İşleme
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    resized_frame = cv2.resize(frame_rgb, (224, 224))
    input_frame = resized_frame / 255.0  # Normalizasyon

    # Modelden Tahmin Al
    predictions = model.predict(np.expand_dims(input_frame, axis=0))[0]

    # Tahmin Edilen Noktaları Çizme
    h, w, _ = frame.shape
    for i in range(num_landmarks):
        x = int(predictions[2 * i] * w)
        y = int(predictions[2 * i + 1] * h)
        cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)

    # Görüntüyü Ekrana Yazdırma
    cv2.imshow("Pose Estimation", frame)

    # Çıkış için 'q' Tuşuna Bas
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()