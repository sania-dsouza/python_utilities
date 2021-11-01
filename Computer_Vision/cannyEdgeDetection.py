import numpy as np
from matplotlib import pyplot as plt
import cv2 as cv

img = cv.imread('scream_test.jpeg')
# Convert to graycsale
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

img_blur = cv.GaussianBlur(img_gray, (3,3), 0)

edges = cv.Canny(img_blur,70,200)

plt.subplot(121);
plt.title('Original')
plt.imshow(img)

plt.subplot(122);
plt.title('Canny image')
plt.imshow(edges)

plt.show()



