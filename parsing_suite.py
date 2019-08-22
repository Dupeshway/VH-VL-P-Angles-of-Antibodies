#!/bin/env python3

#List directories:

'''Useful: https://realpython.com/working-with-files-in-python/'''

import re
import os
import shutil
from config import config as cg
#from df_pangles import dfing_free_complex as dfc
from clean_pdb import clean_pdb as cp
from residue_extract import interface_residues as ir
from file_management import file_management as fm
import csv


pdbpath='/home/yobi/AbPackingAngle_V2.1/LH_Combined_Martin/'

"""
#Generating dataset of packing angles
#=================================

#writes list of files in directory to given txt file
w = open('pdb_list.txt', 'a+')
w.truncate(0)
fm.write_list(cp.list_directory(pdbpath), 'pdb_list.txt')



#reads list of pdb files within text file and extracts listed pdbs from folder
w = open('bash_Script_2extract_flex_pdbs.txt', 'a+')
w.truncate(0)
#This should appear later as well
fm.write_list(cp.write2_bash('flex_pdb_list.txt'), 'bash_Script_2extract_flex_pdbs.txt')



#write the list to a bash executable,
w = open('bash_prangle_list.txt', 'a+')
w.truncate(0)
fm.write_list(cp.bash4_pack('pdb_list.txt'),'bash_prangle_list.txt')


#Simply open text file, clean(garbled lines, approx 50)
#and write to a csvfile (works for Libre calc)
w = open('full_prangle_list.csv', 'a+')
w.truncate(0)
cp.prangleclean4_csv('/home/yobi/AbPackingAngle_V2.1/complex_pangles.txt','full_prangle_list.csv')


#convert txt file pdb to have commas for input to R and stat analysis
#copy csv pangle column to text file and add commas
w = open('noredund_commas4R.txt', 'a+')
w.truncate(0)
fm.write_list(cp.add_commas('noredund_nocomma.txt'),'noredund_commas4R.txt')


#Generate dataset for Complexed: 1) seperate list, 2)use list in bash4pack 3)run abpangle

cp.clean4pdb_extraction('list_all_complex.txt','list_all_complexed_4extract.txt')

#Generate dataset for Free: 1) 2) 3)

cp.clean4pdb_extraction('list_all_free.txt','list_all_free_4extract.txt')


#Turn the 4extract.txt files into bash Abangle executable script
    #free pdbs
w = open('free_4bash.txt', 'a+')
w.truncate(0)
fm.write_list(cp.bash4_pack('list_all_free_4extract.txt','free_pangles.txt'),'free_4bash.txt')

    #complexed pdbs
w = open('complex_4bash.txt', 'a+')
w.truncate(0)
fm.write_list(cp.bash4_pack('list_all_complexed_4extract.txt', 'complex_pangles.txt'),'complex_4bash.txt')



#convert txt file pdb to have commas for input to R and stat analysis
#copy csv pangle column to text file and add commas
w = open('free_commas4R.txt', 'a+')
w.truncate(0)
fm.write_list(cp.add_commas('free_nocommas.txt'),'free_commas4R.txt')

w = open('complex_commas4R.txt', 'a+')
w.truncate(0)
fm.write_list(cp.add_commas('complex_nocommas.txt'),'complex_commas4R.txt')




#converts all plain pdbs into '','' and identifies 5+ pdbs per line
w=open('fiveplus_pdbs.txt', 'a+')
w.truncate(0)

fm.write_list(cp.apost_commas_4pdbs('list_all_freevscomplex.txt'), 'fiveplus_pdbs.txt')




#Stage 1: Replace comma duplicates with singles
w=open('fiveplus_pdbs_s1.txt', 'a+')
w.truncate(0)
fm.write_list(cp.replace_commas_withcomma('fiveplus_pdbs.txt'), 'fiveplus_pdbs_s1.txt')


#Stage 2: Remove comma that appears at the end of some lines
w=open('fiveplus_pdbs_s2.txt', 'a+')
w.truncate(0)
fm.write_list(cp.remove_commas_end('fiveplus_pdbs.txt'), 'fiveplus_pdbs_s2.txt')

#stage 3: add apostraphes around commas
w=open('fiveplus_pdbs_s3.txt', 'a+')
w.truncate(0)
fm.write_list(cp.apost_aroundcommas('fiveplus_pdbs_s1.txt'), 'fiveplus_pdbs_s3.txt')

#Stage 4: homogenise " into '
w=open('fiveplus_pdbs_s4.txt', 'a+')
w.truncate(0)
fm.write_list(cp.same_apostraphes('fiveplus_pdbs_s3.txt'), 'fiveplus_pdbs_s4.txt')

#Stage 5: Format for pandas dataframe
w=open('fiveplus_pdbs_s5.txt', 'a+')
w.truncate(0)
fm.write_list(cp.split_semicolon_4pdbs('fiveplus_pdbs_s4.txt'), 'fiveplus_pdbs_s5.txt')

#Stage 6: homogenise " into '
w=open('ready4df_pangle.txt', 'a+')
w.truncate(0)
fm.write_list(cp.alternate_input_4df('fiveplus_pdbs_s5.txt'), 'ready4df_pangle.txt')


#free_g1=df_all_pangles.loc[['1MHH_1','1NLB_1','1YMH_1']]


#Creating groups of pdbs and extracting pangles from dataframe
w=open('extracted_group_pangles.txt', 'a+')

free_g=''
complex_g=''
group_no=0


#for index, words in enumerate(dfc.free_all_groups):

 #   group_no+=1
  #  print('fg_',str(group_no),'<-c(',words,')')
    
for index, words in enumerate(dfc.complex_all_groups):
    print('cg_',str(index+1),'<-c(',words,')\n')

#convert txt file pdb to have commas for input to R and stat analysis
#copy csv pangle column to text file and add commas
w = open('free_commas4R.txt', 'a+')
w.truncate(0)
fm.write_list(cp.add_commas('free_nocommas.txt'),'free_commas4R.txt')


w = open('noredund_complex_commas4R.txt', 'a+')
w.truncate(0)
fm.write_list(cp.add_commas('nonredund_complex_nocommas.txt'),'nonredund_complex_commas4R.txt')



#Generate dataframe from all pdb(?)
#================================

df=fm.csv_2df('all_pdbs.csv') #creates dataframe of all pdbs

#gen_4r.all_pangle_groupjoin()

#gen_4r.range_gen4_allgroups()
#gen_4r.mean_gen4_allgroups()
#gen_4r.sd_gen4_allgroups()

#gen_4r.sd_gen4_freegroups()
#gen_4r.sd_gen4_complexgroups()
#gen_4r.mean_gen4_freegroups()
#gen_4r.mean_gen4_complexgroups()

#gen_4r.range_gen4_complexgroups()
#gen_4r.range_gen4_freegroups()


#Extracting PDBs by Flexibility grade(list in textfile)
#=============================================
#Reads list of pdb files within text file and extracts listed pdbs from folder

#provides bash script for extracting pdbs linked to Grade 1 flexibility
w = open('flex_code/bash_flex_g1_pdbs.txt', 'a+')
w.truncate(0)
fm.write_list(cp.write2_bash('flex_code/flex_grade1_list.txt', 'Grade_1'), 'flex_code/bash_flex_g1_pdbs.txt')

#provides bash script for extracting pdbs linked to Grade 2 flexibility
w = open('bash_flex_g2_pdbs.txt', 'a+')
w.truncate(0)
fm.write_list(cp.write2_bash('flex_code/flex_grade2_list.txt', 'Grade_2'), 'flex_code/bash_flex_g2_pdbs.txt')

#provides bash script for extracting pdbs linked to Grade 3 flexibility
w = open('bash_flex_g3_pdbs.txt', 'a+')
w.truncate(0)
fm.write_list(cp.write2_bash('flex_code/flex_grade3_list.txt', 'Grade_3'), 'flex_code/bash_flex_g3_pdbs.txt')

#Now copy these into a bash script

"""

