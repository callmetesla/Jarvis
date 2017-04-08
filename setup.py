#Done by Arun(https://github.com/callmetesla)
import cv2,numpy
import os
datasets='datasets'
#Narrowing down to users face
cascadexml='XML/haarcascade_frontalface_default.xml'
faceDetection=cv2.CascadeClassifier(cascadexml)
#Argument changes depending upon the camera used
camera=cv2.VideoCapture(0)
id=raw_input("Enter your name:")
if not os.path.isdir(datasets):
    os.mkdir(datasets)
    os.mkdir(os.path.join(datasets,id))
else:
    try:
        os.mkdir(os.path.join(datasets,id))
    except  Exception:
        print(Exception)
width,height=(130,100)
counter=1
while True:
    ret,im=camera.read()
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces=faceDetection.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in faces:
        counter+=1
        cv2.rectangle(im,(x,y),(x+w,y+h),(255,0,0),2)
        face=gray[y:y+h,x:x+w]
        resized=cv2.resize(face,(width,height))
        cv2.imwrite('%s/%s.jpg' % (os.path.join(datasets,id),counter),resized)
    if(counter>31):
        break
    print counter
    cv2.imshow("Faces",im)
    key=cv2.waitKey(100)
    if key==27:
        break
camera.release()
cv2.destroyAllWindows()
