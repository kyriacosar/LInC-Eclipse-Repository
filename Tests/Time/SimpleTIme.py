'''
Created on Jul 3, 2017

@author: kyriacos
'''
    
if __name__ == "__main__":
    time = 0
    even = 0
    odd = 0
    
    while time <= 2359:
        print time
        if time % 2 == 0:
            even += 1
        else:
            odd += 1
            
        time += 1
        
        if (time % 100 % 60) == 0:
            time += 40
            
    print("Even time: "+str(even))
    print("Odd time: "+str(odd))
