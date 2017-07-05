'''
Created on Jun 22, 2017

@author: kyriacos
'''

import json

if __name__ == '__main__':
    e_file_in = open("../TwitterDataDictionaries/Twitter_Non_Entrepreneurs_FaceAttributes_Dictionaries.json", "r")
    e_file_out = open("Twitter_Non_Entrepreneurs_Pose.txt", "w")
    
    yaw = 0
    roll = 0
    pitch = 0
    count = 0
    
    for record in e_file_in:   
        jDict = json.loads(record)
        yaw += jDict['faceAttributes']['headPose']['yaw']
        roll += jDict['faceAttributes']['headPose']['roll']
        pitch += jDict['faceAttributes']['headPose']['pitch']
        count += 1
    
    e_file_out.write("Average non Entrepreneur head pose:\n\n")
    e_file_out.write('Yaw: '+str(yaw/count)+"\n")
    e_file_out.write('Roll: '+str(roll/count)+"\n")
    e_file_out.write('Pitch: '+str(pitch/count)+"\n")