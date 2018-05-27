import csv
import numpy as np
import cv2
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image

df1 =  pd.read_csv('tesdata.csv',header=None)
col = df1[0]
row = df1.loc[0 , 1: ]
arr = np.array(row)
arr_new = arr.reshape(480,640)
img = Image.fromarray(np.uint8(arr_new),'L' )
img.show()

