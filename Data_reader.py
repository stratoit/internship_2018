import csv
import numpy as np
import cv2

with open('tesdata.csv','rb') as f:
	reader =  csv.reader(f)
	for row in reader:
		print type(row[1])
#		np.reshape(arr,(640,480))
#		cv2.imshow('frame',arr)
