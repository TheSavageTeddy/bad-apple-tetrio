import cv2

video = cv2.VideoCapture('./bad_apple.mp4')

frame_number = 1
while video.isOpened():
    ret, frame = video.read()
    if not ret:
        break
    cv2.imwrite(f'./frames/{frame_number}.jpg', frame)
    frame_number += 1

video.release()