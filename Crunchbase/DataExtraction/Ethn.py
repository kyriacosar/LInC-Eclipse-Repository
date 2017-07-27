'''
Created on Jul 27, 2017

@author: kyriacos
'''
import json

def getForEthn(ethn, entre):
    male = 0
    maleAge = 0
    female = 0
    femaleAge = 0
    count = 0
    
    fileIn = "../../../../Documents/Crunchbase Project Data/Complete/Data Dictionaries/Attributes_Dictionaries.json"
    fileOut = "../../../../Documents/Crunchbase Project Data/Complete/Data Extraction/"+ethn+"_Gender_Percentages.txt"
    e_file_in = open(fileIn, "r")
    e_file_out = open(fileOut, "w")
    
    for record in e_file_in:  
        try:
            jDict = json.loads(record)
            
            is_entre = jDict['isEntre']
            
            str_gender = str(jDict['MSAttributes']['gender'])
            
            try:
                str_ethn = str(jDict['MSAttributes']['ethnicity'])
                if str_ethn == 'Asian':
                    if is_entre == entre:
                        if str_gender == 'male':
                            male += 1
                            maleAge += jDict['MSAttributes']['age']
                        else:
                            female += 1
                            femaleAge += jDict['MSAttributes']['age']
                        count += 1
            except KeyError:                    
                print 
                
        except ValueError:
            print("Error in json to dictionary translation.")
            
    e_file_out.write("Gender percentages among "+ethn+" Entrepreneurs:\n\n")
   
    e_file_out.write("Males: "+str(male)+" out of "+str(count)+" with percentage "+str(maleE/float(countE)*100.0))
    e_file_out.write("\nFemales: "+str(female)+" out of "+str(count)+" with percentage "+str(femaleE/float(countE)*100.0))
    
    e_file_out.write("\n\nAverage age among Asian Entrepreneurs:\n\n")
    e_file_out.write("Male: "+str(maleAge/male))
    e_file_out.write("\nFemale: "+str(femaleAge/female)) 
    
