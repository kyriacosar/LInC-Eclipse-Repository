'''
Created on Jun 29, 2017

@author: kyriacos
'''

#import json
from DataDictionaries.JsonFormatter import jsonFormatter
    
if __name__ == '__main__':
    e_file_in = open("../../../../Documents/Crunchbase Project Data/Complete/Data Output/Attributes_Output.json", 'r')
    e_file_out = open("../../../../Documents/Crunchbase Project Data/Complete/Data Dictionaries/Attributes_Dictionaries.json", "w")
    
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