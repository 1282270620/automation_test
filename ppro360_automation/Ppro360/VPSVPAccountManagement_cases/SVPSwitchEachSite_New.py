'''
Created on 20180125

@author: luming.zhao
'''

import unittest
from public_method.Get_configration_data import Get_configration_data
from public_method.Login import Login
from AdminSystem_Pages.AdminHomepage import AdminHomepage
from public_method import Gl
from VPSVPAccountManagement_Pages.VPAddPage import VPAddPage
from VPSVPAccountManagement_Pages.VPSVPaccountPage import VPSVPaccountPage
from VPSVPAccountManagement_Pages.Loblist_ForvpOrsvp import Loblist_ForvpOrsvp
from AdminSystem_Pages.AddOMWarnningpage import AddOMWarningpage
from VPSVPAccountManagement_Pages.VPSVPLoginTabletPage import VPSVPLoginTabletPage
import time
from Tablet_pages.HeaderPage import HeaderPage
from public_method.Check_Tablet import Check_Tablet
import copy


class SVP_SwitchEachSite(unittest.TestCase):


    def setUp(self):
        self.caseID="SVPSwitchEachSite_New"
        GetData=Get_configration_data()
        #Get VXI url
        self.VXI_tableturl=GetData.get_VXI_TabletUrl()
        self.VXI_adminurl=GetData.get_VXI_AdminUrl()
        #Get AWS url
        self.AWS_tableturl=GetData.get_AWS_TabletUrl()
        self.AWS_adminurl=GetData.get_AWS_AdminUrl()
        #Get AWS LOBs
        self.AWSLOBs_list=GetData.get_AWSLOBs_list()
        #Get VXI LOBs
        self.VXILOBs_list=GetData.get_VXILOBs_list()
        #get superadmin account
        SAdminaccount=GetData.get_SAdminaccount()
        self.SAdminuserid=SAdminaccount['SAdminuserid']
        self.SAdminpassword=SAdminaccount['SAdminpassword']
        
        #Get SVP account
        AdminOMaccount=GetData.get_AdminOMaccount()
        self.AdminOMuserid=AdminOMaccount["AdminOMuserid"]
        SVPaccount=GetData.get_SVPaccount()
        self.SVPuserid=SVPaccount["SVPuserid"]

        #Get OM account
        OMaccount=GetData.get_OMaccount()
        self.OMuserid=OMaccount["OMuserid"]
        self.OMpassword=OMaccount["OMpassword"]

        #Get all lobs from CSV
        self.testLOBSITE_list=GetData.get_LOBSITEtoTest(self.caseID)
        self.firstname="RichardSVP"
        self.lastname="ClaydermanSVP"
        #Whose database name is special
        #self.lob_databasespecial=GetData.get_SpecialLobforDatabase()
        #Database info
        self.host=GetData.get_StageNodeHost(92)
        self.dbuser=GetData.get_StageDatabaseUser()
        self.dbpassword=GetData.get_StageDatabasePassword()
        self.LOB_lists=GetData.get_AllLOBs_list()
        #Get AWS LOBs
        self.AWSLOBs_list=GetData.get_AWSLOBs_list()
        #Get VXI LOBs
        self.VXILOBs_list=GetData.get_VXILOBs_list()


    def test_AddSVPAccount(self):
        GetConfig=Get_configration_data()
        LOBlist_svp=Loblist_ForvpOrsvp()
        CT=Check_Tablet()
        #LOBlist=LOBlistPage()
        #Test several LOBs
        for i in range(0,len(self.testLOBSITE_list)):
            Flag=GetConfig.get_LOBSITE_STATUS(self.testLOBSITE_list[i])
            if Flag==True:
                each_LOBSITE=self.testLOBSITE_list[i].split(":")
                lobname=each_LOBSITE[0]
                if lobname in self.AWSLOBs_list:
                    Adminurl=self.AWS_adminurl
                    tableturl=self.AWS_tableturl
                elif lobname in self.VXILOBs_list:
                    Adminurl=self.VXI_adminurl
                    tableturl=self.VXI_tableturl
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
                    #VPa.click_VPSVPadd()
                    #LOBlist=LOBlistPage(self,'index')

                    AllLOBlists_page=LOBlist_svp.get_loblists_page()
                    print "From configration data,LOB number (include AOL) is ", len(self.LOB_lists)
                    print "From page,LOB number is ", len(AllLOBlists_page)
                    assert len(self.LOB_lists)==len(AllLOBlists_page)+1
                    
                    AddVP.click_vpsvp()
                    AddVP.select_RoleSVP()
                    time.sleep(Gl.waittime)
                    AddVP.input_VPSVPfirstname(self.firstname)
                    AddVP.input_VPSVPlastname(self.lastname)
                    newhrid=self.SVPuserid+"0"
                    AddVP.input_VPSVPhrid(newhrid)

                    time.sleep(Gl.waittime)
                    
                    MaxLOBindex=len( AllLOBlists_page)
                    LOBlist_svp.select_AllLOB(MaxLOBindex)
                    
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
                    #time.sleep(10)                   
                    newpassword=VPa.get_newVPSVPpwd()
                    print "Create SVP successfully: ",
                    print self.firstname+" "+self.lastname+","+newhrid+','+newpassword 
                    L.logout_admin()                  
                    
                #3.Login tablet with following info:
                    #1) select any lob+site
                    #2) This SVP accountA.
                    
                    
                    L.Login_tablet(tableturl,lobname,sitename,newhrid,newpassword)
                    
                    CT.Check_TabletHomepageCircle_VPSVP(lobname)
                    
                    H=HeaderPage()
                    #Check  tablet homepage tittle
                    assert H.get_HeaderTittle()=="Performance Pro 360" #Verify tablet homepage title is correct
                    #Check LOB
                    assert H.get_loginLob()==lobname #Verify lob is correct
                    #Check Site
                    assert H.get_loginSite()==sitename #Verify site is correct
                    #Check login name
                    SVPname=self.firstname+" "+self.lastname
                    assert H.get_loginName()==SVPname # Verify login name is correct
                    #Check Role
                    assert H.get_loginRole()=="SVP" #Verify the role is correct
                    
                    
                    
                    
                    #Click setting icon form top right corner.
                    #Select option 'Switch LOB/Site'.
                    ###########Add by Sabrina, to get the same type lob list except itself.##############
                    if lobname in self.VXILOBs_list:
                        switch_lob_list=copy.deepcopy(self.VXILOBs_list)
                    elif lobname in self.AWSLOBs_list:
                        switch_lob_list=copy.deepcopy(self.AWSLOBs_list)
                    else:
                        print lobname,"does not belong to neither VXI nor AWS, please check this lob!"
                    switch_lob_list.remove(lobname)#Only can swtich to other lob who belong to the same type lob, and includes itself.
                    ###########Add by Sabrina, to get the same type lob list except itself.##############
                    #lobindex=1
                    SVPloginTPage=VPSVPLoginTabletPage()
                    SVPloginTPage.click_settingButton()
                    SVPloginTPage.click_SwitchLOBSitesLink()
                    
                    SVPloginTPage.click_LOBdropdownbutton()
                    CheckLOBsname_page=SVPloginTPage.get_checkLOBsnamepage()
                    print CheckLOBsname_page
                    
                    #############Add by Sabrina,select the correct lob###############
                    for i in range(1,len(CheckLOBsname_page)+1):
                        if SVPloginTPage.get_anylobname_inSwitchPage(i) in switch_lob_list:
                            lobindex=i
                            break
                    #############Add by Sabrina,select the correct lob###############        
                    
                    
                    #here must be clicked the other section except the sites drop-down button,
                    #because it's position may not be found
                    SVPloginTPage.select_LOBtoswitch(lobindex) #select first LOB
                    newlobname=SVPloginTPage.get_swithloginLOBname()
                    SVPloginTPage.click_Sitedropdownbutton()
                    SVPloginTPage.get_checkSitesnamepage()
                    CheckSITEsname_page=SVPloginTPage.get_checkSitesnamepage()
                    print CheckSITEsname_page
                    
                    siteindex=2#siteindex must be match vxi-lob or aws-lob
                    SVPloginTPage.select_Sitetoswitch(siteindex) #select second SITE
                    newsitename=SVPloginTPage.get_swithloginSITEname()
                    SVPloginTPage.click_Swichbutton()
                    
                    #Check new LOB name
                    print newlobname,H.get_loginLob()
                    assert H.get_loginLob()==newlobname #Verify newlob is correct
                    #Check Site name
                    assert H.get_loginSite()==newsitename #Verify newsite is correct
                    
                    #Check login name
                    SVPname=self.firstname+" "+self.lastname
                    assert H.get_loginName()==SVPname # Verify login name is correct
                    #Check Role
                    assert H.get_loginRole()=="SVP" #Verify the role is correct
                    
                    
     
        
    def tearDown(self):
        #Gl.driver.quit()
        pass
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()