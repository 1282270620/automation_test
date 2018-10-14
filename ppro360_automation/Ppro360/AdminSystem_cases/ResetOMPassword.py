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
from AdminSystem_Pages.OMAddPage import OMAddPage
from AdminSystem_Pages.OMResetPasswordPage import OMResetPasswordPage
from AdminSystem_Pages.LoginAdminPage import LoginAdminPage
from Tablet_pages.HeaderPage import HeaderPage
from AdminSystem_Pages.AddOMWarnningpage import AddOMWarningpage

class ResetOMPassword(unittest.TestCase):
    
    def setUp(self):
        #Case ID
        self.caseID="ResetOMPassword"
        
        GetData=Get_configration_data()
        #Get OM account
        OMaccount=GetData.get_OMaccount()
        self.OMuserid=OMaccount["OMuserid"]
        self.OMpassword=OMaccount["OMpassword"]
        #Get all lobs from CSV
        self.testLOBSITE_list=GetData.get_LOBSITEtoTest(self.caseID)
        #New OM's info
        self.firstname="Richard"
        self.lastname="Clayderman"


    def test_ResetOMPassword(self):
        GetConfig=Get_configration_data()
        #Test several LOBs
        for i in range(0,len(self.testLOBSITE_list)):
            Flag=GetConfig.get_LOBSITE_STATUS(self.testLOBSITE_list[i])
            if Flag==True:
                each_LOBSITE=self.testLOBSITE_list[i].split(":")
                lobname=each_LOBSITE[0]
                ##GET THE CORRECT URL#####
                adminurl=GetConfig.get_Test_AdminUrl(lobname)
                tableturl=GetConfig.get_Test_Tablet(lobname)
                ##GET THE CORRECT URL#####
                #Get Site to test
                site_list=each_LOBSITE[1].split("*")
                for n in range(0,len(site_list)):
                    sitename=site_list[n]
                    GetConfig.print_StartTest_message(lobname, sitename)
                    #Step1:Login admin system
                    L=Login()
                    L.Login_admin(adminurl,lobname, sitename, self.OMuserid, self.OMpassword)
                    #Step2:Enter to OM account page and Add a OM(1,4) for testing
                    Admin=AdminHomepage()
                    Admin.Enter_OMaccountbrowse()
                    OMaccount=OMaccountPage(1)
                    OMaccount.click_OMadd()
                    time.sleep(Gl.waittime)
                    OMadd=OMAddPage()
                    OMadd.input_fisrtname(self.firstname)
                    time.sleep(Gl.waittime)
                    OMadd.input_lastname(self.lastname)
                    time.sleep(Gl.waittime)
                    hrid=self.OMuserid+"0"
                    OMadd.input_hrid(hrid)
                    time.sleep(Gl.waittime)
                    OMadd.click_addOM()
                    time.sleep(Gl.waittime)
                    i=0
                    AddWarn=AddOMWarningpage()
                    while OMadd.warningwidonw_ispopup()==True:
                        AddWarn.click_OK()
                        #print hrid,
                        #print " is existed.And try again!"
                        OMadd.clear_hrid()
                        hrid=hrid+str(i)
                        OMadd.input_hrid(hrid)
                        OMadd.click_addOM()
                        i=i+1

                    OldPassword=OMaccount.get_newOMpwd()
                    #Step2:Verify the page of ResetPassword
                    OMaccount.click_OMaccount()
                    time.sleep(Gl.waittime)
                    OMaccount.click_ResetPWDbutton()
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
                    assert OMaccount.get_OMAtittle()=="Browse L3 Accounts"
                    assert OMaccount.get_newOMpwd()==OldPassword
                    #Step4:Verify save button is enable after click reset-password button
                    OMaccount.click_OMaccount()
                    time.sleep(Gl.waittime)
                    OMaccount.click_ResetPWDbutton()
                    #time.sleep(Gl.waittime)
                    OMRe.click_ResetPWDbutton()
                    time.sleep(Gl.waittime)
                    assert OMRe.SaveButton_disabled()=="btn btn-primary"
                    #Step5:Verify password is changed after click reset-password button and save button
                    OMRe.click_savebutton()
                    time.sleep(Gl.waittime)
                    assert OMaccount.get_OMAtittle()=="Browse L3 Accounts"
                    newOMpwd=OMaccount.get_newOMpwd()
                   
                    assert newOMpwd != OldPassword#Verify new password is not the same with old password
                    time.sleep(Gl.waittime)
                    L.logout_admin()
                    time.sleep(5*Gl.waittime)
                    #Step6: Verify this OM can not Login admin with new password(No permission)
                    #L=Login(self.url,lobname,sitename,self.hrid,newOMpwd)
                    L.Login_admin(adminurl,lobname, sitename, hrid,newOMpwd)
                    time.sleep(Gl.waittime)
                    LoginAdmin=LoginAdminPage(adminurl,Gl.driver)
                    assert LoginAdmin.get_nopermission()=="You don't have enough permission."
                    #Step7:Verify this OM can login tablet with new password
                    L.Login_tablet(tableturl, lobname, sitename,hrid,newOMpwd)
                    time.sleep(Gl.waittime)
                    Header=HeaderPage()
                    assert Header.get_HeaderTittle()=="Performance Pro 360"
                    
                    L.logout_tablet()
                    
                    GetConfig.print_EndTest_message(lobname, sitename)
     

    def tearDown(self):
        #Gl.driver.quit()
        pass
            


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()