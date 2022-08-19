import os
import glob
from tqdm import tqdm
import argparse
import cv2

#コマンドライン引数
parser = argparse.ArgumentParser()
parser.add_argument('--dir', type=str)
parser.add_argument('--img_type', type=str)

args = parser.parse_args()
DIR = args.dir
FILE_TYPE = args.img_type

def main():
    total_num = sum(os.path.isfile(os.path.join(DIR+'/images', name)) for name in os.listdir(DIR+'/images'))
    bar = tqdm(total=total_num)
    bar.set_description('rate')
    
    for pathAndFilename in glob.iglob(os.path.join(DIR+'/images', "*."+FILE_TYPE)):
        title, ext = os.path.splitext(os.path.basename(pathAndFilename))
        img = cv2.imread(DIR+'/images/'+title+ext)
        r_file = open(DIR+'/labels/'+title+'.txt', mode="r")
        lines = r_file.readlines()
        r_file.close()
        for line in lines:
            cls = int(line.split(' ')[0])
            color = set_color(cls)
            start_point = (int(line.split(' ')[1]),int(line.split(' ')[2]))
            end_point   = (int(line.split(' ')[3]),int(line.split(' ')[4]))
            img = cv2.rectangle(img, start_point, end_point, color, 2)
            cv2.putText(img, str(cls), (start_point[0],start_point[1]+20), cv2.FONT_HERSHEY_PLAIN, 4, color, 5, cv2.LINE_AA)
        cv2.imwrite('./output/'+title+ext,img)
        bar.update(1)
    bar.close
    
def set_color(cls):
    if cls%3 == 0:
        color = ((cls*40)%255,0,0)
    elif cls%3 == 1:
        color = (0,(cls*40)%255,0)
    else:
        color = (0,0,(cls*40)%255)
    return color

main()
