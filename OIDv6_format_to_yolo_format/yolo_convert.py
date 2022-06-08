import glob, os, cv2
import numpy as np
from convert_module import *
from tqdm import tqdm
import time
import argparse

#コマンドライン引数
parser = argparse.ArgumentParser()
parser.add_argument('--in_dir', type=str)
parser.add_argument('--cls_list_file_name', type=str)
parser.add_argument('--resize_en', action='store_true')
parser.add_argument('--img_size', type=int)
parser.add_argument('--rename_en', action='store_true')
args = parser.parse_args()
input_path = args.in_dir
cls_list_file_name = args.cls_list_file_name
resize_en= args.resize_en
img_size = args.img_size
rename_en = args.rename_en

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


# convert here
for cls_str in cls_list:
    os.system(f"mkdir ./output/{cls_str}")
    os.system(f"mkdir ./output/{cls_str}/images")
    os.system(f"mkdir ./output/{cls_str}/labels")
    image_path = input_path+'/'+cls_str+'/images'
    label_path = input_path+'/'+cls_str+'/labels'
    output_image_path = './output/'+cls_str+'/images'
    output_label_path = './output/'+cls_str+'/labels'
    
    DIR = label_path
    total_num = sum(os.path.isfile(os.path.join(DIR, name)) for name in os.listdir(DIR))
    bar = tqdm(total=total_num)
    bar.set_description(cls_str+' rate')
    
    for pathAndFilename in glob.iglob(os.path.join(image_path, "*.jpg")):
        #print(pathAndFilename)
        title, ext = os.path.splitext(os.path.basename(pathAndFilename))
        in_file_path =  image_path+'/'+title+'.jpg'
        img = cv2.imread(in_file_path)
    
        in_file_path =  label_path+'/'+title+'.txt'
        r_file = open(in_file_path, mode="r")
        lines = r_file.readlines()
        r_file.close()
        if(resize_en):
            img,labels = img_resize_square(img,lines,rename_en,cls_list)
            
            height,width = img.shape[:2]
            img = cv2.resize(img , (int(width*(img_size/width)), int(height*(img_size/width))))
            for cnt,label in enumerate(labels):
                labels[cnt,0] = int(labels[cnt,0])
                labels[cnt,1] *= img_size/width
                labels[cnt,2] *= img_size/height
                labels[cnt,3] *= img_size/width
                labels[cnt,4] *= img_size/height
            size = [img_size,img_size]
            for cnt,label in enumerate(labels):
                box = (label[1],label[3],label[2],label[4])
                convert_label = convert(size,box)
                labels[cnt,1] = convert_label[0]
                labels[cnt,2] = convert_label[1]
                labels[cnt,3] = convert_label[2]
                labels[cnt,4] = convert_label[3]
        else:
            labels = make_label(lines,rename_en,cls_list)
            height,width = img.shape[:2]
            size = [width,height]
            for cnt,label in enumerate(labels):
                box = (label[1],label[3],label[2],label[4])  
                convert_label = convert(size,box)
                labels[cnt,1] = convert_label[0]
                labels[cnt,2] = convert_label[1]
                labels[cnt,3] = convert_label[2]
                labels[cnt,4] = convert_label[3]

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
        
    
    bar.close
    
