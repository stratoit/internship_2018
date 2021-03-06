# Remote server code with necessary changes made (TRAIN DATA COLLECTION)
import socket
import time
import sys
import csv
import threading
import cv2 as cv2
import numpy as np

steer_angle = 70
tot_speed = 530
 
HOST = '192.168.0.10'   # Symbolic name meaning all available interfaces
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

#Function for saving data with timestamp
def WriteListtoCSV(new_data):
#	print(type(new_data))
	_, frame = cap.read(0)
	_, frame = cap.read(0)
	_, frame = cap.read(0)
	_, frame = cap.read(0)
	_, frame = cap.read(0)
	_, frame = cap.read(0)
	frame1 = cv2.resize(frame,None,fx = 0.5,fy=0.5)
#	frame = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
	cv2.imwrite("Latest.jpg",frame1)
	arr = np.asarray(frame1) #CHECK ORDER OF H AND W
	data=[new_data]
	arr = arr.flatten()
	new_arr = data+arr.tolist()

#	print(len(new_arr))
	with open ('traindata.csv','a',newline='') as csvfile:
		writer = csv.writer(csvfile,delimiter=",")
		writer.writerow(new_arr) #check

#Function for handling connections. This will be used to create threads
def clientthread(conn):
	global steer_angle,tot_speed
    #infinite loop so that function do not terminate and thread do not end.
	while True:
        	#Sending to Client

		default = cv2.imread('arrow_keys.png')
		cv2.imshow('controller',default)
		print("Enter key:")

		x = cv2.waitKey(0) & 0xFF
		
		if(x == ord("w")):
			tot_speed+=1
			#WriteListtoCSV(tot_speed)
			conn.sendall(str(8).encode('utf-8'))
		elif(x == ord('s')):
			tot_speed-=1
			#WriteListtoCSV(tot_speed)
			conn.sendall(str(0).encode('utf-8'))
		elif (x == ord('q')):
			if(steer_angle > 19):
				steer_angle-=5
			#WriteListtoCSV(steer_angle)
			#conn.sendall(str(5))
		elif(x == ord('e')):
			if(steer_angle<105):
				steer_angle+=5
			#WriteListtoCSV(steer_angle)
			#conn.sendall(str(2))
		elif(x == ord('a')):
			steer_angle=30
			WriteListtoCSV(steer_angle)
			#conn.sendall(str(6))
		elif(x == ord('d')):
			steer_angle=110
			WriteListtoCSV(steer_angle)
			#conn.sendall(str(1))
		elif(x == ord('z')):
			steer_angle=50
			WriteListtoCSV(steer_angle)
			#conn.sendall(str(4))
		elif(x == ord('c')):
			steer_angle=90
			WriteListtoCSV(steer_angle)
			#conn.sendall(str(3))
		elif(x == ord('x')):
			steer_angle=70
			WriteListtoCSV(steer_angle)
			conn.sendall(str(7).encode('utf-8'))
		elif(x == ord('f')):
			conn.sendall(str(2).encode('utf-8'))
			tot_speed=530
			break;


		#data=conn.recv(1024)
		#print(data)

    #came out of loop
	conn.close()
 
conn, addr = s.accept()
print ('Connected with ' + addr[0] + ':' + str(addr[1]))
t = threading.Thread(target=clientthread, args=(conn,))
t.start()
t.join()
	
#	start_new_thread(imgthread,())
 
s.close()
