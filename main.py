import random, time, datetime, math, sys
from tkinter import image_names
import shuffler
from image_prep import prep
from Slidepuzzle import SlidePuzzle
import googleImgLoader

IMAGE_PATH = "./assets/imageFile.png"
SIZE = 512

phrase = input('What image would you like to input for?\n')

try:
    print('Obtaining image')
    googleImgLoader.writeFileImg(phrase,IMAGE_PATH)
except:
    print('Error getting image, check internet connection')
    sys.exit()
print('Image Obtained')

labels = True

image = prep(IMAGE_PATH,256,labels)

puzzle = SlidePuzzle(image)
puzzle.run()