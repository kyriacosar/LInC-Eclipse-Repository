'''
Created on Jul 26, 2017

@author: kyriacos
'''

import json

if __name__ == '__main__':
    e_file_in = open("../../../../Documents/Crunchbase Project Data/Complete/Data Dictionaries/Attributes_Dictionaries.json", "r")
    e_file_out = open("../../../../Documents/Crunchbase Project Data/Complete/Data Extraction/White_Gender_Percentages.txt", "w")
    
    maleE = 0
    maleAgeE = 0
    femaleE = 0
    femaleAgeE = 0
    countE = 0
    
    maleN = 0
    maleAgeN = 0
    femaleN = 0
    femaleAgeN = 0
    countN = 0
    
    for record in e_file_in:  
        try:
            jDict = json.loads(record)
            
            is_entre = jDict['isEntre']
            
            str_gender = str(jDict['MSAttributes']['gender'])
            
            try:
                str_ethn = str(jDict['MSAttributes']['ethnicity'])
                if str_ethn == 'White':
                    if is_entre == 1:
                        if str_gender == 'male':
                            maleE += 1
                            maleAgeE += jDict['MSAttributes']['age']
                        else:
                            femaleE += 1
                            femaleAgeE += jDict['MSAttributes']['age']
                        countE += 1
                    else:
                        if str_gender == 'male':
                            maleN += 1
                            maleAgeN += jDict['MSAttributes']['age']
                        else:
                            femaleN += 1
                            femaleAgeN += jDict['MSAttributes']['age']
                        countN += 1    
            except KeyError:                    
                print 
                
        except ValueError:
            print("Error in json to dictionary translation.")
            
    e_file_out.write("Gender percentages among White Entrepreneurs:\n\n")
   
    e_file_out.write("Males: "+str(maleE)+" out of "+str(countE)+" with percentage "+str(maleE/float(countE)*100.0))
    e_file_out.write("\nFemales: "+str(femaleE)+" out of "+str(countE)+" with percentage "+str(femaleE/float(countE)*100.0))
    
    e_file_out.write("\n\nAverage age among White Entrepreneurs:\n\n")
    e_file_out.write("Male: "+str(maleAgeE/maleE))
    e_file_out.write("\nFemale: "+str(femaleAgeE/femaleE))
    
    e_file_out.write("\n\n"+"="*60+"\n\n")
    
    e_file_out.write("Gender percentages among White non Entrepreneurs:\n\n")
   
    e_file_out.write("Males: "+str(maleN)+" out of "+str(countN)+" with percentage "+str(maleN/float(countN)*100.0))
    e_file_out.write("\nFemales: "+str(femaleN)+" out of "+str(countN)+" with percentage "+str(femaleN/float(countN)*100.0))
    
    e_file_out.write("\n\nAverage age among White Entrepreneurs:\n\n")
    e_file_out.write("Male: "+str(maleAgeN/maleN))
    e_file_out.write("\nFemale: "+str(femaleAgeN/femaleN))