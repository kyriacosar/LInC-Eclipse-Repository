'''
Created on Jul 24, 2017

@author: kyriacos
'''

import json

if __name__ == '__main__':
    # Opening the necessary files.
    # Input files:
    e_file_in = open("../../../../Documents/Crunchbase Project Data/Microsoft/Crunchbase Results/Data Dictionaries/Crunchbase_Entrepreneurs_FaceAttributes_Dictionaries.json", "r")
    # Output files:
    e_file_out = open("../../../../Documents/Crunchbase Project Data/Microsoft/Crunchbase Results/Data Extraction/Crunchbase_Entrepreneurs_Hair.txt", "w")
    
    # Initialize variables.
    black = 0
    other = 0
    brown = 0
    grey = 0
    red = 0
    blond = 0
    bald = 0
    count = 0
    
    # Adding titles to the output file.
    e_file_out.write("Hair color confidence of Entrepreneurs:\n\n")
    e_file_out.write("ID\t\t\t\t\tBlack\tOther\tBrown\tGrey\tRed\tBlond\tBald\n")
    e_file_out.write("-"*36+"\t"+"-"*5+"\t"+"-"*5+"\t"+"-"*5+"\t"+"-"*4+"\t"+"-"*4+"\t"+"-"*5+"\t"+"-"*4+"\n")
    
    # Reading the JSON formatted face landmarks records.    
    for record in e_file_in:
        try:            
            # Converting the JSON record to a dictionary and isolating the ID field.
            jDict = json.loads(record)
            jID = jDict['_id']
        
            jInv = jDict['faceAttributes']['hair']['invisible']
            hairDict = jDict['faceAttributes']['hair']['hairColorConfidence']
            if jInv:
                jBlack = 0
                jOther = 0
                jBrown = 0
                jGrey = 0
                jRed = 0
                jBlond = 0
                jBald = 0
            elif len(hairDict) == 0:
                jBlack = 0
                jOther = 0
                jBrown = 0
                jGrey = 0
                jRed = 0
                jBlond = 0
                jBald = 0
                jBald = jDict['faceAttributes']['hair']['bald']
                bald += jBald
            else:
                jBlack = jDict['faceAttributes']['hair']['hairColorConfidence']['black']
                jOther = jDict['faceAttributes']['hair']['hairColorConfidence']['other']
                jBrown = jDict['faceAttributes']['hair']['hairColorConfidence']['brown']
                jGrey = jDict['faceAttributes']['hair']['hairColorConfidence']['gray']
                jRed = jDict['faceAttributes']['hair']['hairColorConfidence']['red']
                jBlond = jDict['faceAttributes']['hair']['hairColorConfidence']['blond']
                jBald = 0
                black += jBlack
                other += jOther
                brown += jBrown
                grey += jGrey
                red += jRed
                blond += jBlond      
            
            count += 1          
            
            # Printing results to file.
            e_file_out.write(str(jDict['_id'])+"\t"+str(jBlack)+"\t"+str(jOther)+"\t"+str(jBrown)+"\t"+str(jGrey)+"\t"+str(jRed)+"\t"+str(jBlond)+"\t"+str(jBald)+"\n")
                
        except ValueError:
                print("Error in json to dictionary translation.")
    
    # Calculating the average pupil distance and writing in the output file.
    totalAvg = black/count + other/count + brown/count + grey/count + red/count + blond/count + bald/count
    e_file_out.write("\nAverages:\n")
    e_file_out.write("Black:\t"+str(black/count/totalAvg)+"\n")
    e_file_out.write("Other:\t"+str(other/count/totalAvg)+"\n")
    e_file_out.write("Brown:\t"+str(brown/count/totalAvg)+"\n")
    e_file_out.write("Grey:\t"+str(grey/count/totalAvg)+"\n")
    e_file_out.write("Red:\t"+str(red/count/totalAvg)+"\n")
    e_file_out.write("Blond:\t"+str(blond/count/totalAvg)+"\n")
    e_file_out.write("Bald:\t"+str(bald/count/totalAvg)+"\n") 