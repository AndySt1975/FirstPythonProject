print("hello world")

name = "Andy"
# die string mit + version
print("Hello "+name)

age = 33
kommazahl = 12.22
print (age)
#die type casting version
print ("bla abla " + str(age))
# print(type(age))

# die Version mit komma
print ("ohne + geht das mit Komma", age, kommazahl)

# das nächste Beispiel ist ein f-string (das gleiche wie in c# das $"bla{field}")
print (f"und die dritte Möglichkeit ist mit f vor dem String {age} und dann in curly Braces {kommazahl} die Variablen")
# sind übrigens die Kommentarzeichen hier nicht wie in c# das //


# if werden ohne klammer und geschweifte klammern geschrieben, dafür mit :

frage = False

if frage:
    print("frage ist true")
else: print ("frage ist false")

# normale deklaration mit initialisierung
x = 1
y = 2
z = 3

#oder zusammen
u, v, w = 4, 5, 6
# noch dämlicher
dämlich = totaldämlich = absolutdämlich = 8
print("die einzeldeklaration ",x,y,z)
print("die multikackmethode", u, v, w)
print("die dämlichste Version ", dämlich, totaldämlich, absolutdämlich)


