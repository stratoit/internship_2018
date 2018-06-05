import cv2 as cv2
import numpy as np

my_data = np.loadtxt('tesdata.csv', delimiter=',')
import time

font                   = cv2.FONT_HERSHEY_SIMPLEX
bottomLeftCornerOfText = (10,50)
fontScale              = 1
fontColor              = (255,255,255)
lineType               = 2

for i in range(0,my_data.shape[0]-1):
	arr = my_data[i , 1:]
	command = my_data[i,0]

	arr_new = arr.reshape(240,320,3)
	cv_img = arr_new.astype(np.uint8)
	cv2.putText(cv_img,'%d'%command, bottomLeftCornerOfText, font, fontScale,fontColor,lineType)
	cv2.imshow('image',cv_img)
	cv2.waitKey(0)
#	img = Image.fromarray(np.uint8(arr_new),'RGB')
#	img = img.resize((128, 128), PIL.Image.ANTIALIAS)
#	img.show()
#	time.sleep(2)
#	img.close()

