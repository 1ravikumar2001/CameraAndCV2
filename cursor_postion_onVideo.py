import cv2

def click_event(event, x, y, flags, params):

	# checking for left mouse clicks
	if event == cv2.EVENT_LBUTTONDOWN:

		# displaying the coordinates
		# on the Shell
		print(x, ' ', y)

		# displaying the coordinates
		# on the image window
		font = cv2.FONT_HERSHEY_SIMPLEX
		cv2.putText(frame, str(x) + ',' +
					str(y), (x,y), font,
					1, (255, 0, 0), 2)
		cv2.imshow('frame', frame)

	# checking for right mouse clicks	
	if event==cv2.EVENT_RBUTTONDOWN:

		# displaying the coordinates
		# on the Shell
		print(x, ' ', y)

		# displaying the coordinates
		# on the image window
		font = cv2.FONT_HERSHEY_SIMPLEX
		b = frame[y, x, 0]
		g = frame[y, x, 1]
		r = frame[y, x, 2]
		cv2.putText(frame, str(b) + ',' +
					str(g) + ',' + str(r),
					(x,y), font, 1,
					(255, 255, 0), 2)
		cv2.imshow('frame', frame)





print("Press the SPACE BAR to pause and Resume the video")

cap = cv2.VideoCapture('210235TP3J321B000001f17e807b4a#14$_S20220601160001_E20220601160025.ts')
if not cap.isOpened():
    print("Error opening video")

while(cap.isOpened()):
    status, frame = cap.read()
    if status:
        cv2.imshow('frame', frame)
    key = cv2.waitKey(10)

    if key == 32:
        cv2.setMouseCallback('frame', click_event)
        print('Space Bar Has been Pressed')
        
        
        cv2.waitKey()
    elif key == ord('q'):

        break
        

cap.release()
cv2.destroyAllWindows()           