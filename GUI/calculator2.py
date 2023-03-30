# Calculator program nilli von den Kommentaren Spaghetti-code 
# In python
#-----------------------------
def addition(x,y):
    output1 = (x + y)
    return output1
#-----------------------------
def subtraction(x,y):
    output2 = (x - y)
    return output2
#-----------------------------
def multiplication(x,y):
    output3 = (x * y)
    return output3
#-----------------------------
def division(x,y):
    output = (x / y)
    return output
#-----------------------------
def square(z):
    output4 = (z * z)
    return output4
#-----------------------------
def cube(z):
    output5 = (z * z * z)
    return output5
#-----------------------------
def factorial_pos(z):
    output6 = 1
    for i in range(z,1,-1):
        output6 = (output6 * i)
    return output6
#-----------------------------
def factorial_neg(z):
    output7 = -1
    for i in range(z,-1):
        output7 = (output7 * i)
    return output7
#-----------------------------
def exp_pos(b,p):
    output8 = 1
    for i in range(p):
        output8 = (output8 * b)
    return output8
#-----------------------------
def exp_neg(b,p):
    output9 = -1
    for i in range(p):
        output9 = (output9 * b)
    return output9
#-----------------------------
def mtp_tables_ps(x,y):
    print("\nResult:\n")
    for i in range(1,y+1):
        print(f"{x} x {i} = {x*i}")
    else:
        print(f'''\nThese are the multiplication tables
of {x} with-in the range of {y}''')
#-----------------------------
def mtp_tables_ng(x,y):
    print("\nResult:\n")
    for i in range(-1,(y-1),-1):
        print(f"{x} x {i} = {x*i}")
    else:
        print(f'''\nThese are the multiplication tables
of {x} with-in the range of {y}''')
#-----------------------------
def operator(c):
    if(c == ('+')):
        try:
            x = float(input("Enter 1st number\n: "))
            y = float(input("Enter 2nd number\n: "))
        except ValueError:
            print("You can only enter integers.Try to run again!")
        else:
            print("Result:")
            print(addition(x,y))
    elif(c == ('-')):
        try:
            x = float(input("Enter 1st number\n: "))
            y = float(input("Enter 2nd number\n: "))
        except ValueError:
            print("You can only enter integers.Try to run again!")
        else:
            print("Result:")
            print(subtraction(x,y))
    elif(c == ('*')):
        try:
            x = float(input("Enter 1st number\n: "))
            y = float(input("Enter 2nd number\n: "))
        except ValueError:
            print("You can only enter integers.Try to run again!")
        else:
            print("Result:")
            print(multiplication(x,y))
    elif(c == ('/')):
        try:
            x = float(input("Enter 1st number\n: "))
            y = float(input("Enter 2nd number\n: "))
            division(x,y)
        except ValueError:
            print("You can only enter integers.Try to run again!")
        except ZeroDivisionError:
            print("You cant divide by 0.Try to run again!")
        else:
            print("Result:")
            print(division(x,y))
    elif(c == ("**")):
        try:
            z = float(input("Enter the number to sqaure it\n: "))
        except ValueError:
            print("You can only enter integers.Try to run again!")
        else:
            print("Result:")
            print(square(z))
    elif(c == ("***")):
        try:
            z = float(input("Enter the number to cube it\n: "))
        except ValueError:
            print("You can only enter integers.Try to run again!")
        else:
            print("Result:")
            print(cube(z))
    elif(c == ('!')):
        try:
            z = int(input("Enter the number to calculate its factorial\n: "))
            if(z > 0):
                print("Result:")
                print(factorial_pos(z))
            elif(z < 0):
                print("Result:")
                print(factorial_neg(z))
            else:
                if(z == 0):
                    print("Result:")
                    print(z*0)
                else:
                    pass
        except ValueError:
            print("You can only enter Integers.Try to run again!")
    elif(c == ('exp')):
        try:
            b = int(input("Enter the base number\n: "))
            p = int(input("Enter the power number\n: "))
            if(p < 0):
                print("You cant enter negative integers as Power.Try to run again!")
            elif(b > 0):
                print("Result:")
                print(exp_pos(b,p))
            elif(b < 0):
                print("Result:")
                print(exp_neg(b,p))
            elif(b == 0):
                print("Result:")
                print(b*0)
            else:
                pass
        except ValueError:
            print("You can only enter Integers.Try to run again!")
    elif(c == "mtp"):
        try:
            x = int(input("Enter the number for its multiplication tables\n: "))
            y = int(input("Enter the range for the tables\n: "))
            if(y > 0):
                mtp_tables_ps(x,y)
            elif(y < 0):
                mtp_tables_ng(x,y)
            else:
                print("Result:")
                print(x*y)
        except ValueError:
            print("You can only enter Integers.Try to run again!")
    else:
        print("Invalid operator!")
#-----------------------------
def new_program(c):
    c = input('''Enter an operator sign:
('+' , '-' , '*' , '/' , '**' , '***' , '!' , 'exp' , 'mtp')\n: ''')
    operator(c)
#-----------------------------
c = input('''Enter an operator sign:
('+' , '-' , '*' , '/' , '**' , '***' , '!' , 'exp' , 'mtp')\n: ''')
operator(c)
print()
ctn = input('''Do you want to continue your calculation?
Enter 'y' for Yes / 'n' for No.\n: ''')

ctn_cmd = ['y','Y','n','N']

while(ctn == 'y' or ctn == 'Y'):
    print()
    new_program(c)
    print()
    ctn = input('''Do you want to continue your calculation?
Enter 'y' for Yes / 'n' for No.\n: ''')
if(ctn == 'n' or ctn == 'N'):
    print()
    print("Thank you for using the calculator.\n")
else:
    if(ctn not in ctn_cmd):
        print("Invalid command!Try to run again.")
    else:
        pass
#-----------------------------
# Code finished successfully