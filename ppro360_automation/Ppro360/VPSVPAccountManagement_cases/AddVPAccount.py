'''
Created on 20180104

@author: luming.zhao
'''

import unittest
from public_method.Get_configration_data import Get_configration_data
from public_method.Login import Login
import time
from public_method import Gl
from AdminSystem_Pages.AdminHomepage import AdminHomepage
from VPSVPAccountManagement_Pages.VPAddPage import VPAddPage
from VPSVPAccountManagement_Pages.VPSVPaccountPage import VPSVPaccountPage
from Tablet_pages.HeaderPage import HeaderPage
from AdminSystem_Pages.LoginAdminPage import LoginAdminPage
from AdminSystem_Pages.AddOMWarnningpage import AddOMWarningpage
from VPSVPAccountManagement_Pages.Loblist_ForvpOrsvp import Loblist_ForvpOrsvp
from VPSVPAccountManagement_Pages.VPSVPLoginTabletPage import VPSVPLoginTabletPage
from Tablet_pages.LoginTabletPage import LogintabletPage
from public_method.Check_Tablet import Check_Tablet



class AddVPAccount(unittest.TestCase):
    


    def setUp(self):
        
        #Case ID
        self.caseID="AddVPAccount"
        GetData=Get_configration_data()
        #Get VP account
        
        VPaccount=GetData.get_VPaccount()
        self.VPuserid=VPaccount["VPuserid"]
        #get superadmin account
        SAdminaccount=GetData.get_SAdminaccount()
        self.SAdminuserid=SAdminaccount['SAdminuserid']
        self.SAdminpassword=SAdminaccount['SAdminpassword']

        #Get OM account
        OMaccount=GetData.get_OMaccount()
        self.OMuserid=OMaccount["OMuserid"]
        self.OMpassword=OMaccount["OMpassword"]
        #Get all lobs from CSV
        self.testLOBSITE_list=GetData.get_LOBSITEtoTest(self.caseID)
        #New OM's info
        self.firstname="RichardVP"
        self.lastname="ClaydermanVP"
        #All-LOBs in configration file
        #self.AllLOBs="All-LOBs"
        self.LOB_lists=GetData.get_AllLOBs_list()


    def test_AddVPAccount(self):
        GetConfig=Get_configration_data()
        LOBlist_svp=Loblist_ForvpOrsvp()
        CheckTablet=Check_Tablet()
        #Test several LOBs
        for i in range(0,len(self.testLOBSITE_list)):
            Flag=GetConfig.get_LOBSITE_STATUS(self.testLOBSITE_list[i])
            if Flag==True:
                each_LOBSITE=self.testLOBSITE_list[i].split(":")
                lobname=each_LOBSITE[0]
                ##GET THE CORRECT URL#####
                Adminurl=GetConfig.get_Test_AdminUrl(lobname)
                tableturl=GetConfig.get_Test_Tablet(lobname)
                ##GET THE CORRECT URL#####
                #Get Site to test
                site_list=each_LOBSITE[1].split("*")
                for n in range(0,len(site_list)):
                    sitename=site_list[n]
                    GetConfig.print_StartTest_message(lobname, sitename)
                    #Step4:Login admin system
                    L=Login()
                    L.Login_admin(Adminurl,lobname, sitename, self.SAdminuserid, self.SAdminpassword)
                    #Step2:Enter to OM account page
                    Admin=AdminHomepage()
                    Admin.Enter_VPSVPaccountbrowse()
                    #Step5.1:Check all OMs are showning sort by modification date
                    #Step6:Enter to Add OM page
                    VPSVPindex=1
                    VPa=VPSVPaccountPage(VPSVPindex)
                    VPa.click_VPSVPadd()
                    #Step7:Cancel add VPorSVP
                    AddVP=VPAddPage()
                    AddVP.click_Cancel()
                    assert VPa.get_VPSVPAtittle() == "Browse VP / SVP Accounts"#Back to VP SVP accounts page
                    #Step8:Re-Generate password 
                    time.sleep(Gl.waittime)
                    VPa.click_VPSVPadd()
                    AddVP.regenerate_password()
                    #Step9:Check each LOB name
                    AllLOBlists_page=LOBlist_svp.get_loblists_page()
                    
                    print "From configration data,LOB number (include AOL) is ", len(self.LOB_lists)
                    print "From page,LOB number is ", len(AllLOBlists_page)
                    assert len(self.LOB_lists)==len(AllLOBlists_page)+1
                    time.sleep(Gl.waittime)

                    MaxLOBindex=len( AllLOBlists_page)
                    LOBlist_svp.select_AllLOB(MaxLOBindex)

                    print self.LOB_lists
                    print AllLOBlists_page
                    
                    index=3 #check ISM has 7 sites
                    LOBlist_svp.select_AllLOB(index)
                    time.sleep(Gl.waittime)

                    index=13 #check LCBB has 4 sites
                    LOBlist_svp.select_AllLOB(index)
                    
                    
                    index=15 #check DTVRCX has 5 sites
                    LOBlist_svp.select_AllLOB(index)
                    index=23 #check CLG   has 4 sites
                    LOBlist_svp.select_AllLOB(index)
                   
                    #Step6: Enter to Add VPSVP page and add VPSVP again
                    AllLobs={}
                    for i in range(0,len(AllLOBlists_page)):
                        OneLob=AllLOBlists_page[i].replace("+ ","")
                        Index=i+1
                        AllLobs[OneLob]=Index
                        #print AllLobs
        
                    SelectedLOBINDEX=AllLobs[lobname]
                    #print "SelectedLOBINDEX:", SelectedLOBINDEX  
                    time.sleep(Gl.waittime)
                    AddVP.select_loblist(SelectedLOBINDEX)
                    AddVP.input_VPSVPfirstname(self.firstname)
                    AddVP.input_VPSVPlastname(self.lastname)
                    newhrid=self.VPuserid+"0"
                    AddVP.input_VPSVPhrid(newhrid)
                    AddVP.click_addVPSVP()
                    i=0
                    AddWarn=AddOMWarningpage()
                    while AddVP.warningwidonw_ispopup()==True:
                        AddWarn.click_OK()
                        print newhrid,
                        print " is existed.And try again!"
                        AddVP.clear_hrid()
                        newhrid=newhrid+str(i)
                        AddVP.input_VPSVPhrid(newhrid)
                        time.sleep(Gl.waittime)
                        
                        
                        AddVP.click_addVPSVP()
                        i=i+1
                                       
                    newpassword=VPa.get_newVPSVPpwd()
                    print "Create VP successfully: ",
                    print self.firstname+" "+self.lastname+","+newhrid+','+newpassword 
                    L.logout_admin()                     
                    #Step7:Login Admin with new OM account
                    L.Login_admin(Adminurl, lobname, sitename, newhrid, newpassword)
                    LAdminPage=LoginAdminPage(Adminurl,Gl.driver)
                    
                    time.sleep(Gl.waittime)
                    print LAdminPage.get_nopermission
                    assert LAdminPage.get_nopermission()=="You don't have enough permission."#Verify that VP can not login Admin System.

                    #Step8: Login tablet with new OM account
                    time.sleep(Gl.waittime)

                    
                    L.Login_tablet(tableturl,lobname,sitename,newhrid,newpassword)
                    
                    CheckTablet.Check_TabletHomepageCircle_VPSVP(lobname)
                    H=HeaderPage()
                    #Check  tablet homepage tittle
                    assert H.get_HeaderTittle()=="Performance Pro 360" #Verify tablet homepage title is correct
                   
                    
                    #Check LOB
                    assert H.get_loginLob()==lobname #Verify lob is correct
                    #Check Site
                    assert H.get_loginSite()==sitename #Verify site is correct
                    #Check login name
                    VPname=self.firstname+" "+self.lastname
                    assert H.get_loginName()==VPname # Verify login name is correct
                    #Check Role
                    assert H.get_loginRole()=="VP" #Verify the role is correct
                    
                    L.logout_tablet()
                    GetConfig.print_EndTest_message(lobname, sitename)
                    
                    time.sleep(Gl.waittime)
                    LoginTablet=LogintabletPage(tableturl,Gl.driver)
                    LoginTablet.open()
                    LoginTablet.click_lobname_box_dropdown()
                    SVPloginTPage=VPSVPLoginTabletPage()
                    SVPloginTPage.get_loginlob()
                    #lobindex1=2
                    #siteindex1=2
                    lobindex=2  #lobindex should not equal to SelectedLOBINDEX
                    if lobindex==SelectedLOBINDEX:                        
                        newlobname=LoginTablet.get_eachlobname(lobindex)
                        lobindex1=lobindex-1
                        SVPloginTPage.click_loginlob(lobindex1)
                    else:
                        newlobname=LoginTablet.get_eachlobname(lobindex)
                        lobindex1=lobindex
                        SVPloginTPage.click_loginlob(lobindex1)
                           
                    LoginTablet.click_sitename_box_dropdown()
                    siteindex=1
                    newsitename=LoginTablet.get_eachsitename(siteindex)
                    siteindex1=siteindex
                    SVPloginTPage.click_loginstie(siteindex1)
                    userid=newhrid
                    password=newpassword
                    
                    LoginTablet.input_userid(userid)
                    LoginTablet.input_password(password)
                    
                    LoginTablet.click_login()
                    print "error You are not allowed to access the site " + newlobname + "-" +newsitename+"." +"Error code is [9981]."
                    #assert LoginTablet.get_nopermission()=="error You are not allowed to access the site " + lobindex1 + "-" +siteindex1+"." "Error code is [9981]."
                     
     
               
                        
    
        
    def tearDown(self):
        #Gl.driver.quit()
        pass

if __name__ == "__main__":
    #import sys; sys.argv = ['', 'Test.testName']
    unittest.main()