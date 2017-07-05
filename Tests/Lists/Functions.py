'''
Created on Jun 19, 2017

@author: kyriacos
'''

num_list = [4,5,2,3,6,1]

print("Length: " + str(len(num_list)))
print("Minimum value: " + str(min(num_list)))
print("Maximum effort: " + str(max(num_list)))
print("Sum: " + str(sum(num_list)))

num_list.remove(6)
print(num_list)

num_list.insert(5, "a")
print(num_list)

num_list.reverse()
print(num_list)

num_list.insert(6, [1,2,3])
num_list.sort()
print(num_list)

num_list.extend("lmao")
print(num_list)

word = "Zoro"
list_word = list(word)
list_word.sort()
print(list_word)

print(list_word.pop())
print(list_word)