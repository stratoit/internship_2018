import cv2 as cv2
import numpy as np

import csv
import time


cap = cv2.VideoCapture(0)
if cap.isOpened()== 0 :
	print("Camera not opening")

count =0

while(True):

	_, frame1 = cap.read(0)
	frame = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
	cv2.imshow('frame',frame)
	

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

		#print max(perimeter)
		maxindex= perimeter.index(max(perimeter))

		cv2.drawContours( vis2, contours, maxindex +1, (255,0,0), -1)

		img_grey = cv2.cvtColor(vis2,cv2.COLOR_BGR2GRAY)
		arr = np.asarray(img_grey).reshape((h,w)) #CHECK ORDER OF H AND W

		arr = arr.flatten()
		print(arr)
		with open("img_pixels.csv", 'a') as f:
			writer = csv.writer(f)
			now = time.strftime('%d-%m-%Y %H:%M:%S')
			writer.writerow([arr,now])


		count += 1
	elif key == ord('q'):
		break
    

cap.release()
cv2.destroyAllWindows()
