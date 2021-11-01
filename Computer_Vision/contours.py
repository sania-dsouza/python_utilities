import numpy as np
import cv2 as cv

img = cv.imread('scream_test.jpeg')
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

ret, thres = cv.threshold(img_gray, 200, 255, 0)

con, hierarchy = cv.findContours(thres, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)[-2:]

#print(con)

img_con = cv.drawContours(img, con, -1, (0,0, 255), 3)

cv.imshow('contours', img_con)
cv.waitKey(0)