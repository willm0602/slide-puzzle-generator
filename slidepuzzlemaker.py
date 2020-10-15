import tkinter
from tkinter import Frame, PhotoImage, Label, Button
import PIL
import time


def MakeSlidePuzzle(tileSpots, finalImage):
    
    win = tkinter.Tk()
    main = Frame(win)
    buttonList = []
    imgList = []
    startTime = 0
    endTime = 0
    #checks if the puzzle has been solved
    def checkWin(order):
        properOrder = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, None]
        return(properOrder==order)

    '''
    @nullSpot tile that is empty
    @buttonSpot tile to be moved
    @surroundingSpots the valid spots the tile can move to
    handles clicking on tiles
    '''
    def click(button, buttonValue):
        nullSpot = tileSpots.index(None)
        buttonSpot = tileSpots.index(buttonValue)
        
        #establishes surrounding spots
        surroundingSpots = [nullSpot-1,nullSpot-4,nullSpot+1,nullSpot+4]
     
        #swaps tiles
        if(buttonSpot in surroundingSpots):
            tileSpots[nullSpot] = buttonValue
            tileSpots[buttonSpot] = None
            nullSpot,buttonSpot = buttonSpot,nullSpot
            imgList[nullSpot], imgList[buttonSpot]=imgList[buttonSpot],imgList[nullSpot]
            buttonList[buttonSpot].configure(image=imgList[buttonSpot])
            buttonList[nullSpot].configure(image=imgList[nullSpot])
            print(tileSpots)
            
            #checks if the user won
            if(checkWin(tileSpots)):
                endTime = time.time()
                dtime = endTime-startTime
                main.destroy()
                myimage=PhotoImage(file='./assets/winscreen.png')
                finalScreen = Frame(win)
                label = Label(finalScreen,image=myimage)
                label.image = myimage
                label.pack()
                text = ('Final time: '+str(round(dtime,2)))
                timeLabel = Label(finalScreen,text=text,bg='DeepSkyBlue2',font=('Arial',18))
                timeLabel.place(x=100,y=320)
                finalScreen.pack()
                
    #adds each tile          
    for i in range(0,16):
        j = tileSpots[i]
        if not j == None:
            y = int(j/4)
            x = j%4
            area = (64*x,64*y,64*(x+1),64*(y+1))
            cropped = finalImage.crop(area)
            myimage=PIL.ImageTk.PhotoImage(cropped)
            imgList.append(myimage)
        else:
            img = PIL.ImageTk.PhotoImage(file='./assets/black.png')
            imgList.append(img)
        button = Button(main, image=imgList[i])
        button.configure(command=lambda k=i: click(button,tileSpots[k]))
        buttonList.append(button)
        button.grid(row=int(i/4),column=(i%4))
    print('puzzle generated')
    print('starting timer')
    startTime = time.time()
    main.pack()
    win.mainloop()
