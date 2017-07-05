'''
Created on Jun 19, 2017

@author: kyriacos
'''

print(len(['spam!',1,['Brie','Roquefort','Pol le Veq'],[1,2,3]]))

alist = [3, 67, "cat", 3.14, False] 
print(len(alist))

blist = [3, 67, "cat", [56, 57, "dog"], [ ], 3.14, False] 
print(len(blist))

x= range(0,4) 
print(x)
print(len(x)) 

numbers = [17, 123, 87, 34, 66, 8398, 44] 
print(numbers[2]) 
print(numbers[9-8]) 
print(numbers[-2]) 
print(numbers[len(numbers)-1])

alist = [3, 67, "cat", [56, 57, "dog"], [ ], 3.14, False] 
print(alist[2][0])

fruit = ["apple","orange","banana","cherry"] 
print("apple" in fruit) 
print("pear" in fruit)

alist = [1,3,5] 
blist = [2,4,6] 
print(alist + blist)

alist = [1,3,5] 
print(alist * 3)

origlist = [45, 76, 34, 55] 
print(origlist*3) 
newlist = [origlist] * 3 
print(newlist)

alist = ['a', 'b', 'c', 'd', 'e', 'f'] 
alist[1:4] = ['x', 'y'] 
print(alist)

alist = ['a', 'd', 'f'] 
alist[1:1] = ['b', 'c'] 
print(alist) 
alist[4:4] = ['e'] 
print(alist)

mylist = [] 
mylist.append(5) 
mylist.append(27) 
mylist.append(3) 
mylist.append(12) 
print(mylist) 
mylist.sort()   #probably an error 
print(mylist)

alist = [4,2,8,6,5] 
alist.append(True) 
alist.append(False) 
print(alist)

alist = [4,2,8,6,5] 
alist.insert(2,True) 
alist.insert(0,False) 
print(alist)

alist = [4,2,8,6,5] 
temp = alist.pop(2) 
temp = alist.pop() 
print(alist) 

