#generates a slide puzzle from a specified image

import tkinter
from tkinter import PhotoImage, Label, Button, image_names
import shuffler
from splitimage import splitImage
import time

SHUFFLES = 200 #number of movements the slide puzzle is shuffled by

class SlidePuzzle():

	#constructor
	#@param image the image being used for the puzzle
	#@win the tkinter window
	#@tileSpots list of which tile is in what position
	#@value self.null the location of the "null" tile (the empty space on the board)
	#@value imageList list of each section of the image for the slide puzzle
	def __init__(self, image):
		self.win = tkinter.Tk("Slide Puzzle")
		tileSpots = list(range(15))
		tileSpots.append(None)
		self.tileSpots = shuffler.shuffle(tileSpots,SHUFFLES)
		self.imageList = splitImage(image)
		self.null = tileSpots.index(None)

	#determines if the slide puzzle is done
	#by checking if each tile is in the right place
	def checkWin(self):
		return(self.tileSpots[:15] == list(range(15)))

	#switches the position of two tiles on the board
	def swap(self,i,j):
		self.tileSpots[i], self.tileSpots[j] = self.tileSpots[j], self.tileSpots[i]
		iValue = self.tileSpots[i]
		if not iValue:
			iValue = 15
		iPhoto = self.imageList[iValue] #not affiliated with Apple Inc. :)
		self.buttons[i].configure(image=iPhoto, command = lambda i=i: self.move(i))

		jValue = self.tileSpots[j]
		jPhoto = self.imageList[jValue]
		self.buttons[j].configure(image=jPhoto, command = lambda j=j: self.move(j))

	#moves a non-empty tile into the null spot
	def move(self,i):
		if i in [self.null+4,self.null+1, self.null -1, self.null-4]:
			self.swap(i,self.null)
			self.null = i
		if self.checkWin():
			self.done = time.time()
			self.gameOver()

	#clears the Tkinter window
	def clearWin(self):
		for w in self.win.winfo_children():
			w.destroy()

	#displays the time when the slide puzzle is completed
	def gameOver(self):
		totalTime = self.done - self.start
		self.clearWin()
		text = ('Final time: '+str(round(totalTime,2)))
		timeLabel = Label(self.win,text=text,bg='DeepSkyBlue2',font=('Arial',18))
		timeLabel.pack()

	#launches the slide puzzle
	#creates each button needed for the puzzle
	def run(self):
		self.buttons = []
		for i in list(range(16)):# + [None]:
			value = self.tileSpots[i]
			button = Button(self.win)
			if value == None:
				button.configure(image=self.imageList[15])
			else:
				button.configure(image=self.imageList[value])

			button.configure(command=lambda i=i: self.move(i))
			if i == None:
				button.grid(row=3,column=3)
			else:
				button.grid(row=int(i/4),column=(i%4))
			self.buttons.append(button)
		self.start = time.time()
		self.win.mainloop()