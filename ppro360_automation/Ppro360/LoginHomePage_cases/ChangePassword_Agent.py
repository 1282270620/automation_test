'''
Created on Mar 10, 2017

@author: SabrinaGuo
'''
import unittest
from public_method.Get_configration_data import Get_configration_data
from public_method.Login import Login
from public_method import Gl
from Tablet_pages.HeaderPage import HeaderPage
from Tablet_pages.TabletHomepage import TabletHomepage
from AdminSystem_Pages.LoginAdminPage import LoginAdminPage
from Tablet_pages.ChangPwd_warningPage import ChangPwd_warningPage
from Tablet_pages.LoginTabletPage import LogintabletPage
import time
from public_method.Get_AllRoleAccountForTest import Get_AllRoleAccountForTest
from public_method.AddOrChangeUserInfo import AddOrChangeUserInfo

class ChangePassword_Agent(unittest.TestCase):


    def setUp(self):
        #Case ID
        self.caseID="ChangePassword_Agent"
        
        GetData=Get_configration_data()
        #Get OM account
        OMaccount=GetData.get_OMaccount()
        self.OMuserid=OMaccount["OMuserid"]
        self.OMpassword=OMaccount["OMpassword"]
        #Get all lobs from CSV
        self.testLOBSITE_list=GetData.get_LOBSITEtoTest(self.caseID)
          


    def test_ChangePassword_Agent(self):
        Tablet=TabletHomepage()
        GetAgent=Get_AllRoleAccountForTest()
        ChUserInfo=AddOrChangeUserInfo()
        GetConfig=Get_configration_data()
        #Test several LOBs
        for i in range(0,len(self.testLOBSITE_list)):
            Flag=GetConfig.get_LOBSITE_STATUS(self.testLOBSITE_list[i])
            if Flag==True:
                each_LOBSITE=self.testLOBSITE_list[i].split(":")
                lobname=each_LOBSITE[0]
                ##GET THE CORRECT URL#####
                Adminurl=GetConfig.get_Test_AdminUrl(lobname)
                tableturl=GetConfig.get_Test_Tablet(lobname)
                ##GET THE CORRECT URL#####
                #Get Site to test
                site_list=each_LOBSITE[1].split("*")
                for n in range(0,len(site_list)):
                    sitename=site_list[n]
                    GetConfig.print_StartTest_message(lobname, sitename)
                    #Step0:Login tablet system and find out a Agent for testing
                    GetAgent=Get_AllRoleAccountForTest()
                    '''TLInfo=GetAgent.get_TLInfoFromMyteamInfo(self.tableturl, lobname, sitename, self.OMuserid, self.OMpassword)
                    TLuserid=TLInfo['Hrid']
                    TLpassword=TLInfo['Password']
                    AgentInfo=GetAgent.get_AgentInfoFrom_TLMyteamInfo(self.tableturl, lobname, sitename, TLuserid, TLpassword)
                    AgentHrid=AgentInfo["Hrid"]
                    AgentPassword=AgentInfo["Password"]
                    AgentName=AgentInfo["Name"]'''
                    #AgentInfo=GetAgent.get_AgentInfoFromTablet(self.tableturl, lobname, sitename, self.OMuserid, self.OMpassword,"Month-To-Date")
                    #AgentInfo=GetAgent.get_AgentInfoFromTablet(tableturl, lobname, sitename, self.OMuserid, self.OMpassword, "Month-To-Date", self.adminurl)
                    AgentInfo=GetAgent.get_TLandAgentInfofromAdmin_Byrole(Adminurl, lobname, sitename, self.OMuserid, self.OMpassword, "Agent")
                    AgentHrid=AgentInfo["Hrid"]
                    AgentPassword=AgentInfo["Password"]
                    AgentName=AgentInfo["Name"]
                    
                                          
                    #Step1:Agent Login tablet   
                    L=Login()                
                    L.Login_tablet(tableturl,lobname, sitename, AgentHrid, AgentPassword)
                    time.sleep(Gl.waittime)
                    #Step2.1:Check TabletHomepage
                    
                    #Check performance circle
                    assert Tablet.get_performancename() == "Performance"#Verify performance displayed
                    #Check MyAchievement circle
                    assert Tablet.get_MyAchievementname() == "My Achievement"#Verify My Achievement displayed
                    #Check coaching circle
                    assert Tablet.get_Agent_coachingname() == "Coaching"#Verify Coaching displayed
                    
                    #Step2.2:Check Agent name and LOB&SITE
                    Header=HeaderPage()
                    assert Header.get_loginName()==AgentName
                    assert Header.get_loginRole()=="AGENT"
                    assert Header.get_loginLob()==lobname
                    assert Header.get_loginSite()==sitename
                    #Step2.3:Check page title
                    assert Header.get_HeaderTittle()=="Performance Pro 360"
                    
                    #Step3:Change password
                    #Step3.1: Enter to change password page
                    Header.click_settingButton()
                    Header.click_changePasswordLink()
                    assert Header.get_HeaderTittle()=="Change Password"
                    #Step3.2:Input all password and click Cancel button
                    NewPassword="1A @b!"
                    ChUserInfo.ChangePassword_Cancel(AgentPassword, NewPassword, NewPassword)
                    #Check back to tablet homepage after click cancel button
                    assert Header.get_HeaderTittle()=="Performance Pro 360"
                    L.logout_tablet()
                    #Verify the password of agent is not changed,Login with TL
                    #AgentInfo_new1=GetAgent.get_AgentInfoFromTablet(self.tableturl, lobname, sitename, self.OMuserid, self.OMpassword,"Month-To-Date")
                    AgentInfo_new1=GetAgent.get_TLandAgentInfofromAdmin(Adminurl, lobname, sitename, self.OMuserid, self.OMpassword, AgentHrid)
                    AgentPassword_new1=AgentInfo_new1["Password"]
                    print AgentPassword_new1,AgentPassword
                    assert AgentPassword_new1==AgentPassword
                    
                    #Step4:renter to change password page to change password
                    L.Login_tablet(tableturl,lobname, sitename, AgentHrid, AgentPassword)
                    time.sleep(Gl.waittime)
                    Header.click_settingButton()
                    Header.click_changePasswordLink()
                    ChUserInfo.ChangePassword_Save(AgentPassword, NewPassword, NewPassword)
                    ChangePWDwaring=ChangPwd_warningPage()
                    #assert ChangePWDwaring.get_waringtitle()=="Succeed"
                    assert ChangePWDwaring.get_warningmessage()=="Your password is successfully changed. Please use your new password to login again."
                    ChangePWDwaring.click_OKbutton()
                    #Step5: Re-Login tablet with old password
                    L.Login_tablet(tableturl, lobname, sitename, AgentHrid, AgentPassword)
                    LoginTablet=LogintabletPage(tableturl,Gl.driver)
                    #assert LoginTablet.get_IDorPWDincorectInfo()=="Incorrect ID or Password."
                    #Step6: Re-Login tablet with new password
                    L.Login_tablet(tableturl, lobname, sitename, AgentHrid, NewPassword)
                    #Check performance circle
                    assert Tablet.get_performancename() == "Performance"#Verify performance displayed
                    #Check MyAchievement circle
                    assert Tablet.get_MyAchievementname() == "My Achievement"#Verify My Achievement displayed
                    #Check coaching circle
                    assert Tablet.get_Agent_coachingname() == "Coaching"#Verify Coaching displayed
                    L.logout_tablet()
                    #Step7:Try to login Admin
                    L.Login_admin(Adminurl, lobname, sitename, AgentHrid, NewPassword)
                    LoginAdmin=LoginAdminPage(Adminurl,Gl.driver)
                    time.sleep(Gl.waittime)
                    assert LoginAdmin.get_nopermission()=="You don't have enough permission."
                    #Step9:Verify the password has been changed to the new one
                    #AgentInfo_new2=GetAgent.get_AgentInfoFromTablet(self.tableturl, lobname, sitename, self.OMuserid, self.OMpassword,"Month-To-Date")
                    AgentInfo_new2=GetAgent.get_TLandAgentInfofromAdmin(Adminurl, lobname, sitename, self.OMuserid, self.OMpassword, AgentHrid)
                    AgentPassword_new2=AgentInfo_new2["Password"]
                    assert AgentPassword_new2==NewPassword
                    
                    #Step10: Reset the password to the oldone
                    L.Login_tablet(tableturl,lobname, sitename, AgentHrid, NewPassword)
                    Header.click_settingButton()
                    Header.click_changePasswordLink()
                    ChUserInfo.ChangePassword_Save(NewPassword, AgentPassword, AgentPassword)
                    ChangePWDwaring.click_OKbutton()
                    
                    GetConfig.print_EndTest_message(lobname, sitename)
                     
    def tearDown(self):
        #Gl.driver.quit() 
        pass  
        
          

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()