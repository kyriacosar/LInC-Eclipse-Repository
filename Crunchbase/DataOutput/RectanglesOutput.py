'''
Created on Jul 26, 2017

@author: kyriacos
'''

from pymongo import MongoClient

if __name__ == '__main__':
    client = MongoClient("localhost", 27017, maxPoolSize=50)
    db=client['Crunchbase']
    collection_Entrepreneurs=db['CrunchbaseData']
    cursor = collection_Entrepreneurs.find({"$and":[{"faceplusplus":{"$exists":True}, "$where" : "this.faceplusplus.length == 1"},{"$where" : "this.faceAttributes.length == 1"}]},{"isEntre":1, "faceAttributes.faceRectangle":1, "faceplusplus.face_rectangle":1})
    #"faceAttributes.0":{"$exists":"false"}
    e_file_out = open("../../../../Documents/Crunchbase Project Data/Complete/Data Output/Rectangles_Output.json", 'w')
    
    for document in cursor:
        e_file_out.write(str(document)+"\n")