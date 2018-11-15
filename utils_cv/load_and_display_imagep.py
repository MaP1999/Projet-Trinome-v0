
import cv2 as cv
import numpy as np

def load_and_display_image(filename):
    img = cv.imread(filename)
    taille = img.shape[:2]
    px=[]
    for i in range(taille[0]):
        for j in range(taille[1]):
             px =img[i,j]
             moyenne = (px[0]+px[1]+px[2])/3
             img[i,j] = [moyenne,moyenne,moyenne]
    # print(px)
    cv.imshow('image',img)
    cv.waitKey(0)
    #return







