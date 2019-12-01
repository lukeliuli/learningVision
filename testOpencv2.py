import cv2
 
cap = cv2.VideoCapture(1)
 
while True:
	success,img = cap.read()
	cv2.imshow('img',img)
	k = cv2.waitKey(1)
	if k==27:
		break;
cap.release()

