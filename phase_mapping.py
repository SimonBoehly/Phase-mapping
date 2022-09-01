#write down phase mapping routine

import numpy as np
def phased_dictionary(dictionaries,sensitivity=1):
    total_dict_phased={}
    for key in key_list(dictionaries):
        total_dict_phased[key]=0
        
        
        
        
     #get mean_fid array with mean number of counts
    #get mean values
    mean_fid={}
    for key in key_list(dictionaries):
        mean_fid[key]=0
    
    
#fill up the array
    for dictionary in dictionaries:
        for key in dictionary:
            mean_fid[key]+=dictionary[key]
    for key in mean_fid:
        mean_fid[key]/=len(dictionaries)
        
    #fill up
    for dictionary in dictionaries:
        for key in total_dict_phased:
            if key in dictionary:
                total_dict_phased[key]+=dictionary[key]*np.exp(1j*2*np.pi*dictionary[key]*sensitivity/mean_fid[key])
    return(total_dict_phased)
    
    
    
    
    
    
    
    
    
    

def key_list(dictionaries):
    """
    returns list of all keys given in a list of dictionaries
    arguments: dictionaries, array of dictionaries
    """
    key_list=[]
    for dictionary in dictionaries:
        for key in dictionary:
            if key not in key_list:
                key_list.append(key)
                
    return(key_list)
                
                
                
def total_dict(dictionaries):
    """
    returns the simple superposition of all dictionaries
    
    
    """
    
    dict_total={}
    for key in key_list(dictionaries):
        dict_total[key]=0
    #normalze dictionaries
    
    for dictionary in dictionaries:
        total=sum(dictionary.values())
        for key in dictionary:
            dictionary[key]/=total
    #add values
    
    for dictionary in dictionaries:
        for key in key_list(dictionaries):
            if key in dictionary:
                dict_total[key]+=dictionary[key]
    return(dict_total)
    
    
    
    
    
    
    
    
    
    
    
    
    
    