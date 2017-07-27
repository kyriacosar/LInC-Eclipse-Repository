'''
Created on Jun 27, 2017

@author: kyriacos
'''

import json

if __name__ == '__main__':
    e_file_in = open("../DataDictionaries/Non_Entrepreneurs_FaceLandmarks_Dictionaries.json", "r")
    e_file_in_rect = open("../DataDictionaries/Non_Entrepreneurs_Rectangles_Dictionaries.json", "r")
    
    count = 0
    non_entrepreneurs_count = 0
        
    for record in e_file_in:   
        try:
            jDict = json.loads(record)
            
            for rectRecord in e_file_in_rect:
                rectDict = json.loads(rectRecord)
                if rectDict['_id'] == jDict['_id']:
                    count += 1
                    break    
            
            non_entrepreneurs_count += 1
        except ValueError:
                print("Error in json to dictionary translation.")
    
    print ("The amount of non entrepreneurs is "+str(non_entrepreneurs_count))
    print ("ID matches found: "+str(count))