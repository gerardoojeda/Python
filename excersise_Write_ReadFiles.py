#Run this prior to starting the exercise
from random import randint as rnd

memReg = 'members.txt'
exReg = 'inactive.txt'
fee =('yes','no')

def genFiles(current,old):
    with open(current,'w+') as writefile:
        writefile.write('Membership No  Date Joined  Active  \n')
        data = "{:^13}  {:<11}  {:<6}\n"

        for rowno in range(20):
            date = str(rnd(2015,2020))+ '-' + str(rnd(1,12))+'-'+str(rnd(1,25))
            writefile.write(data.format(rnd(10000,99999),date,fee[rnd(0,1)]))


    with open(old,'w+') as writefile:
        writefile.write('Membership No  Date Joined  Active  \n')
        data = "{:^13}  {:<11}  {:<6}\n"
        for rowno in range(3):
            date = str(rnd(2015,2020))+ '-' + str(rnd(1,12))+'-'+str(rnd(1,25))
            writefile.write(data.format(rnd(10000,99999),date,fee[1]))


def cleanFiles(currentMem, exMem):
    '''
    currentMem: File containing list of current members
    exMem: File containing list of old members

    Removes all rows from currentMem containing 'no' and appends them to exMem
    '''
    with open(memReg, 'r') as writefile:
        with open(exReg,'a')as appendfile:
            #we start from the begining of the data
            writefile.seek(0)
            members=writefile.readlines()
            #now the heather
            Header=members[0]
            members.pop(0)
            inactive = [member for member in members if ('no' in member)]
            for member in active:
                if 'no' in member:
                    inactive.append(member)

            appendfile.seek(0)
            appendfile.write(Header)
            for member in members:
                if (member in inactive):
                    appendFile.write(member)
                else:
                    writeFile.write(member)
            writeFile.truncate()








# Code to help you see the files
# Leave as is
genFiles(memReg,exReg)
memReg = 'members.txt'
exReg = 'inactive.txt'
cleanFiles(memReg, exReg)

headers = "Membership No  Date Joined  Active  \n"
with open(memReg, 'r') as readFile:
    print("Active Members: \n\n")
    print(readFile.read())

with open(exReg, 'r') as readFile:
    print("Inactive Members: \n\n")
    print(readFile.read())
