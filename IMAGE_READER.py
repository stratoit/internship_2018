import cv2 as cv2
import time

command = 500
cv_img = cv2.imread('Latest.jpg')

font                   = cv2.FONT_HERSHEY_SIMPLEX
bottomLeftCornerOfText = (10,50)
fontScale              = 1
fontColor              = (255,255,255)
lineType               = 2

cv2.putText(cv_img,'%d'%command, 
    bottomLeftCornerOfText, 
    font, 
    fontScale,
    fontColor,
    lineType)

cv2.imshow("img",cv_img)
cv2.waitKey(0)
