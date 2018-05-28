
import csv
import cv2 as cv2
import numpy as np

cap = cv2.VideoCapture(0)
if cap.isOpened()== 0 :
	print("Camera not opening")
while True:
	_, frame1 = cap.read(0)
	cv2.imshow('frame1',frame1)
	data = [500]
	arr = np.asarray(frame1) #CHECK ORDER OF H AND W
	arr = arr.flatten()
	new_arr = data+arr.tolist()
	key= cv2.waitKey(1) & 0xFF
	if key == ord('a'):
		with open ('tesdata.csv','a') as csvfile:
			writer = csv.writer(csvfile)
			writer.writerow(new_arr) #check

