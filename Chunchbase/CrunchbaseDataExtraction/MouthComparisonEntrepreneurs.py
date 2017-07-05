'''
Created on Jun 29, 2017

@author: kyriacos
'''

import json
import math

if __name__ == '__main__':
    e_file_in = open("../CrunchbaseDataDictionaries/Crunchbase_Entrepreneurs_FaceLandmarks_Dictionaries.json", "r")
    e_file_in_att = open("../CrunchbaseDataDictionaries/Crunchbase_Entrepreneurs_FaceAttributes_Dictionaries.json", "r")
    e_file_in_rect = open("../CrunchbaseDataDictionaries/Crunchbase_Entrepreneurs_Rectangles_Dictionaries.json", "r")
    e_file_out = open("Crunchbase_Entrepreneurs_Mouth_Length_Comparison.txt", "w")
    
    rectList = []
    pos = 0
    len_sum = 0
    adjusted_len_sum = 0
    count = 0
    
    e_file_out.write("Mouth length comparison of Entrepreneurs:\n\n")
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
                leftY = jDict['faceLandmarks']['mouthLeft']['y']
                leftX = jDict['faceLandmarks']['mouthLeft']['x']
                rightY = jDict['faceLandmarks']['mouthRight']['y']
                rightX = jDict['faceLandmarks']['mouthRight']['x']
                yaw = math.fabs(yawDict['faceAttributes']['headPose']['yaw'])
                partY = math.pow((leftY - rightY), 2)
                partX = math.pow((leftX - rightX), 2)
                length = math.sqrt(partY+partX)
                length = math.sqrt(math.pow(length,2)+math.pow(yaw, 2))
                len_sum += length
                adjusted_len = length*100/rectSide
                adjusted_len_sum += adjusted_len
                count += 1
                
                if str(jDict['_id']).__len__() >= 16:
                    e_file_out.write(str(jDict['_id'])+"\t"+str(length)+"\t\t"+str(rectSide)+"\t\t"+str(adjusted_len)+"\n")
                elif str(jDict['_id']).__len__() >= 8:
                    e_file_out.write(str(jDict['_id'])+"\t\t"+str(length)+"\t\t"+str(rectSide)+"\t\t"+str(adjusted_len)+"\n")
                else:
                    e_file_out.write(str(jDict['_id'])+"\t\t\t"+str(length)+"\t\t"+str(rectSide)+"\t\t"+str(adjusted_len)+"\n")
                
        except ValueError:
                print("Error in json to dictionary translation.")
            
    e_file_out.write("\nAverage distance: "+str(len_sum/count))
    e_file_out.write("\nAverage adjusted distance: "+str(adjusted_len_sum/count))