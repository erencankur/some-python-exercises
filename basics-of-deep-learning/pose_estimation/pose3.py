import cv2
import mediapipe as mp

# MediaPipe pose modülü
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

# Video kaynağını başlat (webcam)
cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, image = cap.read()
    if not success:
        break

    # Görüntüyü simetrik olarak çevirerek düzeltir
    image = cv2.flip(image, 1)

    # Görüntüyü BGR'den RGB'ye çevir
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Pose tahminini uygula
    results = pose.process(image)

    # Görüntüyü tekrar BGR formatına çevir
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    # Pose anahtar noktalarını çiz
    if results.pose_landmarks:
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

    # Sonucu ekranda göster
    cv2.imshow('Pose Estimation', image)

    # 'q' tuşuna basılınca çıkış yap
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kaynakları serbest bırak
cap.release()
cv2.destroyAllWindows()