#Extracting Residues
#=======================

#Grade 1 extraction
#==================
w = open(cg.path_2flexcode+'grade1_residues.txt', 'a+')
w.truncate(0)

Grade_1=''
Grade_1 += ir.find_aa_lightchain(cg.path_2flexpdbs+'Grade_1/'+'4M6M_1.pdb')
Grade_1 += ir.find_aa_lightchain(cg.path_2flexpdbs+'Grade_1/'+'4M6N_1.pdb')
Grade_1 += ir.find_aa_lightchain(cg.path_2flexpdbs+'Grade_1/'+'4M5Y_1.pdb')
Grade_1 += ir.find_aa_lightchain(cg.path_2flexpdbs+'Grade_1/'+'4M5Z_1.pdb')
Grade_1 += ir.find_aa_lightchain(cg.path_2flexpdbs+'Grade_1/'+'4NUG_1.pdb')
Grade_1 += ir.find_aa_lightchain(cg.path_2flexpdbs+'Grade_1/'+'5FUU_1.pdb')
Grade_1 += ir.find_aa_lightchain(cg.path_2flexpdbs+'Grade_1/'+'6DCQ_1.pdb')
Grade_1 += ir.find_aa_lightchain(cg.path_2flexpdbs+'Grade_1/'+'6MAR_1.pdb')
Grade_1 += ir.find_aa_lightchain(cg.path_2flexpdbs+'Grade_1/'+'5WTG_1.pdb')
Grade_1 += ir.find_aa_lightchain(cg.path_2flexpdbs+'Grade_1/'+'5WK2_1.pdb')
Grade_1 += ir.find_aa_lightchain(cg.path_2flexpdbs+'Grade_1/'+'5WK3_1.pdb')
Grade_1 += ir.find_aa_lightchain(cg.path_2flexpdbs+'Grade_1/'+'5WTH_1.pdb')

