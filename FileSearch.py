# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 18:23:55 2019

@author: Zi
"""

from os import listdir 
from os.path import isfile, join, realpath, dirname

class FileSearch:
    """    
    Funcion: searchFile
    Input:  path_name: the path of the folder
            search_name: the search that you want to do
    Output: return a list of all the file in the path_name folder that match your search_name
    
    """    
    
    def searchFile (self,path_name, search_name):
        front_flag = False # this is to check if * is at the front or the end
        file_name_list = []
        files_in_path = [f for f in listdir(path_name) if isfile(join(path_name, f))]
    
        if (search_name[0] == "*"):
            front_flag = True
        elif (search_name[len(search_name) - 1] == "*"):
            front_flag = False
        else:
            return file_name_list
        
        #NOTE: because the list is not in order for search from the back, we will
        #have to bruce force it. 
        if front_flag: 
            for i in files_in_path:
                if (len(i)) >= len (search_name) - 1: # -1 because we do not count the "*"
                    if i[len(i)-(len(search_name) - 1):len(i)].upper() == search_name[1:len(search_name)].upper():
                        file_name_list.append(i)                        
        
        else:
            index = self.binarySearch(files_in_path, 0, len(files_in_path)-1, search_name[0:len(search_name)-1])
            if index == -1: 
                return file_name_list
            
            
            file_name_list.append(files_in_path[index])
            
            i = index -1
            while i >= 0: 
                if len(files_in_path[i]) >= len(search_name) - 1:
                    if files_in_path[i][0:len(search_name)-1].upper() == search_name[0:len(search_name)-1].upper():
                        file_name_list.append(files_in_path[i])
                        i = i - 1
                    else:
                        break
                else: 
                    break 
            
            i = index + 1
            while i < len(files_in_path): 
                if len(files_in_path[i]) >= len(search_name) - 1:
                    if files_in_path[i][0:len(search_name)-1].upper() == search_name[0:len(search_name)-1].upper():
                        file_name_list.append(files_in_path[i])
                        i = i + 1
                    else:
                        break
                else: 
                    break 

            
        return file_name_list
    
    #arr = array, l = left, r = right, x = search
    def binarySearch (self,arr, left, right, x): 
        # Check base case 
        if right >= left: 
    
            mid = int(left + (right-left)/2)
    
            # this is to make sure we are not out of range
            if len(arr[mid]) < len(x):
                i = len(arr[mid]) 
            else:
                i = len(x)
                
            # If element is present at the middle itself 
            if arr[mid][0:i].upper() == x[0:i].upper():
                if i == len(x):
                    return mid 
                # the null character is before the letter
                else:
                    self.binarySearch(arr, mid+1, right, x)
            
            # If element is smaller than mid, 
            elif arr[mid][0:i].upper() > x[0:i].upper():
                return self.binarySearch(arr, left, mid-1, x) 
      
            # Else the element can only be present in right subarray 
            else: 
                return self.binarySearch(arr, mid+1, right, x) 
      
        else: 
            # Element is not present in the array 
            return -1
      
        
