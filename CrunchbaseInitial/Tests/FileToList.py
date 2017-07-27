'''
Created on Jun 28, 2017

@author: kyriacos
'''

import json

if __name__ == '__main__':
    rectList=[]
    pos = 0
    count = 1
    
    e_file_in = open("../DataDictionaries/Non_Entrepreneurs_FaceLandmarks_Dictionaries.json", "r")
    e_file_in_rect = open("../DataDictionaries/Non_Entrepreneurs_Rectangles_Dictionaries.json", "r")
    e_file_out = open("Optimization.txt", "w")
    
    for rectRecord in e_file_in_rect:
        rectList.append(rectRecord)
            
    for record in e_file_in:   
        
        jDict = json.loads(record)  
        jID = jDict['_id']
        
        rectDict = json.loads(rectList[pos])
        rectID = rectDict['_id']
        
        while rectID < jID:
            pos += 1
            rectDict = json.loads(rectList[pos])
            rectID = rectDict['_id']     
            
        print "jID is "+str(jID)+" and rectID is "+str(rectID)
        if rectID == jID:
            e_file_out.write(jID)
            e_file_out.write('\n')
            count += 1
            pos += 1
        
