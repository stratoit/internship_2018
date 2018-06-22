import numpy as np
from keras.models import Sequential
from sklearn.preprocessing import LabelEncoder
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
from keras.layers import Dense, Conv2D, MaxPooling2D, Flatten,Dropout, Input, ZeroPadding2D,Convolution2D
from keras import optimizers
from keras.constraints import maxnorm
from keras.utils import np_utils
from keras.models import model_from_yaml,Model
from keras import regularizers
# from keras.applications.vgg16 import VGG16
from keras.utils.vis_utils import plot_model

#Change here
img_rows = 55
img_columns = 100

input_shape = (img_rows,img_columns,3)
# input = Input(shape=input_shape,name = 'image_input')
# model = VGG16(weights='imagenet',include_top=False)
# model = model(input)
# x = Flatten(name='flatten')(model)
# x = Dense(512, activation='relu', name='fc1')(x)
# x = Dense(256, activation='relu', name='fc2')(x)
# x = Dense(3, activation='softmax', name='predictions')(x)
# # plot_model(model, to_file='vgg.png')

# model=Model(input=input,output=x)

model = Sequential()
model.add(ZeroPadding2D((1,1),input_shape=input_shape))
model.add(Convolution2D(64, 3, 3, activation='relu'))
model.add(ZeroPadding2D((1,1)))
model.add(Convolution2D(64, 3, 3, activation='relu'))
model.add(MaxPooling2D((2,2), strides=(2,2)))

model.add(ZeroPadding2D((1,1)))
model.add(Convolution2D(128, 3, 3, activation='relu'))
model.add(ZeroPadding2D((1,1)))
model.add(Convolution2D(128, 3, 3, activation='relu'))
model.add(MaxPooling2D((2,2), strides=(2,2)))

model.add(ZeroPadding2D((1,1)))
model.add(Convolution2D(256, 3, 3, activation='relu'))
model.add(ZeroPadding2D((1,1)))
model.add(Convolution2D(256, 3, 3, activation='relu'))
model.add(ZeroPadding2D((1,1)))
model.add(Convolution2D(256, 3, 3, activation='relu'))
model.add(MaxPooling2D((2,2), strides=(2,2)))

model.add(ZeroPadding2D((1,1)))
model.add(Convolution2D(512, 3, 3, activation='relu'))
model.add(ZeroPadding2D((1,1)))
model.add(Convolution2D(512, 3, 3, activation='relu'))
model.add(ZeroPadding2D((1,1)))
model.add(Convolution2D(512, 3, 3, activation='relu'))
model.add(MaxPooling2D((2,2), strides=(2,2)))

model.add(ZeroPadding2D((1,1)))
model.add(Convolution2D(512, 3, 3, activation='relu'))
model.add(ZeroPadding2D((1,1)))
model.add(Convolution2D(512, 3, 3, activation='relu'))
model.add(ZeroPadding2D((1,1)))
model.add(Convolution2D(512, 3, 3, activation='relu'))
model.add(MaxPooling2D((2,2), strides=(2,2)))

model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(3, activation='softmax'))

print('Model Loaded')

data = []
labels = []

my_data = np.loadtxt('UNAUG_55_100_TRAIN_6.csv', delimiter=',',dtype='i4')
print('Data loaded')

labels = my_data[:,0].tolist()
le = LabelEncoder()
labels = le.fit_transform(labels)
labels = np_utils.to_categorical(labels, 3)

data = my_data[:,1:]

data,labels = shuffle(data,labels,random_state=2)

print("[INFO] constructing training/testing split...")
(trainData, testData, trainLabels, testLabels) = train_test_split(data, labels, test_size=0.1, random_state=2)

trainData = trainData.reshape(trainData.shape[0], img_rows, img_columns,3)
testData = testData.reshape(testData.shape[0], img_rows, img_columns,3)

trainData = trainData.astype('float32')
testData = testData.astype('float32')

# trainData /= 255
# testData /= 255

from keras.applications.vgg16 import preprocess_input
# prepare the image for the VGG model
trainData = preprocess_input(trainData)
testData = preprocess_input(testData)

print('trainData shape:', trainData.shape)
print(trainData.shape[0], 'train samples')
print(testData.shape[0], 'test samples')

# train the model using Adam
print("[INFO] compiling model...")
lr = 0.0001
beta_1 = 0.9
beta_2 = 0.999
epsilon = 10 ** (-8)
opt = optimizers.Adam(lr=lr, beta_1=beta_1, beta_2=beta_2, epsilon=epsilon, clipnorm=1.)

model.compile(loss="categorical_crossentropy", optimizer=opt, metrics=["categorical_accuracy"])
model.fit(trainData, trainLabels, epochs=20, batch_size=32,verbose=1)

# show the accuracy on the testing set
print("[INFO] evaluating on testing set...")
(loss, accuracy) = model.evaluate(testData, testLabels,batch_size=10, verbose=1)
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

