'''
Created on Mar 21, 2017

@author: symbio
'''
import unittest
from public_method.Get_configration_data import Get_configration_data
from public_method.Login import Login
from Tablet_pages.HeaderPage import HeaderPage
from public_method.Get_AllRoleAccountForTest import Get_AllRoleAccountForTest
from public_method.AddOrChangeUserInfo import AddOrChangeUserInfo
from Tablet_pages.ChangePasswordPage import ChangePasswordPage
from public_method import Gl

class ChangeToInvalidPassword_LC(unittest.TestCase):


    def setUp(self):
        #Case ID
        self.caseID="ChangeToInvalidPassword_LC"
        
        GetData=Get_configration_data()
        #Get URL 
        self.tableturl=GetData.get_TabletUrl()
        self.adminurl=GetData.get_AdminUrl()
        #Get OM account
        OMaccount=GetData.get_OMaccount()
        self.OMuserid=OMaccount["OMuserid"]
        self.OMpassword=OMaccount["OMpassword"]
        #Get LC userid
        self.LCuserid=GetData.get_LCuserid()
        #Get all lobs from CSV
        self.testLOBSITE_list=GetData.get_LOBSITEtoTest(self.caseID)


    def test_ChangeToInvalidPassword_LC(self):
        GetLC=Get_AllRoleAccountForTest()
        ChUserInfo=AddOrChangeUserInfo()
        ChPWDpage=ChangePasswordPage()
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
                    #Step0:Login admin system to get LC's Password
                    LCInfo=GetLC.get_LCInfo(self.adminurl,lobname, sitename, self.OMuserid, self.OMpassword, self.LCuserid)
                    #LCname=LCInfo['Name']
                    LCpassword=LCInfo["Password"]
                    #Step1:LC Login tablet                   
                    L=Login()
                    L.Login_tablet(self.tableturl,lobname, sitename, self.LCuserid, LCpassword)
                    #Step2:Enter to ChangePassword page
                    Header=HeaderPage()
                    Header.click_settingButton()
                    #Step2.1:Verify changepassword and logout is shown correctly
                    #print Header.ChangePassword_Existed()
                    #assert Header.ChangePassword_Existed()==True
                    #print Header.Logout_Existed()
                    #assert Header.Logout_Existed()==True
                    Header.click_changePasswordLink()
                    assert Header.get_HeaderTittle()=="Change Password"
                    #Step2.2:Verify new password and re-new password are space
                    currentPassword=LCpassword
                    newPassword='      '
                    reNewPassword='      '
                    ChUserInfo.ChangePassword_Save(currentPassword, newPassword, reNewPassword)
                    assert ChPWDpage.get_newpasswordmessage()=="Password may not be empty."
                    #Step2.3:Verify currentPassword is not correct
                    currentPassword='1A 2B33'
                    newPassword='111111'
                    reNewPassword='111111'
                    ChUserInfo.ChangePassword_Save(currentPassword, newPassword, reNewPassword)
                    #assert ChPWDpage.get_currentpasswordmessage()=="Incorrect password"
                    assert ChPWDpage.get_Incorrectpasswordmessage()=="error Incorrect password"
                    #Step2.4:Verify new password doesn't match.
                    currentPassword=LCpassword
                    newPassword='123321'
                    reNewPassword='1234567'
                    ChUserInfo.ChangePassword_Save(currentPassword, newPassword, reNewPassword)
                    assert ChPWDpage.get_renewpasswordmessage()=="new password doesn't match."
                    #Step2.5:Verify 21 characters: 'Password must be 6-20 characters.'
                    currentPassword=LCpassword
                    newPassword='00 1 qedc$rfvTGB~!@#$'#21 characters
                    reNewPassword='00 1 qedc$rfvTGB~!@#$'#21 characters
                    ChUserInfo.ChangePassword_Save(currentPassword, newPassword, reNewPassword)
                    assert ChPWDpage.get_newpasswordmessage()=="Password must be 6-20 characters."
                    #Step2.6:Verify 1 character: 'Password must be 6-20 characters.'
                    currentPassword=LCpassword
                    newPassword="0" #1 characters
                    reNewPassword="0" #1 characters
                    ChUserInfo.ChangePassword_Save(currentPassword, newPassword, reNewPassword)
                    assert ChPWDpage.get_newpasswordmessage()=="Password must be 6-20 characters."
                    #Step2.7: Verify all are empty
                    currentPassword=""
                    newPassword=""
                    reNewPassword=""
                    ChUserInfo.ChangePassword_Save(currentPassword, newPassword, reNewPassword)
                    assert ChPWDpage.get_currentpasswordmessage()=="Password may not be empty."
                    #Step2.8:Verify all are LCpassword
                    currentPassword=LCpassword
                    newPassword=LCpassword
                    reNewPassword=LCpassword
                    ChUserInfo.ChangePassword_Save(currentPassword, newPassword, reNewPassword)
                    assert ChPWDpage.get_newpasswordmessage()=="new password must be different from the current password."
                    
                    L.logout_tablet()
                    
                    
                    GetConfig.print_EndTest_message(lobname, sitename)
        
    def tearDown(self):
        Gl.driver.quit()                   

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_ChangeToInvalidPassword_LC']
    unittest.main()