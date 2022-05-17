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
    os.system(f"rm -rf {OUT_DIR}/labels")
    os.system(f"rm -rf {OUT_DIR}/images")
    os.system(f"mkdir {OUT_DIR}/labels")
    os.system(f"mkdir {OUT_DIR}/images")
    
    total_num = sum(os.path.isfile(os.path.join(DIR+'/images', name)) for name in os.listdir(DIR+'/images'))
    bar = tqdm(total=total_num)
    bar.set_description('rate')
    for pathAndFilename in glob.iglob(os.path.join(DIR+'/images', "*."+FILE_TYPE)):
        title, ext = os.path.splitext(os.path.basename(pathAndFilename))
        img = cv2.imread(DIR+'/images/'+title+ext)
        
        in_file_path =  DIR+'/labels/'+title+'.txt'
        r_file = open(in_file_path, mode="r")
        lines = r_file.readlines()
        r_file.close()
            
        img,labels = img_resize_square(img,lines)
        
        height,width = img.shape[:2]
        img = cv2.resize(img , (int(width*(RESIZE_SIZE/width)), int(height*(RESIZE_SIZE/width))))
        for cnt,label in enumerate(labels):
            labels[cnt,0] = int(labels[cnt,0])
            labels[cnt,1] *= RESIZE_SIZE/width
            labels[cnt,2] *= RESIZE_SIZE/height
            labels[cnt,3] *= RESIZE_SIZE/width
            labels[cnt,4] *= RESIZE_SIZE/height
        for cnt,label in enumerate(labels):
            box = (label[1],label[3],label[2],label[4])
            size = [RESIZE_SIZE,RESIZE_SIZE]
            convert_label = convert(size,box)
            labels[cnt,1] = convert_label[0]
            labels[cnt,2] = convert_label[1]
            labels[cnt,3] = convert_label[2]
            labels[cnt,4] = convert_label[3]
            
        #####output###
        cv2.imwrite(OUT_DIR+'/images/'+title+ext,img)
        out_text_file = open(OUT_DIR+'/labels/'+title+'.txt', "wt")
        for label in labels:
            out_text_file.write(str(int(label[0]))+' ')
            out_text_file.write(str(label[1])+' ')
            out_text_file.write(str(label[2])+' ')
            out_text_file.write(str(label[3])+' ')
            out_text_file.write(str(label[4])+'\n')
        
        out_text_file.close()
        #############
        
        
        bar.update(1)

    bar.close
    
main()
