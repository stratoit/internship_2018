# Packages from remote server
import socket
import time
import sys
import csv
import cv2 as cv2
import numpy as np
import threading

# Packages from best net
import tensorflow as tf
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


# Read model from disk
yaml_file = open('model1.yaml', 'r')
loaded_model_yaml = yaml_file.read()
yaml_file.close()
loaded_model = model_from_yaml(loaded_model_yaml)

# load weights into new model
loaded_model.load_weights("model1.h5")
print("Loaded model from disk")

model = tf.get_default_graph()
# # train the model using Adam
# print("[INFO] compiling model...")
# lr = 0.0001
# beta_1 = 0.9
# beta_2 = 0.999
# epsilon = 10 ** (-8)
# opt = optimizers.Adam(lr=lr, beta_1=beta_1, beta_2=beta_2, epsilon=epsilon, clipnorm=1.)
# loaded_model.compile(loss="binary_crossentropy", optimizer=opt, metrics=["categorical_accuracy"])



 
HOST = '192.168.0.2'   # Symbolic name meaning all available interfaces
PORT = 8888 # Arbitrary non-privileged port

cap = cv2.VideoCapture(0)
if cap.isOpened()== 0 :
	print("Camera not opening")
	

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ('Socket created')
 
#Bind socket to local host and port
try:
	s.bind((HOST, PORT))
except (socket.error , msg):
	print ('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
	sys.exit()
     
print ('Socket bind complete')
 
#Start listening on socket
s.listen(10)
print ('Socket now listening')



#Function for saving data with steer angle
def WriteListtoCSV():
	global model
	with model.as_default():
	#	global loaded_model
	#	defined multiple time to clear buffer
		_, frame = cap.read(0)
		_, frame = cap.read(0)
		_, frame = cap.read(0)
		_, frame = cap.read(0)
		_, frame = cap.read(0)
		_, frame = cap.read(0)
		frame1 = cv2.resize(frame,None,fx = 0.5,fy=0.5)
		cv2.imwrite("Latest.jpg",frame1)
		arr = np.asarray(frame1) #CHECK ORDER OF H AND W
		arr = arr.flatten()
		new_arr = arr.tolist()
		data = preprocessing.scale(arr)
		data = data/ 255.0
		ynew = loaded_model.predict_classes(data.reshape(1,230400))
		yprob = loaded_model.predict_proba(data.reshape(1,230400))
		
		yn = (int(ynew[0]))*30 + 40
		
		####### show the input and predicted output CHANGE THIS FOR SENDING TO SOCKET ######## FIRST CHECK IF PREDICTIONS ARE WORKING WITH SAMPLE IMAGES
		print("Probability=%s, Predicted=%d" % (yprob[0], yn))

		new_arr1 = [int(yn)]+new_arr
		with open ('PREDICTIONS.csv','a',newline='') as csvfile: ##REMOVE NEWLINE FOR PYTHON 3
			writer = csv.writer(csvfile,delimiter=",")
			writer.writerow(new_arr1) #check
		return (int(yn))

		# 0 for 40
		# 1 for 70
		# 2 for 100

#Function for handling connections. This will be used to create threads
def clientthread(conn):
    #infinite loop so that function do not terminate and thread do not end.
	while True:  
		default = cv2.imread('arrow_keys.png')
		cv2.imshow('controller',default)
		print("Enter key:")
		y = cv2.waitKey(100) & 0xFF
		if (y == ord('w')):
			print('success')
			conn.sendall(str(8).encode('utf-8'))
			print('success')
			continue
		elif (y == ord('s')):
			conn.sendall(str(0).encode('utf-8')) 
			continue
		elif (y == ord('f')):
			break
		else :
			x = WriteListtoCSV()
			print(x)
			conn.sendall(str(int(x/10)).encode('utf-8'))
		
		
		#time.sleep(.5)
	#came out of loop

	cap.release()
	cv2.destroyAllWindows()
	conn.close()

conn, addr = s.accept()
print ('Connected with ' + addr[0] + ':' + str(addr[1]))
t = threading.Thread(target=clientthread, args=(conn,))
t.start()
t.join()
	
#	start_new_thread(imgthread,())
 
s.close()
