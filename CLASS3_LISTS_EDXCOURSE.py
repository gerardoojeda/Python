import sys
#indexing
# Create a list
L = ["Michael Jackson", 10.1, 1982]
print(L)
# Print the elements on each index
print('the same element using negative and positive indexing:\n Postive:',L[0],
'\n Negative:' , L[-3]  )
print('the same element using negative and positive indexing:\n Postive:',L[1],
'\n Negative:' , L[-2]  )
print('the same element using negative and positive indexing:\n Postive:',L[2],
'\n Negative:' , L[-1]  )
# Sample List
print(["Michael Jackson", 10.1, 1982, [1, 2], ("A", 1)])
# Use extend to add elements to list
print('este')
L = [ "Michael Jackson", 10.2]
L.extend(['pop', 10])
print()
print(len(L))
# Use append to add elements to list in !!ONE SPOT ONLY

L = [ "Michael Jackson", 10.2]
L.append(['pop', 10])
print(L)
print(len(L))
print(L[2])
# Change the element based on the index

A = ["disco", 10, 1.2,89]
print('Before change:', A)
A[2] = 'hard rock'
print('After change:', A)
# Delete the element based on the index

print('Before change:', A)
del(A[1])
print('After change:', A)
# Split the string, default is by space
print('hard rock'.split())
print(A)
# Split the string by comma
T=[('A,B,C,D')]
print(len(T))
T='A,B,C,D'.split(',')
print(len(T))
# Copy (copy by reference) the list A

A = ["hard rock", 10, 1.2]
B = A
print('A:', A)
print('B:', B)
# Examine the copy by reference and change a value for example hard rock to banana
# and this will change the value of B as well
print('B[0]:', B[0])
B[0] = "banana"
print('B[0]:', B[0])
print(A)
print(B)
# Clone (clone by value) the list A
#its important that if you clone the A list and do a change in A this will not reflect the changes in F
F = A[:]#cloning
print('F: ',F)

print('F[0]:', F[0])
A[0] = "hard rock"#changing the value of A[0]
print('A:',A)
print('F:', F)