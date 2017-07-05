'''
Created on Jun 19, 2017

@author: kyriacos
'''

from __future__ import print_function

my_dict = {'a':2, 3:['x', 'y'], 'joe':'smith'} 

for key in my_dict.keys():   
    print(key, end=", ")
    
print()
    
for value in my_dict.values():     
    print(value, end=", ")
print()

print()

a_dict = {k:v for  k,v  in zip(range(0,7), 'abcdeff')} 
print(a_dict)

b_dict = {v:k for k,v in a_dict.items()}
print(b_dict)
    

