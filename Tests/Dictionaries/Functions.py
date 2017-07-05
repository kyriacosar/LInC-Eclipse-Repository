'''
Created on Jun 19, 2017

@author: kyriacos
'''

myDict = {1:'one', 2:'to'}
yourDict = {2:'two', 3:'three', 4:'four'}

myDict.update(yourDict)
print(myDict)

print(myDict.items())
print(myDict.values())
print(myDict.keys())

print(myDict.pop(1))
print(myDict)