
import cv2
def load_and_display_image(filename):
    img = cv2.imread(filename)
    taille = img.shape[:2]
    px=[]
    for i in range(taille[0]):
        for j in range(taille[1]):
             px =img[i,j]
             moyenne = (px[0]+px[1]+px[2])/3
             img[i,j] = [moyenne,moyenne,moyenne]
    print(px)
    cv2.imshow('image',img)
    cv2.waitKey(0)
    #return







