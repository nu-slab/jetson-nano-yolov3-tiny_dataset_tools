import glob, os, cv2
import numpy as np
from module import *
from tqdm import tqdm
import time
import argparse

#コマンドライン引数
parser = argparse.ArgumentParser()
parser.add_argument('--in_dir', type=str)
parser.add_argument('--img_type', type=str)

args = parser.parse_args()
input_path = args.in_dir
FILE_TYPE = args.img_type

OUT_DIR = "./output"
input_image_path =input_path+'/images' 
input_label_path =input_path+'/labels' 
output_image_path =OUT_DIR+'/images' 
output_label_path =OUT_DIR+'/labels' 

# プログレスバー
total_num = sum(os.path.isfile(os.path.join(input_image_path, name)) for name in os.listdir(input_image_path))
bar = tqdm(total=total_num)
#bar.set_description(cls_str+' rate')

for pathAndFilename in glob.iglob(os.path.join(input_image_path, "*."+FILE_TYPE)):
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))
    
    #img load
    in_file_path =  input_image_path+'/'+title+'.jpg'
    img = cv2.imread(in_file_path)
    ##label load
    in_file_path =  input_label_path+'/'+title+'.txt'
    r_file = open(in_file_path, mode="r")
    lines = r_file.readlines()
    r_file.close()
    
    labels = extract_lines(lines)
        
    height,width = img.shape[:2]
    for cnt,label in enumerate(labels):
        x1,y1,x2,y2 = convert_reverse(width=width,height=height,x=float(label[1]),y=float(label[2]),w=float(label[3]),h=float(label[4]))
        labels[cnt,0] = int(label[0])
        labels[cnt,1] = int(x1)
        labels[cnt,2] = int(y1)
        labels[cnt,3] = int(x2)
        labels[cnt,4] = int(y2)
    
    #####output###
    cv2.imwrite(output_image_path+'/'+title+'.'+FILE_TYPE,img)
    out_text_file = open(output_label_path+'/'+title+'.txt', "wt")
    for label in labels:
        out_text_file.write(str(int(label[0]))+' ')
        out_text_file.write(str(int(label[1]))+' ')
        out_text_file.write(str(int(label[2]))+' ')
        out_text_file.write(str(int(label[3]))+' ')
        out_text_file.write(str(int(label[4]))+'\n')
    out_text_file.close()
    
    bar.update(1)
    

bar.close
