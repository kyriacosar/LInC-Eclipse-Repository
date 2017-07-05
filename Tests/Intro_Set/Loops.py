'''
Created on Jun 19, 2017

@author: kyriacos
'''

from __future__ import print_function

print("if/elif/else:")
x=input("Enter a number for x: ")
y=input("Enter a number for y: ")
if x<y:
    print("x is smaller than y")
elif x>y:
    print("y is smaller than x")
else:
    print("x and y are equal")


print("\nwhile loop:")
j=1
while j<20:
    print(j)
    j=j+1
    

print("\nfor loop:") 
for i in range(1, 20, 2):
    print(i)

print("\nstring for loop for words:")
word = "wordw"
for letter in word:
    print(chr(ord(letter)-ord('a')+ord('A')) ,end=" ")
    
print("\n\nstring for loop for sentences:")
sentence = "testing sentence given as input in a for loop"
for word in sentence.split():
    print(word)
