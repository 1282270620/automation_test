'''
Created on Mar 22, 2017

@author: symbio
'''
import unittest
from public_method.Get_configration_data import Get_configration_data
from public_method.Login import Login
from AdminSystem_Pages.AdminHomepage import AdminHomepage
from public_method.AdminSystem_Actions import AdminSystem_Actions
from public_method import Gl
import time
from AdminSystem_Pages.PerformanceUploadPage import PerformanceUploadPage
from public_method.Get_file import Get_file

class PerformanceFile_TodayOrLaterThanToday(unittest.TestCase):


    def setUp(self):
        self.caseID="PerformanceFile_TodayOrLaterThanToday"
        GetData=Get_configration_data()
        #Get URL 
        self.adminurl=GetData.get_AdminUrl()
        #Get OM account
        OMaccount=GetData.get_OMaccount()
        self.OMuserid=OMaccount["OMuserid"]
        self.OMpassword=OMaccount["OMpassword"]
        #Get all lobs from CSV
        self.testLOBSITE_list=GetData.get_LOBSITEtoTest(self.caseID)
        
        self.filetype="performance"
        self.filedir=Gl.PerformanceFile_Directory



    def test_PerformanceFile_TodayOrLaterThanToday(self):
        GetConfig=Get_configration_data()
        L=Login()
        AdminPage=AdminHomepage()
        PerUpload=PerformanceUploadPage()
        AdminAction=AdminSystem_Actions()
        Getfile=Get_file()
        TodayDate=GetConfig.get_ServerCurrentDate().replace("-","")
        TomorrowDate=GetConfig.get_FutureDate(1).replace("/","")
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
                    ###########################Start to do testing#####################################
                    #Step1:Open Admin page and Prepare the test file(today and tomorrow)
                    L.Login_admin(self.adminurl, lobname, sitename, self.OMuserid, self.OMpassword)
                    #Step2:Prepare the test file(today) to do testing
                    filenamelist=Getfile.get_FileFromDir(self.filedir, self.filetype, lobname, sitename)
                    filename=filenamelist[0]
                    filename_today=Getfile.get_fileNeedToUpload(self.filedir, self.filetype, lobname, sitename,filename,TodayDate)
                    AdminPage.Enter_PerformanceUpload()
                    #Step2.1:Open the upload window to upload performance file
                    PerUpload.Click_BrowseFlie()
                    AdminAction.Upload_File(filename_today)
                    
                    #Step2.2: Waiting for uploading
                    while PerUpload.get_upload_message()=="Data is being processed...":
                        time.sleep(Gl.waittime)
                    #Step2.3:Verify:Upload the today file
                    Failed_message_expected="You should upload the data before today."
                    Failed_message_actual=PerUpload.get_upload_message()
                    TryAgainDisplayed=PerUpload.TryAgain_link_displayed()
                    assert Failed_message_actual==Failed_message_expected
                    assert TryAgainDisplayed==True
                    
                    #Step3:Prepare the test file(tomorrow) to do testing
                    filename_tomorrow=Getfile.get_fileNeedToUpload(self.filedir, self.filetype, lobname, sitename,filename_today,TomorrowDate)
                    AdminPage.Enter_PerformanceUpload()
                    #Step3.1:Open the upload window to upload performance file
                    PerUpload.Click_BrowseFlie()
                    AdminAction.Upload_File(filename_tomorrow)
                    
                    #Step3.2: Waiting for uploading
                    while PerUpload.get_upload_message()=="Data is being processed...":
                        time.sleep(Gl.waittime)
                    #Step3.3:Verify:Upload the today file
                    Failed_message_expected="You should upload the data before today."
                    Failed_message_actual=PerUpload.get_upload_message()
                    TryAgainDisplayed=PerUpload.TryAgain_link_displayed()
                    assert Failed_message_actual==Failed_message_expected
                    assert TryAgainDisplayed==True
                    
                    

                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
    
    def tearDown(self):
        Gl.driver.quit()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()