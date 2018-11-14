import numpy as np
import cv2 as cv

chdir='C://Users//Marvin//Documents//CentraleSupélec//Cours//CodingWeeks//Projet-Trinome-v0//data//tetris_blocks.png'
tetris='tetris_blocks.png'

def load_and_display_image(filename):
    img=cv2.imread(filename,0)
    cv2.imshow('fenetre',img)
    cv2.waitKey(0)
    # print(img)
