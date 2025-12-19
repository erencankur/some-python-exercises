import tensorflow as tf
import tensorflow_hub as hub
import cv2
import numpy as np

# TensorFlow Hub'dan model yükleme
model = hub.load("https://tfhub.dev/google/movenet/singlepose/lightning/4")

# Modelin giriş ve çıkış işaretlerini kontrol etme
inference_func = model.signatures['serving_default']

# Bunu çalıştırmak için, videonun her bir karesini alacağız
def run_inference(model, image):
    # Görseli TensorFlow modeline uygun formatta hazırlama
    image = cv2.resize(image, (192, 192))  # Modelin beklediği boyut
    input_image = tf.convert_to_tensor(image, dtype=tf.int32)  # int32 olarak dönüştürme
    input_image = input_image[tf.newaxis,...]  # Batch boyutu ekleme

    # Modeli çalıştırma (predictions)
    outputs = inference_func(input_image)
    
    keypoints = outputs['output_0'].numpy()
    return keypoints

def draw_keypoints(image, keypoints):
    height, width, _ = image.shape
    for i in range(keypoints.shape[1]):  # 17 eklem noktası
        kp = keypoints[0, 0, i]  # 0. kişi, 0. batch
        x, y = int(kp[1] * width), int(kp[0] * height)
        confidence = kp[2]
        if confidence > 0.1:  # Güven skoru 0.3'ten yüksekse çizelim
            cv2.circle(image, (x, y), 5, (0, 255, 0), -1)
    return image

cap = cv2.VideoCapture(0) # Video kaynağını al

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    frame = cv2.flip(frame, 1) # Kameranın simetrik görüntüsünü düzeltmek için yatayda çevirme

    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # Görseli RGB formatına dönüştür
    
    keypoints = run_inference(model, image_rgb) # Modeli çalıştır
    
    frame = draw_keypoints(frame, keypoints) # Anahtar noktalarını çiz
    
    cv2.imshow('Pose Estimation', frame) # Sonucu göster
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()