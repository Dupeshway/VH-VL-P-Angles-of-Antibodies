#!/usr/bin/env python
 
import csv
import sys
import pprint
import pandas as pd
import seaborn as sns
import scipy as sy
import matplotlib.pyplot as plt

import re
import os
import shutil
from clean_pdb import clean_pdb as cp
from file_management import file_management as fm
from config import config as cg
from Bio.PDB import *

class dfing_free_complex:
    
    sns.set(style="whitegrid", palette="muted")

    df= pd.read_csv('all_pdb_pangles.csv')

    #df = pd.melt(df, id_vars=['Time step (secs)'], value_vars=['inlet_temperature_sht15 (degc)','mosfet_temperature (degc)'])

    shape= df.shape
    head=df.head

    #dfx=df[['All_pdb_code','All_pdb_pangles']]
    df_all_pangles=df.set_index('All_pdb_code',drop=True) #purely by the index
    #print(df_all_pangles)

    free_all_groups=[]
    complex_all_groups=[]

    f=open('ready4df_pangle.txt')
    raw_data=f.read().splitlines()

    free_g1=df_all_pangles.loc[['1A6U_1']]
    complex_g1=df_all_pangles.loc[['1A6V_1','1A6V_2','1A6W_1']]
    free_g2=df_all_pangles.loc[['1CFQ_1']]
    complex_g2=df_all_pangles.loc[['1BOG_1','1CFN_1','1CFS_1','1CFT_1','1HH6_1','1HH9_1','1HI6_1']]
    free_g3=df_all_pangles.loc[['1DBA_1']]
    complex_g3=df_all_pangles.loc[['1DBB_1','1DBJ_1','1DBK_1','1DBM_1','2DBL_1']]
    free_g4=df_all_pangles.loc[['1DQM_1','1DQQ_1']]
    complex_g4=df_all_pangles.loc[['1DQJ_1','1NBY_1','1NBZ_1']]
    free_g5=df_all_pangles.loc[['1HZH_1']]
    complex_g5=df_all_pangles.loc[['1N0X_1','2NY7_1','3RU8_1','5VN8_1']]
    free_g6=df_all_pangles.loc[['1HIL_1']]
    complex_g6=df_all_pangles.loc[['1HIM_1','1HIN_1','1IFH_1']]
    free_g7=df_all_pangles.loc[['1MHH_1','1NLB_1','1YMH_1']]
    complex_g7=df_all_pangles.loc[['1MRD_1','1MRE_1','1MRF_1','1N64_1','1XCQ_1','1XCT_1','1XF5_1']]
    free_g8=df_all_pangles.loc[['1FVC_1','4HKZ_1','4UB0_1','5XHF_1','6BHZ_1','6BI0_1','6BI2_1']]
    complex_g8=df_all_pangles.loc[['1N8Z_1','5XHG_1','6OGE_2']]
    free_g9=df_all_pangles.loc[['1OAQ_1','1OAR_1']]
    complex_g9=df_all_pangles.loc[['1OAX_1','1OAY_1','1OAU_1','1OAZ_1']]
    free_g10=df_all_pangles.loc[['1P7K_1','1XF2_1','1XF3_1','1XF4_1']]
    complex_g10=df_all_pangles.loc[['1I8M_1','1P7K_2','1XF2_2','2FR4_1']]
    free_g11=df_all_pangles.loc[['1RFD_1']]
    complex_g11=df_all_pangles.loc[['1Q72_1','1QYG_1','1RIU_1','1RIV_1']]
    free_g12=df_all_pangles.loc[['1RZ8_1']]
    complex_g12=df_all_pangles.loc[['1RZJ_1','1RZK_1','1YYL_1','1YYM_1','2I5Y_1','2I60_1','2NXY_1','2NXZ_1','2NY0_1','2NY1_1','2NY2_1','2NY3_1','2NY4_1','2NY5_1','2NY6_1','4JM2_1','4RQS_1','5A7X_1','5A8H_1']]
    free_g13=df_all_pangles.loc[['1YY8_1','4GW1_1','4GW5_1','5ESQ_1','5ETU_1','5EUK_1','5F88_1','5FF6_1','5HPM_1','5HYQ_1','5I2I_1','5I76_1','5ICX_1','5ICY_1','5ICZ_1','5ID0_1','5ID1_1','5IOP_1','5IR1_1','5ITF_1','5IV2_1','5IVZ_1','5T1K_1','5T1L_1','5T1M_1','5TH2_1','6AU5_1','6AXP_1','6AYN_1','6AZK_1','6AZL_1']]
    complex_g13=df_all_pangles.loc[['1YY9_1','4KRO_1','4KRP_1']]
    free_g14=df_all_pangles.loc[['2AJU_1']]
    complex_g14=df_all_pangles.loc[['2AJS_1','2AJV_1','2AJX_1','2AJY_1','2AJZ_1','2AK1_1']]
    free_g15=df_all_pangles.loc[['1Q9K_1','1Q9L_1','2R1X_1']]
    complex_g15=df_all_pangles.loc[['2R1W_1','2R1Y_1','2R23_1','2R2B_1','2R2E_1','2R2H_1','3BPC_1','3SY0_1','3T4Y_1','3T65_1','3T77_1']]
    free_g16=df_all_pangles.loc[['3C5S_1']]
    complex_g16=df_all_pangles.loc[['3BZ4_1','3C6S_1','3GGW_1']]
    free_g17=df_all_pangles.loc[['3DUU_2']]
    complex_g17=df_all_pangles.loc[['3DUS_1','3DUU_1','3DV6_1']]
    free_g18=df_all_pangles.loc[['1MQK_1']]
    complex_g18=df_all_pangles.loc[['1AR1_1','1QLE_1','3EHB_1','3HB3_1']]
    free_g19=df_all_pangles.loc[['3IJH_1','3IJS_2','3IJY_1','3IKC_1']]
    complex_g19=df_all_pangles.loc[['3IJS_1']]
    free_g20=df_all_pangles.loc[['3OAZ_1','6E5P_1','6MNF_1','6N32_1']]
    complex_g20=df_all_pangles.loc[['2OQJ_1','3OAY_1','3OAZ_2','3OB0_1','4RBP_1','6CXG_1','6CXL_1','6MSY_1','6MU3_1','6MUB_1','6N2X_1','6N35_1']]
    free_g21=df_all_pangles.loc[['3OKD_1','3OKE_1','3OKM_1']]
    complex_g21=df_all_pangles.loc[['3OKK_1','3OKL_1','3OKN_1','3OKO_1']]
    free_g22=df_all_pangles.loc[['3M8O_1','3QNX_1','3QNY_1']]
    complex_g22=df_all_pangles.loc[['3QG6_1','3QG7_1','3QO0_1','3QO1_1']]
    free_g23=df_all_pangles.loc[['3QPQ_1']]
    complex_g23=df_all_pangles.loc[['3QPQ_2','3ULU_3','3ULV_3']]
    free_g24=df_all_pangles.loc[['3RVT_1','3RVU_1']]
    complex_g24=df_all_pangles.loc[['3RVV_1','3RVW_1','3RVX_1','5VPG_1','5VPH_1','5VPL_1']]
    free_g25=df_all_pangles.loc[['3TNN_2','3TNN_1']]
    complex_g25=df_all_pangles.loc[['4H8W_1','5W4L_1']]
    free_g26=df_all_pangles.loc[['6B3D_1']]
    complex_g26=df_all_pangles.loc[['3TV3_1','3TYG_1','5ACO_1','5C7K_1','5JS9_1','5JSA_1']]
    free_g27=df_all_pangles.loc[['3ULS_1']]
    complex_g27=df_all_pangles.loc[['3NA9_1','3ULU_1','3ULV_1']]
    free_g28=df_all_pangles.loc[['1RZ7_1']]
    complex_g28=df_all_pangles.loc[['3JWD_1','3JWO_1','4DVR_1']]
    free_g29=df_all_pangles.loc[['4FNL_2']]
    complex_g29=df_all_pangles.loc[['4F33_1','4F3F_1','4FNL_1','4FP8_1','4FQR_1','6ML8_1']]
    free_g30=df_all_pangles.loc[['4FQH_1','4NZT_1']]
    complex_g30=df_all_pangles.loc[['4FQI_1','4FQV_1','5CJQ_1','5CJS_1','6CNV_1']]
    free_g31=df_all_pangles.loc[['4HIE_1','4HIJ_1']]
    complex_g31=df_all_pangles.loc[['4HIH_2','4HII_1']]
    free_g32=df_all_pangles.loc[['4JDV_2']]
    complex_g32=df_all_pangles.loc[['4JAM_1','4JAN_1','4JDV_1']]
    free_g33=df_all_pangles.loc[['4LLV_1','4XBP_1','4XCC_1','4XCE_2','5CIP_1']]
    complex_g33=df_all_pangles.loc[['3EO0_1','3EO1_1','4KV5_1','4KXZ_1','1TZG_1','2FX7_1','2FX8_1','2FX9_1','4NGH_1','4NHC_1','4WY7_1','4XBG_1','4XC1_1','4XC3_1','4XCN_1','4XCY_1']]
    free_g34=df_all_pangles.loc[['4M6M_1','4M6N_1']]
    complex_g34=df_all_pangles.loc[['4M5Y_1','4M5Z_1']]
    free_g35=df_all_pangles.loc[['4M7Z_1','4M93_1','4MA1_1']]
    complex_g35=df_all_pangles.loc[['4MA1_3','4M7J_1']]
    free_g36=df_all_pangles.loc[['4OUU_1']]
    complex_g36=df_all_pangles.loc[['4P3C_1','4P3D_1','4QXU_1']]
    free_g37=df_all_pangles.loc[['4R26_1']]
    complex_g37=df_all_pangles.loc[['4R2G_1','5T3S_1','6IEQ_1']]
    free_g38=df_all_pangles.loc[['4RFE_1']]
    complex_g38=df_all_pangles.loc[['4R97_1','4R9Y_1','4RFN_1','5FCU_1']]
    free_g39=df_all_pangles.loc[['4TRP_1','4TUO_1']]
    complex_g39=df_all_pangles.loc[['4TPR_1','4TQE_1','4TUJ_1','4TUK_1','4TUL_1']]
    free_g40=df_all_pangles.loc[['4LLV_1','4XBP_1','4XCC_1','5CIP_1']]
    complex_g40=df_all_pangles.loc[['1TZG_1','2FX7_1','2FX8_1','2FX9_1','4NGH_1','4NHC_1','4WY7_1','4XBG_1','4XC1_1','4XC3_1','4XCN_1','4XCY_1']]
    free_g41=df_all_pangles.loc[['4XPB_1','4XPT_1']]
    complex_g41=df_all_pangles.loc[['4M48_1','4XNU_1','4XNX_1','4XP1_1','4XP4_1','4XP5_1','4XP6_1','4XP9_1','4XPA_1','4XPF_1','4XPG_1','4XPH_1']]
    free_g42=df_all_pangles.loc[['4YNY_1']]
    complex_g42=df_all_pangles.loc[['4YO0_1','6AL0_1','6AL1_1','6ICC_1','6ICF_1']]
    free_g43=df_all_pangles.loc[['4ODU_1','4Z95_1']]
    complex_g43=df_all_pangles.loc[['4ODT_1','4Z8F_1']]
    free_g44=df_all_pangles.loc[['5DK3_1']]
    complex_g44=df_all_pangles.loc[['5B8C_2','5GGS_1','5JXE_1']]
    free_g45=df_all_pangles.loc[['5EZI_1','5EZJ_1','5EZL_1']]
    complex_g45=df_all_pangles.loc[['5EZO_1']]
    free_g46=df_all_pangles.loc[['5H30_1','5H32_1']]
    complex_g46=df_all_pangles.loc[['4UT9_1','5H37_1']]
    free_g47=df_all_pangles.loc[['2XA8_1','4X7S_1','4X7T_1','5HYS_1']]
    complex_g47=df_all_pangles.loc[['5HYS_3','5HYS_4']]
    free_g48=df_all_pangles.loc[['5I8E_1']]
    complex_g48=df_all_pangles.loc[['5I8C_1','6ME1_1','6NC3_1']]
    free_g49=df_all_pangles.loc[['5JNY_1']]
    complex_g49=df_all_pangles.loc[['4G6F_1','4U6G_1','5GHW_1','5T6L_1','5T80_1','5T85_1']]
    free_g50=df_all_pangles.loc[['5K8A_1']]
    complex_g50=df_all_pangles.loc[['3IXT_1','3QWO_1','4ZYP_2','6OE5_1']]
    free_g51=df_all_pangles.loc[['4OZ4_1','5MP5_1','5MUQ_1','5MVJ_1','5MX3_1']]
    complex_g51=df_all_pangles.loc[['5MO3_1','5MP1_1','5MP3_1','5MP5_2','5MTH_1']]
    free_g52=df_all_pangles.loc[['5TLJ_2']]
    complex_g52=df_all_pangles.loc[['5OCY_1','5OD0_1','5TL5_1','5TLK_3']]
    free_g53=df_all_pangles.loc[['2A6D_1','2A6J_1','2A6K_1','5VGA_1']]
    complex_g53=df_all_pangles.loc[['2A6D_2','2A6I_1']]
    free_g54=df_all_pangles.loc[['5WTG_1']]
    complex_g54=df_all_pangles.loc[['5WK2_1','5WK3_1','5WTH_1']]
    free_g55=df_all_pangles.loc[['1FVC_1','4HKZ_1','4UB0_1','5XHF_1','6BHZ_1','6BI0_1','6BI2_1']]
    complex_g55=df_all_pangles.loc[['1N8Z_1','5XHG_1','6OGE_2']]
    free_g56=df_all_pangles.loc[['6AL4_1']]
    complex_g56=df_all_pangles.loc[['6A76_1','6A77_1','6A78_1','6AL5_1']]
    free_g57=df_all_pangles.loc[['6B3D_1']]
    complex_g57=df_all_pangles.loc[['3TV3_1','3TYG_1','5ACO_1','5C7K_1','5JS9_1','5JSA_1']]
    free_g58=df_all_pangles.loc[['6C6X_1']]
    complex_g58=df_all_pangles.loc[['6BLA_1','6C5V_1','6C6Y_1']]
    free_g59=df_all_pangles.loc[['3OAZ_1','6E5P_1','6MNF_1','6N32_1']]
    complex_g59=df_all_pangles.loc[['2OQJ_1','3OAY_1','3OAZ_2','3OB0_1','4RBP_1','6CXG_1','6CXL_1','6MNF_2','6MSY_1','6MU3_1','6MUB_1','6N2X_1','6N35_1']]
    free_g60=df_all_pangles.loc[['4NUG_1']]
    complex_g60=df_all_pangles.loc[['5FUU_1','6DCQ_1','6MAR_1']]
    free_g61=df_all_pangles.loc[['6D9G_1']]
    complex_g61=df_all_pangles.loc[['6DZV_1','6DZW_1','6DZY_1','6DZZ_1']]
    free_g62=df_all_pangles.loc[['6EA5_1','6EA7_1']]
    complex_g62=df_all_pangles.loc[['6DZL_1','6DZM_1','6EA5_2','6EA7_2']]
    free_g63=df_all_pangles.loc[['6GLW_1']]
    complex_g63=df_all_pangles.loc[['5JUE_1','6FN1_1','6FN4_1','6QEE_1','6QEX_1']]
    free_g64=df_all_pangles.loc[['4FNL_2']]
    complex_g64=df_all_pangles.loc[['4FNL_1','4FP8_1','4FQR_1','6ML8_1']]
    free_g65=df_all_pangles.loc[['3OAZ_1','6E5P_1','6MNF_1','6N32_1']]
    complex_g65=df_all_pangles.loc[['2OQJ_1','3OAY_1','3OAZ_2','3OB0_1','4RBP_1','6CXG_1','6CXL_1','6MNF_2','6MSY_1','6MU3_1','6MUB_1','6N2X_1','6N35_1']]
    free_g66=df_all_pangles.loc[['6NB6_1','6NB7_1','6NB8_1']]
    complex_g66=df_all_pangles.loc[['6NB6_2']]


    free_all_groups.append(free_g1)
    free_all_groups.append(free_g2)
    free_all_groups.append(free_g3)
    free_all_groups.append(free_g4)
    free_all_groups.append(free_g5)
    free_all_groups.append(free_g6)
    free_all_groups.append(free_g7)
    free_all_groups.append(free_g8)
    free_all_groups.append(free_g9)
    free_all_groups.append(free_g10)
    free_all_groups.append(free_g11)
    free_all_groups.append(free_g12)
    free_all_groups.append(free_g13)
    free_all_groups.append(free_g14)
    free_all_groups.append(free_g15)
    free_all_groups.append(free_g16)
    free_all_groups.append(free_g17)
    free_all_groups.append(free_g18)
    free_all_groups.append(free_g19)
    free_all_groups.append(free_g20)
    free_all_groups.append(free_g21)
    free_all_groups.append(free_g22)
    free_all_groups.append(free_g23)
    free_all_groups.append(free_g24)
    free_all_groups.append(free_g25)
    free_all_groups.append(free_g26)
    free_all_groups.append(free_g27)
    free_all_groups.append(free_g28)
    free_all_groups.append(free_g29)
    free_all_groups.append(free_g30)
    free_all_groups.append(free_g31)
    free_all_groups.append(free_g32)
    free_all_groups.append(free_g33)
    free_all_groups.append(free_g34)
    free_all_groups.append(free_g35)
    free_all_groups.append(free_g36)
    free_all_groups.append(free_g37)
    free_all_groups.append(free_g38)
    free_all_groups.append(free_g39)
    free_all_groups.append(free_g40)
    free_all_groups.append(free_g41)
    free_all_groups.append(free_g42)
    free_all_groups.append(free_g43)
    free_all_groups.append(free_g44)
    free_all_groups.append(free_g45)
    free_all_groups.append(free_g46)
    free_all_groups.append(free_g47)
    free_all_groups.append(free_g48)
    free_all_groups.append(free_g49)
    free_all_groups.append(free_g50)
    free_all_groups.append(free_g51)
    free_all_groups.append(free_g52)
    free_all_groups.append(free_g53)
    free_all_groups.append(free_g54)
    free_all_groups.append(free_g55)
    free_all_groups.append(free_g56)
    free_all_groups.append(free_g57)
    free_all_groups.append(free_g58)
    free_all_groups.append(free_g59)
    free_all_groups.append(free_g60)
    free_all_groups.append(free_g61)
    free_all_groups.append(free_g62)
    free_all_groups.append(free_g63)
    free_all_groups.append(free_g64)
    free_all_groups.append(free_g65)
    free_all_groups.append(free_g66)

    complex_all_groups.append(complex_g1)
    complex_all_groups.append(complex_g2)
    complex_all_groups.append(complex_g3)
    complex_all_groups.append(complex_g4)
    complex_all_groups.append(complex_g5)
    complex_all_groups.append(complex_g6)
    complex_all_groups.append(complex_g7)
    complex_all_groups.append(complex_g8)
    complex_all_groups.append(complex_g9)
    complex_all_groups.append(complex_g10)
    complex_all_groups.append(complex_g11)
    complex_all_groups.append(complex_g12)
    complex_all_groups.append(complex_g13)
    complex_all_groups.append(complex_g14)
    complex_all_groups.append(complex_g15)
    complex_all_groups.append(complex_g16)
    complex_all_groups.append(complex_g17)
    complex_all_groups.append(complex_g18)
    complex_all_groups.append(complex_g19)
    complex_all_groups.append(complex_g20)
    complex_all_groups.append(complex_g21)
    complex_all_groups.append(complex_g22)
    complex_all_groups.append(complex_g23)
    complex_all_groups.append(complex_g24)
    complex_all_groups.append(complex_g25)
    complex_all_groups.append(complex_g26)
    complex_all_groups.append(complex_g27)
    complex_all_groups.append(complex_g28)
    complex_all_groups.append(complex_g29)
    complex_all_groups.append(complex_g30)
    complex_all_groups.append(complex_g31)
    complex_all_groups.append(complex_g32)
    complex_all_groups.append(complex_g33)
    complex_all_groups.append(complex_g34)
    complex_all_groups.append(complex_g35)
    complex_all_groups.append(complex_g36)
    complex_all_groups.append(complex_g37)
    complex_all_groups.append(complex_g38)
    complex_all_groups.append(complex_g39)
    complex_all_groups.append(complex_g40)
    complex_all_groups.append(complex_g41)
    complex_all_groups.append(complex_g42)
    complex_all_groups.append(complex_g43)
    complex_all_groups.append(complex_g44)
    complex_all_groups.append(complex_g45)
    complex_all_groups.append(complex_g46)
    complex_all_groups.append(complex_g47)
    complex_all_groups.append(complex_g48)
    complex_all_groups.append(complex_g49)
    complex_all_groups.append(complex_g50)
    complex_all_groups.append(complex_g51)
    complex_all_groups.append(complex_g52)
    complex_all_groups.append(complex_g53)
    complex_all_groups.append(complex_g54)
    complex_all_groups.append(complex_g55)
    complex_all_groups.append(complex_g56)
    complex_all_groups.append(complex_g57)
    complex_all_groups.append(complex_g58)
    complex_all_groups.append(complex_g59)
    complex_all_groups.append(complex_g60)
    complex_all_groups.append(complex_g61)
    complex_all_groups.append(complex_g62)
    complex_all_groups.append(complex_g63)
    complex_all_groups.append(complex_g64)
    complex_all_groups.append(complex_g65)
    complex_all_groups.append(complex_g66)
