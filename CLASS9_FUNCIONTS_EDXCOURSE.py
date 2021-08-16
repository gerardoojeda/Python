import sys
# First function example: Add 1 to a and store as b
def add(a):
    """
    add 1 to a
    """
    b = a + 1
    print(a, "if you add one", b)
    return(b)

c=add(10)
print(c)
# Get a help on add function

help(add)
#---------------------------------------------------------------
# Define a function for multiple two numbers
def Mult(a, b):
    c = a * b
    return (c)
    print('This is not printed')

result = Mult(100, 2.5)#INCLUSE WE CAN MULTIPLY FLOATS OR STR
print(result)
#----------------------------------------------------------------------------------
#Variables in functions
# Function Definition
def square(a):
    # Local variable b
    b = 1
    c = a * a + b
    print(a, "if you square + 1", c)
    return (c)
#--------------------------------------------------------------------------------
# Define functions, one with return value None and other without return value
def MJ():
    print('Michael Jackson')
#or cuold also be
def MJ1():
    print('Michael Jackson')
    return (None)
#---------------------------------------------------------------------------------
#predefined functions
# Build-in function print()
album_ratings = [10.0, 8.5, 9.5, 7.0, 7.0, 9.5, 9.0, 9.5]
print(album_ratings)
# Use sum() to add every element in a list or tuple together
sum(album_ratings)
# Show the length of the list or tuple
len(album_ratings)
#------------------------------------------------------------------------------------
# Function example

def type_of_album(artist, album, year_released):
    print(artist, album, year_released)
    if year_released > 1980:
        return "Modern"
    else:
        return "Oldie"


x = type_of_album("Michael Jackson", "Thriller", 1980)
print(x)
#--------------------------------------------------------------------------------------
#setting a default value in a function
# Example for setting param with default value
def isGoodRating(rating=4):
    if (rating < 7):
        print("this album sucks it's rating is", rating)

    else:
        print("this album is good its rating is", rating)

isGoodRating()
isGoodRating(10)
#---------------------------------------------------------------------------------------
artist = "Michael Jackson"
def funcprinter(artist):
    global internal_var #if you dont define this variable as global yu would print it in the main code
    internal_var= "Whitney Houston"
    print(artist,"is an artist")

funcprinter(artist)
funcprinter(internal_var)
#------------------------------------------------------------------------------------
def printAll(*args): # All the arguments are 'packed' into args which can be treated like a tuple
    print("No of arguments:", len(args))
    for argument in args:
        print(argument)
#printAll with 3 arguments
printAll('Horsefeather','Adonis','Bone')
#printAll with 4 arguments
printAll('Sidecar','Long Island','Mudslide','Carriage')
#----------------------------------------------------------------------------------------
def printDictionary(**args):#as dictorionary
    for key in args:
        print(key + " : " + args[key])

printDictionary(Country='Canada',Province='Ontario',City='Toronto')
#---------------------------------------------------------------------------------------
def addItems(list):#or as a list
    list.append("Three")
    list.append("Four")


myList = ["One", "Two"]

addItems(myList)

print(myList)
