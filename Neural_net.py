from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Activation
from keras.optimizers import SGD
from keras.layers import Dense
from keras.utils import np_utils
from imutils import paths
import numpy as np
import argparse
import cv2
import os


#def image_to_feature_vector(image, size=(32, 32)):
#	# resize the image to a fixed size, then flatten the image into
#	# a list of raw pixel intensities
#	return cv2.resize(image, size).flatten()

# initialize the data matrix and labels list
data = []
labels = []

my_data = np.loadtxt('Data.csv', delimiter=',')

data1 = my_data[:,1:]
labels = my_data[:,0].tolist()

le = LabelEncoder()
labels = le.fit_transform(labels)

data2 = data1 / np.linalg.norm(data1)
data = normalize(data2[:,np.newaxis], axis=0).ravel()

print(data[0,:])

data = data/ 255.0

labels = np_utils.to_categorical(labels, 5) #CHANGE 2 to number of classes

print("[INFO] constructing training/testing split...")
(trainData, testData, trainLabels, testLabels) = train_test_split(data, labels, test_size=0.25, random_state=42)

model = Sequential()
model.add(Dense(768, input_dim=230400, init="uniform",activation="relu"))
model.add(Dense(384, activation="relu", kernel_initializer="uniform"))
model.add(Dense(2))
model.add(Activation("softmax"))

# train the model using SGD
print("[INFO] compiling model...")
sgd = SGD(lr=0.01)
model.compile(loss="crossentropy", optimizer=sgd, metrics=["accuracy"]) #changed to crossentropy
model.fit(trainData, trainLabels, epochs=50, batch_size=128,verbose=1)

# show the accuracy on the testing set
print("[INFO] evaluating on testing set...")
(loss, accuracy) = model.evaluate(testData, testLabels,batch_size=128, verbose=1)
print("[INFO] loss={:.4f}, accuracy: {:.4f}%".format(loss,accuracy * 100))

# dump the network architecture and weights to file
print("[INFO] dumping architecture and weights to file...")
model.save(args["model"])
