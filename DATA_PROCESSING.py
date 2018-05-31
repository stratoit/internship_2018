
import numpy as np

my_data = np.loadtxt('Data.csv', delimiter=',',dtype='i4')

for i in range(0,my_data.shape[0]):
#	arr = my_data[i , 1:]
	
	if my_data[i,0] < 30 :
		my_data[i,0] = 30
	elif my_data[i,0] == 40 : 
		my_data[i,0] = 50
	elif my_data[i,0] == 60 : 
		my_data[i,0] = 70
	elif my_data[i,0] == 80 : 
		my_data[i,0] = 90
	elif my_data[i,0] >= 100 : 
		my_data[i,0] = 110
	np.savetxt('processed_data.csv', my_data, delimiter=',')

	
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

