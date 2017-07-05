'''
Created on Jun 19, 2017

@author: kyriacos
'''
from pkg_resources._vendor.pyparsing import alphas
x="Hello World!"
print(x)
print(x[6])
print(x[6:11])
print(x[:5])
print(x[6:])
print(x[3:-2])

#Comparisons:
print('Is aa smaller than aaz:')
print('aa' < 'aaz')
y='Hello'
z='World'
print('y = '+y)
print('z = '+z)
print('Concatenation: '+y+' '+z+'!')
print('Is \'orl\' in \'World\':')
print('orl' in z)
print('ka'*3)

print('\u0414')

#String functions:
sent = "Hello world!"
print(len(sent))
print(sent.find("wor"))
print(sent.find("fuck"))
print(sent.find("l", 4))
print(sent.replace("world", "fuckers"))
print(sent)

print(sent.split())
print(sent.split("l"))

print(sent.strip('lerH!od'))

print(sent.upper())
print(sent.lower())
print(sent.swapcase())
print(sent.title())

alphas = "Onlyletters"
nums = "1234"
print(alphas.isalpha())
print(nums.isdigit())

mystr = ''
alist = ['hello', 'class'] 
mystr=' '.join(alist) 
print(mystr)

mystr = '' 
alist = ['1', '2', '3', '4'] 
mystr=mystr.join(alist)
print(mystr)

