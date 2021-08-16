# Write line to file
exmp2 = 'C:/Users/carlo/PycharmProjects/Project1/Lessons/Example2.txt'
with open(exmp2, 'w') as writefile:
    writefile.write("This is line A homogey")
#-----------------------------------------------
# Read file
with open(exmp2, 'r') as testwritefile:
        print(testwritefile.read())
print(testwritefile.closed)
#-------------------------------------------------------------------
# Write lines to file
with open(exmp2, 'w') as writefile:
    writefile.write("This is line A\n")
    writefile.write("This is line B\n")
with open(exmp2, 'r') as testwritefile:
        print(testwritefile.read())
#---------------------------------------------------------------------
# Sample list of text
Lines = ["This is line A\n", "This is line B\n", "This is line C\n"]
Lines
line=0
with open(exmp2,'w') as writefile:
    for line in Lines:
        print(line)
        writefile.write(line)#here we are sayving in each line the value of lines for each line

with open('example2.txt','r') as trycheck:
    print(trycheck.read())#here we are checking to sea if it was saved
#------------------------------------------------------------------
#note that everytime is writed is overwritten
with open('Example2.txt', 'w') as writefile:
    writefile.write("Overwrite\n")
with open('Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())
#--------------------------------------------------------------------------
#APPENDING
with open('example2.txt','a') as appenText:
    appenText.write("This is line C\n")
    appenText.write("This is line D\n")
    appenText.write("This is line E\n")

with open('Example2.txt', 'r') as testappendfile:
    print(testappendfile.read())
#------------------------------------------------------------------------------
#ADDITIONAL MODES
with open('Example2.txt', 'a+') as testwritefile:
    testwritefile.write("This is line F\n")
    print(testwritefile.read())#this will not appear the whole thing beause its like a pointer and its not in its correct
    #place so check under
#-------------------------------------------------------------------------------
with open('Example2.txt', 'a+') as testwritefile:
    print("Initial Location: {}".format(testwritefile.tell()))

    data = testwritefile.read()
    if (not data):  # empty strings return false in python
        print('Read nothing')
    else:
        print(testwritefile.read())

    testwritefile.seek(0, 0)  # move 0 bytes from beginning.

    print("\nNew Location : {}".format(testwritefile.tell()))
    data = testwritefile.read()
    if (not data):
        print('Read nothing')
    else:
        print(data)

    print("Location after read: {}".format(testwritefile.tell()))
#-----------------------------------------------------------------------------
with open('Example2.txt', 'r+') as testwritefile:
    data = testwritefile.readlines()
    print(data)
    testwritefile.seek(0, 0)  # write at beginning of file

    testwritefile.write("Line 1" + "\n")
    testwritefile.write("Line 2" + "\n")
    testwritefile.write("Line 3" + "\n")
    testwritefile.write("finished\n")
    # Uncomment the line below
    testwritefile.truncate()
    testwritefile.seek(0, 0)
    print(testwritefile.read())
#---------------------------------------------------------------------------------
#copy from one file to the other
# Copy file to another
with open('Example2.txt','r') as readfile:
    with open('Example3.txt','w') as writefile:
          for line in readfile:
                writefile.write(line)
# Verify if the copy is successfully executed

with open('Example3.txt','r') as testwritefile:
    print(testwritefile.read())