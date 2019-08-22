#!/bin/env python3

'''Useful: https://realpython.com/working-with-files-in-python/'''

import re
import os
import shutil
import pandas as pd
from file_management import file_management as fm
from config import config as cg
import csv

path='/home/yobi/AbPackingAngle_V2.1/code'
path2flex='/home/yobi/AbPackingAngle_V2.1/code/flex_pdbs/'

class interface_residues:

    def find_aa_lightchain(pdb_file):

        residues=pdb_file[-10:]+'\n'

        f= open(pdb_file, 'r')
        raw_data = f.read().splitlines()
        count=0
        
        for index, words in enumerate(raw_data):

            if re.findall('L  43',words) and count==0:
                residues+=words[17:20]+'\n'
                count=1

            if re.findall('L  44',words) and count==1:
                residues+=words[17:20]+'\n'
                count=2


            if re.findall('L  45',words) and count==2:
                residues+=words[17:20]+'\n'
                count=3



            if re.findall('L  46',words) and count==3:
                residues+=words[17:20]+'\n'
                count=4



            if re.findall('L  96',words) and count==4:
                residues+=words[17:20]+'\n'
                count=5


            if re.findall('L  98',words) and count==5:
                residues+=words[17:20]+'\n'
                count=6

        return residues 


    def find_aa_heavychain(pdb_file):

        f= open(pdb_file, 'r')
        raw_data = f.read().splitlines()

        for index, words in enumerate(raw_data):


            if re.findall('H  44',words):
                print(words)


            if re.findall('H  45',words):
                print(words)


            if re.findall('H  46',words):
                print(words)

            if re.findall('H  47',words):
                print(words)

            if re.findall('H  101',words):
                print(words)

            if re.findall('H  105',words):
                print(words)


    def gen_light_chain_parser(file_list, flex_grade):

        f= open(file_list, 'r')
        raw_data = f.read().splitlines()

        print(flex_grade[:-1]+"=''")
        
        residue_parser=''
        
        for i in raw_data:
            residue_parser+=flex_grade[:-1]+' += ir.find_aa_lightchain(cg.path_2flexpdbs+'+"'"+flex_grade+"'+'"+i+"')\n"

        return residue_parser

print(interface_residues.gen_light_chain_parser(cg.path_2flexcode+'flex_grade1_list.txt','Grade_1/'))

print(interface_residues.gen_light_chain_parser(cg.path_2flexcode+'flex_grade2_list.txt','Grade_2/'))

print(interface_residues.gen_light_chain_parser(cg.path_2flexcode+'flex_grade3_list.txt','Grade_3/'))
            
