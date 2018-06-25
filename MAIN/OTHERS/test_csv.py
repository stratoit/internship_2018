# This also helps test the neural net on a validation dataset but instead of calculating the accuracy
# it displays the images with their respective predictions.

import csv
import cv2 as cv2
import numpy as np
import time

# Pacckages from best net
from keras.models import model_from_yaml
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import normalize
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Activation
from keras.optimizers import SGD
from keras.layers import Dense
from keras import optimizers
from keras.constraints import maxnorm
from keras.utils import np_utils
from keras.layers import Dropout

print("Imported")
#Read model from disk
yaml_file = open('model.yaml', 'r')
loaded_model_yaml = yaml_file.read()
yaml_file.close()
loaded_model = model_from_yaml(loaded_model_yaml)

# load weights into new model
loaded_model.load_weights("model.h5")
print("Loaded model from disk")

# train the model using Adam
print("[INFO] compiling model...")
lr = 0.0001
beta_1 = 0.9
beta_2 = 0.999
epsilon = 10 ** (-8)
opt = optimizers.Adam(lr=lr, beta_1=beta_1, beta_2=beta_2, epsilon=epsilon, clipnorm=1.)
loaded_model.compile(loss="binary_crossentropy", optimizer=opt, metrics=["categorical_accuracy"])

print("model compiled")

# Image data
my_data = np.loadtxt('pro_PID_DATA3.csv', delimiter=',')
#data1 = preprocessing.scale(my_data[:,1:])
#data1 = data1/ 255.0

print("preprocessed")

print("data loaded")
font                   = cv2.FONT_HERSHEY_SIMPLEX
bottomLeftCornerOfText = (10,50)
fontScale              = 1
fontColor              = (255,255,255)
lineType               = 2

for i in range(0,my_data.shape[0]):
	arr = my_data[i , 1:]
	command = my_data[i,0]

	#data = preprocessing.scale(arr)
	data = arr/ 255.0
	#data = data1[i,:]

	ynew = loaded_model.predict_classes(data.reshape(1,230400))
	yprob = loaded_model.predict_proba(data.reshape(1,230400))

	comm = (int(ynew[0]))*30 + 40

	arr_new = arr.reshape(240,320,3)
	cv_img = arr_new.astype(np.uint8)

	cv2.putText(cv_img,'%d'%comm, bottomLeftCornerOfText, font, fontScale,fontColor,lineType)
	cv2.imshow('%d'%command,cv_img)
	cv2.waitKey(0)

#	img = Image.fromarray(np.uint8(arr_new),'RGB')
#	img = img.resize((128, 128), PIL.Image.ANTIALIAS)
#	img.show()
#	time.sleep(2)
#	img.close()


