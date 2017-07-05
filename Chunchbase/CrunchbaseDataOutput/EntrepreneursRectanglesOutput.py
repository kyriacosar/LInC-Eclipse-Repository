'''
Created on Jun 29, 2017

@author: kyriacos
'''

from pymongo import MongoClient

if __name__ == '__main__':
    client = MongoClient("localhost", 27017, maxPoolSize=50)
    db=client['Twitter_Photos']
    collection_Entrepreneurs=db['Crunchbase_Rectangles_Entrepreneurs']
    cursor = collection_Entrepreneurs.find({"$where" : "this.faceRectangles.length == 1"} ,{'faceRectangles':1}).sort("_id")
    #"faceAttributes.0":{"$exists":"false"}
    e_file_out = open("Crunchbase_Entrepreneurs_Rectangles_Output.json", 'w')
    
    for document in cursor:
        e_file_out.write(str(document)+"\n")
        #print str(document)
