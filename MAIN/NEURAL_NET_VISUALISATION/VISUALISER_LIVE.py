# This provides the ouputs of the hidden CNN layers for live images.

import csv
import cv2 as cv2
import numpy as np
import threading

# Packages for net
import tensorflow as tf
from keras.models import model_from_yaml
from sklearn import preprocessing
import matplotlib.pyplot as plt
from keras import optimizers
from sklearn.preprocessing import LabelEncoder
from sklearn.utils import shuffle
from keras.utils import np_utils
from keras import optimizers
from keras.utils import np_utils
from sklearn.model_selection import train_test_split
from keras.applications.vgg16 import preprocess_input

print('check')

# Read model from disk
yaml_file = open('model.yaml', 'r')
loaded_model_yaml = yaml_file.read()
yaml_file.close()
loaded_model = model_from_yaml(loaded_model_yaml)

# load weights into new model
loaded_model.load_weights("model.h5")
print("Loaded model from disk")

model = tf.get_default_graph()

cap = cv2.VideoCapture(0)
if cap.isOpened()== 0 :
	print("Camera not opening")


model = tf.get_default_graph()
#Function for saving data with steer angle
def PREDICT():
	global model
	with tf.Session(graph=model) as sess:
		sess.run(tf.global_variables_initializer())
		class TensorFlowTheanoFunction(object):   
			def __init__(self, inputs, outputs):
				self._inputs = inputs
				self._outputs = outputs

			def __call__(self, *args, **kwargs):
				feeds = {}
				for (argpos, arg) in enumerate(args):
					feeds[self._inputs[argpos]] = arg
				return tf.get_default_session().run(self._outputs, feeds)
				
	#	global loaded_model
	#	defined multiple time to clear buffer
		_, frame = cap.read(0)
		_, frame = cap.read(0)
		_, frame = cap.read(0)
		_, frame = cap.read(0)
		_, frame = cap.read(0)
		_, frame = cap.read(0)
		frame1 = cv2.resize(frame,None,fx = 0.5,fy=0.5)

		r = 100.0 / frame1.shape[1]
		dim = (100, int(frame1.shape[0] * r))
	 
		# perform the actual resizing of the image and show it
		cropped = cv2.resize(frame1, dim, interpolation = cv2.INTER_AREA)
		cropped = cropped[20:100, :]
		cropped1 = cropped[10:100,10:90]

		cv2.imwrite("Latest.jpg",cropped1)
		arr = np.asarray(cropped1) #CHECK ORDER OF H AND W
		arr = arr.astype('float32')
		data = preprocess_input(arr)
		#data = arr/ 255.0
		tData=data.reshape(1,45,80,3)
		
		output_layer = loaded_model.layers[9].output # Change 9 according to which layer's output you want
		output_fn = TensorFlowTheanoFunction([loaded_model.layers[0].input],output_layer)
		
		output_image = output_fn(tData)
		# print(output_image.shape)
		# plt.gcf().clear()
		fig = plt.figure(figsize=(8,8))
		for i in range(output_image.shape[3]):
			ax = fig.add_subplot(6,6,i+1)
			ax.imshow(output_image[0,:,:,i])
			plt.xticks(np.array([]))
			plt.yticks(np.array([]))
			plt.tight_layout()
		# x = cv2.waitKey(10) & 0xFF
		# if(x==ord('p')):
		plt.show()

		ynew = loaded_model.predict_classes(tData)
		yprob = loaded_model.predict_proba(tData) #check

		yn = (int(ynew[0]))*30 + 40
		
		####### show the input and predicted output CHANGE THIS FOR SENDING TO SOCKET ######## FIRST CHECK IF PREDICTIONS ARE WORKING WITH SAMPLE IMAGES
		print("Probability=%s, Predicted=%d" % (yprob[0], yn))
		return (int(yn))

#Function for handling connections. This will be used to create threads
def clientthread():
	#infinite loop so that function do not terminate and thread do not end.
	while True:  
		default = cv2.imread('arrow_keys.png')
		cv2.imshow('controller',default)
		print("Enter key:")
		y = cv2.waitKey(80) & 0xFF
		if (y == ord('w')):
			print('success')
			# conn.sendall(str(8).encode('utf-8'))
			print('success')
			continue
		elif (y == ord('s')):
			# conn.sendall(str(0).encode('utf-8')) 
			continue
		elif (y == ord('f')):
			break
		else :
			x = PREDICT()
			print(x)
			# conn.sendall(str(int(x/10)).encode('utf-8'))

	cap.release()
	cv2.destroyAllWindows()

clientthread()

