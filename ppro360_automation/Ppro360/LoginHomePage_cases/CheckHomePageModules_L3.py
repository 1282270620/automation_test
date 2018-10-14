'''
Created on July 10, 2018

@author: Sabrina Guo
'''
import unittest
from public_method.Get_configration_data import Get_configration_data
from public_method.Login import Login
from public_method.Check_Tablet import Check_Tablet
from public_method import Gl


class CheckHomePageModules_L3(unittest.TestCase):


    def setUp(self):
        #Case ID
        self.caseID="CheckHomePageModules_L3"
        
        GetData=Get_configration_data()
        #Get URL 
        #self.tableturl=GetData.get_TabletUrl()
        #self.adminurl=GetData.get_AdminUrl()
        #Get VXI url
        self.VXI_tableturl=GetData.get_VXI_TabletUrl()
        self.VXI_adminurl=GetData.get_VXI_AdminUrl()
        #Get AWS url
        self.AWS_tableturl=GetData.get_AWS_TabletUrl()
        self.AWS_adminurl=GetData.get_AWS_AdminUrl()
        
        #Get OM account
        OMaccount=GetData.get_OMaccount()
        self.userid=OMaccount["OMuserid"]
        self.password=OMaccount["OMpassword"]
        #Get LOBs have no LSACS
        self.LOBs_NoLSACS_list=GetData.get_LOBHasNoLSACS_list()
        #Get all lobs from CSV
        self.testLOBSITE_list=GetData.get_LOBSITEtoTest(self.caseID)
        #Get AWS LOBs
        self.AWSLOBs_list=GetData.get_AWSLOBs_list()
        #Get VXI LOBs
        self.VXILOBs_list=GetData.get_VXILOBs_list()
        #Info of configuration
        self.role="L3"
    def tearDown(self):
        Gl.driver.quit()
        #pass
    


    def test_CheckHomePageModules_L3(self):
        GetConfig=Get_configration_data()
        L=Login()
        #Tablet=TabletHomepage()
        CheckTablet=Check_Tablet()
        for i in range(0,len(self.testLOBSITE_list)):
            Flag=GetConfig.get_LOBSITE_STATUS(self.testLOBSITE_list[i])
            if Flag==True:
                each_LOBSITE=self.testLOBSITE_list[i].split(":")
                lobname=each_LOBSITE[0]
                if lobname in self.AWSLOBs_list:
                    tableturl=self.AWS_tableturl
                elif lobname in self.VXILOBs_list:
                    tableturl=self.VXI_tableturl
                site_list=each_LOBSITE[1].split("*")
                for n in range(0,len(site_list)):
                    sitename=site_list[n]
                    GetConfig.print_StartTest_message(lobname, sitename)    
                L.Login_tablet(tableturl, lobname, sitename, self.userid, self.password)
                CheckTablet.Check_TabletHomepageCircle_ByRole(lobname, self.role)
                L.logout_tablet()
                
                
                
                        
                        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_CoachingLeaderScores_OMFilter']
    unittest.main()