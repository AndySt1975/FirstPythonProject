#text = "Andy schreibt ein Textdokument via Python\nDas ist cool\I´m great"
text = "\nund so schreibe ich eine log datei"
with open('text1.txt','a') as file:
    file.write(text)


# copyfile() =  copies contents of a file
# copy() =       copyfile() + permission mode + destination can be a directory
# copy2() =     copy() + copies metadata (file’s creation and modification times)

import shutil

shutil.copyfile('test.txt','copy.txt') #src,dst