import cv2
import numpy
capture=cv2.VideoCapture('Sample.mp4')
if(capture.isOpened()==False):
  Print("Opening Video Error")
while(capture.isOpened()):
  ret,frame=capture.read()
  if ret==True:
    cv2.imshow("Frame",frame)
    if cv2.waitkey(25) & 0xFF==ord('q'):
      break
    
  else:
    break
  capture.release()
  cv2.destroyAllWindows()
