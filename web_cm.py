import cv2 as cv
import winsound
img = cv.VideoCapture(0)
while img.isOpened():
    ret, frame1 = img.read()
    ret, frame2 = img.read()
    diff = cv.absdiff(frame1,frame2) 
    #it will find the difference between two frames and 
    #show the difference if any but will be of different colours so next we will convert 
    # it into gray scale so the error will be minimized
    gray = cv.cvtColor(diff,cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray,(5,5), 0)
    _, thres = cv.threshold(blur,20,255,cv.THRESH_BINARY) # we use threshhold to cancel the noise or unwanted things dialation is just opposite of the threhold once we apply threhold then we got rid of all the unwanted things then we have interested things and now to make them bigger we can use dialation 
    dialated = cv.dilate(thres, None, iterations=3)
    contours , _ = cv.findContours(dialated , cv.RETR_TREE ,cv.CHAIN_APPROX_SIMPLE) # contour will add boundary on the moving object
     #cv.drawContours(frame1,contours, -1,(0,255,0) ,2)
    for c in contours:
        if cv.contourArea(c) < 2000:   # if the area will be less than 2000 then it will not show contours
            continue
        x,y,w,h = cv.boundingRect(c)
        cv.rectangle(frame1,(x,y) , (x+w,y+h) , (25,255,0) ,2)
        winsound.PlaySound('alert sound.wav' , winsound.SND_ASYNC)
        #winsound.Beep(500,200) this will play built in beep sound whenever there will be movement
    if cv.waitKey(1) == ord('q'):
        break
    cv.imshow('cam1',frame1) 
   