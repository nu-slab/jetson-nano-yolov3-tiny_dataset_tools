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
parser.add_argument('--rename_str', type=str)

parser.add_argument('--color_jitter_en', action='store_true')
parser.add_argument('--random_equalize_en', action='store_true')
parser.add_argument('--random_auto_contrast_en', action='store_true')

args = parser.parse_args()
DIR = args.dir
FILE_TYPE = args.img_type
WIDTH_OF_CHANGE = args.width_of_change
RENAME_STR = args.rename_str

color_jitter_en = args.color_jitter_en
random_equalize_en = args.random_equalize_en
random_auto_contrast_en = args.random_auto_contrast_en

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
        img = Image.open(DIR+'/images/'+title+ext)
        if color_jitter_en:
            transform = transforms.ColorJitter(brightness=WIDTH_OF_CHANGE, contrast=WIDTH_OF_CHANGE, saturation=WIDTH_OF_CHANGE, hue=0)
        elif random_equalize_en:
            transform = transforms.RandomEqualize(p=WIDTH_OF_CHANGE)
        elif random_auto_contrast_en:
            transform = transforms.RandomAutocontrast(p=WIDTH_OF_CHANGE)
        imgs = transform(img)
        imgs.save(OUT_DIR+'/images/'+RENAME_STR+title+ext)
        os.system(f"cp {DIR}/labels/{title}.txt {OUT_DIR}/labels/{RENAME_STR}{title}.txt")
        bar.update(1)


    bar.close()
main()
