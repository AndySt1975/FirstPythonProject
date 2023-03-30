try:
    with open('Text.txt') as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found :(")

with open('Text.txt') as file:
    print()
    print()
    print(file.read())
    print("Meine Func")
