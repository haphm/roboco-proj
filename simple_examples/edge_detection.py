import cv2

img = cv2.imread('rice_img.png', cv2.IMREAD_COLOR)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

canny = cv2.Canny(img_gray, threshold1=150, threshold2=250)

contours, hierarchy = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print(f'number of objects: {len(contours)}')

n = 1

for c in contours:
    (x,y), radius = cv2.minEnclosingCircle(c)
    center = (int(x), int(y))
    cv2.putText(img, f'#{n}', center, cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 1)
    n+=1

cv2.imshow('origin', img)
cv2.imshow('gray', img_gray)
cv2.imshow('canny', canny)

cv2.waitKey(0)
cv2.destroyAllWindows()