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
    
    test_set = ["a*", "as*", "*.txt", "*a.docx", "yt*", "adsfsa*"]
    
    
    
    for i in test_set:
        files_list = []
        print ("\nSearch word:" + i)
        files_list = FS.searchFile (path_name, i)
        print ("List of file: ")
        print (files_list)    
        
    