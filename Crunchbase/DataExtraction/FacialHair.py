'''
Created on Jul 24, 2017

@author: kyriacos
'''

import json

if __name__ == '__main__':
    # Opening the necessary files.
    # Input files:
    e_file_in = open("../../../../Documents/Crunchbase Project Data/Complete/Data Dictionaries/Attributes_Dictionaries.json", "r")
    # Output files:
    e_file_out_E = open("../../../../Documents/Crunchbase Project Data/Complete/Data Extraction/Entrepreneurs_FacialHair.txt", "w")
    
    # Initialize variables.
    sideburns = 0
    beard = 0
    moustache = 0
    count = 0
    
    # Adding titles to the output file.
    e_file_out_E.write("Facial hair confidence of Entrepreneurs:\n\n")
    e_file_out_E.write("ID\t\t\t\t\tSideburns\tBeard\tMoustache\n")
    e_file_out_E.write("-"*36+"\t"+"-"*9+"\t"+"-"*5+"\t"+"-"*9+"\n")
    
    # Reading the JSON formatted face landmarks records.    
    for record in e_file_in:
        try:            
            # Converting the JSON record to a dictionary and isolating the ID field.
            jDict = json.loads(record)
            jID = jDict['_id']
        
            jFH = jDict['faceAttributes']['facialHair']
            jSideburns = jFH['sideburns']
            jBeard = jFH['beard']
            jMoustache = jFH['moustache']
            sideburns += jSideburns
            beard += jBeard
            moustache += jMoustache
            count += 1          
            
            # Printing results to file.
            e_file_out_E.write(str(jDict['_id'])+"\t"+str(jSideburns)+"\t\t"+str(jBeard)+"\t"+str(jMoustache)+"\n")
                
        except ValueError:
                print("Error in json to dictionary translation.")
    
    # Calculating the average pupil distance and writing in the output file.
    totalAvg = sideburns/count + beard/count + moustache/count
    e_file_out_E.write("\nAverages:\n")
    e_file_out_E.write("Sideburns:\t"+str(sideburns/count/totalAvg)+"\n")
    e_file_out_E.write("Beard:\t\t"+str(beard/count/totalAvg)+"\n")
    e_file_out_E.write("Moustache:\t"+str(moustache/count/totalAvg)+"\n")