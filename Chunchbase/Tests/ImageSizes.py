'''
Created on Jun 30, 2017

@author: kyriacos
'''

import json
from PIL import Image

if __name__ == '__main__':
    rectList=[]
    pos = 0
    count = 1
    
    e_file_in = open("../TwitterDataDictionaries/Twitter_Entrepreneurs_FaceLandmarks_Dictionaries.json", "r")
    
    for record in e_file_in:
        rec_dict = json.loads(record)
        iddd = rec_dict['_id']
        break
        
    img_path = "../../../../Documents/Crunchbase Data/images_eter/3469.jpeg"
    img = Image.open(img_path)
    #img.show()
    print img.size