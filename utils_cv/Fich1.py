import cv2


def load_and_display_image(filename):
    img= cv2.imread(filename, 0)
    cv2.imshow('image', img)
    cv2.waitKey(0)

#load_and_display_image("../Data/tetris_blocks.png")
