from tkinter import *
from tkinter import ttk
from random import randint, choice

root = Tk()

time = 500
def mover():
	virus = [
	"Virus","Awit","virus to" 
	]
	x = 360
	y = 684
	h = 300
	w = 250
	rx = randint(0,x)
	ry = randint(0,y)
	hr = randint(50,h)
	hw = randint(50,w)
	rt = choice(virus)
	
	root.title(rt)
	root.geometry(f"{hr}x{hw}")
	root.geometry(f"+{rx}+{ry}")
	root.after(time,mover)
	
root.after(time,mover)

root.mainloop()
