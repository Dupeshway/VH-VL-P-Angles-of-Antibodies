#!/usr/bin/env python
 
import csv
import sys
import pprint
import pandas as pd
import seaborn as sns


import re
import os
import shutil
from clean_pdb import clean_pdb as cp
from config import config as cg
from Bio.PDB import *


        with open(csv_file, 'w') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow((raw_data,'\n'))
            
        print('Data written to:', csv_file) #perhaps preferable to leave this?

f = open('/home/yobi/AbPackingAngle_V2.1/complex_pangles.txt', 'r')
raw_data = f.read().splitlines(),'\n'


w = open('full_prangle_list.csv', 'a+')
w.truncate(0)
for i in raw_data:

    (i)






"""
#1)create a function that only collects redundancies without copies, i.e only _1, no _2,_3 etc

#2)Next up: create a function that can take a text file and output in this format:
# df.ix['1MCO_1', 'Packing angle']

#3)also, clean the PDB codes that have ':' at the end i.e 1Q1J_1:    -57.877257

#4) get rid of outliers? like 5GZr_1/_2 or investigate them further? FURTHER


df=cp.csv_2df('all_pdbs.csv')

print(df.ix['1MCO_1', 'Packing angle']) #HOLY GRAIL!!!! choose by index and column
"""
