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
         

class gen_4r:
    

    def all_pangle_groupjoin():
        for i in range(1,67):
            print('ag_'+str(i)+'<-c(fg_'+str(i)+', cg_'+str(i)+')')

    def range_gen4_allgroups():
        print('range_of_all<-c(max(ag_1)-min(ag_1),')
        for i in range(2,66):
            print('max(ag_'+str(i)+')-min(ag_'+str(i)+'),')
        print('max(ag_'+str(i+1)+')-min(ag_'+str(i+1)+')\n)')

        
    def range_gen4_freegroups():
        print('range_of_free<-c(max(fg_1)-min(fg_1),')
        for i in range(2,66):
            print('max(fg_'+str(i)+')-min(fg_'+str(i)+'),')
        print('max(fg_'+str(i+1)+')-min(fg_'+str(i+1)+')\n)')

    def range_gen4_complexgroups():
        print('range_of_complex<-c(max(cg_1)-min(cg_1),')
        for i in range(2,66):
            print('max(cg_'+str(i)+')-min(cg_'+str(i)+'),')
        print('max(cg_'+str(i+1)+')-min(cg_'+str(i+1)+')\n)')


    def mean_gen4_allgroups():
        print('mean_of_all_groups<-c(mean(ag_1),')
        for i in range(2,66):
            print('mean(ag_'+str(i)+'),')
        print('mean(ag_'+str(i+1)+')\n )')
    
    def mean_gen4_freegroups():
        print('mean_of_complex_groups<-c(mean(fg_1),')
        for i in range(2,66):
            print('mean(fg_'+str(i)+'),')
        print('mean(fg_'+str(i+1)+')\n )')

    def mean_gen4_freegroups():
        print('mean_of_complex_groups<-c(mean(fg_1),')
        for i in range(2,66):
            print('mean(fg_'+str(i)+'),')
        print('mean(fg_'+str(i+1)+')\n )')

    def mean_gen4_complexgroups():
        print('mean_of_complex_groups<-c(mean(cg_1),')
        for i in range(2,66):
            print('mean(cg_'+str(i)+'),')
        print('mean(cg_'+str(i+1)+')\n )')


    def sd_gen4_allgroups():
        print('sd_of_all_groups<-c(sd(ag_1),')
        for i in range(2,66):
            print('sd(ag_'+str(i)+'),')
        print('sd(ag_'+str(i+1)+')\n )')

    def sd_gen4_freegroups():
        print('sd_of_free_groups<-c(sd(fg_1),')
        for i in range(2,66):
            print('sd(fg_'+str(i)+'),')
        print('sd(fg_'+str(i+1)+')\n )')

    def sd_gen4_complexgroups():
        print('sd_of_complex_groups<-c(sd(cg_1),')
        for i in range(2,66):
            print('sd(cg_'+str(i)+'),')
        print('sd(cg_'+str(i+1)+')\n )')


class dfing_pandas:

    def nan_replace():
        for i in df.SD_all_groups:
            if i == 'NaN':
                i=i.replace('NaN','0')
        print(i)

        for i in df.SD_free_groups:
            if i == 'NaN':
                i=i.replace('NaN','0')
        print(i)

        for i in df.SD_complex_groups:
            if i == 'NaN':
                i=i.replace('NaN','0')


