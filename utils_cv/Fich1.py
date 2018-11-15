import numpy as np
import cv2 as cv

chdir='C://Users//Marvin//Documents//CentraleSupélec//Cours//CodingWeeks//Projet-Trinome-v0//data//tetris_blocks.png'
tetris='tetris_blocks.png'

def load_and_display_image(filename):
    img=cv2.imread(filename,0)
    cv2.imshow('fenetre',img)
    cv2.waitKey(0)
<<<<<<< HEAD

#load_and_display_image("../Data/tetris_blocks.png")
=======
    # print(img)
>>>>>>> 7f35f214c3dbac34cb9a02eedc2a5955fdb7c117
