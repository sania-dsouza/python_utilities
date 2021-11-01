import cv2 as cv
import sys

img = cv.imread("scream_test.jpeg")

if img is None:
    sys.exit('No image found!')

cv.imshow('Image', img)
print('Pass!')

k = cv.waitKey(0)

print(f'Key pressed: {k}')
if k == ord('s'):
    cv.imwrite('starry_night.jpg', img)

