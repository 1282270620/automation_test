'''
Created on Jan 18, 2017

@author: symbio
'''
import os
from pip import download

class Deleteexistfile(object):
    '''
    classdocs
    '''


    '''
    def __init__(self,downloadpath):
        
        self.downloadpath=downloadpath
        '''
        
        
    def delete_coachfile(self,downloadpath):
        files=os.listdir(downloadpath)
        for filename in files:
            if 'coach' in filename:
                file_delete = downloadpath+'/'+filename
                os.remove(file_delete)
            elif 'coaching' in filename:
                file_delete = downloadpath+'/'+filename
                os.remove(file_delete)
                
    #yalan added below:
    def delete_MyteamFile(self,downloadpath):
        files=os.listdir(downloadpath)
        for filename in files:
            if 'myteam' in filename:
                file_delete = downloadpath+'/'+filename
                os.remove(file_delete)
    
    def delete_TLandAgentAccountsFile(self,downloadpath):   
        files=os.listdir(downloadpath)
        for filename in files:
            if 'L2L1AndAgent' in filename:
                file_delete = downloadpath+'/'+filename
                os.remove(file_delete)        
                 
    #yalan added above
            