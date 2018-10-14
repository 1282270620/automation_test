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

class ChangePassword_TL(unittest.TestCase):


    def setUp(self):
        #Case ID
        self.caseID="ChangePassword_TL"
        
        GetData=Get_configration_data()
        #Get URL 
        self.Adminurl=GetData.get_AdminUrl()
        self.tableturl=GetData.get_TabletUrl()
        #Get OM account
        OMaccount=GetData.get_OMaccount()
        self.OMuserid=OMaccount["OMuserid"]
        self.OMpassword=OMaccount["OMpassword"]
        #Get all lobs from CSV
        self.testLOBSITE_list=GetData.get_LOBSITEtoTest(self.caseID)

    def test_ChangePassword_TL(self):
        GetTL=Get_AllRoleAccountForTest()
        ChUserInfo=AddOrChangeUserInfo()
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
                    #Step0:Login tablet system and enter to My Team Info to select the first TL for testing
                    TL_userid=GetTL.get_TLInfoFromMyteamInfo(self.tableturl,lobname, sitename, self.OMuserid, self.OMpassword)
                    TLinfo=GetTL.get_TLandAgentInfofromAdmin(self.Adminurl, lobname, sitename, self.OMuserid, self.OMpassword, TL_userid)
                    TLname=TLinfo["Name"]
                    TLhrid=TLinfo["Hrid"]
                    TLpassword=TLinfo["Password"]
                    time.sleep(Gl.waittime)
                                          
                    #Step1:TL Login tablet    
                    L=Login()               
                    L.Login_tablet(self.tableturl,lobname, sitename, TLhrid, TLpassword)
                    time.sleep(Gl.waittime)
                    #Step2.1:Check TabletHomepage
                    
                    #Check performance circle
                    assert Tablet.get_performancename() == "Performance"#Verify performance displayed
                    #Check Outlier circle
                    assert Tablet.get_TL_outliername() == "Outlier"#Verify Outlier displayed
                    #Check coaching circle
                    assert Tablet.get_TL_coachingname() == "Coaching"#Verify Coaching displayed
                    #Check triad coaching circle
                    assert Tablet.get_TL_triadcoachingname()=="Triad Coaching"#Verify Triad Coaching displayed
                    #Check My Team Info circle
                    assert Tablet.get_TL_myteaminfoname()=="My Team Info"#Verify My Team Info displayed
                    #Check Coaching Export
                    assert  Tablet.get_CoachingExportname_TL()=="Coaching Export"
                    
                    #Step2.2:Check LC name and LOB&SITE
                    Header=HeaderPage()
                    assert Header.get_loginName()==TLname
                    assert Header.get_loginRole()=="TL"
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
                    ChUserInfo.ChangePassword_Cancel(TLpassword, NewPassword, NewPassword)
                    #Check back to tablet homepage after click cancel button
                    assert Header.get_HeaderTittle()=="Performance Pro 360"
                    L.logout_tablet()
                    TLInfo_new1=GetTL.get_TLandAgentInfofromAdmin(self.Adminurl, lobname, sitename, self.OMuserid, self.OMpassword, TL_userid)
                    
                    L.Login_tablet(self.tableturl, lobname, sitename, self.OMuserid, self.OMpassword)
                    Tablet.click_Myteaminfocircle()
                    assert TLInfo_new1["Password"]==TLpassword
                    L.logout_tablet()
                    #Step4:renter to change password page to change password
                    L.Login_tablet(self.tableturl,lobname, sitename, TLhrid, TLpassword)
                    time.sleep(Gl.waittime)
                    Header.click_settingButton()
                    Header.click_changePasswordLink()
                    ChUserInfo.ChangePassword_Save(TLpassword, NewPassword, NewPassword)
                    ChangePWDwaring=ChangPwd_warningPage()
                    #assert ChangePWDwaring.get_waringtitle()=="Succeed"
                    assert ChangePWDwaring.get_warningmessage()=="Your password is successfully changed. Please use your new password to login again."
                    ChangePWDwaring.click_OKbutton()
                    #Step5: Re-Login tablet with old password
                    L.Login_tablet(self.tableturl, lobname, sitename, TLhrid, TLpassword)
                    LoginTablet=LogintabletPage(self.tableturl,Gl.driver)
                    #assert LoginTablet.get_IDorPWDincorectInfo()=="Incorrect ID or Password."
                    #Step6: Re-Login tablet with new password
                    L.Login_tablet(self.tableturl, lobname, sitename, TLhrid, NewPassword)
                    #Check performance circle
                    assert Tablet.get_performancename() == "Performance"#Verify performance displayed
                    #Check Outlier circle
                    assert Tablet.get_TL_outliername() == "Outlier"#Verify Outlier displayed
                    #Check coaching circle
                    assert Tablet.get_TL_coachingname() == "Coaching"#Verify Coaching displayed
                    #Check triad coaching circle
                    assert Tablet.get_TL_triadcoachingname()=="Triad Coaching"#Verify Triad Coaching displayed
                    #Check My Team Info circle
                    assert Tablet.get_TL_myteaminfoname()=="My Team Info"#Verify My Team Info displayed
                    #Check Coaching Export
                    assert  Tablet.get_CoachingExportname_TL()=="Coaching Export"
                    L.logout_tablet()
                    #Step7:Try to login Admin
                    L.Login_admin(self.Adminurl, lobname, sitename, TLhrid, NewPassword)
                    LoginAdmin=LoginAdminPage(self.Adminurl,Gl.driver)
                    time.sleep(Gl.waittime)
                    assert LoginAdmin.get_nopermission()=="You don't have enough permission."
                    #Step9:Verify the password has been changed to the newone
                    TLInfo_new2=GetTL.get_TLandAgentInfofromAdmin(self.Adminurl, lobname, sitename, self.OMuserid, self.OMpassword, TL_userid)
                    L.Login_tablet(self.tableturl, lobname, sitename, self.OMuserid, self.OMpassword)
                    Tablet.click_Myteaminfocircle()
                    assert TLInfo_new2["Password"]==NewPassword
                    L.logout_tablet()
                    
                    #Step10: Reset the password to the oldone
                    L.Login_tablet(self.tableturl,lobname, sitename, TLhrid, NewPassword)
                    time.sleep(Gl.waittime)
                    Header.click_settingButton()
                    Header.click_changePasswordLink()
                    ChUserInfo.ChangePassword_Save(NewPassword, TLpassword, TLpassword)
                    ChangePWDwaring.click_OKbutton()
                    
                    
                    GetConfig.print_EndTest_message(lobname, sitename)
                 
    def tearDown(self):
        Gl.driver.quit()   
        
          

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()