#!/usr/bin/env python3
from PIL import Image
import os
from tqdm import tqdm


IM_PATH = "/home/student-03-a899d807370d/supplier-data/images/"
for file in tqdm(os.listdir(IM_PATH)):
    outfile =IM_PATH + str(file)[:-5] + ".jpeg"
    try:
        with Image.open(os.path.join(IM_PATH,file)) as im:
            im.convert('RGB').resize((600,400)).save(outfile)
    except OSError as e:
        #if file is not an image, we'll have an error
        print("Error for file {} trying to save in {}".format(file,outfile))
        print(e)
        pass
print("Done!") 
