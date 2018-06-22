import numpy as np
from keras.models import model_from_yaml

my_data = np.loadtxt('pro_DATA.csv', delimiter=',',dtype='i4')
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import normalize
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Activation
from keras.optimizers import SGD
from keras.layers import Dense
from keras import optimizers
from keras.constraints import maxnorm
from keras.utils import np_utils
from keras.layers import Dropout
# from imutils import paths

# import argparse
# import cv2
# import os



#def image_to_feature_vector(image, size=(32, 32)):
#	# resize the image to a fixed size, then flatten the image into
#	# a list of raw pixel intensities
#	return cv2.resize(image, size).flatten()

# initialize the data matrix and labels list
data = []
labels = []


print('Data loaded')

data1 = my_data[:,1:]
labels = my_data[:,0].tolist()

print(data1.shape)
le = LabelEncoder()
labels = le.fit_transform(labels)

#Trying to normalise 2D array by rows
#data = normalize(data2, axis=0)
#data2 = data1 / np.linalg.norm(data1)
#print(data2.shape)
data = preprocessing.scale(data1)
#print(data[0,:])

data = data/ 255.0

#print(data[0,:])

labels = np_utils.to_categorical(labels, 3) #CHANGE 2 to number of classes

print("[INFO] constructing training/testing split...")
(trainData, testData, trainLabels, testLabels) = train_test_split(data, labels, test_size=0.25, random_state=42)

model = Sequential()
model.add(Dense(300,input_dim=230400, kernel_initializer="uniform",activation="relu", kernel_constraint=maxnorm(4)))
model.add(Dropout(0.5))
model.add(Dense(30, activation="relu", kernel_initializer="uniform", kernel_constraint=maxnorm(4)))
model.add(Dropout(0.3))
model.add(Dense(3))
model.add(Activation("softmax"))

# train the model using Adam
print("[INFO] compiling model...")
lr = 0.0001
beta_1 = 0.9
beta_2 = 0.999
epsilon = 10 ** (-8)
opt = optimizers.Adam(lr=lr, beta_1=beta_1, beta_2=beta_2, epsilon=epsilon, clipnorm=1.)
model.compile(loss="binary_crossentropy", optimizer=opt, metrics=["categorical_accuracy"]) #changed to crossentropy
model.fit(trainData, trainLabels, epochs=50, batch_size=10,verbose=1)

# show the accuracy on the testing set
print("[INFO] evaluating on testing set...")
(loss, accuracy) = model.evaluate(testData, testLabels,batch_size=3, verbose=1)
print("[INFO] loss={:.4f}, accuracy: {:.4f}%".format(loss,accuracy * 100))

# dump the network architecture and weights to file
print("[INFO] dumping architecture and weights to file...")


# serialize model to YAML
model_yaml = model.to_yaml()
with open("model.yaml", "w") as yaml_file:
    yaml_file.write(model_yaml)
# serialize weights to HDF5
model.save_weights("model.h5")
print("Saved model to disk")
