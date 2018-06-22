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
import tensorflow as tf
from sklearn.preprocessing import LabelEncoder
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
#Change here
img_rows = 45
img_columns = 80

with tf.Session() as sess:
	data = []
	labels = []

	my_data = np.loadtxt('DONOTUSE.csv', delimiter=',',dtype='i4')
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
	sess.run(tf.global_variables_initializer())
	#Load model
	yaml_file = open('model.yaml', 'r')
	loaded_model_yaml = yaml_file.read()
	yaml_file.close()
	loaded_model = model_from_yaml(loaded_model_yaml)

	# load weights into new model
	loaded_model.load_weights("model.h5")
	print("Loaded model from disk")


	# # train the model using Adam
	print("[INFO] compiling model...")
	lr = 0.0001
	beta_1 = 0.9
	beta_2 = 0.999
	epsilon = 10 ** (-8)
	opt = optimizers.Adam(lr=lr, beta_1=beta_1, beta_2=beta_2, epsilon=epsilon, clipnorm=1.)
	loaded_model.compile(loss="categorical_crossentropy", optimizer=opt, metrics=["categorical_accuracy"])
	print(loaded_model.layers[0].bias.eval())
	
	def plot_filters(layer,x,y):
		filters = layer.kernel.eval()
		fig = plt.figure()
		for j in range(len(filters)):
			ax = fig.add_subplot(y,x,j+1)
			ax.matshow(filters[j][0],cmap = plt.cm.binary)
			plt.xticks(np.array([]))
			plt.yticks(np.array([]))
		plt.tight_layout()
		return plt
		
	# plot_filters(loaded_model.layers[0],8,4).show()
	
	class TensorFlowTheanoFunction(object):   
		def __init__(self, inputs, outputs):
			self._inputs = inputs
			self._outputs = outputs

		def __call__(self, *args, **kwargs):
			feeds = {}
			for (argpos, arg) in enumerate(args):
				feeds[self._inputs[argpos]] = arg
			return tf.get_default_session().run(self._outputs, feeds)
		
	output_layer = loaded_model.layers[1].output
	output_fn = TensorFlowTheanoFunction([loaded_model.layers[0].input],output_layer)
	input_image = trainData[0:1,:,:,:]
	# plt.imshow(input_image[0,:,:,1])
	# plt.show()
	output_image = output_fn(input_image)
	print(output_image.shape)
	fig = plt.figure(figsize=(8,8))
	for i in range(output_image.shape[3]):
		ax = fig.add_subplot(6,6,i+1)
		ax.imshow(output_image[0,:,:,i])
		plt.xticks(np.array([]))
		plt.yticks(np.array([]))
		plt.tight_layout()
	
	plt.show()
	
	
	