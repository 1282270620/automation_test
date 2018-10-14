'''
Created on 2017/3/3

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
from Tablet_pages.HeaderPage import HeaderPage
from Tablet_pages.TabletHomepage import TabletHomepage
from Tablet_pages.Coachinghomepage import Coachinghomepage
from Tablet_pages.TriadCoachinghomepage import TriadCoachinghomepage
from AdminSystem_Pages.LoginAdminPage import LoginAdminPage
from public_method.Get_AllRoleAccountForTest import Get_AllRoleAccountForTest


class AdminEditLCAccountName(unittest.TestCase):
    


    def setUp(self):
        #Case ID
        self.caseID="AdminEditLCAccountName"
        
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
        
        
    def test_AdminEditLCAccountName(self):
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
                    LCname=LCInfo["Name"]
                    OMindex=LCInfo["OMindex"]
                    
                    #Step1:Login admin system
                    L=Login()
                    L.Login_admin(self.adminturl,lobname, sitename, self.OMuserid, self.OMpassword)
                    #Step2.1:Enter to OM account page
                    Admin=AdminHomepage()
                    Admin.Enter_OMaccountbrowse()
                    
                    #Step2.2:Search out the LC hrid which is need to be edit, and enter to the Edit page
                    OMe=OMEditPage()
                    OMa=OMaccountPage(OMindex)
                    
                    OMa.click_OMaccount()
                    time.sleep(Gl.waittime)
                    OMa.click_Editbutton()#Enter to Edit page
                    time.sleep(Gl.waittime)
                    #Step2.2.1: Verify all elements for Edit page
                    assert OMe.get_pagetitle()=="Edit Account"#Check Edit page title
                    assert OMe.get_firstnametitle()=="First Name:"#Check firstname
                    assert OMe.get_lastnametitle()=="Last Name:"#Check lastname
                    assert OMe.get_hridtitle()=="HR ID:"#Check hrid name
                    assert OMe.hridInput_disabled()#Check hrid can not be input
                    assert OMe.get_pwdtitle()=="Password:"#Check Password name
                    assert OMe.pwdInput_disabled()#Check hrid can not be input
                    assert OMe.get_savebutton()=="Save"#Check Save button
                    assert OMe.get_cancelbutton()=="Cancel"#Check Cancel button
                    
                    #Step3: Modify to a new first name and last name, and click Cancel button
                    oldfirstname=LCname.split(" ")[0]
                    oldlastname=LCname.split(" ")[1]
                    newfirstname=oldfirstname+"_new"
                    newlastname=oldlastname+"_new"
                    newOMname=newfirstname+" "+newlastname
                    OMe.Input_firstname(newfirstname)
                    time.sleep(Gl.waittime)
                    OMe.Input_lastname(newlastname)
                    time.sleep(Gl.waittime)
                    OMe.click_cancelbutton()
                    #Step3.1:Verify :Back to  Browse OM Accounts page without this account info changed.
                    assert OMa.get_OMAtittle()=="Browse OM Accounts"
                    assert OMa.get_newOMname()==LCname#Check that the name is not changed
                    
                    #Step4:Modify to a new first name and last name, and click Save button
                    OMa.click_OMaccount()
                    time.sleep(Gl.waittime)
                    OMa.click_Editbutton()#Enter to Edit page
                    time.sleep(Gl.waittime)
                    OMe.Input_firstname(newfirstname)
                    time.sleep(Gl.waittime)
                    OMe.Input_lastname(newlastname)
                    time.sleep(Gl.waittime)
                    OMe.click_savebutton()
                    time.sleep(Gl.waittime)
                    currentdate=GetConfig.get_ServerCurrentDate()
                    currentdate=currentdate.replace('-',"/")
                    #currentdate=datetime.datetime.now().strftime("%Y/%m/%d")
                    alert_info="LC Account for "+newfirstname+newlastname+" ("+self.LCuserid+")"+" is successfully updated."
                    assert OMa.get_alert()==alert_info#Check if alert info is correct.
                    OMa1=OMaccountPage(1)#The account which updated is shown on the first line.
                    assert OMa1.get_newOMname()==newOMname#Check new name
                    time.sleep(Gl.waittime)
                    #assert OMa1.get_modifydate()==currentdate#Check modify date
                    
                    #Step5:Login Tablet to verify the Login name
                    L.logout_admin()#Logout
                    #LT=Login(self.tableturl,lobname,sitename,self.LCuserid,self.LCpassword)
                    L.Login_tablet(self.tableturl,lobname, sitename, self.LCuserid, LCpassword)
                    time.sleep(Gl.waittime)
                    Header=HeaderPage()
                    assert Header.get_loginName()==newOMname#Verify the login name has been updated to the new one
                    Tablet=TabletHomepage()
                    Tablet.click_coachingcircle()
                    time.sleep(Gl.waittime)
                    Coachpage=Coachinghomepage()
                    assert Coachpage.get_CoachName()==newOMname#Verify the Coach name of Coaching has been updated to the new one
                    Header.click_backbutton()
                    time.sleep(Gl.waittime)
                    Tablet.click_Triadcoachingcirecle()
                    time.sleep(Gl.waittime)
                    Triadcoach=TriadCoachinghomepage()
                    assert Triadcoach.get_CoachName()==newOMname#Verify the Coach name of Triad Coaching has been updated to the new one
                    #Back to tablet home page
                    Header.click_backbutton()
                    time.sleep(Gl.waittime)
                    #Check performance circle
                    assert Tablet.get_performancename() == "Performance"#Verify performance displayed
                    #Check coaching circle
                    assert Tablet.get_coachingname() == "Coaching"#Verify Coaching displayed
                    #Check triad coaching circle
                    assert Tablet.get_triadcoachingname()=="Triad Coaching"#Verify Triad Coaching displayed
                    #Check adaptation circle
                    assert Tablet.get_adaptationname_LC()=="Adaptation Rate" #Verify Adaptation Rate displayed
                    #Check My Team Info is not shown
                    Flag=True
                    if Tablet.MyteamInfo_Exist()==True:
                        Flag=False
                    assert Flag
                    
                    L.logout_tablet()
                    #Step6:Verify the LC name is updated in coaching list
                    
                    #Step7:Login Admin with LC account
                    #L1=Login(self.url,lobname,sitename,self.LCuserid,self.LCpassword)
                    L.Login_admin(self.adminturl, lobname, sitename, self.LCuserid,LCpassword)
                    LAdminPage=LoginAdminPage(self.adminturl,Gl.driver)
                    assert LAdminPage.get_nopermission()=="You don't have enough permission."#Verify that OM(1,6) can not login Admin System.
                    
                    GetConfig.print_EndTest_message(lobname, sitename)
                    

                        
 
                        
        
    def tearDown(self):
        Gl.driver.quit()
            


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()