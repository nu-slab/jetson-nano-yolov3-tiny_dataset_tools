import cv2
import numpy as np
def convert(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)
def convert_reverse(width,height,x,y,w,h):
    dw = 1./width
    dh = 1./height
    w = w/dw
    h = h/dh
    x = x/dw
    y = y/dh
    half_w = w/2.0
    half_h = h/2.0
    c1_x = x - half_w
    c1_y = y - half_h
    c2_x = x + half_w
    c2_y = y + half_h
    return int(c1_x),int(c1_y),int(c2_x),int(c2_y)

def extract_lines(lines):
    cnt = 0
    for line in lines:
        cnt+=1
    output = np.zeros((cnt,5))
    cnt = 0
    for line in lines:
        line = line.split()
        output[cnt,0] = line[0]
        output[cnt,1] = line[1]
        output[cnt,2] = line[2]
        output[cnt,3] = line[3]
        output[cnt,4] = line[4] 
        cnt+=1

    return output
