import cv2 as cv2
import numpy as np
from matplotlib import pyplot as plt

#Load parameters
#mtx = np.load('mtx.npy')
#dist = np.load('dist.npy')

### Load one of the test images
#img = cv2.imread('LANE/lane00.jpg')
#h1, w1 = img.shape[:2]

## Obtain the new camera matrix and undistort the image
#newCameraMtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w1, h1), 1, (w1, h1))

cap = cv2.VideoCapture(0)
if cap.isOpened()== 0 :
	print("Camera not opening")

count =0

while(True):

	_, frame1 = cap.read(0)
	frame = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
	cv2.imshow('frame',frame)
	
#	x, y, w, h = roi
#	undistortedImg = undistortedImg[y:y + h, x:x + w]
#	cv2.imshow('undis',undistortedImg)
#	_, th1 = cv2.threshold(undistortedImg, 100, 255, cv2.THRESH_BINARY);
#	h, w = undistortedImg.shape[:2]
#	
#	# Determine contour of all blobs found
#	contours0, hierarchy = cv2.findContours( th1.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
#	contours = [cv2.approxPolyDP(cnt, 3, True) for cnt in contours0]

#	# Draw all contours
#	vis = np.zeros((h, w, 3), np.uint8)
#	cv2.drawContours( vis, contours, -1, (128,255,255), 3, 8)
#	
#	# Show all images
#	titles = ['Original Image','Threshold','Contours', 'Result']
#	images=[frame, th1, vis, vis2]
#	for i in xrange(4):
#	    plt.subplot(2,2,i+1)
#	    plt.imshow(images[i],'gray')
#	    plt.title(titles[i]), plt.xticks([]), plt.yticks([])
#	plt.show()

	key = cv2.waitKey(1) & 0xFF 
 	if key == ord('a') :
		_, th1 = cv2.threshold(frame, 100, 255, cv2.THRESH_BINARY);
		h, w = frame.shape[:2]
		
		# Determine contour of all blobs found
		contours0, hierarchy = cv2.findContours( th1.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
		contours = [cv2.approxPolyDP(cnt, 3, True) for cnt in contours0]

		# Draw all contours
		vis = np.zeros((h, w, 3), np.uint8)
		cv2.drawContours( vis, contours, -1, (128,255,255), 3, 8)
		
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
#		titles = ['Original Image','Threshold','Contours', 'Result']
#		images=[frame, th1, vis, vis2]
#		for i in xrange(4):
#		    plt.subplot(2,2,i+1)
#		    plt.imshow(images[i],'gray')
#		    plt.title(titles[i]), plt.xticks([]), plt.yticks([])
#		plt.show()
		cv2.imwrite("%d.jpg"%count,vis2)
#		Calibration Removed to avoid latency
#		undistortedImg = cv2.undistort(img,mtx,dist)
#		cv2.imwrite("H.jpg",undistortedImg)
		
		count += 1
	elif key == ord('q'):
		break
    

cap.release()
cv2.destroyAllWindows()
