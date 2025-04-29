import cv2
import numpy as np
import datetime
import time
from pyzbar.pyzbar import decode

authorized_codes = []
with open("./whitelist.txt", "r") as file:
    for line in file.readlines():
        line = line.replace("\n", "")
        authorized_codes.append(line)

log_path = "./log.txt"

most_recent_access = {}
time_bwt_logs_th = 5

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()

    frame = cv2.flip(frame, 1)

    qr_info = decode(frame)

    for qr in qr_info:
        data = qr.data
        (x, y, w, h) = qr.rect
        polygon = qr.polygon

        if data.decode() in authorized_codes:
            cv2.putText(frame, "ACCESS GRANTED", (x, y - 30), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 3)
            cv2.putText(frame, data.decode(), (x, y+h+30), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 3)
            if data.decode() not in most_recent_access.keys() or time.time() - most_recent_access[data.decode()] > time_bwt_logs_th:
                most_recent_access[data.decode()] = time.time()
                with open(log_path, "a") as f:
                    f.write(f"{data.decode()} : {datetime.datetime.now()} \n")
                    f.close()

        else:
            cv2.putText(frame, "ACCESS DENIED", (x, y - 20), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 3)
            cv2.putText(frame, data.decode(), (x, y+h+30), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 3)

        cv2.polylines(frame, [np.array(polygon)], True, (0, 255, 0), 5)

    cv2.imshow("webcam", frame)
    k = cv2.waitKey(1)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
