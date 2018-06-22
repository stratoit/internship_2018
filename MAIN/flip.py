import cv2 as cv2
import numpy as np
import csv

my_data = np.loadtxt('pro_different1.csv', delimiter=',')


for i in range(0,my_data.shape[0]):
	arr = my_data[i , 1:]
	command = my_data[i,0]
	arr_new = arr.reshape(240,320,3)
	cv_img = arr_new.astype(np.uint8)
	
	new_c=140-command
	flip_image=cv2.flip(cv_img,1)
	
	
	arr_flip = np.asarray(flip_image) 
	data=[new_c]
	arr_flip = arr_flip.flatten()
	new_arr = data+arr_flip.tolist()
	with open ('pro_different1.csv','a') as csvfile:
		writer = csv.writer(csvfile,delimiter=",")
		writer.writerow(new_arr) 


