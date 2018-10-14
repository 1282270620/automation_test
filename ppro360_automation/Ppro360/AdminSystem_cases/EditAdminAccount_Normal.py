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


class EditAdminAccount_Normal(unittest.TestCase):
    


    def setUp(self):
        #Case ID
        self.caseID="EditAdminAccount_Normal"
        
        GetData=Get_configration_data()
        
        #Get OM account
        OMaccount=GetData.get_OMaccount()
        self.OMuserid=OMaccount["OMuserid"]
        self.OMpassword=OMaccount["OMpassword"]
        #Get all lobs from CSV
        self.testLOBSITE_list=GetData.get_LOBSITEtoTest(self.caseID)
   
       

        
    def test_EditAdminAccount_Normal(self):
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
                    #Step2.1:Enter to OM account page
                    Admin=AdminHomepage()
                    Admin.Enter_OMaccountbrowse()
                       
                    #Step2.2:Search out the OM hrid which is need to be edit, and enter to the Edit page
                    OMe=OMEditPage()
                    OMindex=1
                    Flag=True
                    while Flag:
                        OMa=OMaccountPage(OMindex)
                        if OMa.get_newOMhrid()==self.OMuserid:
                            OMname=OMa.get_newOMname()
                            Flag=False
                            break
                        else:
                            OMindex=OMindex+1
                            continue

                    print OMa.get_newOMhrid()
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
                    oldfirstname=OMname.split(" ")[0]
                    oldlastname=OMname.split(" ")[1]
                    newfirstname=oldfirstname+"_new"
                    newlastname=oldlastname+"_new"
                    newOMname=newfirstname+" "+newlastname
                    OMe.Input_firstname(newfirstname)
                    time.sleep(Gl.waittime)
                    OMe.Input_lastname(newlastname)
                    time.sleep(Gl.waittime)
                    OMe.click_cancelbutton()
                    #Step3.1:Verify :Back to  Browse OM Accounts page without this account info changed.
                    assert OMa.get_OMAtittle()=="Browse L3 Accounts"
                    assert OMa.get_newOMname()==OMname#Check that the name is not changed
                       
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
                    #time.sleep(Gl.waittime)
                    #currentdate=datetime.datetime.now().strftime("%Y/%m/%d")
                    currentdate=GetConfig.get_ServerCurrentDate().replace('-','/')
                    alert_info="L3 Account for "+newfirstname+newlastname+" ("+self.OMuserid+")"+" is successfully updated."
                    print OMa.get_alert()
                    print alert_info
                    assert OMa.get_alert()==alert_info #Check if alert info is correct.
                    OMa1=OMaccountPage(1)#The account which updated is shown on the first line.
                    print  OMa1.get_newOMname()
                    print  newOMname
                    assert OMa1.get_newOMname()==newOMname#Check new name                  
                    assert OMa1.get_modifydate()==currentdate#Check modify date
                       
                    #Step5:Logout and login again, and verify new OM name is shown on the top right.
                    L.logout_admin()#Logout
                    L.Login_admin(adminurl,lobname, sitename, self.OMuserid, self.OMpassword)#Login again
                    assert Admin.get_OMnameOntopright()==newOMname#Verify the OM name on top right is updated to the new one
                    time.sleep(Gl.waittime)
                    #Step6:Verify OM name has been update to the new own for Uploaded By for Roster and Performance
                    #Admin.Enter_Rosterhistory()#Verify Uploaded By for Roster
                    #Admin.Enter_Performancehistory()#Verify Uploaded By for Performance
                       
                    #Step7:Login Tablet to verify the Login name
                    L.logout_admin()#Logout
                    #LT=Login(self.tableturl,lobname,sitename,self.OMuserid,self.OMpassword)
                    L.Login_tablet(tableturl,lobname, sitename, self.OMuserid, self.OMpassword)
                    time.sleep(Gl.waittime)
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
                    GetConfig.print_EndTest_message(lobname, sitename)
                       

                       
        
    def tearDown(self):
        Gl.driver.quit()
        #pass
            


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()