# This code helps load the FCC neural network and test it on a validation dataset
import numpy as np
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
yaml_file = open('model.yaml', 'r')
loaded_model_yaml = yaml_file.read()
yaml_file.close()
loaded_model = model_from_yaml(loaded_model_yaml)
# load weights into new model
loaded_model.load_weights("model.h5")
print("Loaded model from disk")

import cv2 as cv2
import numpy as np

my_data = np.loadtxt('pro_test_DATA.csv', delimiter=',',dtype='i4')

# print("Loaded Data")

# font                   = cv2.FONT_HERSHEY_SIMPLEX
# bottomLeftCornerOfText = (10,50)
# fontScale              = 1
# fontColor              = (255,255,255)
# lineType               = 2

# for i in range(0,my_data.shape[0]-1):
	# arr = my_data[i , 1:]
	# command = my_data[i,0]
	
	# arr_new = arr.reshape(240,320,3)
	# cv_img = arr_new.astype(np.uint8)
	# cv2.putText(cv_img,'%d'%command, bottomLeftCornerOfText, font, fontScale,fontColor,lineType)
	# cv2.imshow('image',cv_img)
	# cv2.waitKey(0)
	
data1 = my_data[:,1:]
labels = my_data[:,0].tolist()

print(data1.shape)
le = LabelEncoder()
labels = le.fit_transform(labels)
labels = np_utils.to_categorical(labels, 3)
#Trying to normalise 2D array by rows
#data = normalize(data2, axis=0)
#data2 = data1 / np.linalg.norm(data1)
#print(data2.shape)
data = preprocessing.scale(data1)
#print(data[0,:])

data = data/ 255.0

# train the model using Adam
print("[INFO] compiling model...")
lr = 0.0001
beta_1 = 0.9
beta_2 = 0.999
epsilon = 10 ** (-8)
opt = optimizers.Adam(lr=lr, beta_1=beta_1, beta_2=beta_2, epsilon=epsilon, clipnorm=1.)
loaded_model.compile(loss="binary_crossentropy", optimizer=opt, metrics=["categorical_accuracy"])

# show the accuracy on the testing set
print("[INFO] evaluating on testing set...")
(loss, accuracy) = loaded_model.evaluate(data, labels,batch_size=10, verbose=1)
print("[INFO] loss={:.4f}, accuracy: {:.4f}%".format(loss,accuracy * 100))