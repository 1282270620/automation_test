'''
Created on Mar 21, 2017

@author: symbio
'''
import unittest
from public_method.Get_configration_data import Get_configration_data
from public_method import Gl
from Tablet_pages.LoginTabletPage import LogintabletPage


class LoginPage(unittest.TestCase):


    def setUp(self):
        #Case ID
        self.caseID="LoginPage"
        
        GetData=Get_configration_data()
        #Get URL 
        self.tableturl=GetData.get_TabletUrl()
        #Get All LOBs list
        self.AllLOBs_Expected_List=GetData.get_AllLOBs_list()
        


    def test_LoginPage(self):
        print self.caseID
        GetData=Get_configration_data()
        #Step1:Open table login page
        login_page=LogintabletPage(self.tableturl,Gl.driver)
        login_page.open()
        TabletTitleVersion_list=login_page.get_TabletTitleVersion()
        assert TabletTitleVersion_list[0]==GetData.get_Tablet_Title()
        assert TabletTitleVersion_list[1]==GetData.get_Tablet_Version()
        
        #Check if each lob is correct
        login_page.click_lobname_box_dropdown()#Click lob name box drop down
        lobindex=1
        LOB_Flag=login_page.eachlob_Exist(lobindex)
        while LOB_Flag:
            assert login_page.get_eachlobname(lobindex) in self.AllLOBs_Expected_List#Verify all lob names from page are the same as those from Excel.
            lobindex=lobindex+1
        
        for i in range(0,len(self.AllLOBs_Expected_List)):
            lobname=self.AllLOBs_Expected_List[i]
            Allsites_eachlob_Expected_list=GetData.get_AllSITEsForEachLOB_list(lobname)
            #time.sleep(Gl.waittime)
            login_page.select_lob(lobname)#Select lob name
            assert login_page.get_defaultsitename()==Allsites_eachlob_Expected_list[0]#Verify the default site name
            login_page.click_sitename_box_dropdown()#Click site name box drop down
            
            siteindex=1
            SITE_Flag=login_page.eachsite_Exist(siteindex)
            while SITE_Flag:
                assert login_page.get_eachsitename(siteindex) in Allsites_eachlob_Expected_list#Verify all site names from page are the same as those from Excel.
                siteindex=siteindex+1
            
            login_page.click_lobname_box_dropdown()
            
        
    def tearDown(self):
        Gl.driver.quit()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()