'''
Created on Jul 27, 2017

@author: kyriacos
'''

import json

if __name__ == '__main__':
    e_file_in = open("../../../../Documents/Crunchbase Project Data/Complete/Data Dictionaries/Attributes_Dictionaries.json", "r")
    e_file_out = open("../../../../Documents/Crunchbase Project Data/Complete/Data Extraction/Ethnicity_Gender_Percentages.txt", "w")
    
    maleE = 0
    maleAgeE = 0
    femaleE = 0
    femaleAgeE = 0
    whiteE = 0
    whiteAgeE = 0
    blackE = 0
    blackAgeE = 0
    asianE = 0
    asianAgeE = 0
    countE = 0
    
    maleN = 0
    maleAgeN = 0
    femaleN = 0
    femaleAgeN = 0
    whiteN = 0
    whiteAgeN = 0
    blackN = 0
    blackAgeN = 0
    asianN = 0
    asianAgeN = 0
    undefN = 0
    undefAgeN = 0
    countN = 0
    
    for record in e_file_in:   
        try:
            jDict = json.loads(record)
            
            is_entre = jDict['isEntre']
            
            if is_entre == 1:
                str_gender = str(jDict['MSAttributes']['gender'])
                if str_gender == 'male':
                    maleE += 1
                    maleAgeE += jDict['MSAttributes']['age']
                elif str_gender == 'female':
                    femaleE += 1
                    femaleAgeE += jDict['MSAttributes']['age']
                
                str_ethn = str(jDict['MSAttributes']['ethnicity'])
                if str_ethn == 'White':
                    whiteE += 1
                    whiteAgeE += jDict['MSAttributes']['age']
                elif str_ethn == 'Black':
                    blackE += 1
                    blackAgeE += jDict['MSAttributes']['age']
                elif str_ethn == 'Asian':
                    asianE += 1
                    asianAgeE += jDict['MSAttributes']['age']
                
                countE += 1
            else:
                str_gender = str(jDict['MSAttributes']['gender'])
                if str_gender == 'male':
                    maleN += 1
                    maleAgeN += jDict['MSAttributes']['age']
                elif str_gender == 'female':
                    femaleN += 1
                    femaleAgeN += jDict['MSAttributes']['age']
                
                try:
                    str_ethn = str(jDict['MSAttributes']['ethnicity'])
                    if str_ethn == 'White':
                        whiteN += 1
                        whiteAgeN += jDict['MSAttributes']['age']
                    elif str_ethn == 'Black':
                        blackN += 1
                        blackAgeN += jDict['MSAttributes']['age']
                    elif str_ethn == 'Asian':
                        asianN += 1
                        asianAgeN += jDict['MSAttributes']['age']
                except KeyError:
                    undefN += 1  
                    undefAgeN += jDict['MSAttributes']['age']                    
                
                countN += 1
        except ValueError:
            print("Error in json to dictionary translation.")
            
    e_file_out.write("Ethnicity and gender percentages and average age among Entrepreneurs:\n\n")
   
    e_file_out.write("Gender Percentages:\n")
    e_file_out.write("Males: "+str(maleE)+" out of "+str(countE)+" with percentage "+str(maleE/float(countE)*100.0))
    e_file_out.write("\nFemales: "+str(femaleE)+" out of "+str(countE)+" with percentage "+str(femaleE/float(countE)*100.0))
    
    e_file_out.write("\n\nEthnicity Percentages:\n")
    e_file_out.write("Asian: "+str(asianE)+" out of "+str(countE)+" with percentage "+str(asianE/float(countE)*100.0))
    e_file_out.write("\nBlack: "+str(blackE)+" out of "+str(countE)+" with percentage "+str(blackE/float(countE)*100.0))
    e_file_out.write("\nWhite: "+str(whiteE)+" out of "+str(countE)+" with percentage "+str(whiteE/float(countE)*100.0))
    
    e_file_out.write("\n\nGender Average Age:\n")
    e_file_out.write("Male: "+str(maleAgeE/maleE))
    e_file_out.write("\nFemale: "+str(femaleAgeE/femaleE))
    
    e_file_out.write("\n\nEthnicity Average Age:\n")
    e_file_out.write("Asian: "+str(asianAgeE/asianE))
    e_file_out.write("\nBlack: "+str(blackAgeE/blackE))
    e_file_out.write("\nWhite: "+str(whiteAgeE/whiteE))
    
    e_file_out.write("\n\n"+"="*60+"\n\n")
    
    e_file_out.write("Ethnicity and gender percentages and average age among non Entrepreneurs:\n\n")
   
    e_file_out.write("Gender Percentages:\n")
    e_file_out.write("Males: "+str(maleN)+" out of "+str(countN)+" with percentage "+str(maleN/float(countN)*100.0))
    e_file_out.write("\nFemales: "+str(femaleN)+" out of "+str(countN)+" with percentage "+str(femaleN/float(countN)*100.0))
    
    e_file_out.write("\n\nEthnicity Percentages:\n")
    e_file_out.write("Asian: "+str(asianN)+" out of "+str(countN)+" with percentage "+str(asianN/float(countN)*100.0))
    e_file_out.write("\nBlack: "+str(blackN)+" out of "+str(countN)+" with percentage "+str(blackN/float(countN)*100.0))
    e_file_out.write("\nWhite: "+str(whiteN)+" out of "+str(countN)+" with percentage "+str(whiteN/float(countN)*100.0))
    e_file_out.write("\nUndefined: "+str(undefN)+" out of "+str(countN)+" with percentage "+str(undefN/float(countN)*100.0))
    
    e_file_out.write("\n\nGender Average Age:\n")
    e_file_out.write("Male: "+str(maleAgeN/maleN))
    e_file_out.write("\nFemale: "+str(femaleAgeN/femaleN))
    
    e_file_out.write("\n\nEthnicity Average Age:\n")
    e_file_out.write("Asian: "+str(asianAgeN/asianN))
    e_file_out.write("\nBlack: "+str(blackAgeN/blackN))
    e_file_out.write("\nWhite: "+str(whiteAgeN/whiteN))
    e_file_out.write("\nUndefined: "+str(undefAgeN/undefN))