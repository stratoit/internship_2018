import numpy as np
import cv2
import matplotlib.pyplot as plt
from keras.models import Sequential
from sklearn.preprocessing import LabelEncoder
from sklearn.utils import shuffle
from keras import optimizers
from keras.constraints import maxnorm
from keras.utils import np_utils
from keras.models import model_from_yaml

#Change here
img_rows = 45
img_columns = 80

#Load model
yaml_file = open('model.yaml', 'r')
loaded_model_yaml = yaml_file.read()
yaml_file.close()
loaded_model = model_from_yaml(loaded_model_yaml)

# load weights into new model
loaded_model.load_weights("model.h5")
print("Loaded model from disk")

my_data = np.loadtxt('pro_pid6_addon_test_45_80_withflip.csv', delimiter=',',dtype='i4')

data = my_data[:,1:]
labels = my_data[:,0].tolist()

print(data.shape)
le = LabelEncoder()
labels = le.fit_transform(labels)
labels = np_utils.to_categorical(labels, 3)

data,labels = shuffle(data,labels,random_state=2)

data = data.reshape(data.shape[0], img_rows, img_columns,3)

data = data.astype('float32')

# data /= 255
from keras.applications.vgg16 import preprocess_input
# # prepare the image for the VGG model
data = preprocess_input(data)

from keras.applications.vgg16 import preprocess_input
# prepare the image for the VGG model
# data = preprocess_input(data)

# # train the model using Adam
print("[INFO] compiling model...")
lr = 0.0001
beta_1 = 0.9
beta_2 = 0.999
epsilon = 10 ** (-8)
opt = optimizers.Adam(lr=lr, beta_1=beta_1, beta_2=beta_2, epsilon=epsilon, clipnorm=1.)
loaded_model.compile(loss="categorical_crossentropy", optimizer=opt, metrics=["categorical_accuracy"])

# show the accuracy on the testing set
print("[INFO] evaluating on testing set...")
(loss, accuracy) = loaded_model.evaluate(data, labels,batch_size=10, verbose=1)
print("[INFO] loss={:.4f}, accuracy: {:.4f}%".format(loss,accuracy * 100))