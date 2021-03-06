'''
Created on Jun 30, 2017

@author: kyriacos
'''

import math

def calculatePupilDistance(leftX, leftY, rightX, rightY, yaw, rectSide):
    # Calculating pupil distance by using the distance between two points formula.
    partY = math.pow((leftY - rightY), 2)
    partX = math.pow((leftX - rightX), 2)
    dist = math.sqrt(partY+partX)
                
    # Using the Pythagorean theorem to adjust pupil distance based on yaw.
    dist = math.sqrt(math.pow(dist,2)+math.pow(yaw, 2))
                
    # Adjusting pupil distance based on the face rectangle size.
    adjusted_dist = dist*100/rectSide
    
    return adjusted_dist
    
if __name__ == '__main__':
    
    adjusted_dist = calculatePupilDistance(58.2, 64.2, 84.5, 63, -13.7, 60)
    
    print("Medium quality adjusted pupil distance = "+str(adjusted_dist))
    
    adjusted_dist = calculatePupilDistance(83.1, 90.4, 119.4, 88.8, -17.5, 83)
    
    print("High quality adjusted pupil distance = "+str(adjusted_dist))
    