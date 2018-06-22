# Run this code in order to load camera parameters and undistort new images
# saved in the given folder

#Necessary imports
import numpy as np
import cv2
import glob

#Load parameters
mtx = np.load('mtx.npy')
dist = np.load('dist.npy')

## Load one of the test images (CHANGE)
img = cv2.imread('LANE/lane00.jpg')
h, w = img.shape[:2]

# Obtain the new camera matrix and undistort the image
newCameraMtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w, h), 1, (w, h))

count = 0

#Read files in the folder named LANE, with named 1.jpg, 2.jpg and so on ... and undistort them
for path in glob.iglob('LANE/*.jpg'):

	img = cv2.imread(path)
	undistortedImg = cv2.undistort(img,mtx,dist)
	x, y, w, h = roi
	undistortedImg = undistortedImg[y:y + h, x:x + w]
	cv2.imwrite('undistorted-LANE/lane%d.jpg'%count,undistortedImg)
	count +=1

#Clear all
cv2.destroyAllWindows()
