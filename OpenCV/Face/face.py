from picamera import PiCamera
import cv2
import time
import io
import numpy

camera = PiCamera()
camera.resolution = (320, 240)
#camera.framerate = 16
stream = io.BytesIO()

for f in camera.capture_continuous(stream, format="jpeg"):

    buff = numpy.fromstring(stream.getvalue(), dtype=numpy.uint8)
    image = cv2.imdecode(buff, 1)
    face_cascade = cv2.CascadeClassifier('/usr/share/opencv/haarcascades/haarcascade_frontalface_alt.xml')

    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 5)
    print "Found "+str(len(faces))+" face(s)"
    for (x,y,w,h) in faces:
        cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)

    cv2.imshow("face", image)
    key = cv2.waitKey(1) & 0xFF

    # if the `q` key is pressed, break from the lop
    if key == ord("q"):
        break

    stream.truncate()
    stream.seek(0)
