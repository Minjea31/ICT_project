from ultralytics import YOLO
from ultralytics.engine.results import BaseTensor
from ultralytics.engine.results import Keypoints
from percent import *
from edge import *
import torch
import numpy as np
import serial
import time
import cv2


model = YOLO('yolov8m-pose.pt')
results = model.predict(data='coco-pose.yaml', source="2", show=True, conf=0.3, stream=True)

class Keypoints(BaseTensor):
    def __init__(self, keypoints, orig_shape) -> None:
        if keypoints.ndim == 2:
            keypoints = keypoints[None, :]
        if keypoints.shape[2] == 3:  
            mask = keypoints[..., 2] < 0.5  
            keypoints[..., :2][mask] = 0
        super().__init__(keypoints, orig_shape)
        self.has_visible = self.data.shape[-1] == 3

    def xy(self):
        return self.data[..., :2]

    def xyn(self):
        xy = self.xy.clone() if isinstance(self.xy, torch.Tensor) else np.copy(self.xy)
        xy[..., 0] /= self.orig_shape[1]
        xy[..., 1] /= self.orig_shape[0]
        return xy

    def conf(self):
        return self.data[..., 2] if self.has_visible else None
    
circle_keypoints = [[0.49139280125195617, 0.06930693069306931], [0.5039123630672926, 0.16006600660066006], 
             [0.06103286384976526, 0.14521452145214522], [0.26134585289514867, 0.1716171617161716], 
             [0.3974960876369327, 0.19306930693069307], [0.6071987480438185, 0.20297029702970298], 
             [0.7496087636932708, 0.2079207920792079], [0.94679186228482, 0.20957095709570958], 
             [0.4303599374021909, 0.4834983498349835], [0.622848200312989, 0.4900990099009901], 
             [0.2566510172143975, 0.6666666666666666], [0.24882629107981222, 0.9587458745874587], 
             [0.7183098591549296, 0.731023102310231], [0.8763693270735524, 0.9653465346534653]]

def get_keypoints(results):
    for result in results:
        if result.keypoints:
            keypoints = result.keypoints.xyn
            if len(keypoints[0]) > 0:  
                x0, y0 = keypoints[0][0].tolist()[:2]
                x1, y1 = keypoints[0][1].tolist()[:2]
                x2, y2 = keypoints[0][2].tolist()[:2]
                x3, y3 = keypoints[0][3].tolist()[:2]
                x4, y4 = keypoints[0][4].tolist()[:2]
                x5, y5 = keypoints[0][5].tolist()[:2]
                x6, y6 = keypoints[0][6].tolist()[:2]
                x7, y7 = keypoints[0][7].tolist()[:2]
                x8, y8 = keypoints[0][8].tolist()[:2]
                x9, y9 = keypoints[0][9].tolist()[:2]
                x10, y10 = keypoints[0][10].tolist()[:2]
                x11, y11 = keypoints[0][11].tolist()[:2]
                x12, y12 = keypoints[0][12].tolist()[:2]
                x13, y13 = keypoints[0][13].tolist()[:2]
                x14, y14 = keypoints[0][14].tolist()[:2]
                x15, y15 = keypoints[0][15].tolist()[:2]  
                x16, y16 = keypoints[0][16].tolist()[:2]  

                n0, m0 = circle_keypoints[0][0], circle_keypoints[0][1]
                n1, m2 = circle_keypoints[1][1], circle_keypoints[0][1]
                n2, m2 = circle_keypoints[2][1], circle_keypoints[0][1]
                n3, m3 = circle_keypoints[3][1], circle_keypoints[0][1]
                n4, m4 = circle_keypoints[4][1], circle_keypoints[0][1]
                n5, m5 = circle_keypoints[5][1], circle_keypoints[0][1]
                n6, m6 = circle_keypoints[6][1], circle_keypoints[0][1]
                n7, m7 = circle_keypoints[7][1], circle_keypoints[0][1]
                n8, m8 = circle_keypoints[8][1], circle_keypoints[0][1]
                n9, m9 = circle_keypoints[9][1], circle_keypoints[0][1]
                n10, m10 = circle_keypoints[10][1], circle_keypoints[0][1]
                n11, m11 = circle_keypoints[11][1], circle_keypoints[0][1]
                n12, m12 = circle_keypoints[12][1], circle_keypoints[0][1]
                n13, m13 = circle_keypoints[13][1], circle_keypoints[0][1]


                test1 = abs(x0 - n0)
                test2 = abs(y0 - m0)
                value = test1 + test2


                serial_port='/dev/ttyACM0'
                ser=serial.Serial(serial_port,9600,timeout=1)
                number = value
                ser.write(bytes(str(value), 'utf-8'))
                ser.close()
                
                print(value)
                return value                


result_keypoints = get_keypoints(results)
