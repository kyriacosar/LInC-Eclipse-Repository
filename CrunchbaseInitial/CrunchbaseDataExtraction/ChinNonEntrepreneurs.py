'''
Created on Jul 24, 2017

@author: kyriacos
'''

import json
import math

if __name__ == '__main__':
    e_file_in = open("../../../../Documents/Crunchbase Project Data/Microsoft/Crunchbase Results/Data Dictionaries/Crunchbase_Non_Entrepreneurs_FacePoints_Dictionaries.json", "r")
    e_file_in_att = open("../../../../Documents/Crunchbase Project Data/Microsoft/Crunchbase Results/Data Dictionaries/Crunchbase_Non_Entrepreneurs_FaceAttributes_Dictionaries.json", "r")
    e_file_in_rect = open("../../../../Documents/Crunchbase Project Data/Microsoft/Crunchbase Results/Data Dictionaries/Crunchbase_Non_Entrepreneurs_Rectangles_Dictionaries.json", "r")
    e_file_out = open("../../../../Documents/Crunchbase Project Data/Microsoft/Crunchbase Results/Data Extraction/Crunchbase_Non_Entrepreneurs_Chin_Prominence.txt", "w")
    
    e_file_out.write("Chin prominence of non Entrepreneurs with reduced yaw range [-10, 10]:\n\n")
    
    # Initialize variables.
    pos = 0
    adjusted_widthA_sum = 0
    adjusted_widthB_sum = 0
    ratio_sum = 0
    count = 0
    
    # Initialize a new list for adding the rectangle attributes dictionaries.
    rectList = []
    
    # Adding the rectangle attributes dictionaries in the list.
    for rectRecord in e_file_in_rect:
        rectList.append(rectRecord)
        
    e_file_out.write("ID\t\t\t\t\tTop\t\tBottom\t\tRatio\n")
    e_file_out.write("-"*36+"\t"+"-"*13+"\t"+"-"*13+"\t"+"-"*14+"\n")
    
    for record in e_file_in:   
        try:
            # Reading the JSON formatted face attributes records.
            yawRecord = e_file_in_att.readline()
            
            # Converting the JSON record to a dictionary and isolating the ID field.
            jDict = json.loads(record)
            jID = jDict['_id']
        
            # Converting the JSON record to a dictionary and isolating the ID field.
            rectDict = json.loads(rectList[pos])
            rectID = rectDict['_id']
            
            # This loop is used to find matching IDs for the face landmarks and rectangle attributes records.
            while rectID < jID:
                pos += 1
                rectDict = json.loads(rectList[pos])
                rectID = rectDict['_id']
            
            # If the IDs match after the loop then the distance is calculated.
            # If not, there's no match because the records are sorted based on the ID field.   
            if rectID == jID:
                # Fetching the side of the face rectangle.
                rectSide = rectDict['faceRectangle']['width']
                
                # Converting the face attributes JSON record to a dictionary and isolating the yaw field.
                yawDict = json.loads(yawRecord)            
                yaw = math.fabs(yawDict['faceAttributes']['headPose']['yaw'])
                
                if (yaw>=-10 and yaw<=10):
            
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
                    
                    # Adjusting face width based on the face rectangle size.
                    adjusted_widthA = widthA*100/rectSide
                    
                    # Adding the width to a sum in order to calculate the average width.
                    adjusted_widthA_sum += adjusted_widthA
                    
                    # Calculating top face width by using the distance between two points formula.
                    partX = math.pow((contour_leftB_x - contour_rightB_x), 2)
                    partY = math.pow((contour_leftB_y - contour_rightB_y), 2)
                    widthB = math.sqrt(partY+partX)
                    
                    # Using the Pythagorean theorem to adjust face width based on yaw.
                    widthB = math.sqrt(math.pow(widthB,2)+math.pow(yaw, 2))
                    
                    # Adjusting face width based on the face rectangle size.
                    adjusted_widthB = widthB*100/rectSide
                    
                    # Adding the width to a sum in order to calculate the average width.
                    adjusted_widthB_sum += adjusted_widthB
                    
                    # Calculating FHWR.
                    ratio = adjusted_widthA / adjusted_widthB
                    
                    # Adding the ratio to a sum in order to calculate the average ratio.
                    ratio_sum += ratio
                    
                    count += 1
            
                    # Based on the ID length, the right amount of tabs are written to the output file.
                    if str(jDict['_id']).__len__() >= 16:
                        e_file_out.write(str(jDict['_id'])+"\t")
                    elif str(jDict['_id']).__len__() >= 8:
                        e_file_out.write(str(jDict['_id'])+"\t\t")
                    else:
                        e_file_out.write(str(jDict['_id'])+"\t\t\t")
                    
                    if len(str(adjusted_widthA)) <= 7:
                        e_file_out.write(str(adjusted_widthA)+"\t\t")
                    else:
                        e_file_out.write(str(adjusted_widthA)+"\t")
                    
                    if len(str(adjusted_widthB)) <= 7:
                        e_file_out.write(str(adjusted_widthB)+"\t\t"+str(ratio)+"\n")
                    else:
                        e_file_out.write(str(adjusted_widthB)+"\t"+str(ratio)+"\n")
            
        except ValueError:
            print("Error in json to dictionary translation.")
            
    # Calculating the average height, width and FHWR and writting in the output file.
    e_file_out.write("\nAverage top width: "+str(adjusted_widthA_sum/count))
    e_file_out.write("\nAverage bottom width: "+str(adjusted_widthB_sum/count))
    e_file_out.write("\nAverage ratio: "+str(ratio_sum/count))