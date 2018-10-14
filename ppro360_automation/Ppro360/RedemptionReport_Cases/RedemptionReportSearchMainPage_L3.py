'''
Created on 2018.8.3

@author: haodong.liu
'''

import unittest
import time
from public_method import Gl
from public_method.Get_configration_data import Get_configration_data
from public_method.Login import Login
from public_method.Coach_Triad_General import Coach_Triad_General
from Tablet_pages.TabletHomepage import TabletHomepage
from Tablet_pages.Coachinghomepage import Coachinghomepage
from CoachingAndTriadCoaching_Pages.BasicInfoforCoaching import BasicInfoforCoaching
from Tablet_pages.HeaderPage import HeaderPage
from public_method.Get_AllRoleAccountForTest import Get_AllRoleAccountForTest
from RedemptionReport_Cases.RedemptionReport_Page import RedemptionReport_Page


class RedemptionReportSearchMainPage_L3(unittest.TestCase):


    def setUp(self):
        #Case ID
        self.caseID="RedemptionReportSearchMainPage_L3"
        
        GetData=Get_configration_data()
        #Get URL 
        self.tableturl=GetData.get_TabletUrl()
        self.Adminurl=GetData.get_AdminUrl()
        #Get OM account
        OMaccount=GetData.get_OMaccount()
        self.OMuserid=OMaccount["OMuserid"]
        self.OMpassword=OMaccount["OMpassword"]
        #Get all lobs from CSV
        self.testLOBSITE_list=GetData.get_LOBSITEtoTest(self.caseID)
        #
        self.ExitsLACSandLACLS_Lobs=['ICM']
        self.NotExitsLACSandLACLS_lobs=[]
        
        self.CurrentDate=GetData.get_ServerCurrentDate()
        #Database info
        self.host=GetData.get_StageDatabaseHost()
        self.hostindex=92
        self.dbuser=GetData.get_StageDatabaseUser()
        self.dbpassword=GetData.get_StageDatabasePassword()
        
    def test_Outlier_AddQualityAssuanceForm(self):
        CT=Coach_Triad_General()
        GetConfig=Get_configration_data()
        Tablet=TabletHomepage()
        BasicInfo=BasicInfoforCoaching()
        RedemptionReportPage=RedemptionReport_Page()
        Coach=Coach_Triad_General()
        Getaccount=Get_AllRoleAccountForTest()
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
                   
                    #Login tablet,and Get HRID using for testing
                    L=Login()
                    L.Login_tablet(self.tableturl,lobname,sitename,self.OMuserid,self.OMpassword)
                    if lobname in self.ExitsLACSandLACLS_Lobs:
                        Tablet.Click_RedemptionReport(11)
                    else:
                        Tablet.Click_RedemptionReport(9)
                    
                    #Check defalutValues
                    assert RedemptionReportPage.get_TLNameDefaultValue()=='All'
                    RedemptionReportPage.Click_TLNameDropDown()
                    time.sleep(5)
                    ALLTLName=RedemptionReportPage.get_all_TLName()
                    print ALLTLName
                    RedemptionReportPage.Click_TLNameDropDown()
                    assert RedemptionReportPage.get_DatefaultValue(1)==''
                    assert RedemptionReportPage.get_DatefaultValue(2)==''
                    #assert RedemptionReportPage.get_DatafaultValue()==''
                    assert RedemptionReportPage.get_FilterButtonDatafaultStutus()=='true'
                    assert RedemptionReportPage.get_ExportButtonDatafaultStutus()=='true'
                    
                    #Filter Data
                    RedemptionReportPage.Click_TLNameDropDown()
                    time.sleep(5)
                    RedemptionReportPage.Select_TL(2)
                    
                        
                    

    #def tearDown(self):
    #    Gl.driver.quit()                
                    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()   

