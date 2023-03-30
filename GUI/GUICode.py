from tkinter import *

window = Tk () # instantiate an insance of a window
window.geometry("640x420")
window.title("Andy Main Window")

icon = PhotoImage(file='logo.png')# photofile has to be in root-order or complete path:
window.iconphoto(True, icon)
window.config(background="black")#you can enter #hexcode for different colors

label = Label(window,
               text="Andy is the greatest coder in the world",
               font=('Arial',20,'bold'),
               fg='green',
               bg='black',
               relief=RAISED,#umrandung  FLAT, RAISED, SUNKEN, GROOVE, RIDGE
               bd=6,        #rahmenbreite
               padx=20,     #abstandx
               pady=5,     #abstandy
               image=icon,  #bild (überschreibt den Text ohne compound)
               compound="bottom")      

label.pack()# this one put the label in the center | another way to put the label on the window is label.place(x=0,y=0)

window.mainloop() # place window on computer screen, listen for events

