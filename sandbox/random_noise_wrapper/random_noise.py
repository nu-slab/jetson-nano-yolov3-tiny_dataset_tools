from PIL import Image
from torch.utils import data as data
from torchvision import transforms as transforms

import os
import numpy
import glob
from tqdm import tqdm
import argparse

#コマンドライン引数
parser = argparse.ArgumentParser()
parser.add_argument('--dir', type=str)
parser.add_argument('--out_dir', type=str)
parser.add_argument('--img_type', type=str)
parser.add_argument('--width_of_change', type=float)
parser.add_argument('--set_count', type=int)

args = parser.parse_args()
DIR = args.dir
FILE_TYPE = args.img_type
WIDTH_OF_CHANGE = args.width_of_change
SET_COUNT = args.set_count
TRANS_FILE_TYPE_NUM = 3

OUT_DIR = "./output"

def main():
    os.system(f"rm -rf  {OUT_DIR}")
    os.system(f"mkdir {OUT_DIR}")
    os.system(f"rm -rf {OUT_DIR}/labels")
    os.system(f"rm -rf {OUT_DIR}/images")
    os.system(f"mkdir {OUT_DIR}/labels")
    os.system(f"mkdir {OUT_DIR}/images")
    
    total_num = sum(os.path.isfile(os.path.join(DIR+'/images', name)) for name in os.listdir(DIR+'/images')) *SET_COUNT *TRANS_FILE_TYPE_NUM
    bar = tqdm(total=total_num)
    bar.set_description('rate')
    
    for now_set_count in range(SET_COUNT):
        for pathAndFilename in glob.iglob(os.path.join(DIR+'/images', "*."+FILE_TYPE)):
            title, ext = os.path.splitext(os.path.basename(pathAndFilename))
            img = Image.open(DIR+'/images/'+title+ext)
            if not now_set_count==0:
                transform_jitter = transforms.ColorJitter(brightness=WIDTH_OF_CHANGE, contrast=WIDTH_OF_CHANGE, saturation=WIDTH_OF_CHANGE, hue=0)
                img_color_jitter = transform_jitter(img)
            else:
                img_color_jitter = img

            transform_random_equalize = transforms.RandomEqualize(p=WIDTH_OF_CHANGE)
            transform_random_auto_contrast = transforms.RandomAutocontrast(p=WIDTH_OF_CHANGE)

            img_random_equalize = transform_random_equalize(img_color_jitter)
            img_random_auto_contrast = transform_random_auto_contrast(img_color_jitter)

            # color jitter
            RENAME_STR = str(now_set_count)+'_color_jitter_'
            img_color_jitter.save(OUT_DIR+'/images/'+RENAME_STR+title+ext)
            os.system(f"cp {DIR}/labels/{title}.txt {OUT_DIR}/labels/{RENAME_STR}{title}.txt")
            #### random_equalize
            RENAME_STR = str(now_set_count)+'_random_equalize_'
            img_random_equalize.save(OUT_DIR+'/images/'+RENAME_STR+title+ext)
            os.system(f"cp {DIR}/labels/{title}.txt {OUT_DIR}/labels/{RENAME_STR}{title}.txt")
            #### random_auto_contrast
            RENAME_STR = str(now_set_count)+'_random_auto_contrast_'
            img_random_auto_contrast.save(OUT_DIR+'/images/'+RENAME_STR+title+ext)
            os.system(f"cp {DIR}/labels/{title}.txt {OUT_DIR}/labels/{RENAME_STR}{title}.txt")
            
            bar.update(TRANS_FILE_TYPE_NUM)
    bar.close()
main()
