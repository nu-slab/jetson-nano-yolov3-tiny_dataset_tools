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

def img_resize_square_only_img(img):
    height,width = img.shape[:2]
    tmp = img[:, :]
    if(height > width):
        size = height
        limit = width
    else:
        size = width
        limit = height
    start = int((size - limit) / 2)
    fin = int((size + limit) / 2)
    new_img = cv2.resize(np.zeros((1, 1, 3), np.uint8), (size, size))
    if(size == height):
        new_img[:, start:fin] = tmp
    else:
        new_img[start:fin, :] = tmp

    return new_img
