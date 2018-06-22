# This code loads the images saved in a csv file, converts them to HSV, orthogonally changes 
# the HSV values(i.e. at a time only one of h,s,v is changed) and saves the new images back into
# csv with the old ones

import cv2 as cv2
import numpy as np
import csv
my_data = np.loadtxt('SMALL_CROP4.csv', delimiter=',',dtype='i4')

for i in range(0,my_data.shape[0]):
	arr = my_data[i , 1:]
	command = my_data[i,0]
	arr_new = arr.reshape(55,100,3)
	cv_img = arr_new.astype(np.uint8)
	hsv = cv2.cvtColor(cv_img, cv2.COLOR_BGR2HSV) #convert it to hsv
	h, s, v = cv2.split(hsv)
	v1=v + 15
	v2=v-50
	h1=h+50
	h2=h-50
	h3=h+100
	h4=h-100
	s1=s+100
	s2=s-100
	s3=s+50
	s4=s-50
	final_hsv1 = cv2.merge((h, s, v1))
	final_hsv2 = cv2.merge((h, s, v2))
	final_hsv3 = cv2.merge((h1, s, v))
	final_hsv4 = cv2.merge((h2, s, v))
	final_hsv5 = cv2.merge((h3, s, v))
	final_hsv6 = cv2.merge((h4, s, v))
	final_hsv7 = cv2.merge((h, s1, v))
	final_hsv8 = cv2.merge((h, s2, v))
	final_hsv9 = cv2.merge((h, s3, v))
	final_hsv10 = cv2.merge((h, s4, v))
	
	img1 = cv2.cvtColor(final_hsv1, cv2.COLOR_HSV2BGR)
	img2 = cv2.cvtColor(final_hsv2, cv2.COLOR_HSV2BGR)
	img3 = cv2.cvtColor(final_hsv3, cv2.COLOR_HSV2BGR)
	img4 = cv2.cvtColor(final_hsv4, cv2.COLOR_HSV2BGR)
	img5 = cv2.cvtColor(final_hsv5, cv2.COLOR_HSV2BGR)
	img6 = cv2.cvtColor(final_hsv6, cv2.COLOR_HSV2BGR)
	img7 = cv2.cvtColor(final_hsv7, cv2.COLOR_HSV2BGR)
	img8 = cv2.cvtColor(final_hsv8, cv2.COLOR_HSV2BGR)
	img9 = cv2.cvtColor(final_hsv9, cv2.COLOR_HSV2BGR)
	img10 = cv2.cvtColor(final_hsv10, cv2.COLOR_HSV2BGR)
	
	ar1 = np.asarray(img1)
	ar2 = np.asarray(img2)
	ar3 = np.asarray(img3)
	ar4 = np.asarray(img4)
	ar5 = np.asarray(img5)
	ar6 = np.asarray(img6)
	ar7 = np.asarray(img7)
	ar8 = np.asarray(img8)
	ar9 = np.asarray(img9)
	ar10 = np.asarray(img10)
	
	ar1 = ar1.flatten()
	ar2 = ar2.flatten()
	ar3 = ar3.flatten()
	ar4 = ar4.flatten()
	ar5 = ar5.flatten()
	ar6 = ar6.flatten()
	ar7 = ar7.flatten()
	ar8 = ar8.flatten()
	ar9 = ar9.flatten()
	ar10 = ar10.flatten()
	
	with open ('SMALL_CROP4.csv','a',newline='') as csvfile:
		writer = csv.writer(csvfile,delimiter=",")
		
		new_arr = [my_data[i,0]]+ar1.tolist()
		writer.writerow(new_arr)
		new_arr = [my_data[i,0]]+ar2.tolist()
		writer.writerow(new_arr)
		new_arr = [my_data[i,0]]+ar3.tolist()
		writer.writerow(new_arr)
		new_arr = [my_data[i,0]]+ar4.tolist()
		writer.writerow(new_arr)
		new_arr = [my_data[i,0]]+ar5.tolist()
		writer.writerow(new_arr)
		new_arr = [my_data[i,0]]+ar6.tolist()
		writer.writerow(new_arr)
		new_arr = [my_data[i,0]]+ar7.tolist()
		writer.writerow(new_arr)
		new_arr = [my_data[i,0]]+ar8.tolist()
		writer.writerow(new_arr)
		new_arr = [my_data[i,0]]+ar9.tolist()
		writer.writerow(new_arr)
		new_arr = [my_data[i,0]]+ar10.tolist()
		writer.writerow(new_arr)
		
#	img = Image.fromarray(np.uint8(arr_new),'RGB')
#	img = img.resize((128, 128), PIL.Image.ANTIALIAS)
#	img.show()
#	time.sleep(2)
#	img.close()

