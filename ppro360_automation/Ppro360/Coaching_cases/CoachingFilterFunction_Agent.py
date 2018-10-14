'''
Created on Jan 23, 2017

@author: symbio
'''
import unittest
from public_method import Gl
from public_method.Get_configration_data import Get_configration_data
from public_method.Login import Login
from Tablet_pages.Coachinghomepage import Coachinghomepage
from Tablet_pages.HeaderPage import HeaderPage
from Tablet_pages.TabletHomepage import TabletHomepage
from public_method.Coach_Triad_General import Coach_Triad_General
from public_method.Get_AllRoleAccountForTest import Get_AllRoleAccountForTest
import time


class CoachingFilterFunction_Agent(unittest.TestCase):


    def setUp(self):
        #Case ID
        self.caseID="CoachingFilterFunction_Agent"
        
        GetData=Get_configration_data()
        #Get URL 
        self.tableturl=GetData.get_TabletUrl()
        self.adminurl=GetData.get_AdminUrl()
        #Get OM account
        OMaccount=GetData.get_OMaccount()
        self.OMuserid=OMaccount["OMuserid"]
        self.OMpassword=OMaccount["OMpassword"]
        #Get all lobs from CSV
        self.testLOBSITE_list=GetData.get_LOBSITEtoTest(self.caseID)


    def test_CoachingFilterFunction_Agent(self):
        CT=Coach_Triad_General()
        Tablet=TabletHomepage()
        GetConfig=Get_configration_data()
        #Test several LOBs
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
                    coach_list=GetConfig.get_CoachingFormList(lobname)
                    #Step0:Login tablet system and find out a Agent for testing
                    GetAgent=Get_AllRoleAccountForTest()
                    #AgentInfo=GetAgent.get_AgentInfoFromTablet(self.tableturl, lobname, sitename, self.OMuserid, self.OMpassword,"LastTwoMonth")
                    AgentInfo=GetAgent.get_AgentInfoFromTablet(self.tableturl, lobname, sitename, self.OMuserid, self.OMpassword, "Month-To-Date", self.adminurl)
                    AgentHrid=AgentInfo["Hrid"]
                    AgentPassword=AgentInfo["Password"]
                    
                    #Step1:login with TL role.
                    L=Login()
                    L.Login_tablet(self.tableturl,lobname,sitename,AgentHrid,AgentPassword)
                    #Step2:Entercoaching module.
                    Tablet.click_Agent_coachingcircle()
                    #Step3:Check CoachName and EmployeeName
                    CoachHome=Coachinghomepage()
                    Header=HeaderPage()
                    if CoachHome.get_CoachName()=="All" and CoachHome.get_EmployeeName()==Header.get_loginName():
                        print "Coachname and Empployeename are correct!!"                   
                    
                    #Step4:Check type drop-down.
                    DropDownlist=CT.Get_typelist()
                    print DropDownlist
                    print coach_list
                    assert DropDownlist==coach_list
                    
                    #Step4:Logout
                    #L=Login(self.url,lobname,sitename,AGENTuserid,AGENTpassword)
                    L.logout_tablet()
                    
                    GetConfig.print_EndTest_message(lobname, sitename)
                    time.sleep(5*Gl.waittime)
                    continue
    def tearDown(self):
        #Gl.driver.quit()
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
