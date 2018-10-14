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
from AdminSystem_Pages.AdminHomepage import AdminHomepage
from AdminSystem_Pages.OMaccountPage import OMaccountPage
from public_method.Get_AllRoleAccountForTest import Get_AllRoleAccountForTest
from public_method.AddOrChangeUserInfo import AddOrChangeUserInfo

class ChangePassword_OM(unittest.TestCase):

    def setUp(self):
        #Case ID
        self.caseID="ChangePassword_OM"
        
        GetData=Get_configration_data()
        #Get URL 
        self.adminturl=GetData.get_AdminUrl()
        self.tableturl=GetData.get_TabletUrl()
        #Get OM account
        OMaccount=GetData.get_OMaccount()
        self.OMuserid=OMaccount["OMuserid"]
        self.OMpassword=OMaccount["OMpassword"]
        #Get all lobs from CSV
        self.testLOBSITE_list=GetData.get_LOBSITEtoTest(self.caseID)


    def test_ChangePassword_OM(self):
        GetOM=Get_AllRoleAccountForTest()
        ChUserInfo=AddOrChangeUserInfo()
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
                    #Step0:Login admin system to Add a OM(1,4) for testing
                    L=Login()
                    L.Login_admin(self.adminturl,lobname, sitename, self.OMuserid, self.OMpassword)
                    #Step2:Enter to OM account page and Add a OM(1,4) for testing
                    OMfirstname="Testfirst"
                    OMlastname="Testlast"
                    NewOMhrid=self.OMuserid+"0"
                    Admin=AdminHomepage()
                    Admin.Enter_OMaccountbrowse()
                    OMaccount=OMaccountPage(1)
                    OMaccount.click_OMadd()
                    time.sleep(Gl.waittime)
                    NewOMhrid=ChUserInfo.AddOMatAdmin(OMfirstname, OMlastname, NewOMhrid)
                    
                    #Enter to OM account page and Search out the OM hrid which is need to be changed password
                    
                    NewOMinfo=GetOM.get_AccountFromAdmin(NewOMhrid)
                    OMname=NewOMinfo["Name"]
                    Oldpassword=NewOMinfo["Password"]
                    
                    L.logout_admin()                       
                    #Step1:OM(1,4) Login tablet                   
                    L.Login_tablet(self.tableturl,lobname, sitename, NewOMhrid, Oldpassword)
                    #Step2.1:Check TabletHomepage
                    Tablet=TabletHomepage()
                    #Check performance circle
                    assert Tablet.get_performancename() == "Performance"#Verify performance displayed
                    #Check coaching circle
                    assert Tablet.get_coachingname() == "Coaching"#Verify Coaching displayed
                    #Check triad coaching circle
                    assert Tablet.get_triadcoachingname()=="Triad Coaching"#Verify Triad Coaching displayed
                    #Check adaptation circle
                    #assert Tablet.get_adaptationname()=="Adaptation Rate" #Verify Adaptation Rate displayed
                    #Check My Team Info circle
                    assert Tablet.get_myteaminfoname()=="My Team Info"#Verify My Team Info displayed
                    #Check Coaching Export
                    assert  Tablet.get_CoachingExportname_OM()=="Coaching Export"
                    
                    #Step2.2:Check LC name and LOB&SITE
                    Header=HeaderPage()
                    assert Header.get_loginName()==OMname
                    assert Header.get_loginRole()=="L3"
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
                    
                    ChUserInfo.ChangePassword_Cancel(Oldpassword, NewPassword, NewPassword)
                    #Check back to tablet homepage after click cancel button
                    assert Header.get_HeaderTittle()=="Performance Pro 360"
                    L.logout_tablet()
                    #Check password is not changed after click Cancel button
                    L.Login_admin(self.adminturl,lobname, sitename, self.OMuserid, self.OMpassword)
                    
                    OM_AccountInfo_new1=GetOM.get_AccountFromAdmin(NewOMhrid)
                    assert OM_AccountInfo_new1['Password']==Oldpassword
                    L.logout_admin()
                    
                    #Step4:renter to change password page to change password
                    L.Login_tablet(self.tableturl,lobname, sitename, NewOMhrid, Oldpassword)
                    Header.click_settingButton()
                    Header.click_changePasswordLink()
                    print Oldpassword
                    print NewPassword
                    ChUserInfo.ChangePassword_Save(Oldpassword, NewPassword, NewPassword)
                    ChangePWDwaring=ChangPwd_warningPage()
                    assert ChangePWDwaring.get_waringtitle()=="Succeed"
                    assert ChangePWDwaring.get_warningmessage()=="Your password is successfully changed. Please use your new password to login again."
                    ChangePWDwaring.click_OKbutton()
                    
                    #Step5: Re-Login tablet with old password
                    L.Login_tablet(self.tableturl,lobname, sitename, NewOMhrid, Oldpassword)
                    LoginTablet=LogintabletPage(self.tableturl,Gl.driver)
                    #assert LoginTablet.get_IDorPWDincorectInfo()=="Incorrect ID or Password."
                    #Step6: Re-Login tablet with new password
                    L.Login_tablet(self.tableturl,lobname, sitename, NewOMhrid, NewPassword)
                    #Check performance circle
                    assert Tablet.get_performancename() == "Performance"#Verify performance displayed
                    #Check coaching circle
                    assert Tablet.get_coachingname() == "Coaching"#Verify Coaching displayed
                    #Check triad coaching circle
                    assert Tablet.get_triadcoachingname()=="Triad Coaching"#Verify Triad Coaching displayed
                    #Check adaptation circle
                    #assert Tablet.get_adaptationname()=="Adaptation Rate" #Verify Adaptation Rate displayed
                    #Check My Team Info circle
                    assert Tablet.get_myteaminfoname()=="My Team Info"#Verify My Team Info displayed
                    #Check Coaching Export
                    assert  Tablet.get_CoachingExportname_OM()=="Coaching Export"
                    L.logout_tablet()
                    #Step7:Try to login Admin
                    L.Login_admin(self.adminturl,lobname, sitename, NewOMhrid, NewPassword)
                    LoginAdmin=LoginAdminPage(self.adminturl,Gl.driver)
                    time.sleep(Gl.waittime)
                    assert LoginAdmin.get_nopermission()=="You don't have enough permission."
                    #Step8: Login with Admin account to check the new password
                    L.Login_admin(self.adminturl,lobname, sitename, self.OMuserid, self.OMpassword)
                    OM_AccountInfo_new2=GetOM.get_AccountFromAdmin(NewOMhrid)
                    assert OM_AccountInfo_new2['Password']==NewPassword
                    L.logout_admin()
                    time.sleep(Gl.waittime)
                    
                    #Step9: Reset the password to the oldone
                    L.Login_tablet(self.tableturl,lobname, sitename, NewOMhrid, NewPassword)
                    time.sleep(Gl.waittime)
                    Header.click_settingButton()
                    Header.click_changePasswordLink()
                    ChUserInfo.ChangePassword_Save(NewPassword, Oldpassword, Oldpassword)
                    ChangePWDwaring.click_OKbutton()

                    
                    GetConfig.print_EndTest_message(lobname, sitename)
    
                     
    def tearDown(self):
        #Gl.driver.quit()
        pass   
        
          

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()