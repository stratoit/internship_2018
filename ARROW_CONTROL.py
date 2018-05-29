import cv2

while True:
	#Sending to Client
	frame = cv2.imread('arrow_keys.png')
	cv2.imshow('controller',frame)
	print("Enter key:")
	x = cv2.waitKey(0) & 0xFF
	if (x == ord('a')):
		print("left")
	elif(x == ord('s')):
		print("back")
	elif(x == ord('d')):
		print("right")
	elif(x == ord("w")):
		print("front")


