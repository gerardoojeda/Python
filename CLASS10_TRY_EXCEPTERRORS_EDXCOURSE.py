import sys
# potential code before try catch,in this case if you imput a 0 or a letter will not become succesful and
# would print an error
a = 1

try:
    b = int(input("Please enter a number to divide a"))
    a = a / b
    print("Success a=", a)
except:
    print("There was an error")
#-----------------------------------------------------------------------------
a = 1

try:
    b = int(input("Please enter a number to divide a"))
    a = a / b
    print("Success a=", a)
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")
#-------------------------------------------------------------------------------
a = 1

try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")
else:
    print("success a=",a)
#----------------------------------------------------------------------------
a = 1
try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")
else:
    print("success a=",a)
finally:
    print("Processing Complete")
