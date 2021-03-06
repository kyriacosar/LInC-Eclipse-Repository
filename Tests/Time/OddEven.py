'''
Created on Jul 3, 2017

@author: kyriacos
'''

def digitSum(num):
    sumT = 0
    while num > 0:
        rem = num % 10
        num = num / 10
        sumT += rem
    return sumT

def timeCheck(time):
    res = digitSum(time)
    if res >= 10:
        res = digitSum(res)
    if res >= 10:
        res = digitSum(res)
    print("Digit sum: "+str(res))
    if res % 2 == 0:
        return True
    else:
        return False
    
if __name__ == "__main__":
    time = 0
    even = 0
    odd = 0
    
    while time <= 2359:
        print("Current time: "+str(time))
        if timeCheck(time):
            even += 1
        else:
            odd += 1
            
        time += 1
        
        if (time % 100 % 60) == 0:
            time += 40
            
    print("Even time: "+str(even))
    print("Odd time: "+str(odd))
