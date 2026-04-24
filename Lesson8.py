import os



fileHandle = open("test.txt","r")
listoflines = fileHandle.readlines()
for line in listoflines:
    print(line)
fileHandle.close()