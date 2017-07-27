'''
Created on Jul 24, 2017

@author: kyriacos
'''

import json
import math

if __name__ == '__main__':
    e_file_in = open("../../../../Documents/Crunchbase Project Data/FacePlusPlus/Crunchbase Results/Data Dictionaries/Crunchbase_Entrepreneurs_FaceLandmarks_Dictionaries.json", "r")
    e_file_in_att = open("../../../../Documents/Crunchbase Project Data/FacePlusPlus/Crunchbase Results/Data Dictionaries/Crunchbase_Entrepreneurs_FaceAttributes_Dictionaries.json", "r")
    e_file_out = open("../../../../Documents/Crunchbase Project Data/FacePlusPlus/Crunchbase Results/Data Extraction/Crunchbase_Entrepreneurs_Chin_Prominence.txt", "w")
    
    e_file_out.write("Chin prominence of Entrepreneurs with reduced yaw and pitch range [-10, 10]:\n\n")
    
    # Initialize variables.
    pos = 0
    widthA_sum = 0
    widthB_sum = 0
    ratio_sum = 0
    count = 0
        
    e_file_out.write("ID\t\t\t\t\tRatio\n")
    e_file_out.write("-"*36+"\t"+"-"*13+"\n")
    
    for record in e_file_in:   
        try:
            # Reading the JSON formatted face attributes records.
                        
            # Converting the JSON record to a dictionary and isolating the ID field.
            jDict = json.loads(record)
            jID = jDict['_id']
        
            # Converting the face attributes JSON record to a dictionary and isolating the yaw and pitch field.
            poseRecord = e_file_in_att.readline()
            poseDict = json.loads(poseRecord)            
            yaw = math.fabs(poseDict['attributes']['headpose']['yaw_angle'])
            pitch = math.fabs(poseDict['attributes']['headpose']['pitch_angle'])
            
            if yaw >= -10 and yaw <= 10 and pitch >= -10 and pitch <= 10:
        
                contour_leftA_x = jDict['landmark']['contour_left1']['x']
                contour_leftA_y = jDict['landmark']['contour_left1']['y']
                contour_rightA_x = jDict['landmark']['contour_right1']['x']
                contour_rightA_y = jDict['landmark']['contour_right1']['y']
                contour_leftB_x = jDict['landmark']['contour_left5']['x']
                contour_leftB_y = jDict['landmark']['contour_left5']['y']
                contour_rightB_x = jDict['landmark']['contour_right5']['x']
                contour_rightB_y = jDict['landmark']['contour_right5']['y'] 
                
                # Calculating top face width by using the distance between two points formula.
                partX = math.pow((contour_leftA_x - contour_rightA_x), 2)
                partY = math.pow((contour_leftA_y - contour_rightA_y), 2)
                widthA = math.sqrt(partY+partX)
                
                # Using the Pythagorean theorem to adjust face width based on yaw.
                widthA = math.sqrt(math.pow(widthA,2)+math.pow(yaw, 2))
                
                # Adding the width to a sum in order to calculate the average width.
                widthA_sum += widthA
                
                # Calculating top face width by using the distance between two points formula.
                partX = math.pow((contour_leftB_x - contour_rightB_x), 2)
                partY = math.pow((contour_leftB_y - contour_rightB_y), 2)
                widthB = math.sqrt(partY+partX)
                
                # Using the Pythagorean theorem to adjust face width based on yaw.
                widthB = math.sqrt(math.pow(widthB,2)+math.pow(yaw, 2))
                
                # Adding the width to a sum in order to calculate the average width.
                widthB_sum += widthB
                
                # Calculating FHWR.
                ratio = widthA / widthB
                
                # Adding the ratio to a sum in order to calculate the average ratio.
                ratio_sum += ratio
                
                count += 1
        
                # Based on the ID length, the right amount of tabs are written to the output file.
                if str(jDict['_id']).__len__() >= 16:
                    e_file_out.write(str(jDict['_id'])+"\t"+str(ratio)+"\n")
                elif str(jDict['_id']).__len__() >= 8:
                    e_file_out.write(str(jDict['_id'])+"\t\t"+str(ratio)+"\n")
                else:
                    e_file_out.write(str(jDict['_id'])+"\t\t\t"+str(ratio)+"\n")
        except ValueError:
            print("Error in json to dictionary translation.")
            
    # Calculating the average height, width and FHWR and writting in the output file.
    e_file_out.write("\nAverage ratio: "+str(ratio_sum/count))