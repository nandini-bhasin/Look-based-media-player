import numpy as numpy
import cv2
import keyboard

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
#face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')
#face_cascade = cv2.CascadeClassifier('F:/"A. Nandini"/"7th sem"/"Look based media player"/FindFace/OpenCV-Python-Series/src/cascades/data/haarcascade_eye.xml')
  
number=0
cap = cv2.VideoCapture(0)

flagPrev = False

while(True):       
    #capture frame by frame
    ret, frame = cap.read()
    #convert to grey scale
    gray  = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #identify any faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
    #scalefactor value high may make it more accurate, but too high and it will become a problem

    
    flag = False

    faces = faces[0:1]

    for (x, y, w, h) in faces:
        #roi = region of interest
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        #values are pixel values or coordinates
        #y+h => starts at y, add height
        #x+w => starts at x, add width


        #draw a rectange around face
        color = (255, 0, 0) #color of rectangle in rgb
        stroke = 2 #thickness
        cv2.rectangle(frame, (x, y), (x+w, y+h), color, stroke)
        #frame => we want to draw on the original frame
        #starting coordinates and ending coordinates 

        
        flag = True
        if(flagPrev != flag) :
            number+=1
            print("change! ")
            print(number)
            keyboard.press_and_release('space')
            flagPrev = not flagPrev

        flagPrev = flag

    
    
    if(flagPrev != flag) :
        number +=1
        print("change! ")
        print(number)
        keyboard.press_and_release('space')
        flagPrev = not flagPrev


    #display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

#release the capture
cap.release()
cv2.destroyAllWindows()   