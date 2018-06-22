# This file can be modified to resize and crop the images stored in the csv file
# and re-save them. We tried various neural networks on different image sizes as well as 
# by cropping the images to reduce the size of feature vectors. You can have your application
# modified according to your usage

import cv2 as cv2
import numpy as np
import csv

my_data = np.loadtxt('pro_DIFFERENT1_WITHFLIP_45_80.csv', delimiter=',',dtype='i4')

for i in range(0,my_data.shape[0]):
	arr = my_data[i , 1:]
	# The below line forms a 240* 320 * 3 image
	arr_new = arr.reshape(240,320,3)
	cv_img = arr_new.astype(np.uint8)
	
	# print(cropped.shape)
	r = 100.0 / cv_img.shape[1]
	dim = (100, int(cv_img.shape[0] * r))
	 
	# perform the actual resizing of the image and show it
	
	# The below line would make the image 75 * 100 * 3
	cropped = cv2.resize(cv_img, dim, interpolation = cv2.INTER_AREA)
	# The below line would make the image 55 * 100 * 3
	cropped= cropped[20:100, :]
	# The below line would make the image 45 * 80 * 3
	cropped= cropped[10:100, 10:90]
	
	arr = np.asarray(cropped)
	arr = arr.flatten()
	new_arr = [my_data[i,0]]+arr.tolist()
	with open ('UNAUG_45_80_TRAIN_6_WITHFLIP.csv','a',newline='') as csvfile:
		writer = csv.writer(csvfile,delimiter=",")
		writer.writerow(new_arr)