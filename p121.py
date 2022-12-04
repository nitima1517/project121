import cv2
import time
import numpy as np
video=cv2.VideoCapture(0)
image=cv2.imread("black.png")
while True:
    time.sleep(2)
    ret,frame=video.read()
    print(frame)
    frame=cv2.resize(frame,(640,480))
    image=cv2.resize(image,(640,480))
    upperb=np.array([104,153,70])
    lowerb=np.array([30,30,0])
    mask=cv2.inRange(frame,lowerb,upperb)
    res=cv2.bitwise_and(frame,frame,mask=mask)

    f=frame-res
    f=np.where(f==0,image,f)
    cv2.imshow("video",frame)
    cv2.imshow("mask",f)

    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break

video.release()
cv2.destroyAllWindows()    