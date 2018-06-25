# This is just like test_csv.py but for convolutional neural networks
import numpy as np
import cv2
import matplotlib.pyplot as plt
from keras.models import Sequential
from sklearn.preprocessing import LabelEncoder
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
from keras.layers import Dense, Conv2D, MaxPooling2D, Flatten
from keras import optimizers
from keras.constraints import maxnorm
from keras.utils import np_utils
from keras.models import model_from_yaml

#Change here
img_rows = 75
img_columns = 100

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
loaded_model.compile(loss="categorical_crossentropy", optimizer=opt, metrics=["categorical_accuracy"])

print("model compiled")

# Image data
my_data = np.loadtxt('SMALLER_DATA4.csv', delimiter=',')

print("data loaded")

font                   = cv2.FONT_HERSHEY_SIMPLEX
bottomLeftCornerOfText = (10,50)
fontScale              = 1
fontColor              = (255,255,255)
lineType               = 2

for i in range(0,my_data.shape[0]):
	data = my_data[i , 1:]
	arr=data
	command = my_data[i,0]

	data = data.reshape(1,img_rows, img_columns,3)

	data = data.astype('float32')

	data /= 255

	ynew = loaded_model.predict_classes(data)
	yprob = loaded_model.predict_proba(data)

	comm = (int(ynew[0]))*30 + 40

	arr_new = arr.reshape(75,100,3)
	cv_img = arr_new.astype(np.uint8)

	cv2.putText(cv_img,'%d'%comm, bottomLeftCornerOfText, font, fontScale,fontColor,lineType)
	cv2.imshow('%d'%command,cv_img)
	cv2.waitKey(0)

#	img = Image.fromarray(np.uint8(arr_new),'RGB')
#	img = img.resize((128, 128), PIL.Image.ANTIALIAS)
#	img.show()
#	time.sleep(2)
#	img.close()


