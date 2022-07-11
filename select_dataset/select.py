import os
import glob
from tqdm import tqdm
import random
import argparse
import time

#コマンドライン引数
parser = argparse.ArgumentParser()
parser.add_argument('--in_dir', type=str)
parser.add_argument('--out_dir', type=str)
parser.add_argument('--img_type', type=str)
parser.add_argument('--percentage', type=str)

args = parser.parse_args()
DIR = args.in_dir
OUT_DIR = args.out_dir
FILE_TYPE = args.img_type
PERCENTAGE = float(int(args.percentage)/100)

dataset_types = ["train","valid","test"]

def main():    
    os.system(f"rm -rf {OUT_DIR}/test")
    os.system(f"rm -rf {OUT_DIR}/train")
    os.system(f"rm -rf {OUT_DIR}/valid")
    os.system(f"mkdir {OUT_DIR}/test")
    os.system(f"mkdir {OUT_DIR}/train")
    os.system(f"mkdir {OUT_DIR}/valid")
    os.system(f"mkdir {OUT_DIR}/test/images")
    os.system(f"mkdir {OUT_DIR}/train/images")
    os.system(f"mkdir {OUT_DIR}/valid/images")
    os.system(f"mkdir {OUT_DIR}/test/labels")
    os.system(f"mkdir {OUT_DIR}/train/labels")
    os.system(f"mkdir {OUT_DIR}/valid/labels")

    for dataset_type in dataset_types:
        total_num = sum(os.path.isfile(os.path.join(DIR+'/'+dataset_type+'/images', name)) for name in os.listdir(DIR+'/'+dataset_type+'/images'))
        out_text = ""
        for tmp_cnt,pathAndFilename in enumerate(glob.iglob(os.path.join(DIR+'/'+dataset_type+'/images', "*."+FILE_TYPE))):
            print("\r"+str(dataset_type)+':'+str(tmp_cnt+1)+'/'+str(total_num),end="")
            title, ext = os.path.splitext(os.path.basename(pathAndFilename))
            if random.uniform(0.0, 1.0)<=PERCENTAGE:
                out_text += OUT_DIR+'/'+dataset_type+'/images/'+title+ext+'\n'
                os.system(f"cp -r  {DIR}/{dataset_type}/images/{title}{ext} {OUT_DIR}/{dataset_type}/images/{title}{ext}")
                os.system(f"cp -r  {DIR}/{dataset_type}/labels/{title}.txt {OUT_DIR}/{dataset_type}/labels/{title}.txt")
        out_text_files = open(OUT_DIR+"/"+dataset_type+".txt", mode='w')
        out_text_files.write(out_text)
        print()
    
main()
