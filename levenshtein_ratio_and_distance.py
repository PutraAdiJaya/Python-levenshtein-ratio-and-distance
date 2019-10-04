
import shutil
import re

import numpy as np
  
#LEVENSTAIN
def levenshtein_ratio_and_distance(s, t ):

    # INI MATRIK KOSONG
    rows = len(s)+1
    cols = len(t)+1
    distance = np.zeros((rows,cols),dtype = int)
    #JARAK
    for i in range(1, rows):
        for k in range(1,cols):
            distance[i][0] = i
            distance[0][k] = k

    #PROSE SEMUA HURUF
    for col in range(1, cols):
        for row in range(1, rows):
            if s[row-1] == t[col-1]:
                cost = 0 #KARAKTER SAMA
            else:
                cost = 2 #KARAKTER BEDA
            distance[row][col] = min(distance[row-1][col] + 1,      # DELETE
                                 distance[row][col-1] + 1,          # INSERT
                                 distance[row-1][col-1] + cost)     # DITAMBAHKAN

    # HITUNG JARAK TOTALS
    Ratio = ((len(s)+len(t)) - distance[row][col]) / (len(s)+len(t))
    return  Ratio
 
