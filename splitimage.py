#splits a PIL image into a 4x4 grid with a black space at the end

import PIL

def splitImage(image):
    imgList = [] #list of each tiles image for the slide puzzle
    for i in range(15):
        y = int(i/4) #row that the tile is in
        x = i%4 #col. that the tile is in
        area = (64*x,64*y,64*(x+1),64*(y+1))
        cropped = image.crop(area)
        myimage=PIL.ImageTk.PhotoImage(cropped)
        imgList.append(myimage)
    nullImg = PIL.ImageTk.PhotoImage(file='./assets/black.png')
    imgList.append(nullImg)
    return(imgList)