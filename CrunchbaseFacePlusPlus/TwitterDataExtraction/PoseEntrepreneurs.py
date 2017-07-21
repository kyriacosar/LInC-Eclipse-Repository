'''
Created on Jul 21, 2017

@author: kyriacos
'''

import json

if __name__ == '__main__':
    e_file_in = open("../../../../Documents/Crunchbase Project Data/FacePlusPlus/Twitter Results/Data Dictionaries/Twitter_Entrepreneurs_FaceAttributes_Dictionaries.json", "r")
    e_file_out = open("../../../../Documents/Crunchbase Project Data/FacePlusPlus/Twitter Results/Data Extraction/Twitter_Entrepreneurs_Pose.txt", "w")
    
    yaw = 0
    roll = 0
    pitch = 0
    count = 0
    
    for record in e_file_in:   
        jDict = json.loads(record)
        yaw += jDict['attributes']['headpose']['yaw_angle']
        roll += jDict['attributes']['headpose']['roll_angle']
        pitch += jDict['attributes']['headpose']['pitch_angle']
        count += 1
    
    e_file_out.write("Average Entrepreneur head pose:\n\n")
    e_file_out.write('Yaw: '+str(yaw/count)+"\n")
    e_file_out.write('Roll: '+str(roll/count)+"\n")
    e_file_out.write('Pitch: '+str(pitch/count)+"\n")