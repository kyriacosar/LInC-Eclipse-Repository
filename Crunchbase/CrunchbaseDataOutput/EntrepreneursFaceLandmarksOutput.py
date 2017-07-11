'''
Created on Jun 29, 2017

@author: kyriacos
'''

from pymongo import MongoClient

if __name__ == '__main__':
    client = MongoClient("localhost", 27017, maxPoolSize=50)
    db=client['Twitter_Photos']
    collection_Entrepreneurs=db['Crunchbase_Faces_Entrepreneur']
    cursor = collection_Entrepreneurs.find({"$where" : "this.faceAttributes.length == 1"} ,{'faceAttributes.faceLandmarks':1})
    #"faceAttributes.0":{"$exists":"false"}
    e_file_out = open("../../../../Documents/Crunchbase Project Data/Crunchbase Results/Data Output/Crunchbase_Entrepreneurs_FaceLandmarks_Output.json", 'w')
    
    for document in cursor:
        e_file_out.write(str(document)+"\n")