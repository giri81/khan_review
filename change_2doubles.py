'''
Created on 14-Dec-2015

@author: girish
'''

import collections
import re

def check(word):

    frequency_dictionary = dict(collections.Counter(word))
    
    for key in frequency_dictionary.keys():
        if frequency_dictionary[key] == 1:
            del frequency_dictionary[key]      
        
        key_list = [str(item) for item in frequency_dictionary.keys()]
        counter = 0
    
    for item in key_list:
        regex = re.compile(item+"+")
        temp_tuple = regex.findall(word)
        for tuple_item in temp_tuple:
            if len(tuple_item) ==  2:
                counter = counter + 1
    return counter
       
       
def read():
    with open('word.txt', "r") as filehandler:
        for word in filehandler:
            if check(word) == 3:
                print word
                
if __name__ == "__main__":
    read()

            
    
    

    
    