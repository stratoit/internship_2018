
import csv
import cv2 as cv2
import numpy as np

cap = cv2.VideoCapture(0)
if cap.isOpened()== 0 :
	print("Camera not opening")
while True:
	_, frame1 = cap.read(0)
	frame = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
	data = [500]
#	print data
	_, th1 = cv2.threshold(frame, 100, 255, cv2.THRESH_BINARY);
	h, w = frame.shape[:2]
	cv2.imwrite("Latest.jpg",th1)
	cv2.imshow('th1',th1)
	arr = np.asarray(th1).reshape((h,w)) #CHECK ORDER OF H AND W

	arr = arr.flatten()
	new_arr = data+arr.tolist()
	key= cv2.waitKey(1) & 0xFF
	if key == ord('a'):
		with open ('tesdata.csv','a') as csvfile:
			writer = csv.writer(csvfile)
			writer.writerow(new_arr) #check

