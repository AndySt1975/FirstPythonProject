from tkinter import *

# button = you click it, then it does stuff

count = 0

def click():
    global count
    count+=1
    label.config(text=str(count))
    print(count)

window = Tk()
window.config(bg="black")   #hatebackground white bye - die you bastard

photo = PhotoImage(file='logo.png')

button = Button(window,
                text="click me!",
                command=click,
                font=("Arial Black",30),
                fg="#00FF00",
                bg="black",
                activeforeground="#00FF00",
                activebackground="black",
                state=ACTIVE,
                image=photo,
                compound='bottom')
button.pack()

label = Label(window,text=str(count),font=("Arial Black",30),fg="Green", bg="Black")
label.pack()

window.mainloop()