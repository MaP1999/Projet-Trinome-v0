
import cv2
def load_and_display_image(filename):
    img = cv2.imread(filename,0)
    #taille = shape(img)
    #for i in range(taille[0]):
    #    for j in range(taille[1]):
    #        px =img[i,j]
    #        for i in range(2):
    #            moyenne = (px[0]+px[1]+px[2])/3
    #            px = [moyenne,moyenne,moyenne]
    cv2.imshow('image',img)
    cv2.waitKey(0)
    #return





