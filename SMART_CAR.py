import socket
import time
import sys
import csv
from thread import *
import cv2 as cv2
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
 
HOST = '192.168.0.5'   # Symbolic name meaning all available interfaces
PORT = 8888 # Arbitrary non-privileged port

cap = cv2.VideoCapture(0)
if cap.isOpened()== 0 :
	print("Camera not opening")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'
 
#Bind socket to local host and port
try:
	s.bind((HOST, PORT))
except socket.error , msg:
	print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
	sys.exit()
     
print 'Socket bind complete'
 
#Start listening on socket
s.listen(10)
print 'Socket now listening'

#Function for saving data with steer angle
def WriteListtoCSV():
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
	data = preprocessing.scale(new_arr)
	data = data/ 255.0
	ynew = model.predict_classes([data])
	yprob = model.predict_proba([data])
	####### show the input and predicted output CHANGE THIS FOR SENDING TO SOCKET ######## FIRST CHECK IF PREDICTIONS ARE WORKING WITH SAMPLE IMAGES
	print("Probability=%s, Predicted=%s" % (yprob[0], ynew[0]))
	with open ('PREDICTIONS.csv','a',newline='') as csvfile: ##REMOVE NEWLINE FOR PYTHON 3
		writer = csv.writer(csvfile,delimiter=",")
		writer.writerow(new_arr) #check

#Function for handling connections. This will be used to create threads
def clientthread(conn):
    #infinite loop so that function do not terminate and thread do not end.
	while True:        
		x = WriteListtoCSV()
		print(x)
		time.sleep(0.5)

    #came out of loop
	conn.close()

#now keep talking with the client
while 1:
    #wait to accept a connection - blocking call
	conn, addr = s.accept()
	print 'Connected with ' + addr[0] + ':' + str(addr[1])

    #start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
	start_new_thread(clientthread ,(conn,))
#	start_new_thread(imgthread,())
 
s.close()
