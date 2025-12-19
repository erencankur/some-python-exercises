import numpy as np
import cv2
import os
import json
import tensorflow as tf
from tensorflow.keras import layers, models  # type: ignore
from tensorflow.keras.preprocessing.image import load_img, img_to_array # type: ignore

# 1. Veri Hazırlığı (Gerçek veri kümesi kullanma)
# Burada, "train_images" ve "train_labels" verilerinizi yüklemeniz gerekiyor.
# MPII veya COCO gibi veri kümeleri kullanabilirsiniz.

# Veri kümesi dizini
dataset_dir = '/path/to/your/dataset'  # Kendi veri kümenizin yolunu buraya girin
train_image_dir = os.path.join(dataset_dir, 'train_images')  # Eğitim görüntüleri
train_label_dir = os.path.join(dataset_dir, 'train_labels')  # Eğitim etiketleri (JSON veya CSV formatında)

# Eğitim verilerini ve etiketlerini yükleyin
def load_images(image_dir, label_dir, image_size=(224, 224)):
    images = []
    labels = []

    # Eğitim görüntülerini ve etiketlerini yükle
    for filename in os.listdir(image_dir):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            # Görüntüyü yükle
            img_path = os.path.join(image_dir, filename)
            image = load_img(img_path, target_size=image_size)
            image = img_to_array(image) / 255.0  # Görüntüyi normalize et
            images.append(image)

            # Etiket dosyasını yükle
            label_path = os.path.join(label_dir, filename.replace('.jpg', '.json'))  # Etiketlerin JSON formatında olduğunu varsayalım
            with open(label_path, 'r') as label_file:
                label_data = json.load(label_file)
                labels.append(np.array(label_data['keypoints']))  # Anahtar noktaları (x, y, z)

    return np.array(images), np.array(labels)

# Eğitim verilerini ve etiketlerini yükle
train_images, train_labels = load_images(train_image_dir, train_label_dir)

# Doğrulama verileri (benzer şekilde doğrulama veri kümesinden yüklenebilir)
val_images, val_labels = load_images(train_image_dir, train_label_dir)  # Burada doğrulama veri kümesi de kullanabilirsiniz

# 2. Model Tasarımı (CNN ile vücut duruşu tahmin modeli)
def create_pose_estimation_model(input_shape=(224, 224, 3)):
    model = models.Sequential()

    # İlk konvolüsyonel katman
    model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=input_shape))
    model.add(layers.MaxPooling2D((2, 2)))

    # Daha fazla konvolüsyonel katman
    model.add(layers.Conv2D(64, (3, 3), activation='relu'))
    model.add(layers.MaxPooling2D((2, 2)))

    model.add(layers.Conv2D(128, (3, 3), activation='relu'))
    model.add(layers.MaxPooling2D((2, 2)))

    # Tam bağlantılı katmanlar
    model.add(layers.Flatten())
    model.add(layers.Dense(512, activation='relu'))
    model.add(layers.Dense(17 * 3))  # 17 anahtar nokta, her biri için 3 koordinat (x, y, z)

    return model

# Modeli oluştur
model = create_pose_estimation_model()

# Modeli derle
model.compile(optimizer='adam', loss='mse')

# 3. Modeli Eğitme
model.fit(train_images, train_labels, epochs=10, batch_size=32, validation_data=(val_images, val_labels))

# 4. Modeli Değerlendirme
# Test verisi ile modelin doğruluğunu test et
test_images = np.random.random((20, 224, 224, 3))  # 20 adet test verisi
test_labels = np.random.random((20, 17, 3))  # 20 adet test etiketleri

test_loss = model.evaluate(test_images, test_labels)
print(f"Test Loss: {test_loss}")

# 5. Yeni Görüntülerle Tahmin Yapma
# Yeni bir görüntü üzerinde tahmin yapalım (örneğin webcam'den alınan görüntü)
cap = cv2.VideoCapture(0)

while True:
    success, image = cap.read()
    if not success:
        break

    # Görüntüyü simetrik olarak çevirerek düzeltir
    image = cv2.flip(image, 1)

    # Görüntüyü BGR'den RGB'ye çevir
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Görüntüyü model için uygun boyutta yeniden boyutlandır
    image_resized = cv2.resize(image_rgb, (224, 224))  # 224x224 boyutunda olmalı
    image_input = np.expand_dims(image_resized, axis=0)  # (1, 224, 224, 3) boyutuna çevir

    # Model ile tahmin yap
    predicted_keypoints = model.predict(image_input)

    # Tahmin edilen anahtar noktaları (17 anahtar nokta, her biri için x, y, z koordinatları)
    predicted_keypoints = predicted_keypoints.reshape((17, 3))  # (17, 3) şeklinde

    # Görüntüye tahmin edilen anahtar noktalarını çiz
    for (x, y, z) in predicted_keypoints:
        # 2D koordinatları (x, y) olarak çizim yapıyoruz (z koordinatını ihmal ediyoruz)
        cv2.circle(image, (int(x * image.shape[1]), int(y * image.shape[0])), 5, (0, 255, 0), -1)

    # Sonucu ekranda göster
    cv2.imshow('Pose Estimation', image)

    # 'q' tuşuna basılınca çıkış yap
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kaynakları serbest bırak
cap.release()
cv2.destroyAllWindows()