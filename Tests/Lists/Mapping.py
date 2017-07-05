'''
Created on Jun 19, 2017

@author: kyriacos
'''

def power2(x):
    xSquared= x**2
    return xSquared

lSquares = list(map(power2, range(1,5)))
print(lSquares)

lSquares2 = list(i**3 for i in range(1,5))
print(lSquares2)