class clean_pdb:


    def appending_groups():
        '''WIP
        Simplistic appendment of free and complex groups
        of pdb formatted for dataframe
        '''

        free_all_groups=''
        complex_all_groups=''
        group_no=0
        
        for i in range(0,66):
            group_no+=1
            free_all_groups+='free_all_groups.append(free_g'+str(group_no)+')\n'
            complex_all_groups+='complex_all_groups.append(complex_g'+str(group_no)+')\n'

        print(free_all_groups)
        print(complex_all_groups)


            


    def format4_locate_pangles(text_file):
        '''WIP
        read text file with pdbs, return formated lines for locating pangles in df
        input: text file with pdbs
        output: text file with pdbs formated to be located from dataframe
        '''

        f = open(text_file, 'r')
        raw_data = f.read().splitlines()

        for i in raw_data:
            print(i.find(':'))
        return raw_data
    


    def alternate_input_4df(text_file):

        f=open(text_file)
        raw_data=f.read().splitlines()
        group=0
        counter_free=0
        counter_complex=0
        clean_data=''

        
        for index, word in enumerate(raw_data):
            if counter_free==0:
                
                counter_free+=1
                group+=1
                clean_data+='free_g'+str(group)+'=df_all_pangles.loc[['+word+']]\n'
                count_complex=0

            elif counter_complex==0: 
    
                count_complex+=1
                clean_data+='complex_g'+str(group)+'=df_all_pangles.loc[['+word+']]\n'
                counter_free=0
                
        return clean_data


    def replace_commas_withcomma(text_file):

        f=open(text_file)
        raw_data=f.read().splitlines()
        clean_data=''
        raw_singlecommas=[]
        count=0

        #First exchanges all double commas for singles
        for index, word in enumerate(raw_data):
            raw_commas=word.replace(',,',',')+'\n'
            raw_commas=raw_commas.replace(',,',',')
            raw_commas=raw_commas.replace(',,',',')
            raw_commas=raw_commas.replace(',,',',')
            raw_commas=raw_commas.replace(',,','')

            if count==1:
                clean_data+=raw_commas
            else:
                count=count+1

        return clean_data


    def remove_allcommas(text_file):
        #once all doubles are converted to singles, now focuses on remaining duplicates

        f=open(text_file)
        raw_data=f.read().splitlines()
        clean_data=''

        #First exchanges all double commas for singles
        for index, word in enumerate(raw_data):
            raw_singlecommas=word.replace(',','')+'\n'
            clean_data+=raw_singlecommas


        return clean_data


    def apost_aroundcommas(text_file):
        '''WIP
        adds apostraphes around commas in fiveplus_pdbs_clean
        '''
        f=open(text_file)
        raw_data=f.read().splitlines()
        clean_data=''

        #First exchanges all double commas for singles
        for index, word in enumerate(raw_data):
            raw_singlecommas=word.replace(',',"','")+'\n'
            clean_data+=raw_singlecommas


        return clean_data

    def remove_commas_end(text_file):
        '''WIP
        removes comma in fiveplus_pdbs_clean from end of line
        '''
        f=open(text_file)
        raw_data=f.read().splitlines()
        clean_data=''
        count=0

        w=open('fiveplus_pdbs_squeaky.txt', 'a+')

        for i in raw_data:
            if i[-1]==',':
                print('comma at end')
                clean_data=raw_data[:-1]

            else:
                clean_data=raw_data

        return clean_data
                                    

            
            

    def plus4_identifier_4pdbs(file_list):
        '''WIP : currently splits and returns length of line (['free',''complex'])
        Turn pdb file names to be surrounded by apostraphes and commas except at the end
        input: file with list of pdb file names
        output: same format of list of pdb names encompassed by aposts and commas
        '''
        test=('1V7M_1,1V7M_2,1V7N_1,1V7N_2,1V7N_3,1V7N_4')
        testlist=('')


        splitter=':'
        
        f=open(file_list)
        raw_data=f.read().splitlines()
        #turns file into list

        five_plus_pdbs=[]
        
        for index, word in enumerate(raw_data):

            #splits along ':' identifies lines with 5+ pdbs in whatever configuation
            split_fc=word.split(splitter)
            print(index, split_fc)
            if len(word)>28:
                #print(index,'large enough')
                five_plus_pdbs += word+'\n'

            else:
                print(word,'too small')

    def split_semicolon_4pdbs(file_list):
        '''WIP : currently splits and returns length of line (['free',''complex'])
        Turn pdb file names to be surrounded by apostraphes and commas except at the end
        input: file with list of pdb file names
        output: same format of list of pdb names encompassed by aposts and commas
        '''
        splitter=':'
        
        f=open(file_list)
        raw_data=f.read().splitlines()
        #turns file into list


        clean_data=''
        
        for index, word in enumerate(raw_data):

            #splits along ':'
            split_fc = word.replace(':',"'\n'")
            clean_data += str(split_fc)+'\n'


        return clean_data


    def same_apostraphes(text_file):
        '''WIP
        changes all " into '
        '''
        f=open(text_file)
        raw_data=f.read().splitlines()
        #turns file into list
        clean_data=''

        for index, word in enumerate(raw_data):
            raw_still=word.replace('"',"'")+"'\n"
            word.replace(':',"':'")
            clean_data+="'"+raw_still



        return clean_data
        



    def remove_duplicates(datafile): #doing this with csv?
        '''Take all pdbs and identify those with a _1 and keep them only,
        use Martins code
        '''

        test=['1ABC_1, 1ABC_2', '2DEF_2']

        #test.split(',')
        #prior_pdb=''

        it_test=iter(test)


        print(next(it_test))
        print(it_test)

        
        #perhaps do this on excel? Have done so, much simpler

        

    def csv_2df(csv_file):
        '''COMPLETE
        takes file and returns dataframe by pandas, made the pdb code the index
        input:csv file
        output: returns dataframe of csv file
        HELP : https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html#pandas.read_csv
        '''
        
        with open(csv_file) as fh:
            df = pd.read_csv(fh)

        df.set_index('PDB code', inplace=True)

        return df


    def chain_extractor(file_list):
        '''WIP
        opens Ab pdb files and checks the 7th line for whether it is a chain
        this is to help determine whether the pdb file is free or complexed
        input: txt file with pdb file names
        ouput: txt fule of pdb file names that tagged complexed or free
        '''
        f=open(file_list)
        raw_data=f.read().splitlines()

        free_list=''
        complex_list=''
        
        wf = open(free_list, 'a')
        wf.truncate(0)

        wc = open(complex_list, 'a')
        wc.truncate(0)
        
        for line in raw_data:
            if line[17] =='M':
                free_list += line[:6]+'.pdb\n'
                print(line[:6]+' is Free')
                
            elif line[17] == 'C':
                complex_list += line[:6]+'.pdb\n'
                print(line[:6]+' is Complexed')

        return free_list+complex_list #not sure about this



    def basic_chain_extractor(file_list):
        '''Wip
        opens Ab pdb files and checks the 7th line for whether it is a chain
        this is to help determine whether the pdb file is free or complexed
        input: txt file with pdb file names
        ouput: list of pdb file names that tagged complexed or free 
        '''
        f=open(file_list)
        raw_data=f.read().splitlines()
        clean_data=''

        for line in raw_data:
            pdbfile='/home/yobi/Documents/Bioinformatics/Project/LH_combo/LH_Combined_Chothia/'+line
            fp=open(pdbfile)

            good_data=fp.readlines()
            clean_data+=line[:6]+good_data[8]


    def list_directory(path):
        '''
        Lists all files present in a directory, useful when downloading pdb databases
        input: path to your directory
        output: returns list of all files in directory
        '''
        
        #path = '/home/yobi/AbPackingAngle_V2.1/LH_Combined_Martin/'
        data=''

        for filename in os.listdir(path):
            data+=filename+'\n'

        return data


    def add_commas(file):
        '''Simply adds commas to the end of lines for R or CSV
        input:
        output: returns list of 
        '''

        f=open(file)
        raw_data=f.read().splitlines()

        clean_data=''
        
        for i in raw_data:
            clean_data += i+',\n'
            
        return clean_data


    def bash4_pack(text_file, file2_bash2):
        '''Wip
        To convert a list of pdb files into a executable script in
        abpackingangle v2 in a BASH shell
        input: file to read, file to write to
        output(txt file with BASH executable script for ABangle)
        '''
        f=open(text_file, 'r')
        raw_data=f.read().splitlines()
        clean_data=''

        w= open(file2_bash2, 'a')
        w.truncate(0)

        for line in raw_data:
            clean_data+='./abpackingangle -p '+line[:-4]+ ' -q '+cg.martinpdb_path+line+'>>'+file2_bash2+'\n'
        
        return clean_data


    def prangleclean4_csv(data_file, write_file):
        '''Complete
        to extract and place in cells in a csv, complexed and non-complexed pdbs
        input: txt file with list of complex vs non-complex
        output: csv file with this information in seperate cells
        '''


        with open(write_file, 'w') as out:
            with open(data_file) as f:

                for line_no, line in enumerate(f):
                    if len(line) < 20:
                        out.write(line)

                    else:
                        print('Removing line {0}'.format(line_no))




    def write2_bash(text_file, folder_4extract):
        '''COMPLETE
        Convert the file list of pdbs into bash script that would copy the files
        into another folder
        input: file with list of pdb files
        output: bash script for copying pdbs to specified file
        '''
        f=open(text_file, 'r') #must have .pdb
        data=f.read().splitlines()
        bashful=''
        
        w = open(cg.b_script,'a+')
        w.truncate(0)
        for i in data:
            bashful+='cp -v '+i+' '+path2flex+folder_4extract+'\n'

        return bashful


    def run_bash():
        '''Script to open and run a bash file, for cohesion when running the entire
        program, MAY NOT BE NECESSARY
        '''



    def clean4pdb_extraction(list_file, w_file):
        '''COMPLETE
        clean list and add .pdb for later file extraction
        list_file: file with list of wanted pdbs,
        w_file: write list to this file
        output: returns desired list of pdb files for extract
        '''
        f=open(list_file,'r')
        raw_data=f.read().splitlines()
        
        clean_data=[]
        rough_data=[]
        seperator=','
        pdb='.pdb'

        for line in raw_data:
        
            rough_data+=line.split(seperator)
            line.replace(',','\n')

        w = open(w_file,'a+')
        w.truncate(0)
        for i in rough_data:
            w.write(i[0:6]+'.pdb\n')
        print('Data written to:', w_file)



    def redund_over2(text_file):
        '''to extract only redundant pdb codes with 3 or more codes in a single line
        input: text file with redundant codes arranged in a single line
        output: text file with codes arranged
        '''

        f = open(text_file)
        raw_data=f.read().splitlines()

        count=0
        clean_data=''
        for line in raw_data:
            length=len(line)
            if length>16:
                clean_data+=line+'\n'

            count+=1
        return clean_data



    def redund_directory():
        '''WiP
        input: should be folder directory, unlikely to use anything other than the same folder
        capture files from folder than only have redundancies
        output: folder with redundant pdb files
        '''

        folder= '/home/yobi/Documents/Bioinformatics/Project/LH combined CHothia/LH_Combined_Chothia/'
        with os.scandir(folder) as entries:
            gary=''
        with os.scandir(folder) as entries:
            for entry in entries:
                gary+=entry.name+'\n'
            print(gary)


