import numpy as np
import cv2


def face_detection(filename):
    im = cv2.imread(filename)
    detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(im,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = im[y:y+h, x:x+w]
    cv2.imshow("pic", im)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


face_detection('../data//lenna.jpg')
