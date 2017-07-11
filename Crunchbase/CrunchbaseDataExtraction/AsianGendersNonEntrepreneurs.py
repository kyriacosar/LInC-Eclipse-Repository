'''
Created on Jul 11, 2017

@author: kyriacos
'''

import json
import math

if __name__ == '__main__':
    e_file_in = open("../../../../Documents/Crunchbase Project Data/Crunchbase Results/Data Dictionaries/Crunchbase_Non_Entrepreneurs_FaceAttributes_Dictionaries.json", "r")
    e_file_out = open("../../../../Documents/Crunchbase Project Data/Crunchbase Results/Data Extraction/Crunchbase_Asian_Non_Entrepreneurs_Gender_Percentages.txt", "w")
    
    male = 0
    female = 0
    count=0
    
    for record in e_file_in:   
        try:
            jDict = json.loads(record)
            
            str_gender = str(jDict['faceAttributes']['gender'])
            
            try:
                str_ethn = str(jDict['faceAttributes']['ethnicity'])
                if str_ethn == 'Asian':
                    if str_gender == 'male':
                        male += 1
                    elif str_gender == 'female':
                        female += 1
                    count += 1
            except KeyError:                    
                print 
                
        except ValueError:
            print("Error in json to dictionary translation.")
            
    e_file_out.write("Gender percentages among asian non Entrepreneurs:\n\n")
   
    e_file_out.write("Males: "+str(male)+" out of "+str(count)+" with percentage "+str(math.ceil((male/float(count))*100.0)))
    e_file_out.write("\nFemales: "+str(female)+" out of "+str(count)+" with percentage "+str(math.floor((female/float(count))*100.0)))