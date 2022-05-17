import os
import glob
from tqdm import tqdm
import argparse

#コマンドライン引数
parser = argparse.ArgumentParser()
parser.add_argument('--in_dir', type=str)
parser.add_argument('--out_dir', type=str)
parser.add_argument('--img_type', type=str)
parser.add_argument('--rename_str', type=str)

args = parser.parse_args()
DIR = args.in_dir
OUT_DIR = args.out_dir
FILE_TYPE = args.img_type
rename = args.rename_str

def main():
    os.system(f"rm -rf {OUT_DIR}/labels")
    os.system(f"rm -rf {OUT_DIR}/images")
    os.system(f"mkdir {OUT_DIR}/labels")
    os.system(f"mkdir {OUT_DIR}/images")
    total_num = sum(os.path.isfile(os.path.join(DIR+'/images', name)) for name in os.listdir(DIR+'/images'))
    bar = tqdm(total=total_num)
    bar.set_description('rate')

    for pathAndFilename in glob.iglob(os.path.join(DIR+'/images', "*."+FILE_TYPE)):
        title, ext = os.path.splitext(os.path.basename(pathAndFilename))
        # txt copy & rename
        title_out = rename + title
        os.system(f"cp {DIR}/labels/{title}.txt {OUT_DIR}/labels/{title_out}.txt")
        # img copy & rename
        os.system(f"cp {DIR}/images/{title}.{FILE_TYPE} {OUT_DIR}/images/{title_out}.{FILE_TYPE}")
        bar.update(1)
        
    bar.close
    


main()
