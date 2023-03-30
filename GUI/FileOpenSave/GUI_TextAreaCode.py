from tkinter import *
from tkinter import filedialog

def saveFile():
    file = filedialog.asksaveasfile(
                                    defaultextension='.txt',
                                    filetypes=[
                                        ("Text file",".txt"),
                                        ("HTML file", ".html"),
                                        ("All files", ".*"),
                                    ])
    if file is None:
        return
    filetext = str(text.get(1.0,END))
    file.write(filetext)
    file.close()

window = Tk()
text = Text(window,
            bg="light yellow",
            font=("Ink Free",25),
            height=8,
            width=20,
            padx=20,
            pady=20)
text.pack()
button = Button(text='save',command=saveFile)
button.pack()
window.mainloop()