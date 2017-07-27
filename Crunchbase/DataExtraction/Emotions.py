'''
Created on Jun 29, 2017

@author: kyriacos
'''

import json

if __name__ == '__main__':
    e_file_in = open("../../../../Documents/Crunchbase Project Data/Complete/Data Dictionaries/Attributes_Dictionaries.json", "r")
    e_file_out = open("../../../../Documents/Crunchbase Project Data/Complete/Data Extraction/Emotions.txt", "w")
    
    sadnessE = 0
    neutralE = 0
    contemptE = 0
    disgustE = 0
    angerE = 0
    surpriseE = 0
    fearE = 0
    happinessE = 0
    countE = 0
    
    sadnessN = 0
    neutralN = 0
    contemptN = 0
    disgustN = 0
    angerN = 0
    surpriseN = 0
    fearN = 0
    happinessN = 0
    countN = 0
    
    for record in e_file_in:   
        try:
            jDict = json.loads(record)
            
            is_entre = jDict['isEntre']
            
            if is_entre == 1:
                sadnessE += jDict['MSAttributes']['emotion']['sadness']
                neutralE += jDict['MSAttributes']['emotion']['neutral']
                contemptE += jDict['MSAttributes']['emotion']['contempt']
                disgustE += jDict['MSAttributes']['emotion']['disgust']
                angerE += jDict['MSAttributes']['emotion']['anger']
                surpriseE += jDict['MSAttributes']['emotion']['surprise']
                fearE += jDict['MSAttributes']['emotion']['fear']
                happinessE += jDict['MSAttributes']['emotion']['happiness']
                countE += 1
            else:
                sadnessN += jDict['MSAttributes']['emotion']['sadness']
                neutralN += jDict['MSAttributes']['emotion']['neutral']
                contemptN += jDict['MSAttributes']['emotion']['contempt']
                disgustN += jDict['MSAttributes']['emotion']['disgust']
                angerN += jDict['MSAttributes']['emotion']['anger']
                surpriseN += jDict['MSAttributes']['emotion']['surprise']
                fearN += jDict['MSAttributes']['emotion']['fear']
                happinessN += jDict['MSAttributes']['emotion']['happiness']
                countN += 1
        except ValueError:
            print("Error in json to dictionary translation.")
    
    e_file_out.write("Average Entrepreneur emotions:\n\n")
    e_file_out.write('Sadness: '+str(sadnessE/countE)+"\n")
    e_file_out.write('Neutral: '+str(neutralE/countE)+"\n")
    e_file_out.write('Contempt: '+str(contemptE/countE)+"\n")
    e_file_out.write('Disgust: '+str(disgustE/countE)+"\n")
    e_file_out.write('Anger: '+str(angerE/countE)+"\n")
    e_file_out.write('Surprise: '+str(surpriseE/countE)+"\n")
    e_file_out.write('Fear: '+str(fearE/countE)+"\n")
    e_file_out.write('Happiness :'+str(happinessE/countE)+"\n")
    e_file_out.write('Total :'+str((sadnessE+neutralE+contemptE+disgustE+angerE+surpriseE+fearE+happinessE)/countE))
    
    e_file_out.write("\n\n"+"="*60+"\n\n")
    
    e_file_out.write("Average Entrepreneur emotions:\n\n")
    e_file_out.write('Sadness: '+str(sadnessN/countN)+"\n")
    e_file_out.write('Neutral: '+str(neutralN/countN)+"\n")
    e_file_out.write('Contempt: '+str(contemptN/countN)+"\n")
    e_file_out.write('Disgust: '+str(disgustN/countN)+"\n")
    e_file_out.write('Anger: '+str(angerN/countN)+"\n")
    e_file_out.write('Surprise: '+str(surpriseN/countN)+"\n")
    e_file_out.write('Fear: '+str(fearN/countN)+"\n")
    e_file_out.write('Happiness :'+str(happinessN/countN)+"\n")
    e_file_out.write('Total :'+str((sadnessN+neutralN+contemptN+disgustN+angerN+surpriseN+fearN+happinessN)/countN))
    