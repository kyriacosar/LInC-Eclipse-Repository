'''
Created on Jul 14, 2017

@author: kyriacos
'''

import json

if __name__ == '__main__':
    e_file_in = open("../../../../Documents/Crunchbase Project Data/Crunchbase Results/Data Dictionaries/Crunchbase_Non_Entrepreneurs_FaceAttributes_Dictionaries.json", "r")
    e_file_out = open("../../../../Documents/Crunchbase Project Data/Excel Imports/Crunchbase Imports/Crunchbase_Non_Entrepreneurs_Emotions.txt", "w")
    
    for record in e_file_in:
        try:
            jDict = json.loads(record)
            e_file_out.write(str(jDict['faceAttributes']['emotion']['sadness'])+","+str(jDict['faceAttributes']['emotion']['neutral'])+",")
            e_file_out.write(str(jDict['faceAttributes']['emotion']['contempt'])+","+str(jDict['faceAttributes']['emotion']['disgust'])+",")
            e_file_out.write(str(jDict['faceAttributes']['emotion']['anger'])+","+str(jDict['faceAttributes']['emotion']['surprise'])+",")
            e_file_out.write(str(jDict['faceAttributes']['emotion']['fear'])+","+str(jDict['faceAttributes']['emotion']['happiness'])+"\n")
        except ValueError:
            print("Error in json to dictionary translation.")