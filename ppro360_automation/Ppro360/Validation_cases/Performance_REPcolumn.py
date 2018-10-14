'''
Created on Mar 30, 2017

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
from AdminSystem_Pages.PerformanceHistoryPage import PerformanceHistoryPage


class Performance_REPcolumn(unittest.TestCase):


    def setUp(self):
        self.caseID="Performance_REPcolumn"
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
        self.NoComma_filedir=Gl.PerformanceFile_NocommaInREPForISM_Directory


    def test_Performance_REPcolumn(self):
        GetConfig=Get_configration_data()
        L=Login()
        AdminPage=AdminHomepage()
        PerUpload=PerformanceUploadPage()
        PerHistory=PerformanceHistoryPage()
        AdminAction=AdminSystem_Actions()
        Getfile=Get_file()
        YesterdayDate=GetConfig.get_LastDate(1)
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
                    #Step0: Prepare the test file
                    #Get the fileaddress and name whose REP has no Comma
                    filenamelist=Getfile.get_FileFromDir(self.NoComma_filedir, self.filetype, lobname, sitename)
                    filename=filenamelist[0]
                    NoComma_filename=Getfile.get_fileNeedToUpload(self.NoComma_filedir, self.filetype, lobname, sitename,filename,YesterdayDate)
                    NoComma_filenamelist= NoComma_filename.split("\\")
                    uploadfilename= NoComma_filenamelist[len( NoComma_filenamelist)-1]
                    
                    
                    #Step1:Open Admin page and Enter to Performance browse history page, to check if there is the same file which will be uploaded.
                    L.Login_admin(self.adminurl, lobname, sitename, self.OMuserid, self.OMpassword)
                    AdminPage.Enter_Performancehistory()
                    #Check if there the same file existed,if the file existed, delete it
                    ParamsDict=AdminAction.get_PerformanceHistory_params(lobname)
                    filename_index=ParamsDict["filename_index"]
                    delete_index=ParamsDict["delete_index"]
                        
                    if PerHistory.get_PerformanceFilename(lobname,1)==uploadfilename:
                        PerHistory.click_PerformanceFilename(lobname,1)
                        PerHistory.click_Delete_button(lobname,1)
                        time.sleep(Gl.waittime)
                        AdminAction.Delete_FileUploaded(self.OMpassword)
                    
                    #Step2:Open Admin page and Enter to Performance-Upload page
                    AdminPage.Enter_PerformanceUpload()
                    #Step2.1:Open the upload window to upload performance file who has more sheets visible
                    PerUpload.Click_BrowseFlie()
                    AdminAction.Upload_File(NoComma_filename)
                    #Step2.2: Waiting for uploading
                    while PerUpload.get_upload_message()=="Data is being processed...":
                        time.sleep(Gl.waittime)
                    #Step2.3:Verify 3 check point:Upload yesterday file
                    Failed_message_agent_expected='''For agent sheet, it contains invalid REP.\nThe related row number are:\n[6]\nPlease verify and fix it manually if necessary.'''
                    Failed_message_TL_expected='''For team lead sheet, it contains invalid Coach.\nThe related row number are:\n[6]\nPlease verify and fix it manually if necessary.'''
                    Failed_message_BOTH_expected='''For team lead sheet, it contains invalid Coach.\nThe related row number are:\n[6]\nPlease verify and fix it manually if necessary.\nFor agent sheet, it contains invalid REP.\nThe related row number are:\n[6]\nPlease verify and fix it manually if necessary.'''
                    Failed_message_actual=PerUpload.get_upload_message()
                    TryAgainDisplayed=PerUpload.TryAgain_link_displayed()
                    if 'agent' in Failed_message_actual:
                        if 'team lead' in Failed_message_actual:
                            assert Failed_message_actual==Failed_message_BOTH_expected
                        else:
                            assert Failed_message_actual==Failed_message_agent_expected
                    else:
                        assert Failed_message_actual==Failed_message_TL_expected
                        
                    
                    assert TryAgainDisplayed==True
    
    
    
    def tearDown(self):
        Gl.driver.quit()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()