print(Grade_1)

fm.write_list(Grade_1 ,cg.path_2flexcode+'grade1_residues.txt')

#Grade 2 extraction
#==================
w = open(cg.path_2flexcode+'grade2_residues.txt', 'a+')
w.truncate(0)

Grade_2=''
Grade_2 += ir.find_aa_lightchain(cg.path_2flexpdbs+'Grade_2/'+'4JDV_2.pdb')
Grade_2 += ir.find_aa_lightchain(cg.path_2flexpdbs+'Grade_2/'+'4JAM_1.pdb')
Grade_2 += ir.find_aa_lightchain(cg.path_2flexpdbs+'Grade_2/'+'4JAN_1.pdb')
Grade_2 += ir.find_aa_lightchain(cg.path_2flexpdbs+'Grade_2/'+'4JDV_1.pdb')
Grade_2 += ir.find_aa_lightchain(cg.path_2flexpdbs+'Grade_2/'+'4RFE_1.pdb')
Grade_2 += ir.find_aa_lightchain(cg.path_2flexpdbs+'Grade_2/'+'4R97_1.pdb')
Grade_2 += ir.find_aa_lightchain(cg.path_2flexpdbs+'Grade_2/'+'4R9Y_1.pdb')
Grade_2 += ir.find_aa_lightchain(cg.path_2flexpdbs+'Grade_2/'+'4RFN_1.pdb')
Grade_2 += ir.find_aa_lightchain(cg.path_2flexpdbs+'Grade_2/'+'5FCU_1.pdb')
Grade_2 += ir.find_aa_lightchain(cg.path_2flexpdbs+'Grade_2/'+'6EA5_1.pdb')
Grade_2 += ir.find_aa_lightchain(cg.path_2flexpdbs+'Grade_2/'+'6EA7_1.pdb')
Grade_2 += ir.find_aa_lightchain(cg.path_2flexpdbs+'Grade_2/'+'6DZL_1.pdb')
Grade_2 += ir.find_aa_lightchain(cg.path_2flexpdbs+'Grade_2/'+'6DZM_1.pdb')
Grade_2 += ir.find_aa_lightchain(cg.path_2flexpdbs+'Grade_2/'+'6EA5_2.pdb')
Grade_2 += ir.find_aa_lightchain(cg.path_2flexpdbs+'Grade_2/'+'6EA7_2.pdb')
Grade_2 += ir.find_aa_lightchain(cg.path_2flexpdbs+'Grade_2/'+'5H30_1.pdb')
Grade_2 += ir.find_aa_lightchain(cg.path_2flexpdbs+'Grade_2/'+'5H32_1.pdb')
Grade_2 += ir.find_aa_lightchain(cg.path_2flexpdbs+'Grade_2/'+'4UT9_1.pdb')
Grade_2 += ir.find_aa_lightchain(cg.path_2flexpdbs+'Grade_2/'+'5H37_1.pdb')
Grade_2 += ir.find_aa_lightchain(cg.path_2flexpdbs+'Grade_2/'+'4M7Z_1.pdb')
Grade_2 += ir.find_aa_lightchain(cg.path_2flexpdbs+'Grade_2/'+'4M93_1.pdb')
Grade_2 += ir.find_aa_lightchain(cg.path_2flexpdbs+'Grade_2/'+'4MA1_1.pdb')
Grade_2 += ir.find_aa_lightchain(cg.path_2flexpdbs+'Grade_2/'+'4MA1_3.pdb')
Grade_2 += ir.find_aa_lightchain(cg.path_2flexpdbs+'Grade_2/'+'4M7J_1.pdb')

