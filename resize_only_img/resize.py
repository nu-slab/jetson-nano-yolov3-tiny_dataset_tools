from convert_module import *
import cv2
import os
import numpy
import glob
from tqdm import tqdm
import argparse

#コマンドライン引数
parser = argparse.ArgumentParser()
parser.add_argument('--dir', type=str)
parser.add_argument('--resize_size', type=int)
parser.add_argument('--img_type', type=str)

args = parser.parse_args()
DIR = args.dir
RESIZE_SIZE = args.resize_size
FILE_TYPE = args.img_type
OUT_DIR = "./output"

def main():
    os.system(f"rm -rf  {OUT_DIR}")
    os.system(f"mkdir {OUT_DIR}")
    
    total_num = sum(os.path.isfile(os.path.join(DIR, name)) for name in os.listdir(DIR))
    bar = tqdm(total=total_num)
    bar.set_description('rate')
    for pathAndFilename in glob.iglob(os.path.join(DIR, "*."+FILE_TYPE)):
        title, ext = os.path.splitext(os.path.basename(pathAndFilename))
        img = cv2.imread(DIR+'/'+title+ext)            
        img = img_resize_square_only_img(img)
        height,width = img.shape[:2]
        img = cv2.resize(img , (int(width*(RESIZE_SIZE/width)), int(height*(RESIZE_SIZE/width))))
        
        #####output###
        cv2.imwrite(OUT_DIR+'/'+title+ext,img)
        #############
        
        bar.update(1)

    bar.close
    
main()
