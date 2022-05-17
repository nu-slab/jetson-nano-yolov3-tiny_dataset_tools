import os
import glob
from tqdm import tqdm
import random
import argparse

#コマンドライン引数
parser = argparse.ArgumentParser()
parser.add_argument('--in_dir', type=str)
parser.add_argument('--out_dir', type=str)
parser.add_argument('--img_type', type=str)

args = parser.parse_args()
DIR = args.in_dir
OUT_DIR = args.out_dir
FILE_TYPE = args.img_type

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
    
    total_num = sum(os.path.isfile(os.path.join(DIR+'/images', name)) for name in os.listdir(DIR+'/images'))
    bar = tqdm(total=total_num)
    bar.set_description('rate')
    print("total num : ", total_num)
    test_file =  open(OUT_DIR+"/test.txt", mode='w')
    train_file = open(OUT_DIR+"/train.txt", mode='w')
    valid_file = open(OUT_DIR+"/valid.txt", mode='w') 
    for pathAndFilename in glob.iglob(os.path.join(DIR+'/images', "*."+FILE_TYPE)):
        title, ext = os.path.splitext(os.path.basename(pathAndFilename))
        random_num = random.random()
        if random_num <= 0.7: #train
            train_file.write(OUT_DIR+"/train/images/"+title+"."+FILE_TYPE+"\n")
            os.system(f"cp {DIR}/labels/{title}.txt {OUT_DIR}/train/labels/{title}.txt")
            os.system(f"cp {DIR}/images/{title}.{FILE_TYPE} {OUT_DIR}/train/images/{title}.{FILE_TYPE}")
        elif random_num <= 0.9: #valid 
            valid_file.write(OUT_DIR+"/valid/images/"+title+"."+FILE_TYPE+"\n")
            os.system(f"cp {DIR}/labels/{title}.txt {OUT_DIR}/valid/labels/{title}.txt")
            os.system(f"cp {DIR}/images/{title}.{FILE_TYPE} {OUT_DIR}/valid/images/{title}.{FILE_TYPE}")
        else:#test
            test_file.write(OUT_DIR+"/test/images/"+title+"."+FILE_TYPE+"\n")
            os.system(f"cp {DIR}/labels/{title}.txt {OUT_DIR}/test/labels/{title}.txt")
            os.system(f"cp {DIR}/images/{title}.{FILE_TYPE} {OUT_DIR}/test/images/{title}.{FILE_TYPE}")
        
        bar.update(1)
        
    bar.close
    test_file.close()
    train_file.close()
    valid_file.close()

main()
