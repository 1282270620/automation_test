'''
Created on Mar 22, 2017

@author: symbio
'''
#from AdminSystem_Pages.PerformanceUploadPage import PerformanceUploadPage
import os
from public_method.Get_file import Get_file
from AdminSystem_Pages.DeleteUploadedDataPage import DeleteUploadedDataPage
import time
import Gl
class AdminSystem_Actions(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
    def Upload_File(self,filename):
        GetFile=Get_file()
        print(GetFile.Get_Widget_upload_address())
        widgetfile=GetFile.Get_Widget_upload_address()+"\UploadFile.exe"
        os.system("%s %s"%(widgetfile,filename))
        time.sleep(2*Gl.waittime)
        
    def get_PerformanceHistory_params(self,lobname):
        if lobname in ["ISM","LCBB"]:
            filename_index=2
            delete_index=4
        else:
            filename_index=1
            delete_index=3
        ParamsDict={"filename_index":filename_index,"delete_index":delete_index}
        return ParamsDict
        
    
    def Delete_FileUploaded(self,OMpassword):
        DeleteFile=DeleteUploadedDataPage()
        DeleteFile.click_warning_message(1)
        DeleteFile.click_warning_message(2)
        DeleteFile.click_warning_message(3)
        DeleteFile.Input_password(OMpassword)
        DeleteFile.Click_delete_button()



        
        
        
        
        