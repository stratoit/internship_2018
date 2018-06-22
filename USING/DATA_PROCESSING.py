import csv
import numpy as np

my_data = np.loadtxt('1.csv', delimiter=',',dtype='i4')
#my_data = np.fromfile('DATA.csv', dtype='i4', count=-1, sep=',')

for i in range(0,my_data.shape[0]):
#	arr = my_data[i , 1:]

	if my_data[i,0] < 60 :
		my_data[i,0] = 40
	elif my_data[i,0] > 80 : 
		my_data[i,0] = 100
	elif my_data[i,0] >=60 and my_data[i,0] <=80 : 
		my_data[i,0] = 70
	
	new_arr = [my_data[i,0]]+my_data[i,1:].tolist()
	# print(new_arr)
	with open ('pro_test_DATA.csv','a',newline='') as csvfile:
		writer = csv.writer(csvfile,delimiter=",")
		writer.writerow(new_arr)

print(my_data.shape)

	
#To show images :
#	arr_new = arr.reshape(240,320,3)
#	cv_img = arr_new.astype(np.uint8)
#	cv2.putText(cv_img,'%d'%command, bottomLeftCornerOfText, font, fontScale,fontColor,lineType)
#	cv2.imshow('image',cv_img)
#	cv2.waitKey(0)
#	img = Image.fromarray(np.uint8(arr_new),'RGB')
#	img = img.resize((128, 128), PIL.Image.ANTIALIAS)
#	img.show()
#	time.sleep(2)
#	img.close()

