import cv2,numpy,os
(images, labels, names, id) = ([], [], {}, 0)
calculate={}
datasets='datasets'
for(subdirs,dirs,files) in os.walk(datasets):
    for subdir in dirs:
        names[id]=subdir
        calculate[subdir]=0
        subject=os.path.join(datasets,subdir)
        for file in os.listdir(subject):
            path=subject+'/'+file
            label=id
            images.append(cv2.imread(path,0))
            labels.append(int(label))
        id+=1
width,height=(130,100)
(images,labels)=[numpy.array(lis) for lis in [images,labels]]
rec=cv2.face.createFisherFaceRecognizer()
rec.train(images,labels)
faceD=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
camera=cv2.VideoCapture(0)
co=1
while True:
    ret,im=camera.read()
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces=faceD.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in faces:
        co+=1
        cv2.rectangle(im,(x,y),(x+w,y+h),(255,0,0),2)
        face=gray[y:y+h,x:x+w]
        resized=cv2.resize(face,(width,height))
        prediction=rec.predict(resized)
        print co
        cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,0),3)
        if prediction<500:
            calculate[names[prediction]]+=1
        else:
            print "not recognized"
    cv2.imshow("face",im)
    if(cv2.waitKey(10)==27):
        break
key, value = max(calculate.iteritems(), key=lambda x:x[1])
if(value==0):
    print "not recognized"
else:
    print key
camera.release()
cv2.destroyAllWindows()
