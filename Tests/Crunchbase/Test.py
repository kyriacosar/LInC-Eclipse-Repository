'''
Created on Jun 20, 2017

@author: kyriacos
'''

import pymongo
import json
from pymongo import MongoClient
from pyasn1.compat.octets import null
from genericpath import exists

if __name__ == '__main__':
    client = MongoClient("localhost", 27017, maxPoolSize=50)
    db=client['Twitter_Photos']
    collection_Entrepreneurs=db['Faces_Entrepreneur']
    cursor = collection_Entrepreneurs.find({"$where" : "this.faceAttributes.length >= 1"} ,{'faceAttributes.faceAttributes':1})
    #"faceAttributes.0":{"$exists":"false"}
    e_file_out = open("Entrepreneurs_File_Output.json", 'w')
    
    for document in cursor:
        print json.dumps(document, indent=4, sort_keys=True)
        e_file_out.write(json.dumps(document, indent=4, sort_keys=True))

          
        


