'''
Created on Jul 19, 2017

@author: kyriacos
'''

import json
import math

if __name__ == '__main__':
    e_file_in = open("../../../../Documents/Crunchbase Project Data/Crunchbase Results/Data Dictionaries/Crunchbase_Entrepreneurs_FacePoints_Dictionaries.json", "r")
    e_file_in_att = open("../../../../Documents/Crunchbase Project Data/Crunchbase Results/Data Dictionaries/Crunchbase_Entrepreneurs_FaceAttributes_Dictionaries.json", "r")
    e_file_in_rect = open("../../../../Documents/Crunchbase Project Data/Crunchbase Results/Data Dictionaries/Crunchbase_Entrepreneurs_Rectangles_Dictionaries.json", "r")
    e_file_out = open("../../../../Documents/Crunchbase Project Data/Crunchbase Results/Data Extraction/Crunchbase_Entrepreneurs_FHWR.txt", "w")
    
    e_file_out.write("FHWR of Entrepreneurs:\n\n")
    
    # Initialize variables.
    pos = 0
    adjusted_height_sum = 0
    adjusted_width_sum = 0
    ratio_sum = 0
    count = 0
    
    # Initialize a new list for adding the rectangle attributes dictionaries.
    rectList = []
    
    # Adding the rectangle attributes dictionaries in the list.
    for rectRecord in e_file_in_rect:
        rectList.append(rectRecord)
        
    e_file_out.write("ID\t\t\t\t\tHeight\t\tWidth\t\tRatio\n")
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
                
                if (yaw>=-20 and yaw<=20):
            
                    contour_left_x = jDict['landmark']['contour_left1']['x']
                    contour_left_y = jDict['landmark']['contour_left1']['y']
                    contour_right_x = jDict['landmark']['contour_right1']['x']
                    contour_right_y = jDict['landmark']['contour_right1']['y']
                    contour_chin_x = jDict['landmark']['contour_chin']['x']
                    contour_chin_y = jDict['landmark']['contour_chin']['y']
                    left_eyebrow_x = jDict['landmark']['left_eyebrow_right_corner']['x']
                    left_eyebrow_y = jDict['landmark']['left_eyebrow_right_corner']['y']
                    right_eyebrow_x = jDict['landmark']['right_eyebrow_left_corner']['x']
                    right_eyebrow_y = jDict['landmark']['right_eyebrow_left_corner']['y']
                    
                    # Calculating eyebrow mid point.
                    mid_eyebrow_x = (left_eyebrow_x + right_eyebrow_x)/2
                    mid_eyebrow_y = (left_eyebrow_y + right_eyebrow_y)/2 
                    
                    # Calculating face height by using the distance between two points formula.
                    partX = math.pow((contour_chin_x - mid_eyebrow_x), 2)
                    partY = math.pow((contour_chin_y - mid_eyebrow_y), 2)
                    height = math.sqrt(partY+partX)
                    
                    # Using the Pythagorean theorem to adjust face height based on yaw.
                    height = math.sqrt(math.pow(height,2)+math.pow(yaw, 2))
                    
                    # Adjusting face width based on the face rectangle size.
                    adjusted_height = height*100/rectSide
                    
                    # Adding the height to a sum in order to calculate the average height.
                    adjusted_height_sum += adjusted_height
                    
                    # Calculating face width by using the distance between two points formula.
                    partX = math.pow((contour_left_x - contour_right_x), 2)
                    partY = math.pow((contour_left_y - contour_right_y), 2)
                    width = math.sqrt(partY+partX)
                    
                    # Using the Pythagorean theorem to adjust face width based on yaw.
                    width = math.sqrt(math.pow(width,2)+math.pow(yaw, 2))
                    
                    # Adjusting face width based on the face rectangle size.
                    adjusted_width = width*100/rectSide
                    
                    # Adding the width to a sum in order to calculate the average width.
                    adjusted_width_sum += adjusted_width
                    
                    # Calculating FHWR.
                    ratio = adjusted_height / adjusted_width
                    
                    # Adding the ratio to a sum in order to calculate the average ratio.
                    ratio_sum += ratio
                    
                    count += 1
            
                    # Based on the ID length, the right amount of tabs are written to the output file.
                    if str(jDict['_id']).__len__() >= 16:
                        e_file_out.write(str(jDict['_id'])+"\t"+str(adjusted_height)+"\t"+str(adjusted_width)+"\t"+str(ratio)+"\n")
                    elif str(jDict['_id']).__len__() >= 8:
                        e_file_out.write(str(jDict['_id'])+"\t\t"+str(adjusted_height)+"\t"+str(adjusted_width)+"\t"+str(ratio)+"\n")
                    else:
                        e_file_out.write(str(jDict['_id'])+"\t\t\t"+str(adjusted_height)+"\t"+str(adjusted_width)+"\t"+str(ratio)+"\n")            
            
        except ValueError:
            print("Error in json to dictionary translation.")
            
    # Calculating the average height, width and FHWR and writting in the output file.
    e_file_out.write("\nAverage height: "+str(adjusted_height_sum/count))
    e_file_out.write("\nAverage width: "+str(adjusted_width_sum/count))
    e_file_out.write("\nAverage ratio: "+str(ratio_sum/count))
