'''
Created on Jun 29, 2017

@author: kyriacos
'''

#import json
from CrunchbaseDataDictionaries.JsonFormatter import jsonFormatter
    
if __name__ == '__main__':
    e_file_in = open("../CrunchbaseDataOutput/Crunchbase_Entrepreneurs_FaceAttributes_Output.json", 'r')
    e_file_out = open("Crunchbase_Entrepreneurs_FaceAttributes_Dictionaries.json", "w")
    
    for line in e_file_in:   
        record = jsonFormatter(line)
        e_file_out.write(record)
        """
        try:
            jdict = json.loads(record)
            e_file_out.write(str(jdict)+"\n")
        except ValueError:
            print("Error!!!")
        """