import random, time, datetime, math, sys
from tkinter import image_names
import shuffler
from image_prep import resize
from slidepuzzlemaker import MakeSlidePuzzle
import googleImgLoader

IMAGE_PATH = "./assets/imageFile.png"
SIZE = 256

phrase = input('What image would you like to input for?\n')
try:
    print('Obtaining image')
    googleImgLoader.writeFileImg(phrase,IMAGE_PATH)
except:
    print('Error getting image, check internet connection')
    sys.exit()
print('Image Obtained')

tiles = list(range(15))
tiles.append(None)
tiles = shuffler.shuffle(tiles,500)

image = resize(IMAGE_PATH,256)

MakeSlidePuzzle(tiles,image)

