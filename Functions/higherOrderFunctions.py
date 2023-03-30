#  Higher Order Function =  a function that either:
#                           1. accepts a function as an argument
#                               or
#                           2. returns a function
#                           (In python, functions are also treated as objects)

# ----- 1. accepts a function as an argument -----
def loud(text):
   return text.upper()

def quiet(text):
   return text.lower()

def hello(func):
   text = func("Hello")
   print(text)


hello(loud)
hello(quiet)
# ------------ 2. returns a function -------------
#def divisor(x):
   #def dividend(y):
       #return y / x
   #return dividend


#divide = divisor(2)    # x = 2 und bleibt 2 ****returns dividend*****
                        #                    ****divide wird zu dividend (returntype) ****   
#print(divide(10))      # x wird aus mir unbekanntem Grund nicht überschrieben und y als dividend gesetzt.....  
                        # macht quasi:  ***** print(divisor(2)(10)) *****
# #ergibt 5.0 nablo func in func kein plan unlogisch.... siehe ****