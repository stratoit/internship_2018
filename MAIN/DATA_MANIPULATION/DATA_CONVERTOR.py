import cv2 as cv2
import numpy as np
import csv

my_data = np.loadtxt('pro_DIFFERENT1_WITHFLIP_45_80.csv', delimiter=',',dtype='i4')

for i in range(0,my_data.shape[0]):
	arr = my_data[i , 1:]
	arr_new = arr.reshape(45,80,3)
	cv_img = arr_new.astype(np.uint8)
	# cropped=cv_img[30:100, 5:95]
	# print(cropped.shape)
	# r = 100.0 / cv_img.shape[1]
	# dim = (100, int(cv_img.shape[0] * r))
	 
	# # perform the actual resizing of the image and show it
	# cropped = cv2.resize(cv_img, dim, interpolation = cv2.INTER_AREA)
	arr = np.asarray(cv_img)
	arr = arr.flatten()
	new_arr = [my_data[i,0]]+arr.tolist()
	with open ('UNAUG_45_80_TRAIN_6_WITHFLIP.csv','a',newline='') as csvfile:
		writer = csv.writer(csvfile,delimiter=",")
		writer.writerow(new_arr)