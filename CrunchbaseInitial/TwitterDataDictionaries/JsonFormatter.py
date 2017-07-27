'''
Created on Jun 21, 2017

@author: kyriacos
'''
import json

def jsonFormatter(record):
    record=record.replace("u'", '"')
    record=record.replace("'", '"')  
    record=record.replace("\"faceAttributes\": [{", "")
    record=record.replace("\"faceRectangles\": [{", "")
    record=record.replace("[]", "{}")
    record=record.replace("[","")
    record=record.replace("]","")   
    record=record.replace("F", 'f')
    record=record.replace("T", 't')   
    record=record.replace("}, {\"color\":", ",")
    record=record.replace(", \"confidence\"", "")
    record=record.replace("hairColor\": {\"color\": ", "hairColorConfidence\": {")
    record=record.replace("}}}}", "}}}")
    record=record.replace("accessories\": {\"type\": ", "accessories\": [")
    record=record.replace("accessories\": {", "accessories\": [")
    record=record.replace("}, {\"type\":", ",")
    record=record.replace("}, \"facialHair", "], \"facialHair")
    record=record.replace("\"faceplusplus\": {", "")
    
    return record

if __name__ == '__main__':
    e_file_in = open("../TwitterDataOutput/Entrepreneurs_File_Output.json", 'r')
    
    for count in range(1, 3):
        line = e_file_in.readline()
        
    print line
    record=jsonFormatter(line)
    print record
    jDict = json.loads(record)
    print jDict