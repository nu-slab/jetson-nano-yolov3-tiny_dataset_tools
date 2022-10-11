import os
import numpy
import glob
from tqdm import tqdm
import argparse

# input
### images/*.jpg
### labele/label.txt
# output
### output/*.txt

DIR = 'image-jpg'
FILE_TYPE = 'jpg'
LABEL = 'label/label.txt'
CLS_STR = '0'

OUT_DIR = "output"

def main():
    os.system(f"rm -rf  {OUT_DIR}")
    os.system(f"mkdir {OUT_DIR}")
    label_file = open(LABEL, "r")
    label_data = label_file.readlines()
    label_file.close()
    total_num = sum(os.path.isfile(os.path.join(DIR, name)) for name in os.listdir(DIR))
    bar = tqdm(total=total_num)
    bar.set_description('rate')
    for i,pathAndFilename in enumerate(glob.iglob(os.path.join(DIR, "*."+FILE_TYPE))):
        title, ext = os.path.splitext(os.path.basename(pathAndFilename))
        #print(label_data[i])
        write_file = open(OUT_DIR+'/'+title+'.txt', "wt")
        write_file.write(CLS_STR+' '+label_data[i])
        write_file.close()
        bar.update(1)
    bar.close
main()
