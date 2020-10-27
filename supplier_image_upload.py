#!/usr/bin/env python3
import requests
import os
from tqdm import tqdm

# This example shows how a file can be uploaded using The Python Requests module
url = "http://localhost/upload/"
IM_PATH = "/home/student-03-2b068cbe729c/supplier-data/images/"

for item in tqdm(os.listdir(IM_PATH)):
  print("Processing...",item)
  name, ext = os.path.splitext(item)
  print("file name:{}, file extension:{}".format(name,ext))
  if ext == ".jpeg":
    with open(os.path.join(IM_PATH,item),'rb') as opened:
      r = requests.post(url, files={'file': opened})
      print("Posting",item)
print("Done!")
