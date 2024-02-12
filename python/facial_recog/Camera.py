import cv2

cam = cv2.VideoCapture('rtsp://10.0.0.58:554')

#cam = cv2.VideoCapture(0)
while True:
    status, frame = cam.read()
    cv2.imshow('webcam', frame)
    if(cv2.waitKey(1) == ord('q')):
        break

cam.release()
cv2.destroyAllWindows()
