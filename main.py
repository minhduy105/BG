# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 21:27:42 2019

@author: Zi
"""
from FileSearch import FileSearch 
from os import listdir 
from os.path import isfile, join, realpath, dirname

import time

if __name__== "__main__":
      
    FS = FileSearch() 
    
    path_name =  dirname(realpath(__file__))
    
    path_name = path_name + "\Files"

    
    print ("Folder name: " + path_name)
    
    with open("test_set.txt") as fp:
        line = fp.readline()
        cnt = 1
        while line:
            print ("\nSearch word:" + line.strip('\n'))
            
            start_time = time.time()
            #deleting new line
            files_list = FS.searchFile (path_name, line.strip('\n'))
            
            end_time = time.time()
            
            print ("List of file: ")
            print (files_list)    
            
            print("Time: %s seconds " % (end_time - start_time))
            
            line = fp.readline()
            cnt += 1
        

    