# crot
Convolution based Object Recognition Detection. 

How to use :

```py
import crot
ngok=crot.Crot()
ngok.setInput('inputs/1.jpeg')
anu=ngok.getObjects()
print('Jumlah Objek Adalah : '+str(len(anu)))
print(anu)
```

Doing in video stream ? Just use RTSP and capture to image:

```py
import cv2
cap = cv2.VideoCapture('rtsp://192.168.86.81:554/11') # it can be rtsp or http stream

ret, frame = cap.read()

if cap.isOpened():
    _,frame = cap.read()
    cap.release() #releasing camera immediately after capturing picture
    if _ and frame is not None:
        cv2.imwrite('inputs/1.jpeg', frame)
		
		
import crot
ngok=crot.Crot()
ngok.setInput('inputs/1.jpeg')
anu=ngok.getObjects()
print('Jumlah Objek Adalah : '+str(len(anu)))
print(anu)
```
