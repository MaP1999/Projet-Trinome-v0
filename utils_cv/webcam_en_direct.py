
import cv2 as cv
# 
# cap = cv.VideoCapture(0)
# 
# while True:
#     ret,im = cap.read()
#     cv.imshow('video test',im)
#     key = cv.waitKey(10)
# 
# cv.destroyAllWindows()

# setup video capture
cap = cv.VideoCapture(0)

ret,im = cap.read()
height, width = im.shape[:2]

while True:
    ret,im = cap.read()

    # trait horizontal
    for i in range(width):
        im[height//2][i] = [0, 0, 255]

    # trait vertical
    for i in range(height):
        im[i][width//2] = [255, 0, 0]

    cv.imshow('video test',im)
    key = cv.waitKey(1)
    
img = cv2.imread('Documents/CentraleSupelec/Cours/CodingWeeks/Projet-Trinome-v0/Data/lenna.jpg', 0)