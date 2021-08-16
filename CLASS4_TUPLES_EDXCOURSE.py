import sys
# Create your first tuple

tuple1 = ("disco",10,1.2 )
print(tuple1)
print(type(tuple1))
# Print the variable on each index

print(tuple1[0])
print(tuple1[1])
print(tuple1[2])
# Print the type of value on each index

print(type(tuple1[0]))
print(type(tuple1[1]))
print(type(tuple1[2]))
# Use negative index to get the value of the third last element

print(tuple1[-3])
# Concatenate two tuples

tuple2 = tuple1 + ("hard rock", 10)
print(tuple2)
# Slice from index 0 to index 2

print('hey',tuple2[0:3])
# Get the length of tuple

print(len(tuple2))
#sorting
# A sample tuple
Ratings = (0, 9, 6, 5, 10, 8, 9, 6, 2)
print(type(Ratings))
Ratings=sorted(Ratings)#this sortes in order the values of the input parameters
print(type(Ratings))

# Create a nest tuple

NestedT =(1, 2, ("pop", "rock") ,(3,4),("disco",(1,2)))
print("Element 2, 0 of Tuple: ",   NestedT[2][0])
print("Element 2, 1 of Tuple: ",   NestedT[2][1])
print("Element 3, 0 of Tuple: ",   NestedT[3][0])
print("Element 3, 1 of Tuple: ",   NestedT[3][1])
print("Element 4, 0 of Tuple: ",   NestedT[4][0])
print("Element 4, 1 of Tuple: ",   NestedT[4][1][0])


# Print the first element in the second nested tuples

print(NestedT[2][1][0:3])#this would get the R of rock
# Print the second element in the second nested tuples

NestedT[4][1][1]#this would get the 4

#get the index for a word
print(NestedT.index(2))