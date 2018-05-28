
import socket
import time
import sys
import csv
from thread import *
import cv2 as cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
 
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

#Function for saving data with timestamp
def WriteListtoCSV(new_data):
#	print(type(new_data))
	_, frame1 = cap.read(0)
	frame = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
#	print data
#	_, th1 = cv2.threshold(frame, 100, 255, cv2.THRESH_BINARY);
	h, w = frame.shape[:2]
	cv2.imwrite("Latest.jpg",frame)
	arr = np.asarray(frame).reshape((h,w)) #CHECK ORDER OF H AND W
	data=[new_data]
	arr = arr.flatten()
	new_arr = data+arr.tolist()

#	print(len(new_arr))
	with open ('tesdata.csv','a') as csvfile:
		writer = csv.writer(csvfile,delimiter=",")
		writer.writerow(new_arr) #check

#Function for handling connections. This will be used to create threads
def clientthread(conn):
    #infinite loop so that function do not terminate and thread do not end.
	while True:
        	#Sending to Client
		x = input('Please give a control command number : ')

		WriteListtoCSV(x);
		conn.sendall(str(x))
		#data=conn.recv(1024)
		#print(data)

    #came out of loop
	conn.close()
 
def imgthread():
	while True:
		_, frame1 = cap.read(0)
		frame = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)

		_, th1 = cv2.threshold(frame, 100, 255, cv2.THRESH_BINARY);
		cv2.imshow('result',th1)

#now keep talking with the client
while 1:
    #wait to accept a connection - blocking call
	conn, addr = s.accept()
	print 'Connected with ' + addr[0] + ':' + str(addr[1])

    #start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
	start_new_thread(clientthread ,(conn,))
#	start_new_thread(imgthread,())
 
s.close()
