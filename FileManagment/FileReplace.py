import os

source = "C:\\Users\\User\\Desktop\\source.txt"
destination = "C:\\Users\\User\\Desktop\\destination.txt"

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source,destination)
        print(source+" was moved")
except FileNotFoundError:
    print(source+" was not found")



    # user posted this example 
    # used shutil to move a file / folder in another logical drive
    #import os
#import shutil

#shutil.move

#source = "movetest.txt"
#destination = "C:\\Users\\Claes\\Desktop\\movetest.txt"

#try:
    #if os.path.exists(destination):
        #print("There is already a file there")
    #else:
       # shutil.move(source,destination) 
       # print(source+" was moved")
#except FileNotFoundError:
    #print(source+" was not found")