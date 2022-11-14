import cv2
import os
import numpy
import glob
from tqdm import tqdm
import argparse
import sys
from PIL import Image

#コマンドライン引数
parser = argparse.ArgumentParser()
parser.add_argument('--dir', type=str)
parser.add_argument('--filetype', type=str)

args = parser.parse_args()
DIR = args.dir
FILE_TYPE = args.filetype
OUT_DIR = "./output"

def main():
    os.system(f"rm -rf  {OUT_DIR}")
    os.system(f"mkdir {OUT_DIR}")
    
    total_num = sum(os.path.isfile(os.path.join(DIR, name)) for name in os.listdir(DIR))
    bar = tqdm(total=total_num)
    bar.set_description('rate')
    for pathAndFilename in glob.iglob(os.path.join(DIR, "*."+FILE_TYPE)):
        title, ext = os.path.splitext(os.path.basename(pathAndFilename))
        rgb_im = Image.open(DIR+'/'+title+ext).convert('RGB')
        rgb_im.save(OUT_DIR+'/'+title+ext)
        bar.update(1)

    bar.close
    
main()
