'''
Created on Mar 7, 2017

@author: SabrinaGuo
'''
import unittest
from public_method.Get_configration_data import Get_configration_data
from public_method.Login import Login
import time
from public_method import Gl
from AdminSystem_Pages.AdminHomepage import AdminHomepage
from AdminSystem_Pages.OMaccountPage import OMaccountPage
from AdminSystem_Pages.OMResetPasswordPage import OMResetPasswordPage
from AdminSystem_Pages.LoginAdminPage import LoginAdminPage
from Tablet_pages.HeaderPage import HeaderPage
from public_method.Get_AllRoleAccountForTest import Get_AllRoleAccountForTest

class ResetLCPassword(unittest.TestCase):
    
    def setUp(self):
        #Case ID
        self.caseID="ResetLCPassword"
        
        GetData=Get_configration_data()
        #Get URL 
        self.adminturl=GetData.get_AdminUrl()
        self.tableturl=GetData.get_TabletUrl()
        #Get OM account
        OMaccount=GetData.get_OMaccount()
        self.OMuserid=OMaccount["OMuserid"]
        self.OMpassword=OMaccount["OMpassword"]
        #Get LC userid
        self.LCuserid=GetData.get_LCuserid()
        #Get all lobs from CSV
        self.testLOBSITE_list=GetData.get_LOBSITEtoTest(self.caseID)
        #New OM's info
        self.firstname="Richard"
        self.lastname="Clayderman"

    def test_ResetLCPassword(self):
        GetLC=Get_AllRoleAccountForTest()
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
                    #Step0:Get LCpassword
                    LCInfo=GetLC.get_LCInfo(self.adminturl,lobname, sitename, self.OMuserid, self.OMpassword, self.LCuserid)
                    LCpassword=LCInfo["Password"]
                    OMindex=LCInfo["OMindex"]
                    #Step1:Login admin system
                    L=Login()
                    L.Login_admin(self.adminturl,lobname, sitename, self.OMuserid, self.OMpassword)
                    #Step2.1:Enter to OM account page
                    Admin=AdminHomepage()
                    Admin.Enter_OMaccountbrowse()
                        
                    #Step2.2:Search out the LC hrid which is need to be edit, and enter to the Edit page
                    OMa=OMaccountPage(OMindex)
                    #Step2:Verify the page of ResetPassword
                    OMa.click_OMaccount()
                    time.sleep(Gl.waittime)
                    OMa.click_ResetPWDbutton()
                    time.sleep(Gl.waittime)
                    OMRe=OMResetPasswordPage()
                    assert OMRe.get_pagetitle()=="Reset Password"
                    assert OMRe.get_firstnametitle()=="First Name:"
                    assert OMRe.firstnameInput_disabled()
                    assert OMRe.get_lastnametitle()=="Last Name:"
                    assert OMRe.lastnameInput_disabled()
                    assert OMRe.get_hridtitle()=="HR ID:"
                    assert OMRe.hridInput_disabled()
                    assert OMRe.get_pwdtitle()=="Password:"
                    assert OMRe.pwdInput_disabled()
                    assert OMRe.SaveButton_disabled()
                    assert OMRe.CancelButton_disabled()=="btn btn-primary"
                    #Step3:Verify the password is not changed if click cancel button
                    OMRe.click_cancelbutton()
                    time.sleep(Gl.waittime)
                    assert OMa.get_OMAtittle()=="Browse L3 Accounts"
                    assert OMa.get_newOMpwd()==LCpassword
                    #Step4:Verify save button is enable after click reset-password button
                    OMa.click_OMaccount()
                    time.sleep(Gl.waittime)
                    OMa.click_ResetPWDbutton()
                    time.sleep(Gl.waittime)
                    OMRe.click_ResetPWDbutton()
                    time.sleep(Gl.waittime)
                    assert OMRe.SaveButton_disabled()=="btn btn-primary"
                    #Step5:Verify password is changed after click reset-password button and save button
                    OMRe.click_savebutton()
                    time.sleep(Gl.waittime)
                    assert OMa.get_OMAtittle()=="Browse L3 Accounts"
                    newOMpwd=OMa.get_newOMpwd()
                    print newOMpwd
                    assert newOMpwd != LCpassword#Verify new password is not the same with old password
                    time.sleep(Gl.waittime)
                    L.logout_admin()
                    #Step6: Verify this LC can not Login admin with new password(No permission)
                    L.Login_admin(self.adminturl,lobname, sitename, self.LCuserid,newOMpwd)
                    time.sleep(Gl.waittime)
                    LoginAdmin=LoginAdminPage(self.adminturl,Gl.driver)
                    time.sleep(Gl.waittime)
                    print LoginAdmin.get_nopermission()
                    assert LoginAdmin.get_nopermission()=="You don't have enough permission."
                    #Step7:Verify this LC can login tablet with new password
                    L.Login_tablet(self.tableturl, lobname, sitename,self.LCuserid,newOMpwd)
                    time.sleep(Gl.waittime)
                    Header=HeaderPage()
                    assert Header.get_HeaderTittle()=="Performance Pro 360"
                    
                    L.logout_tablet()
                    
                    GetConfig.print_EndTest_message(lobname, sitename)
     

    def tearDown(self):
        Gl.driver.quit()
            


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()