import urllib.request
url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/example1.txt'
filename = 'Example1.txt'
urllib.request.urlretrieve(url, filename)
#---------------------------------------------------------------------------------------------
# Read the Example1.txt

example1 = "Example1.txt"
file1 = open("Example1.txt","r")
#WE can see the name of the file
print(file1.name)
print(file1.mode)#this would be read r or write w
#this would read the file
Text=file1.read()
print(Text)
print(type(Text))
#its very important to close the file to save resources
print(file1.closed)#check if its closed
file1.close()
print(file1.closed)#check if its close
#----------------------------------------------------------------------------------------------
#another better way is with with
with open("Example1.txt",'r') as file1:
    FileContent=file1.read()
    print(FileContent)
print(file1.closed)
#--------------------------------------------------------------------------------
# Read first four characters
with open(example1, "r") as file1:
    print(file1.read(9))#READTHE FIRST 9 CHARACTERS
    print(file1.read(4))

#-------------------------------------------------------
with open(example1, "r") as file1:
    print(file1.read(16))
    print(file1.read(5))
    print(file1.read(9))
#-----------------------------------------------------
#read one line
with open(example1, "r") as file1:
    print("first line: " + file1.readline(14))#this comand can only read one line
    print(file1.read(16))
#-----------------------------------------------------
# Iterate through the lines
with open(example1,"r") as file1:
        i = 0;
        for line in file1:
            print("Iteration", str(i), ": ", line)
            i = i + 1
#----------------------------------------------------------------
# Read all lines and save as a list
with open(example1, "r") as file1:
    FileasList = file1.readlines()
    print(FileasList)
    print(FileasList[2])#you can read the value of the line