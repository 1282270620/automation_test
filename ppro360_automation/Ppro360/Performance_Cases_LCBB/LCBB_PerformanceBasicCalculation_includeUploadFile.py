'''
Created on Apr 5, 2017

@author: symbio
'''
import unittest
from Performance_Cases_DTVSS import Get_PerformanceData_Expected_DTVSS.Get_PerformanceData_Expected_DTVSS
from public_method import Gl
from AdminSystem_Pages.RosterUploadPage import RosterUploadPage
from AdminSystem_Pages.PerformanceUploadPage import PerformanceUploadPage
from public_method.Get_configration_data import Get_configration_data
from public_method.Login import Login
from public_method.Get_file import Get_file
from AdminSystem_Pages.AdminHomepage import AdminHomepage
from public_method.AdminSystem_Actions import AdminSystem_Actions


class LCBB_PerformanceBasicCalculation(unittest.TestCase):


    def setUp(self):
        self.caseID="LCBB_PerformanceBasicCalculation"
        GetData=Get_configration_data()
        #Get URL 
        self.adminurl=GetData.get_AdminUrl()
        #Get OM account
        OMaccount=GetData.get_OMaccount()
        self.OMuserid=OMaccount["OMuserid"]
        self.OMpassword=OMaccount["OMpassword"]
        #Get all lobs from CSV
        self.testLOBSITE_list=GetData.get_LOBSITEtoTest(self.caseID)
        
        self.filedir=Gl.LCCBFile_Directory
        self.filetype_R="Roster"
        self.filetype_P="Performance"


    def tearDown(self):
        Gl.driver.quit() 


    def test_LCBB_PerformanceBasicCalculation(self):
        GetConfig=Get_configration_data()
        L=Login()
        Getfile=Get_file()
        AdminPage=AdminHomepage()
        RosterUpload=RosterUploadPage()
        AdminAction=AdminSystem_Actions()
        PerUpload=PerformanceUploadPage()
        for i in range(0,len(self.testLOBSITE_list)):
            Flag=GetConfig.get_LOBSITE_STATUS(self.testLOBSITE_list[i])
            if Flag==True:
                each_LOBSITE=self.testLOBSITE_list[i].split(":")
                lobname=each_LOBSITE[0]
                #Get Site to test
                site_list=each_LOBSITE[1].split("*")
                for n in range(0,len(site_list)):
                    sitename=site_list[n]
                    GetConfig.print_StartTest_message(lobname, sitename)
                    #Step0.1:Prepare files:Roster
                    filedate_R=GetConfig.get_LastDate(32)#The date of Roster must be earlier than date4
                    RFilelist=Getfile.get_FileFromDir(self.filedir, self.filetype_R, lobname, sitename)
                    filename=RFilelist[0]
                    filename_R=Getfile.get_fileNeedToUpload(self.filedir, self.filetype_R, lobname, sitename, filename, filedate_R)
                    #Step0.2:Prepare files:Performance
                    filedate1=GetConfig.get_LastDate(1)
                    filedate2=GetConfig.get_LastDate(2)
                    filedate3=GetConfig.get_LastDate(7)
                    filedate4=GetConfig.get_LastDate(31)
                    Pfilelist=Getfile.get_FileFromDir(self.filedir, self.filetype_P, lobname, sitename)
                    newfilelist=[]
                    #Create date1, date2,date3 files
                    for i in Pfilelist:
                        if i[i.index('.')-1]==1:
                            newfilename1=Getfile.ModifyFileName(i, filedate1)
                            newfilelist.append(newfilename1)
                            Getfile.CopyFile(self.filedir,i, newfilename1)
                        elif i[i.index('.')-1]==2:
                            newfilename2=Getfile.ModifyFileName(i, filedate2)
                            newfilelist.append(newfilename2)
                            Getfile.CopyFile(self.filedir,i, newfilename2)
                        elif i[i.index('.')-1]==3:
                            newfilename3=Getfile.ModifyFileName(i, filedate3)
                            newfilelist.append(newfilename3)
                            Getfile.CopyFile(self.filedir,i, newfilename3)
                    #Creat date4 file        
                    newfilename4=Getfile.ModifyFileName(i, filedate4)
                    newfilelist.append(newfilename4)#All Performance file need to upload(date1,date2,date3,date4)
                    Getfile.CopyFile(self.filedir,Pfilelist[0], newfilename4)
                    
                    #Step0.3:Login with OM to do upload work
                    L.Login_admin(self.adminurl, lobname, sitename, self.OMuserid, self.OMpassword)
                    #Can add some codes to verify if this roster file exists, if Yes, delete it and upload the roster file
                    #Upload Roster
                    AdminPage.Enter_RoserUpload()
                    RosterUpload.Click_BrowseFlie()
                    AdminAction.Upload_File(filename_R)
                    assert RosterUpload.get_upload_message()=="You successfully uploaded ["+filename_R+"]"
                    #Upload Performance
                    for i in newfilelist:
                        AdminPage.Enter_PerformanceUpload()
                        PerUpload.Click_BrowseFlie()
                        AdminAction.Upload_File(i)
                        assert PerUpload.get_upload_message()=="You successfully uploaded ["+i+"]"
                        
                    
                    
                    
                    
        
        #Step1:Upload Roster file
        
        
        #Step2:Upload Performance file:Date1,Date2,Date3,Date4
        
        
        
        
        
        Get_Data=Get_PerformanceData_Expected()
        #Yesterday:linenumber=5-16,21-25
        lineindex=5
        LCBB_Data_Expected=Get_Data.get_LCBB_Performance_Data(lineindex)
        print LCBB_Data_Expected
        
        #for linenumber in range(6,18):
            #LCBB_Data_Expected=Get_Data.get_LCBB_Performance_Data(linenumber)
            #print LCBB_Data_Expected[]


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()