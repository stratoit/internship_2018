import cv2
import numpy as np
from matplotlib import pyplot as plt
import sys


img = cv2.imread('green/2.jpg',0)

#cv2.imshow('original',img)
_, th1 = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY);

h, w = img.shape[:2]

# Determine contour of all blobs found
contours0, hierarchy = cv2.findContours( th1.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
contours = [cv2.approxPolyDP(cnt, 3, True) for cnt in contours0]

# Draw all contours
vis = np.zeros((h, w, 3), np.uint8)
cv2.drawContours( vis, contours, -1, (128,255,255), 3, 8)

# Draw the contour with maximum perimeter (omitting the first contour which is outer boundary of image
# Not necessary in this case
vis2 = np.zeros((h, w, 3), np.uint8)
perimeter=[]
for cnt in contours[1:]:
    perimeter.append(cv2.arcLength(cnt,True))
#print perimeter
#print max(perimeter)
maxindex= perimeter.index(max(perimeter))
#print maxindex

cv2.drawContours( vis2, contours, maxindex +1, (255,0,0), -1)


# Show all images
titles = ['Original Image','Threshold','Contours', 'Result']
images=[img, th1, vis, vis2]
for i in xrange(4):
    plt.subplot(2,2,i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i]), plt.xticks([]), plt.yticks([])
plt.show()



