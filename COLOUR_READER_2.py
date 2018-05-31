from numpy import genfromtxt
import cv2 as cv2
from PIL import Image
import PIL
import numpy as np
my_data = np.loadtxt('HUGE.csv', delimiter=',')
import time


for i in range(0,my_data.shape[0]-1):
	arr = my_data[i , 1:]

	arr_new = arr.reshape(240,320,3)
	img = Image.fromarray(np.uint8(arr_new),'RGB')
	img = img.resize((128, 128), PIL.Image.ANTIALIAS)
	img.show()
	time.sleep(2)
	img.close()

