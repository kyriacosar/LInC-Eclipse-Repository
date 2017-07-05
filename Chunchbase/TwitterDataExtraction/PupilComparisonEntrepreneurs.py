'''
Created on Jun 27, 2017

@author: kyriacos
'''

import json
import math

if __name__ == '__main__':
    e_file_in = open("../TwitterDataDictionaries/Twitter_Entrepreneurs_FaceLandmarks_Dictionaries.json", "r")
    e_file_in_att = open("../TwitterDataDictionaries/Twitter_Entrepreneurs_FaceAttributes_Dictionaries.json", "r")
    e_file_in_rect = open("../TwitterDataDictionaries/Twitter_Entrepreneurs_Rectangles_Dictionaries.json", "r")
    e_file_out = open("Twitter_Entrepreneurs_Pupil_Distance_Comparison.txt", "w")
    
    rectList = []
    pos = 0
    dist_sum = 0
    adjusted_dist_sum = 0
    count = 0
    
    e_file_out.write("Pupil distance comparison of Entrepreneurs:\n\n")
    e_file_out.write("ID\t\t\tOriginal\t\tRect Side\tAdjusted\n")
    e_file_out.write("-"*9+"\t\t"+"-"*13+"\t\t"+"-"*9+"\t"+"-"*13+"\n")
    
    for rectRecord in e_file_in_rect:
        rectList.append(rectRecord)
    
    for record in e_file_in:   
        try:
            yawRecord = e_file_in_att.readline()
            
            jDict = json.loads(record)
            jID = jDict['_id']
        
            rectDict = json.loads(rectList[pos])
            rectID = rectDict['_id']
            
            while rectID < jID:
                pos += 1
                rectDict = json.loads(rectList[pos])
                rectID = rectDict['_id']
                
            if rectID == jID:
                rectSide = rectDict['faceRectangle']['width']
                yawDict = json.loads(yawRecord)                                                                      
                leftY = jDict['faceLandmarks']['pupilLeft']['y']
                leftX = jDict['faceLandmarks']['pupilLeft']['x']
                rightY = jDict['faceLandmarks']['pupilRight']['y']
                rightX = jDict['faceLandmarks']['pupilRight']['x']
                yaw = math.fabs(yawDict['faceAttributes']['headPose']['yaw'])
                partY = math.pow((leftY - rightY), 2)
                partX = math.pow((leftX - rightX), 2)
                dist = math.sqrt(partY+partX)
                dist = math.sqrt(math.pow(dist,2)+math.pow(yaw, 2))
                dist_sum += dist
                adjusted_dist = dist*100/rectSide
                adjusted_dist_sum += adjusted_dist
                count += 1
                
                if str(jDict['_id']).__len__() >= 16:
                    e_file_out.write(str(jDict['_id'])+"\t"+str(dist)+"\t\t"+str(rectSide)+"\t\t"+str(adjusted_dist)+"\n")
                elif str(jDict['_id']).__len__() >= 8:
                    e_file_out.write(str(jDict['_id'])+"\t\t"+str(dist)+"\t\t"+str(rectSide)+"\t\t"+str(adjusted_dist)+"\n")
                else:
                    e_file_out.write(str(jDict['_id'])+"\t\t\t"+str(dist)+"\t\t"+str(rectSide)+"\t\t"+str(adjusted_dist)+"\n")
                
        except ValueError:
                print("Error in json to dictionary translation.")
            
    e_file_out.write("\nAverage distance: "+str(dist_sum/count))
    e_file_out.write("\nAverage adjusted distance: "+str(adjusted_dist_sum/count))