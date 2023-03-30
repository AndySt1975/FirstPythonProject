from tkinter import *
from time import *
# the directive from strftime %something look at the imagefile TimeStringModifier (rootfolder) for different formats
# or look at this link https://docs.python.org/3.2/library/time.html
def update():
    time_string = strftime("%H:%M:%S")
    time_label.config(text=time_string)

    day_string = strftime("%A")
    day_label.config(text=day_string)

    date_string = strftime("%B %d, %Y")
    date_label.config(text=date_string)

    window.after(1000,update)

window = Tk()
window.title("Andy's Clock")
window.config(background="black")

icon = PhotoImage(file='logo.png')
window.iconphoto(True, icon)

time_label = Label(window,font=("Arial",50),fg="#00FF00",bg="black")
#print("To get infos from Label you need to call a label.cget() ", time_label.cget("font"))
time_label.pack()
day_label = Label(window,font=("Verdana",25),fg="#00FF00",bg="black")
day_label.pack()
date_label = Label(window,font=("Verdana",25),fg="#00FF00",bg="black")
date_label.pack()

update()

window.mainloop()