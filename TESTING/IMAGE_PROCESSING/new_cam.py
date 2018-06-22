# This code would apply morphological operations such as dilations, erosions etc on
# a thresholded live stream.

# Necessary imports
import cv2 as cv2
import numpy as np

cap = cv2.VideoCapture(0)
if cap.isOpened()==0 :
     print("Bad Image")

count=0

while(True):

	_, frame = cap.read()
	cv2.imshow('frame',frame)
	
	# Convert to HSV and apply a mask to threshold between two HSV limits
	hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
	l_r=np.array([20,150,130])
	u_r=np.array([30,255,225])
	mask=cv2.inRange(hsv,l_r,u_r)
	res=cv2.bitwise_and(frame,frame,mask=mask)

	# Apply morphological operations
	kernel = np.ones((5,5),np.uint8)
	erosion = cv2.erode(mask,kernel,iterations = 1)
    dilation = cv2.dilate(erosion,kernel,iterations = 1)
	opening = cv2.morphologyEx(dilation, cv2.MORPH_OPEN, kernel)
	closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
	
	#cv2.imshow('frame',frame)
	cv2.imshow('mask',mask)
	#cv2.imshow('res',res)
	#cv2.imshow('erosion',erosion)
	cv2.imshow('dilation',dilation)
	#cv2.imshow('opening',opening)
	cv2.imshow('closing',closing)
        #cv2.imwrite("frame%d.jpg" % count, closing)     # save frame as JPEG file
 	
	# Check for user key press and save if 'a' is pressed
	key= cv2.waitKey(1) & 0xFF 
 	if key == ord('a') :
 		cv2.imwrite("advanced-lane-detection/LANE/lane%d.jpg" % count, frame)
		count += 1
	elif key == ord('q'):
		break
    

cap.release()
cv2.destroyAllWindows()
