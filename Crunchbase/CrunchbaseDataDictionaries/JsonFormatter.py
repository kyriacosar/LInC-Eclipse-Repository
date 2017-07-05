'''
Created on Jun 29, 2017

@author: kyriacos
'''

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
    
    return record