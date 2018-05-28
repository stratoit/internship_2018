import csv
import numpy as np
import cv2
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import matplotlib.image as mpimg
import PIL

df1 =  pd.read_csv('tesdata.csv',header=None)
col = df1[0]
row = df1.loc[1 , 1: ]
arr = np.array(row)
arr_new = arr.reshape(480,640)

#img = Image.fromarray(np.uint8(arr_new),'L')
#img = img.resize((128, 128), PIL.Image.ANTIALIAS)
#img.show()


