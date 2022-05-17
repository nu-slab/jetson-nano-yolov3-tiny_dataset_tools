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
        h,w,_ = img.shape
        r_file = open(DIR+'/labels/'+title+'.txt', mode="r")
        lines = r_file.readlines()
        r_file.close()
        for line in lines:
            cls,start_point,end_point = split_txt(line,h,w)
            color = set_color(cls)
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

def split_txt(str_v,h,w):
    cls = int(str_v.split(' ')[0])
    x1 = int( float(str_v.split(' ')[1]) * w )
    y1 = int( float(str_v.split(' ')[2]) * h )
    xw = int( float(str_v.split(' ')[3]) * w /2)
    yw = int( float(str_v.split(' ')[4]) * h /2)
    start_point = (x1 - xw, y1 - yw )
    end_point   = (x1 + xw, y1 + yw )
    return cls,start_point,end_point

main()
