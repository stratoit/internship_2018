#import socket
#server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#ip=socket.gethostbyname(socket.gethostname())
#port = 1234
#address=(ip,port)
#server.bind(address)
#server.listen(2)
#print "Listening on ",ip,":",port
#client,addr=server.accept()
#print "IP_port_client : ",addr[0],":",addr[1]
#while True:
#	data = client.recv(1024)
#	print "Recieved : ",data
#	print "Ready for processing"
#	client.send("hello")

import socket
import time
import sys
import csv
from thread import *
 
HOST = '192.168.0.5'   # Symbolic name meaning all available interfaces
PORT = 8888 # Arbitrary non-privileged port
 
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
def WriteListtoCSV(data):
	with open ('tesdata.csv','a') as csvfile:
		writer = csv.writer(csvfile)
		now = time.strftime('%d-%m-%Y %H:%M:%S')
		writer.writerow([now,data])

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
 
#now keep talking with the client
while 1:
    #wait to accept a connection - blocking call
	conn, addr = s.accept()
	print 'Connected with ' + addr[0] + ':' + str(addr[1])
     
    #start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
	start_new_thread(clientthread ,(conn,))
 
s.close()
