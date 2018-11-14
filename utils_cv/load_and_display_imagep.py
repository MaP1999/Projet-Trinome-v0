import argparse
import cv2
def load_and_display_image(filename):
    arg = argparse.ArgumentParser()
    arg.add_argument("-i", "--img", dest=filename, default=False, help ="le fichier image à lire")
    arg.add_argument("-d", "--dest", dest="imgdest", help ="le fichier image à sauvegarder")
    args = arg.parse_args()
    imgfile = args.filename
    imgdest = args.imgdest
    img = cv2.imread(filename)
    taille = img.shape()
    for i in range(taille[0]):
        for j in range(taille[1]):
            px =img[i,j]
            for i in range(2):
                moyenne = (px[0]+px[1]+px[2])/3
                px = [moyenne,moyenne,moyenne]
    if (imgdest):
        cv2.imwrite(imgdest,img)

    cv2.imshow('image',img)
    cv2.waitKey(0)
    return








