'''
Created on Jun 19, 2017

@author: kyriacos
'''

def my_square_function(x):
    return x*x

my_dict = {} 
my_list = [2,4,6,8,10] 

for x in my_list: 
    my_dict[x] = my_square_function(x)
    
print(my_dict[8])