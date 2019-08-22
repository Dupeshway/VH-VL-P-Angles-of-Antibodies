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
from clean_pdb import interface_residues as ir
from file_management import file_management as fm
from config import config as cg
from Bio.PDB import *


sns.set(style="whitegrid", palette="muted")

df= pd.read_csv('dataframe_all_groups.csv')

#df = pd.melt(df, id_vars=['Time step (secs)'], value_vars=['inlet_temperature_sht15 (degc)','mosfet_temperature (degc)'])

df_index=df.set_index('all_ab_groups',drop=True) #purely by the index

no_groups= df.all_ab_groups.rename('Each Ab with redund. structures')

#Redundancy count of All, Free, Complex
all_redund_count      =df.all_redund_count.rename('All Redundancies Count')
free_redund_count     =df.free_redund_count.rename('Free Redundancies Count')
complex_redund_count  =df.complex_redund_count.rename('Complex Redundancies Count')

#Mean of All, Free, Complex
mean_all          = df.mean_all_groups.rename('Mean of All Ab sets')
mean_free         = df.mean_free_groups.rename('Mean of Free sets')
mean_complex      = df.mean_complex_groups.rename('Mean of Complex sets')
median_all        = df.all_median.rename('Median of Each Abs')

#Range of All, Free, Complex
range_all         = df.range_all_groups.rename('Range All sets')
range_all_10plus  = df.range_redund_10plus.rename('Range All sets (10+ Redud.')

range_free        = df.range_free_groups.rename('Range Free sets')
range_free_btstrp = df.range_free_btstrp.rename('Range Free sets (Bt-strpd)')
range_free_nan    = df.range_free_nan.rename('Range Free sets (NaNs)')


range_complex     = df.range_complex_groups.rename('Range Complex Sets')
range_complex_btstrp = df.range_complex_btstrp.rename('Range Complex Sets (Bt-strpd)')
range_complex_nan = df.range_complex_nan.rename('Range Complex Sets (NaNs)')

#SD of All, Free, Complex
sd_all            = df.sd_all_groups.rename('SD All Sets')
sd_all_10plus     = df.sd_redund_10plus.rename('SD All Sets (10+ Redud.')

sd_free           = df.sd_free_groups.rename('SD Free Sets')
sd_free_btstrp    = df.sd_free_btstrp.rename('SD Free Sets (Bt-strpd)')
sd_free_nan       = df.sd_free_nan.rename('SD Free Sets (NaNs)')

sd_complex        = df.sd_complex_groups.rename('SD Complex Sets')
sd_complex_btstrp = df.sd_complex_btstrp.rename('SD Complex Sets (Bt-strpd)')
sd_complex_nan    = df.sd_complex_nan.rename('SD Complex Sets (NaNs)')

#create range vs sd df
#data_sd_range   = [[range_all, sd_all]]
#df_sd_range     = pd.DataFrame(data_sd_range)

print(median_all)

"""
#Mean density plot (all 3 in 1)
#=============================

sns.distplot(mean_all, bins=15)
#sns.kdeplot(mean_free)
#sns.kdeplot(mean_complex)

plt.title('Density of Means for All Antibody groups')
plt.legend(loc='upper left')

plt.xlabel('Mean in degrees')
plt.ylabel('Density')
plt.show()

#Mean Scatter plot
#=================

sns.jointplot(mean_free, mean_complex, kind="reg", space=0, color='purple')

#plt.title('Scatter of Means for Antibody groups')
#plt.legend(loc='upper left')


#plt.xlabel('Mean in degrees')
#plt.ylabel('Density')
plt.show()



#Mean across redundancy numbers:
#==============================

sns.jointplot(all_redund_count, mean_all, kind="reg", space=0, color='blue')
sns.jointplot(free_redund_count, mean_free, kind="reg", space=0, color='g')
sns.jointplot(complex_redund_count, mean_complex, kind="reg", space=0, color='r')


plt.title('Scatter of Means for Antibody groups')
plt.legend(loc='lower left')


#plt.xlabel('Mean in degrees')
#plt.ylabel('Density')
plt.show()

"""

#Median plot
#==========

sns.kdeplot(no_groups, median_all)
plt.show()



"""

#Range density plot (all +4 in 10+)
#==============================

sns.distplot(range_all, bins=7, label='All 4+ Redundancies')
sns.distplot(range_all_10plus, bins=7, label='All 10+ Redundancies', color='violet')


plt.title('Density of Range for All Antibody groups')
plt.legend(loc='upper right')

plt.xlabel('Range in degrees')
plt.ylabel('Density')
plt.show()


#Range density plot (all 3 in 1)
#==============================

#sns.kdeplot(range_all, bins=30, shade=True)
#sns.kdeplot(range_free_nan, shade=True)
#sns.kdeplot(range_complex_nan, shade=True)

sns.distplot(range_all, hist=False, bins=10, label='All')
sns.distplot(range_free_nan, bins=7, label='Free (Bt-strped)')
sns.distplot(range_complex_nan, bins=7, label='Complex (Bt-strped)')

plt.title('Density of Range for All Antibody groups')
plt.legend(loc='upper right')

plt.xlabel('Range in degrees')
plt.ylabel('Density')
plt.show()



#Range against redund count (all 3 in 1)
#==============================

sns.jointplot(all_redund_count, range_all, kind="reg", space=0, color='blue')
sns.jointplot(free_redund_count, range_free, kind="reg", space=0, color='g')
sns.jointplot(complex_redund_count, range_complex, kind="reg", space=0, color='r')

plt.show()

"""

#SD of Density plot(all 3 in 1)
#===============================


#sns.kdeplot(sd_all)
#sns.distplot(sd_all, label='All 4+ Redundancies')
#sns.distplot(sd_all_10plus, label='All 10+ Redundancies', color='violet')


sns.jointplot(range_free_nan, sd_free_nan, kind='reg', dropna=True, color='g')
#sns.jointplot(range_complex_nan, sd_complex_nan, kind='reg', dropna=True, color='r')

#sns.distplot(range_free_nan, kind='reg', color='purple', dropna=True)


#plt.title('Density of SD for Antibody groups')
#plt.legend(loc='upper right')

#plt.xlabel('SD in degrees')
#plt.ylabel('Density')
plt.show()

"""

#SD and Range Scatter plot
#===========================

#Plots
#sns.jointplot(range_all, sd_all, kind="reg", space=0, color='seagreen')
sns.kdeplot(sd_all, shade=True)
sns.kdeplot(range_all, shade=True)

sns.jointplot(range_all, sd_all, kind='reg', space=0)

plt.title('Correlation: Range and SD for all Antibody groups')
plt.legend(loc='upper right')

plt.xlabel('Range in degrees')
plt.ylabel('SD in degrees')
plt.show()



#SD Range Free vs Complex
#===============================
sns.kdeplot(sd_free, shade=True)
sns.kdeplot(sd_complex, shade=True)

plt.title('Correlation: Range and SD for all Antibody groups')
plt.legend(loc='upper right')

plt.xlabel('Range in degrees')
plt.ylabel('SD in degrees')
plt.show()





#time_temp2=sns.swarmplot(x='Time step (secs)',y='mosfet_temperature (degc)', data=df, color='green')

#plt.show(all_pdb_pangles)
"""
