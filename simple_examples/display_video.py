import cv2

cap = cv2.VideoCapture('highway6.mp4')

if not cap.isOpened():
    print('Cannot open video')

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        cv2.imshow('Frame', frame)
        if cv2.waitKey(1) == 27:
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()