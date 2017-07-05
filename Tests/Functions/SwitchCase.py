'''
Created on Jun 19, 2017

@author: kyriacos
'''

def crazyWord(word):
        
    for i in range(0, len(word)):
        if (i%2==0):
            if(word[i]>='a' and word[i]<='z'):
                word=word[:i]+chr(ord(word[i])-(ord('a')-ord('A')))+word[i+1:]
        else:
            if(word[i]>='A' and word[i]<='Z'):
                word=word[:i]+chr(ord(word[i])+(ord('a')-ord('A')))+word[i+1:]
    return word
