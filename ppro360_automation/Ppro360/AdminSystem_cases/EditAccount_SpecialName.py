#coding=utf-8
'''
Created on Mar 6, 2017

@author: SabrinaGuo
'''
import unittest
from public_method.Get_configration_data import Get_configration_data
from public_method.Login import Login
import time
from public_method import Gl
from AdminSystem_Pages.AdminHomepage import AdminHomepage
from AdminSystem_Pages.OMaccountPage import OMaccountPage
from AdminSystem_Pages.OMEditPage import OMEditPage



class EditAccount_SpecialName(unittest.TestCase):


    def setUp(self):
        #Case ID
        self.caseID="EditAccount_SpecialName"
        
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


    def test_EditAccount_SpecialName(self):
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
                    #Step1:Login admin system
                    L=Login()
                    L.Login_admin(self.adminturl,lobname, sitename, self.OMuserid, self.OMpassword)
                    #Step2.1:Enter to OM account page
                    Admin=AdminHomepage()
                    Admin.Enter_OMaccountbrowse()
                    
                    #Step2.2:Search out the OM hrid which is need to be edit, and enter to the Edit page
                    OMindex=self.GetOMindex_fromlist(self.OMuserid)
                    OMa1=OMaccountPage(OMindex)
                    OMname=OMa1.get_newOMname()
                    print OMa1.get_newOMhrid()
                    OMa1.click_OMaccount()
                    time.sleep(Gl.waittime)
                    #Step2: Enter to Edit page
                    OMa1.click_Editbutton()#Enter to Edit page
                    time.sleep(Gl.waittime)
                    
                    #Step3.1:Verify a hint info pup-up says the last name is required while last is bank or space
                    oldfirstname=OMname.split(" ")[0]
                    oldlastname=OMname.split(" ")[1]
                    newfirstname=oldfirstname+" @"
                    lastname_space=" "
                    OMe=OMEditPage()
                    OMe.Input_firstname(newfirstname)
                    OMe.clear_lastname()
                    OMe.click_savebutton()
                    assert OMe.lastnameWarning_isdisplayed()#Verify lastname warning message is pop-up
                    assert OMe.get_lastnameWarning()=="This is required"#Verify lastname warning message is correct
                    OMe.Input_lastname(lastname_space)
                    OMe.click_savebutton()
                    assert OMe.lastnameWarning_isdisplayed()#Verify lastname warning message is pop-up
                    assert OMe.get_lastnameWarning()=="This is required"#Verify lastname warning message is correct
                    
                    #Step3.2:Verify long name can be updated (more than 50 characters)
                    firstname_long="The deal will speed up the deployment of the US' Terminal"
                    lastname_long="High Altitude Area Defense system in the ROK Testing"
                    OMe.Input_firstname(firstname_long)
                    time.sleep(Gl.waittime)
                    OMe.Input_lastname(lastname_long)
                    time.sleep(Gl.waittime)
                    OMe.click_savebutton()
                    time.sleep(Gl.waittime)
                    newOMname_long=firstname_long+" "+lastname_long
                    OMindex1=self.GetOMindex_fromlist(self.OMuserid)
                    assert OMindex1==1
                    OMa2=OMaccountPage(OMindex1)
                    assert OMa2.get_newOMname()==newOMname_long#Verify OMname_long is correct
            
                    #Step3.3:Verify short name can be updated (one character)
                    firstname_short="Q"
                    lastname_short="A"
                    OMa2.click_OMaccount()
                    time.sleep(Gl.waittime)
                    OMa2.click_Editbutton()
                    time.sleep(Gl.waittime)
                    OMe.Input_firstname(firstname_short)
                    time.sleep(Gl.waittime)
                    OMe.Input_lastname(lastname_short)
                    time.sleep(Gl.waittime)
                    OMe.click_savebutton()
                    time.sleep(Gl.waittime)
                    newOMname_short=firstname_short+" "+lastname_short
                    OMindex2=self.GetOMindex_fromlist(self.OMuserid)
                    assert OMindex2==1
                    OMa3=OMaccountPage(OMindex2)
                    assert OMa3.get_newOMname()==newOMname_short#Verify OMname_short is correct
                    
                    #Step3.4:Verify other language name can be updated(Chinese ...)
                    firstname_other="ruanjian"
                    lastname_other="12"
                    OMa3.click_OMaccount()
                    time.sleep(Gl.waittime)
                    OMa3.click_Editbutton()
                    time.sleep(Gl.waittime)
                    OMe.Input_firstname(firstname_other)
                    time.sleep(Gl.waittime)
                    OMe.Input_lastname(lastname_other)
                    time.sleep(Gl.waittime)
                    OMe.click_savebutton()
                    time.sleep(Gl.waittime)
                    newOMname_other=firstname_other+" "+lastname_other
                    OMindex3=self.GetOMindex_fromlist(self.OMuserid)
                    assert OMindex3==1
                    OMa4=OMaccountPage(OMindex3)
                    assert OMa4.get_newOMname()==newOMname_other#Verify OMname_other is correct
                    
                    #Step4:Reset OMname to the old one
                    OMa4.click_OMaccount()
                    time.sleep(Gl.waittime)
                    OMa4.click_Editbutton()
                    time.sleep(Gl.waittime)
                    OMe.Input_firstname(oldfirstname)
                    time.sleep(Gl.waittime)
                    OMe.Input_lastname(oldlastname)
                    time.sleep(Gl.waittime)
                    OMe.click_savebutton()
                    L.logout_admin()
                    GetConfig.print_EndTest_message(lobname, sitename)
                    
                        
 
    def GetOMindex_fromlist(self,userid):  
        OMindex=1
        Flag=True
        while Flag:
            OMa=OMaccountPage(OMindex)
            if OMa.get_newOMhrid()==self.OMuserid:
                #return OMa1.get_newOMname()#Return new OMname from OM account list
                return OMindex
                Flag=False
                break
            else:
                OMindex=OMindex+1
                continue 
                         
        
    def tearDown(self):
        Gl.driver.quit()
            


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()