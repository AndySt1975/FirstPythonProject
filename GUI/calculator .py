# **************************************************************
# Python Calculator
# **************************************************************
from tkinter import *

def button_press(num):

    global equation_text

    equation_text = equation_text + str(num)

    equation_label.set(equation_text)

def equals():

    global equation_text

    try:

        total = str(eval(equation_text))

        equation_label.set(total)

        equation_text = total

    except SyntaxError:

        equation_label.set("syntax error")

        equation_text = ""

    except ZeroDivisionError:

        equation_label.set("arithmetic error")

        equation_text = ""

def clear():

    global equation_text

    equation_label.set("")

    equation_text = ""


window = Tk()
window.title("Calculator program")
window.geometry("500x500")

equation_text = ""

equation_label = StringVar()

label = Label(window, textvariable=equation_label, font=('consolas',20), bg="white", width=24, height=2)
label.pack()

frame = Frame(window)
frame.pack()

button1 = Button(frame, text=1, height=4, width=9, font=35,
                 command=lambda: button_press(1))
button1.grid(row=0, column=0)

button2 = Button(frame, text=2, height=4, width=9, font=35,
                 command=lambda: button_press(2))
button2.grid(row=0, column=1)

button3 = Button(frame, text=3, height=4, width=9, font=35,
                 command=lambda: button_press(3))
button3.grid(row=0, column=2)

button4 = Button(frame, text=4, height=4, width=9, font=35,
                 command=lambda: button_press(4))
button4.grid(row=1, column=0)

button5 = Button(frame, text=5, height=4, width=9, font=35,
                 command=lambda: button_press(5))
button5.grid(row=1, column=1)

button6 = Button(frame, text=6, height=4, width=9, font=35,
                 command=lambda: button_press(6))
button6.grid(row=1, column=2)

button7 = Button(frame, text=7, height=4, width=9, font=35,
                 command=lambda: button_press(7))
button7.grid(row=2, column=0)

button8 = Button(frame, text=8, height=4, width=9, font=35,
                 command=lambda: button_press(8))
button8.grid(row=2, column=1)

button9 = Button(frame, text=9, height=4, width=9, font=35,
                 command=lambda: button_press(9))
button9.grid(row=2, column=2)

button0 = Button(frame, text=0, height=4, width=9, font=35,
                 command=lambda: button_press(0))
button0.grid(row=3, column=0)

plus = Button(frame, text='+', height=4, width=9, font=35,
                 command=lambda: button_press('+'))
plus.grid(row=0, column=3)

minus = Button(frame, text='-', height=4, width=9, font=35,
                 command=lambda: button_press('-'))
minus.grid(row=1, column=3)

multiply = Button(frame, text='*', height=4, width=9, font=35,
                 command=lambda: button_press('*'))
multiply.grid(row=2, column=3)

divide = Button(frame, text='/', height=4, width=9, font=35,
                 command=lambda: button_press('/'))
divide.grid(row=3, column=3)

equal = Button(frame, text='=', height=4, width=9, font=35,
                 command=equals)
equal.grid(row=3, column=2)

decimal = Button(frame, text='.', height=4, width=9, font=35,
                 command=lambda: button_press('.'))
decimal.grid(row=3, column=1)

clear = Button(window, text='clear', height=4, width=12, font=35,
                 command=clear)
clear.pack()

window.mainloop()

#Here is the short cut for creating buttons through 9 to 1, order is 9 to 1 not like in Bro's code as 1 to 9, however you can change order if you want;

#btns = []
#btns_nmbr = -1

#for x in range(0, 3):

    #for y in range(0, 3):
        #btns_nmbr += 1

        #btns.append(Button(frame, text=9 - btns_nmbr, height=4, width=9, font=35,
                           #command=lambda btns_nmbr=btns_nmbr: button_press(9 - btns_nmbr)))
       # btns[btns_nmbr].grid(row=x, column=y)


#for other buttons , i think we still need to define it seperately.


# why Lambda-function on buttons:
#the lambda function is actually quite important for the making of the whole thing. 
#usually when we make a button its for example:
#button1 = Button1(window, command = button_press)
#however, in this case we have to pass in an argument for the button_press() 
# function, with num as its parameter (button_press(num))
#by doing button1=Button1(window,command = button_press(1)), 
# we call the function since we added parenthesis at the back of the function, 
# before the button is even pressed. Of course we dont want the command 
# / function bounded to a button to execute before we even press a button, 
# but we cant pass an argument without parathesis (brackets) either, so this is where lambda comes in. 
#The lambda function will prevent the command bounded to the button to activate before 
# we press the button by creating a function on the spot with the expression button_press(1). Hope this helps.