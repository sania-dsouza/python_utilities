#https://docs.opencv.org/master/d3/df2/tutorial_py_basic_ops.html
#
import cv2 as cv

img = cv.imread('scream_test.jpeg')

print('Number of pixels:', img.size)
print('Size of the image:', img.shape)
print('Type of image pixel values:', img.dtype)

#ROI
region = img[280:340, 330:390]
cv.imshow('ROI', region)

k = cv.waitKey(0)
print(f'Key pressed: {k}')

#Channels
blue = img[:,:,0]
cv.imshow('Blue', blue)

l = cv.waitKey(0)
print(f'Key pressed: {l}')



