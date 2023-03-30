from tkinter import *
from time import *

def update():
    time_string = strftime("%H:%M:%S")
    time_label.config(text=time_string)

    time_label.after(1000,update)

window = Tk()
window.title("Andy's Clock")

icon = PhotoImage(file='logo.png')
window.iconphoto(True, icon)

time_label = Label(window,font=("Arial",50),fg="#00FF00",bg="black")
#print("To get infos from Label you need to call a label.cget() ", time_label.cget("font"))
time_label.pack()

update()

window.mainloop()