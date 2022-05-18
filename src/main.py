import cv2
import numpy as np
from matplotlib import pyplot as plt

def show_Image(img):
    obj_img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    plt.imshow(obj_img)
    plt.show()



def main():
    img = cv2.imread('src/imgs/nature.jpg')
   
    show_Image(img)

main()    

