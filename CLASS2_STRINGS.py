import sys
name = "Michael Jackson"
name
print(name)
print(name[0])#indexing
print(name[6])
print(name[14])
print(name[-1])#even with negative nuber works bt backwards
print(name[-15])
print(len(name))#leng gets you the size of the string
#slicing
v=name[0:5]
print(v)
#stride
print(name[0::2])#prints the second of all the string
print(name[0:14:2])#prints the second until the 14th
#concatenate strings
statement=name+' is the best'
print(statement)
#escape sequiencing with the slash /
print(" Michael Jackson \n is the best" )#this /n represents a new line
print(" Michael Jackson \t is the best" )# this /t represent a tab spacing
print(" Michael Jackson \\ is the best" ) #this represents a \ for the place with the double \\
# Convert all the characters in string to upper case
a = "Thriller is the sixth studio album"
print("before upper:", a)
b = a.upper()
print("After upper:", b)
# Replace the old substring with the new target substring is the segment has been found in the string
a = "Michael Jackson is the best"
b = a.replace('best', 'shit')
print(b)
# Find the substring in the string. Only the index of the first elment of substring in string will be the output
name = "Michael Jackson"
name.find('e')
name = "Michael Jackson"
print(name.find('ael'))
# If cannot find the substring in the string
print(name.find('chael'))#the answer will come back -1