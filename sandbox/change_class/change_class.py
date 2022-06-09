import glob, os, cv2
import numpy as np
from change_class_module import *
from tqdm import tqdm
import time
import argparse

#コマンドライン引数
parser = argparse.ArgumentParser()
parser.add_argument('--in_dir', type=str)
parser.add_argument('--cls_change_list_file_name', type=str)



args = parser.parse_args()
input_path = args.in_dir
cls_change_list_file_name = args.cls_change_list_file_name

# input dir (write full path)
#  - images
#  - labels

# ./output
#  - images
#  - labels

cls_change_list_file =  open(cls_change_list_file_name, mode='r')
cls_change_list = cls_change_list_file.readlines()
for i,cls_change_str in enumerate(cls_change_list):
    cls_change_list[i] = cls_change_str.replace('\n','')

cls_change_list = make_array(cls_change_list)
for line in cls_change_list:
    print("cls:"+line[0]+" --> "+line[1])
image_path = input_path+'/images'
label_path = input_path+'/labels'
output_image_path = './output/images'
output_label_path = './output/labels'
os.system(f"mkdir {output_image_path}")
os.system(f"mkdir {output_label_path}")

DIR = label_path
total_num = sum(os.path.isfile(os.path.join(DIR, name)) for name in os.listdir(DIR))
bar = tqdm(total=total_num)
bar.set_description('rate')

for pathAndFilename in glob.iglob(os.path.join(label_path, "*.txt")):
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))
    in_file_path =  image_path+'/'+title+'.jpg'
    img = cv2.imread(in_file_path)

    in_file_path =  label_path+'/'+title+'.txt'
    r_file = open(in_file_path, mode="r")
    lines = r_file.readlines()
    r_file.close()
    labels = make_array(lines)
    for cnt,label in enumerate(labels):
        for cls_change in cls_change_list:
            if cls_change[0]==labels[cnt][0]:
                labels[cnt][0] = cls_change[1]
                break;
            
    ###output###
    cv2.imwrite(output_image_path+'/'+title+'.jpg',img)
    out_text_file = open(output_label_path+'/'+title+'.txt', "wt")
    for label in labels:
        out_text_file.write(str(int(label[0]))+' ')
        out_text_file.write(str(label[1])+' ')
        out_text_file.write(str(label[2])+' ')
        out_text_file.write(str(label[3])+' ')
        out_text_file.write(str(label[4])+'\n')
    out_text_file.close()
    
    bar.update(1)
    