print(Grade_2)

fm.write_list(Grade_2 ,cg.path_2flexcode+'grade2_residues.txt')


#Grade 3 extraction
#==================
w = open(cg.path_2flexcode+'grade3_residues.txt', 'a+')
w.truncate(0)

Grade_3=''
Grade_3 += ir.find_aa_lightchain(cg.path_2flexpdbs+'Grade_3/'+'6AL4_1.pdb')
Grade_3 += ir.find_aa_lightchain(cg.path_2flexpdbs+'Grade_3/'+'6A76_1.pdb')
Grade_3 += ir.find_aa_lightchain(cg.path_2flexpdbs+'Grade_3/'+'6A77_1.pdb')
Grade_3 += ir.find_aa_lightchain(cg.path_2flexpdbs+'Grade_3/'+'6A78_1.pdb')
Grade_3 += ir.find_aa_lightchain(cg.path_2flexpdbs+'Grade_3/'+'6AL5_1.pdb')
Grade_3 += ir.find_aa_lightchain(cg.path_2flexpdbs+'Grade_3/'+'1MQK_1.pdb')
Grade_3 += ir.find_aa_lightchain(cg.path_2flexpdbs+'Grade_3/'+'1AR1_1.pdb')
Grade_3 += ir.find_aa_lightchain(cg.path_2flexpdbs+'Grade_3/'+'1QLE_1.pdb')
Grade_3 += ir.find_aa_lightchain(cg.path_2flexpdbs+'Grade_3/'+'3EHB_1.pdb')
Grade_3 += ir.find_aa_lightchain(cg.path_2flexpdbs+'Grade_3/'+'3HB3_1.pdb')
Grade_3 += ir.find_aa_lightchain(cg.path_2flexpdbs+'Grade_3/'+'4R26_1.pdb')
Grade_3 += ir.find_aa_lightchain(cg.path_2flexpdbs+'Grade_3/'+'4R2G_1.pdb')
Grade_3 += ir.find_aa_lightchain(cg.path_2flexpdbs+'Grade_3/'+'5T3S_1.pdb')
Grade_3 += ir.find_aa_lightchain(cg.path_2flexpdbs+'Grade_3/'+'6IEQ_1.pdb')
Grade_3 += ir.find_aa_lightchain(cg.path_2flexpdbs+'Grade_3/'+'1CFQ_1.pdb')
Grade_3 += ir.find_aa_lightchain(cg.path_2flexpdbs+'Grade_3/'+'1BOG_1.pdb')
Grade_3 += ir.find_aa_lightchain(cg.path_2flexpdbs+'Grade_3/'+'1CFN_1.pdb')
Grade_3 += ir.find_aa_lightchain(cg.path_2flexpdbs+'Grade_3/'+'1CFS_1.pdb')
Grade_3 += ir.find_aa_lightchain(cg.path_2flexpdbs+'Grade_3/'+'1CFT_1.pdb')
Grade_3 += ir.find_aa_lightchain(cg.path_2flexpdbs+'Grade_3/'+'1HH6_1.pdb')
Grade_3 += ir.find_aa_lightchain(cg.path_2flexpdbs+'Grade_3/'+'1HH9_1.pdb')
Grade_3 += ir.find_aa_lightchain(cg.path_2flexpdbs+'Grade_3/'+'1HI6_1.pdb')


print(Grade_3)

fm.write_list(Grade_3 ,cg.path_2flexcode+'grade3_residues.txt')


"""

#Extras
#=========

cp.add_commas('complex_commas.txt','complexAb_commas.txt')

cp.chain_extractor('raw_complexed.txt')
w=open('Redundant_over2.txt','w')
w.truncate(0)
w.write(workshop.redund_over2(cg.redundant_pdbs))

cp.bash4_pack(cg.complex_list, cg.complex_pangle)

cp.chain_extractor('raw_complexed.txt')

cp.bash4_pack(cg.allpdbs)

clean_pdb.write2_csv(cg.complx_file)

clean_pdb.write2_bash()
"""
