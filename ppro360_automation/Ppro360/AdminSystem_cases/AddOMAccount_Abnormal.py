'''
Created on 2017/3/2

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
from AdminSystem_Pages.AddOMWarnningpage import AddOMWarningpage


class AddOMAccount_Abnormal(unittest.TestCase):
    
    def setUp(self):
        
        #Case ID
        self.caseID="AddOMAccount_Abnormal"
        
        GetData=Get_configration_data()
        #Get URL 
        self.adminturl=GetData.get_AdminUrl()
        #Get OM account
        OMaccount=GetData.get_OMaccount()
        self.OMuserid=OMaccount["OMuserid"]
        self.OMpassword=OMaccount["OMpassword"]
        #Get all lobs from CSV
        self.testLOBSITE_list=GetData.get_LOBSITEtoTest(self.caseID)
        #New OM's info
        self.firstname="Richard"
        self.lastname="Clayderman"

    def test_AddOMAccount_Abnormal(self):
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
                    #Step2:Enter to OM account page
                    Admin=AdminHomepage()
                    Admin.Enter_OMaccountbrowse()
                    #Step3:Enter to Add OM page
                    OMindex=1
                    OMa=OMaccountPage(OMindex)
                    OMa.click_OMadd()
                    #Step4:Start to verify "Add OM with special conditions"
                    #Step4.1.1: valid First name, valid last name,HRID=an existing HRID+[space] 
                    AddOM=OMAddPage()
                    AddOM.input_fisrtname(self.firstname)
                    AddOM.input_lastname(self.lastname)
                    hrid_space=self.OMuserid+' '
                    AddOM.input_hrid(hrid_space)
                    time.sleep(Gl.waittime)
                    AddOM.click_addOM()
                    time.sleep(Gl.waittime)
                    #Step4.1.2: Verify if there is a windown pop-up said the hrid existed
                    assert AddOM.warningwidonw_ispopup()
                    AW=AddOMWarningpage()
                    AW.click_OK()
                    ##Step4.2.1: valid First name, no last name,special hrid
                    hrid_sp="^&*221"
                    AddOM.clear_lastname()
                    AddOM.input_hrid(hrid_sp)
                    time.sleep(Gl.waittime)
                    AddOM.click_addOM()
                    time.sleep(Gl.waittime)
                    ##Step4.2.2: Verify if there is a warning message says that last name is required.
                    assert AddOM.lastnameWarning_isdisplayed()
                    ##Step4.3.1: First Name = long text more than 50 characters,Last Name = [space],HR ID = more than 10 digits.
                    firstname_long="The deal will speed up the deployment of the US' Terminal High Altitude Area"
                    lastname_space=" "
                    hrid_long="12345678910"
                    AddOM.input_fisrtname(firstname_long)
                    AddOM.input_lastname(lastname_space)
                    AddOM.input_hrid(hrid_long)
                    AddOM.click_addOM()
                    ##Step4.3.2: Verify if there is a warning message says that last name is required.
                    time.sleep(Gl.waittime)
                    assert AddOM.lastnameWarning_isdisplayed()
                    ##Step4.4.1:First Name = long text more than 20 characters,Last Name = long text more than 20 characters,HR ID = more than 10 digits.
                    lastname_long="Defense system in the ROK"
                    AddOM.input_fisrtname(firstname_long)
                    AddOM.input_lastname(lastname_long)
                    AddOM.input_hrid(hrid_long)
                    AddOM.click_addOM()
                    i=0
                    while AddOM.warningwidonw_ispopup()==True:
                        AW.click_OK()
                        AddOM.clear_hrid()
                        hrid_long=hrid_long+str(i)
                        AddOM.input_hrid(hrid_long)
                        AddOM.click_addOM()
                        i=i+1
                                               
                    #Step4.4.2:Verify all info is the same as standard
                    time.sleep(2*Gl.waittime)
                    assert OMa.get_newOMname()==firstname_long+' '+lastname_long
                    assert OMa.get_newOMhrid()==hrid_long
                    
                    GetConfig.print_EndTest_message(lobname, sitename)
                                          

    def tearDown(self):
        Gl.driver.quit()
            


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()