'''
Created on Dec 21, 2016

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
from Tablet_pages.TabletHomepage import TabletHomepage
from Tablet_pages.HeaderPage import HeaderPage
from AdminSystem_Pages.LoginAdminPage import LoginAdminPage
from AdminSystem_Pages.AddOMWarnningpage import AddOMWarningpage


class AddOMAccount(unittest.TestCase):
    


    def setUp(self):
        
        #Case ID
        self.caseID="AddOMAccount"
        
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
        #New OM's info
        self.firstname="Richard"
        self.lastname="Clayderman"
               



    def test_AddOMAccount(self):
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
                    #Step2.1:Check all OMs are showning sort by modification date
                    #Step3:Enter to Add OM page
                    OMindex=1
                    OMa=OMaccountPage(OMindex)
                    OMa.click_OMadd()
                    #Step4:Re-Generate password 
                    AddOM=OMAddPage()
                    AddOM.regenerate_password()
                    ##Can not find out any method to verify if the password is changed
                    
                    #Step5:Cancel add OM
                    AddOM.click_Cancel()
                    assert OMa.get_OMAtittle() == "Browse L3 Accounts"#Back to OM accounts page
                    #Step6: Enter to Add OM page and add OM again
                    time.sleep(Gl.waittime)
                    OMa.click_OMadd()
                    AddOM.input_fisrtname(self.firstname)
                    AddOM.input_lastname(self.lastname)
                    newhrid=self.OMuserid+"0"
                    AddOM.input_hrid(newhrid)
                    AddOM.click_addOM()
                    i=0
                    AddWarn=AddOMWarningpage()
                    while AddOM.warningwidonw_ispopup()==True:
                        AddWarn.click_OK()
                        print newhrid,
                        print " is existed.And try again!"
                        AddOM.clear_hrid()
                        newhrid=newhrid+str(i)
                        AddOM.input_hrid(newhrid)
                        AddOM.click_addOM()
                        i=i+1
                                       
                    newpassword=OMa.get_newOMpwd()
                    #Gl.driver.quit()
                    print "Create L3 successfully: ",
                    print self.firstname+" "+self.lastname+","+newhrid+','+newpassword 
                    L.logout_admin()                     
                    #Step7:Login Admin with new OM account
                    #L1=Login(self.url,lobname,sitename,newhrid,newpassword)
                    L.Login_admin(self.adminturl, lobname, sitename, newhrid, newpassword)
                    LAdminPage=LoginAdminPage(self.adminturl,Gl.driver)
                    assert LAdminPage.get_nopermission()=="You don't have enough permission."#Verify that OM(1,4) can not login Admin System.
                    #Step8: Login tablet with new OM account
                    time.sleep(Gl.waittime)
                    
                    #L2=Login(self.tableturl,lobname,sitename,newhrid,newpassword)
                    L.Login_tablet(self.tableturl,lobname,sitename,newhrid,newpassword)
                    TabletH=TabletHomepage()
                    #Check performance circle
                    assert TabletH.get_performancename() == "Performance"#Verify performance displayed
                    #Check coaching circle
                    assert TabletH.get_coachingname() == "Coaching"#Verify Coaching displayed
                    #Check triad coaching circle
                    assert TabletH.get_triadcoachingname()=="Triad Coaching"#Verify Triad Coaching displayed
                    #Check my team info circle
                    assert TabletH.get_myteaminfoname()=="My Team Info" #Verify My Team Info displayed
                    #Check adaptation circle
                    #assert TabletH.get_adaptationname()=="Adaptation Rate" #Verify Adaptation Rate displayed
                    H=HeaderPage()
                    #Check  tablet homepage tittle
                    assert H.get_HeaderTittle()=="Performance Pro 360" #Verify tablet homepage title is correct
                    #Check LOB
                    assert H.get_loginLob()==lobname #Verify lob is correct
                    #Check Site
                    assert H.get_loginSite()==sitename #Verify site is correct
                    #Check login name
                    OMname=self.firstname+" "+self.lastname
                    assert H.get_loginName()==OMname # Verify login name is correct
                    #Check Role
                    assert H.get_loginRole()=="L3" #Verify the role is correct
                    
                    L.logout_tablet()
                    GetConfig.print_EndTest_message(lobname, sitename)
                    
                        
        
        
    def tearDown(self):
        Gl.driver.quit()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()