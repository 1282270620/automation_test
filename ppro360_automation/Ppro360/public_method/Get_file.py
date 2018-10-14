'''
Created on Feb 9, 2017

@author: Sabrina Guo
'''
import os
import shutil
import time
from public_method import Gl
import xlrd
class Get_file():
    '''
    classdocs
    '''
    def Get_performance_sheet_Info(self,sheetname): 
        G=Get_file()
        PerformanceData=G.Get_fileaddress(Gl.PerformanceDatafilename)
    
        Performancedata=xlrd.open_workbook(PerformanceData)
        table = Performancedata.sheet_by_name(sheetname)
        return table
    
    def Get_LOBlist_sheet_Info(self,sheetname):
        G=Get_file()
        LOBlistData=G.Get_fileaddress(Gl.configrationfilename)
        
        LOBlistdata=xlrd.open_workbook(LOBlistData)
        table = LOBlistdata.sheet_by_name(sheetname)
        return table
        
 
 
 

    def Get_fileaddress(self,filename):#Get configuration file address
        fileaddress=self.Get_projectaddress()+filename
        return fileaddress
    
    def Get_downloadfileaddress(self,downloadpath,filename_prefix):
        for i in os.listdir(downloadpath):
            if filename_prefix in i:
                fileaddress=downloadpath+i
                print(fileaddress)
        return fileaddress
    
    
    def Get_Widget_upload_address(self): 
        widgetaddress=self.Get_projectaddress()+"Widget"
        return widgetaddress
    
    def Get_projectaddress(self):
        Currentpath= str(os.getcwd())
        Clist=Currentpath.split("\\")
        projectaddress=Currentpath.replace(str(Clist[len(Clist)-1]), '')
        return projectaddress
    
  

    
    def get_fileNeedToUpload(self,filedir,filetype, lobname, sitename,filename,filedate):
        newfilename=self.ModifyFileName(filename, filedate)
        oldfile=os.path.join(filedir,filename)
        newfile=os.path.join(filedir,newfilename)
#         print newfile
        time.sleep(2*Gl.waittime)
        os.rename(oldfile,newfile)
        return newfile

 
            
            
    def get_FileFromDir(self,filedir,filetype, lobname, sitename):
        if lobname!="ISM":
            sitename=sitename.replace("-","").replace(" ", "")
        elif sitename=="MALL-OF-ASIA-PHIL-01":
            sitename="MOA1"
        elif sitename=="MALL-OF-ASIA-PHIL-02":
            sitename="MOA2"
        elif sitename=="CANTON-OH":
            sitename="CANTON"
        
        filename=filetype+"_"+lobname+"_"+sitename+"_"#define the filename which need to be uploaded
        filename=filename.lower()
        Flag=False
        Filelist=[]
        for i in os.listdir(filedir):
            filenamelist=filename.split('_')
            length=len(filenamelist[0])+len(filenamelist[1])+len(filenamelist[2])+3#The length of "performance_lobname_sitename_"
            if filename==i[0:length]:
                Filelist.append(i)
                Flag=True
#         if Flag==False:
#             print "!!There is no any base file to handle,please copy one here!"
#         return Filelist
        
    def ModifyFileName(self,filename,newfiledate):
        filenamelist=filename.split('_')
        length=len(filenamelist[0])+len(filenamelist[1])+len(filenamelist[2])+3##The length of "performance_lobname_sitename_"
        oldfiledate=filename[length:filename.index('.')]
        newfilename=filename.replace(oldfiledate,newfiledate)
        return newfilename
    
    def CopyFile(self,filedir,filename1,filename2):
        oldfilename=os.path.join(filedir,filename1)
        newfilename=os.path.join(filedir,filename2)
        shutil.copy(oldfilename,newfilename)
        
    def DeleteFile(self,filepath,newfilename):
        filedress=os.path.join(filepath,newfilename)
        os.remove(filedress)
        
        
        
        
                
        
                  
        
                
                
                
                
