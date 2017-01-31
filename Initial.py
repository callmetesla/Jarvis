import cv2,os,numpy
import subprocess
from gtts import gTTS
def speak(s):
    print(s)
    tts=gTTS(text=s,lang='en')
    tts.save('t1.mp3')
    os.system('mpg321 -q t1.mp3')
    os.remove('t1.mp3')
def reg():
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
    mean,cal=0,0
    while True:
        ret,im=camera.read()
        gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        faces=faceD.detectMultiScale(gray,1.3,5)
        for(x,y,w,h) in faces:
            co+=1
            cv2.rectangle(im,(x,y),(x+w,y+h),(255,0,0),2)
            face=gray[y:y+h,x:x+w]
            resized=cv2.resize(face,(width,height))
            prediction,conf=rec.predict(resized)
            cal+=conf
            print prediction,conf
            #cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,0),3)
            #cv2.imshow("face",im)
            #cv2.waitKey(0)
            if prediction<500:
                calculate[names[prediction]]+=1
            else:
                print "Not recognized"
        if(co>15):
            mean=cal/15
            print mean
            break
    key, value = max(calculate.iteritems(), key=lambda x:x[1])
    if(value==0 or mean>700):
        print "not recognized"
        return "not recognized"
    else:
        print key
        return key
    camera.release()
    print calculate
    cv2.destroyAllWindows()
if __name__=="__main__":
    speak('Hello')
    speak('Please look at the camera')
    cont=reg()
    if(cont=="not recognized"):
        speak("No Access")
    else:
        speak("Hello "+cont)
        subprocess.call(["python","Speech.py"])
