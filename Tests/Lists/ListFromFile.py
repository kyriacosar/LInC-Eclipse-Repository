'''
Created on Jun 19, 2017

@author: kyriacos
'''

fileIn = open("numbers.txt", "r")
num_table=[]
for line in fileIn.read().split():
    num_table.append(line.split(","))
    
print(num_table)