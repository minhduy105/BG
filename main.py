# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 21:27:42 2019

@author: Zi
"""
from FileSearch import FileSearch 
from os import listdir 
from os.path import isfile, join, realpath, dirname

if __name__== "__main__":
      
    FS = FileSearch() 
    
    path_name =  dirname(realpath(__file__))
    
    path_name = path_name + "\Files"

    
    print ("Folder name: " + path_name)
    
    with open("test_set.txt") as fp:
        line = fp.readline()
        cnt = 1
        while line:
            print ("\nSearch word:" + line)
        
            files_list = FS.searchFile (path_name, line)
            print ("List of file: ")
            print (files_list)    
        
            line = fp.readline()
            cnt += 1
        

    