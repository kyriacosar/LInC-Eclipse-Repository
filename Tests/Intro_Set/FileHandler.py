'''
Created on Jun 19, 2017

@author: kyriacos
'''

newData = 12345
fileOut = open('newDataFile.txt', 'w')
fileOut.write("WTF")
fileOut.close()

fileIn = open("newDataFile.txt", 'r')
print(fileIn.read())
fileIn.close()