import cv2

cap = cv2.VideoCapture(0)       #external webcam 4

while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    h, w, _ = frame.shape

    cx = int(w / 2)
    cy = int(h / 2)

    pixel_center = hsv_frame[cy, cx]
    hue_value = pixel_center[0]
    # print(hue_value)

    color = "Undefined"
    color_threshold = [5, 22, 50, 93, 131, 170]
    color_name = ["RED", "ORANGE", "YELLOW", "GREEN", "BLUE", "VIOLET"]
    for i, threshold in enumerate(color_threshold):
        if hue_value < threshold:
            color = color_name[i]
            break

    pixel_center_bgr = frame[cy, cx]
    b, g, r = int(pixel_center_bgr[0]), int(pixel_center_bgr[1]), int(pixel_center_bgr[2])

    cv2.putText(frame, color, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (b, g, r), 3)
    cv2.circle(frame, (cx, cy), 5, (0, 255, 255), -1)

    cv2.imshow("Color detector", frame)
    k = cv2.waitKey(1)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
