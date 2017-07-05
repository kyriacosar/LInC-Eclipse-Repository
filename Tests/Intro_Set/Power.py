'''
Created on Jun 19, 2017

@author: kyriacos
'''

def power(x, y):
    """
    This method takes two arguments
    and return the first argument to
    the power of the second.
    """
    t=x
    for i in (1, y):
        t=t*x
    return t

