import os
import numpy
import glob
from tqdm import tqdm
import argparse
# images/*.jpg
# output/*.jpg
DIR = 'images'
FILE_TYPE = 'jpg'
OUT_DIR = "output"

def main():
    os.system(f"rm -rf  {OUT_DIR}")
    os.system(f"mkdir {OUT_DIR}")
    
    total_num = sum(os.path.isfile(os.path.join(DIR, name)) for name in os.listdir(DIR))
    bar = tqdm(total=total_num)
    bar.set_description('rate')
    for i,pathAndFilename in enumerate(glob.iglob(os.path.join(DIR, "*."+FILE_TYPE))):
        title, ext = os.path.splitext(os.path.basename(pathAndFilename))
        title_out = "{i:0=10d}".format(i=i)
        os.system(f"mv {DIR}/{title}.{FILE_TYPE} {OUT_DIR}/{title_out}.{FILE_TYPE}")
        bar.update(1)
    bar.close
main()
