import cv2

img = cv2.imread('rice_img.png', cv2.IMREAD_COLOR)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('origin', img)
cv2.imshow('gray', img_gray)

cv2.waitKey(0)
