import glob, os, cv2
import numpy as np
from tqdm import tqdm
import time
import argparse

#コマンドライン引数
parser = argparse.ArgumentParser()
parser.add_argument('--in_dir', type=str)
parser.add_argument('--cls_list_file_name', type=str)
parser.add_argument('--file_type', type=str)

args = parser.parse_args()
input_path = args.in_dir
cls_list_file_name = args.cls_list_file_name
file_type = args.file_type

# input dir (write full path)
#  - cls1 
#    - images
#    - labels
#  - cls2 
#    - images
#    - labels

# ./output
#  - cls1 
#    - images
#    - labels
#  - cls2 
#    - images
#    - labels

cls_list_file =  open(cls_list_file_name, mode='r')
cls_list = cls_list_file.readlines()
for i,cls_str in enumerate(cls_list):
    cls_list[i] = cls_str.replace('\n','')

for cls_str in cls_list:
    image_path = input_path+'/'+cls_str+'/images'
    label_path = input_path+'/'+cls_str+'/labels'
    output_image_path = './output/images'
    output_label_path = './output/labels'
    
    DIR = label_path
    total_num = sum(os.path.isfile(os.path.join(DIR, name)) for name in os.listdir(DIR))
    bar = tqdm(total=total_num)
    bar.set_description(cls_str+' rate')
    
    for pathAndFilename in glob.iglob(os.path.join(image_path, "*."+file_type)):
        #print(pathAndFilename)
        title, ext = os.path.splitext(os.path.basename(pathAndFilename))
        in_file_path = image_path+'/'+title+'.'+file_type
        out_file_path =  output_image_path+'/'+cls_str+title+'.'+file_type
        os.system(f"cp {in_file_path} {out_file_path}")

        in_file_path =  label_path+'/'+title+'.txt'
        out_file_path =  output_label_path+'/'+cls_str+title+'.txt'
        os.system(f"cp {in_file_path} {out_file_path}")
        bar.update(1)
        
    
    bar.close
    
