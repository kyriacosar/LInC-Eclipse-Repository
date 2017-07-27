'''
Created on Jul 21, 2017

@author: kyriacos
'''

import json

if __name__ == '__main__':
    e_file_in_land = open("../../../../Documents/Crunchbase Project Data/Microsoft/Crunchbase Results/Data Dictionaries/Crunchbase_Entrepreneurs_FaceLandmarks_Dictionaries.json", "r")
    e_file_in_att = open("../../../../Documents/Crunchbase Project Data/Microsoft/Crunchbase Results/Data Dictionaries/Crunchbase_Entrepreneurs_FaceAttributes_Dictionaries.json", "r")
    e_file_in_rect = open("../../../../Documents/Crunchbase Project Data/Microsoft/Crunchbase Results/Data Dictionaries/Crunchbase_Entrepreneurs_Rectangles_Dictionaries.json", "r")
    e_file_out = open("../../../../Documents/Crunchbase Project Data/Microsoft/Excel Imports/Crunchbase Imports/Crunchbase_Entrepreneurs.txt", "w")
    
    for record in e_file_in_land:
        try:
            landDict = json.loads(record)
            
            attLine = e_file_in_att.readline()
            attDict = json.loads(attLine)
            
            rectLine = e_file_in_rect.readline()
            rectDict = json.loads(rectLine)
            
            e_file_out.write(str(attDict['faceAttributes']['emotion']['sadness'])+","+str(attDict['faceAttributes']['emotion']['neutral'])+",")
            e_file_out.write(str(attDict['faceAttributes']['emotion']['contempt'])+","+str(attDict['faceAttributes']['emotion']['disgust'])+",")
            e_file_out.write(str(attDict['faceAttributes']['emotion']['anger'])+","+str(attDict['faceAttributes']['emotion']['surprise'])+",")
            e_file_out.write(str(attDict['faceAttributes']['emotion']['fear'])+","+str(attDict['faceAttributes']['emotion']['happiness'])+",")
            
            if attDict['faceAttributes']['gender'] == "male":
                e_file_out.write("1,")
            else:
                e_file_out.write("0,")
            
            e_file_out.write(str(attDict['faceAttributes']['age'])+",")
            
            if attDict['faceAttributes']['makeup']['lipMakeup']:
                e_file_out.write("1,")
            else:
                e_file_out.write("0,")
            
            if attDict['faceAttributes']['makeup']['eyeMakeup']:
                e_file_out.write("1\n")
            else:
                e_file_out.write("0\n")
                                    
        except ValueError:
            print("Error in json to dictionary translation.")