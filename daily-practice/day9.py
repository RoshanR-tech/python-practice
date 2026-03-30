# for fixed patter
def pattern():
    for i in range(2):
        for j in range(6):
            print("*", end=" ")
        print()

pattern()

# increasing triangle
def pattern():
    for i in range (1,4):
        for j in range (1, i+1):
            print ("*", end=" ")
        print()
pattern()

# To print stars in 4 rows and columns 
def pattern():
    for i in range (4):
        for j in range (4):
            print ("*", end=" ")
        print()
pattern()


#function to greet user
def greeting(name):
    print("Hello",name)
greeting("Roshan")
greeting("Vihitha")
