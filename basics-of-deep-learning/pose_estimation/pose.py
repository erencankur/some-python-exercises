import cv2
import mediapipe as mp

# pose modülünü hallettim
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.5, min_tracking_confidence=0.5)
mp_draw = mp.solutions.drawing_utils

# çizim stillerini hallettim
landmark_spec = mp_draw.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=3)
connection_spec = mp_draw.DrawingSpec(color=(255, 0, 0), thickness=2)

camera = cv2.VideoCapture(0)

while True:
    success, image = camera.read()
    if not success:
        break

    image = cv2.flip(image, 1)

    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    results = pose.process(image_rgb)

    # eklemlerin arasını çizdim
    if results.pose_landmarks:
        mp_draw.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS, landmark_spec, connection_spec)

        # eklemlerin koordinatlarını aldım
        for id, landmark in enumerate(results.pose_landmarks.landmark):
            h, w, _ = image.shape
            cx, cy = int(landmark.x * w), int(landmark.y * h)

    cv2.imshow("Pose Detection", image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()