## custom settings
rm_cls_list = [0,1,3,4]
## finish

import os
import numpy
import glob
import argparse
import numpy as np

#コマンドライン引数
parser = argparse.ArgumentParser()
parser.add_argument('--dir', type=str)
parser.add_argument('--img_type', type=str)

args = parser.parse_args()
DIR = args.dir
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
    
    tmp_cnt = 0
    for pathAndFilename in glob.iglob(os.path.join(DIR+'/images', "*."+FILE_TYPE)):
        title, ext = os.path.splitext(os.path.basename(pathAndFilename))
        print("\r"+str(tmp_cnt+1)+'/'+str(total_num),end="")
        #print(title,ext)
        in_file_path =  DIR+'/labels/'+title+'.txt'
        r_file = open(in_file_path, mode="r")
        lines = r_file.readlines()
        r_file.close()

        cnt = 0
        for line in lines:
            cnt+=1
        labels = np.zeros((cnt,5))
        cnt = 0
        for line in lines:
            line = line.split()
            labels[cnt,0] = line[0]
            labels[cnt,1] = line[1]
            labels[cnt,2] = line[2] 
            labels[cnt,3] = line[3]
            labels[cnt,4] = line[4]
            cnt+=1


        output = []
        for cnt,label in enumerate(labels):
            if label[0] in rm_cls_list:
                pass
            else:
                output.append([label[0],label[1],label[2],label[3],label[4]])
        if len(output)==0:
            pass  
        else:
            #######output###
            os.system(f"cp {DIR}/images/{title}.{FILE_TYPE} ./{OUT_DIR}/images/{title}.{FILE_TYPE}")
            out_text_file = open(OUT_DIR+'/labels/'+title+'.txt', "wt")
            for label in labels:
                out_text_file.write(str(int(label[0]))+' ')
                out_text_file.write(str(label[1])+' ')
                out_text_file.write(str(label[2])+' ')
                out_text_file.write(str(label[3])+' ')
                out_text_file.write(str(label[4])+'\n')
                
            out_text_file.close()
            #############
        tmp_cnt += 1
            
main()
