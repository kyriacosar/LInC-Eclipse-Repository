'''
Created on Jul 21, 2017

@author: kyriacos
'''

import json
import math

if __name__ == '__main__':
    # Opening the necessary files.
    # Input files:
    e_file_in = open("../../../../Documents/Crunchbase Project Data/FacePlusPlus/Twitter Results/Data Dictionaries/Twitter_Non_Entrepreneurs_FaceLandmarks_Dictionaries.json", "r")
    e_file_in_att = open("../../../../Documents/Crunchbase Project Data/FacePlusPlus/Twitter Results/Data Dictionaries/Twitter_Non_Entrepreneurs_FaceAttributes_Dictionaries.json", "r")
    e_file_in_rect = open("../../../../Documents/Crunchbase Project Data/FacePlusPlus/Twitter Results/Data Dictionaries/Twitter_Non_Entrepreneurs_Rectangles_Dictionaries.json", "r")
    # Output files:
    e_file_out = open("../../../../Documents/Crunchbase Project Data/FacePlusPlus/Twitter Results/Data Extraction/Twitter_Non_Entrepreneurs_Pupil_Distance_Comparison.txt", "w")
    
    # Initialize variables.
    pos = 0
    dist_sum = 0
    adjusted_dist_sum = 0
    count = 0
        
    # Adding titles to the output file.
    e_file_out.write("Pupil distance comparison of non Entrepreneurs:\n\n")
    e_file_out.write("ID\t\t\tOriginal\t\tRect Side\tAdjusted\n")
    e_file_out.write("-"*9+"\t\t"+"-"*13+"\t\t"+"-"*9+"\t"+"-"*13+"\n")
    
    # Reading the JSON formatted face landmarks records.        
    for record in e_file_in:   
        try:
            # Reading the JSON formatted face attributes records.
            
            # Converting the JSON record to a dictionary and isolating the ID field.
            jDict = json.loads(record)
            jID = jDict['_id']
             
            # Fetching the side of the face rectangle.
            rectRecord = e_file_in_rect.readline()
            rectDict = json.loads(rectRecord)
            rectSide = rectDict['face_rectangle']['width']
             
            # Converting the face attributes JSON record to a dictionary and isolating the yaw and pitch field.
            poseRecord = e_file_in_att.readline()
            poseDict = json.loads(poseRecord)            
            yaw = math.fabs(poseDict['attributes']['headpose']['yaw_angle'])                                                  
                
            # Isolating the x and y attributes of each pupil.           
            leftY = jDict['landmark']['left_eye_pupil']['y']
            leftX = jDict['landmark']['left_eye_pupil']['x']
            rightY = jDict['landmark']['right_eye_pupil']['y']
            rightX = jDict['landmark']['right_eye_pupil']['x']
                
            # Calculating pupil distance by using the distance between two points formula.
            partY = math.pow((leftY - rightY), 2)
            partX = math.pow((leftX - rightX), 2)
            dist = math.sqrt(partY+partX)
                
            # Using the Pythagorean theorem to adjust pupil distance based on yaw.
            dist = math.sqrt(math.pow(dist,2)+math.pow(yaw, 2))
            
            # Adding the distance to a sum in order to calculate the average length.
            dist_sum += dist
                
            # Adjusting pupil distance based on the face rectangle size.
            adjusted_dist = dist*100/rectSide
                
            # Adding the adjusted distance to a sum in order to calculate the average distance.
            adjusted_dist_sum += adjusted_dist
            count += 1
                
            # Based on the ID length, the right amount of tabs are written to the output file.
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