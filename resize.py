import cv2 
import numpy as np

frame1 = cv2.imread('frame0.jpg')
frame = cv2.resize(frame1,None,fx = 0.5,fy=0.5)
cv2.imshow('frame1',frame1)
cv2.imshow('reduced',frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
