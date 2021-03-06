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
from AdminSystem_Pages.PerformanceHistoryPage import PerformanceHistoryPage

class PerformanceFile_EarlierThanToday(unittest.TestCase):


    def setUp(self):
        self.caseID="PerformanceFile_EarlierThanToday"
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



    def test_PerformanceFile_EarlierThanToday(self):
        GetConfig=Get_configration_data()
        L=Login()
        AdminPage=AdminHomepage()
        PerUpload=PerformanceUploadPage()
        PerHistory=PerformanceHistoryPage()
        AdminAction=AdminSystem_Actions()
        Getfile=Get_file()
        #YesterdayDate=GetConfig.get_YesterdayDate()
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
                    #Step0:Open Admin page and Enter to Performance browse history page, to check if there is the same file which will be uploaded.
                    L.Login_admin(self.adminurl, lobname, sitename, self.OMuserid, self.OMpassword)
                    AdminPage.Enter_Performancehistory()
                    #Get the fileaddress and name who is ready to be uploaded
                    filenamelist=Getfile.get_FileFromDir(self.filedir, self.filetype, lobname, sitename)
                    filenametest=filenamelist[0]
                    filename=Getfile.get_fileNeedToUpload(self.filedir, self.filetype, lobname, sitename,filenametest, YesterdayDate)
                    print filename
                    filenamelist=filename.split("\\")
                    uploadfilename=filenamelist[len(filenamelist)-1]
                    #Check if there the same file existed,if the file existed, delete it
                    '''
                    ParamsDict=AdminAction.get_PerformanceHistory_params(lobname)
                    filename_index=ParamsDict["filename_index"]
                    delete_index=ParamsDict["delete_index"]'''
                        
                    if PerHistory.get_PerformanceFilename(lobname,1)==uploadfilename:
                        PerHistory.click_PerformanceFilename(lobname,1)
                        PerHistory.click_Delete_button(lobname,1)
                        time.sleep(Gl.waittime)
                        AdminAction.Delete_FileUploaded(self.OMpassword)
                    
                    #Step1:Open Admin page and Enter to Performance-Upload page
                    AdminPage.Enter_PerformanceUpload()
                    
                    #Step2:Open the upload window to upload performance file
                    PerUpload.Click_BrowseFlie()
                    AdminAction.Upload_File(filename)
                    
                    #Step3: Waiting for uploading
                    while PerUpload.get_upload_message()=="Data is being processed...":
                        time.sleep(Gl.waittime)
                    #Step4:Verify 3 check point:Upload yesterday file
                    Success_message_expected="You successfully uploaded ["+uploadfilename+"]"
                    Success_message_actual=PerUpload.get_upload_message()
                    BrowseUloadHistoryDisplayed=PerUpload.BroweUploadHistory_link_displayed()
                    UploadAnotherDisplayed=PerUpload.UploadAnother_link_displayed()
                    assert Success_message_actual==Success_message_expected
                    assert BrowseUloadHistoryDisplayed==True
                    assert UploadAnotherDisplayed==True
                    time.sleep(Gl.waittime)
                    #Step5:Verify:Upload the same file
                    AdminPage.Enter_PerformanceUpload()
                    PerUpload.Click_BrowseFlie()
                    AdminAction.Upload_File(filename)
                    time.sleep(5*Gl.waittime)
                    Failed_message_expected="You have already uploaded the file ["+uploadfilename+"]."
                    Failed_message_actual=PerUpload.get_upload_message()
                    TryAgainDisplayed=PerUpload.TryAgain_link_displayed()
                    assert Failed_message_actual==Failed_message_expected
                    assert TryAgainDisplayed==True
                    


                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
    
    def tearDown(self):
        Gl.driver.quit()
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()