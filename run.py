#! /usr/bin/env python3
import os
import requests
import json
from tqdm import tqdm
FILES_PATH = "/home/student-03-2b068cbe729c/supplier-data/descriptions"
for file in tqdm(os.listdir(FILES_PATH)):
    with open(os.path.join(FILES_PATH,file),'r') as f:
        dic= {}
        text = f.readlines()
        print(text)
        dic['name']= text[0]
        dic['weight']= int(text[1].split(' ')[0])
        dic['description']=text[2]
        
        name ,ext = os.path.splitext(file)
        
        dic['image_name'] = name + '.jpeg'
        # PROBLEM WHEN USING JSON METHOD : WHY ? json_feedback = json.dumps(dic) response = requests.post("https://35.223.150.140/feedback", 
        # json = json_feedback) if response.status_code == 201:
        #     print("Feedback for {} was sent!".format(file)) else: print("A problem occured for {}. status code is {}: 
        #     ".format(file,response.status_code ))
        response = requests.post("http://35.192.16.229/fruits/", data = dic)
        if response.status_code == 201:
            print("Feedback for {} was sent!".format(file))
        else:
            print("A problem occured for {}. status code is {}: ".format(file,response.status_code )) 
