'''
Created on 2018.1.30

@author: yalan.yin
'''
import unittest
from public_method.Get_configration_data import Get_configration_data
from public_method.Login import Login
from public_method import Gl
from Tablet_pages.HeaderPage import HeaderPage
from Tablet_pages.TabletHomepage import TabletHomepage
from Tablet_pages.MyTeamInfoPage import MyTeamInfoPage
from Tablet_pages.ChangePasswordPage import ChangePasswordPage
from public_method.HandleMySQL import HandleMySQL
from public_method.Deleteexistfile import Deleteexistfile
from public_method.Get_MyTeamContent import Get_MyTeamContent
from public_method.Get_AllRoleAccountForTest import Get_AllRoleAccountForTest
from public_method.Check_Tablet import Check_Tablet
import time



class MyTeamInfo_RosterFileToday_TL(unittest.TestCase):


    def setUp(self):
        #Case ID
        self.caseID="MyTeamInfo_RosterFileToday_TL"
        
        GetData=Get_configration_data()
        #Get OM account
        OMaccount=GetData.get_OMaccount()
        self.OMuserid=OMaccount["OMuserid"]
        self.OMpassword=OMaccount["OMpassword"]
        #Get TL account
        
        
        #Get all lobs from CSV
        self.testLOBSITE_list=GetData.get_LOBSITEtoTest(self.caseID)
        self.UserRole="L1"
        #self.UserName='Antonette Corpus'
        self.PageTitle1='My Team'
        self.PageTitle2='Change Password'
        self.SettingButtonExisting='nav-btn-icon fa fa-cog'
        self.BackButtonExisting='nav-btn-text-inner'
        self.Titleexisting='text-center'
        #Database info
        self.host=GetData.get_StageDatabaseHost()
        self.dbuser=GetData.get_StageDatabaseUser()
        self.dbpassword=GetData.get_StageDatabasePassword()
        #Get default download path
        self.downloadpath=GetData.get_DefaultDownloadPath()
        #Myteam file prefix
        self.filename="myteam"
        
        self.sheetname="My Team"
        #Special lobname
        self.AllSpecialLobs_list=GetData.get_Allspeciallobs_ByDataBase()
        #Special sitename
        self.AllSpecialSites_list=GetData.get_Allspecialsites_ByDataBase()


    def tearDown(self):
        #Gl.driver.quit()
        pass


    def test_MyTeamInfo_RosterFileToday_TL(self):
        HMysql=HandleMySQL()
        L=Login()
        THomepage=TabletHomepage()
        Hpage=HeaderPage()
        GetConfig=Get_configration_data()
        MTpage=MyTeamInfoPage()
        Deletefile=Deleteexistfile()
        GetMyTeamContent=Get_MyTeamContent()
        GetTL=Get_AllRoleAccountForTest()
        CheckTablet=Check_Tablet()
        for i in range(0,len(self.testLOBSITE_list)):
            Flag=GetConfig.get_LOBSITE_STATUS(self.testLOBSITE_list[i])
            if Flag==True:
                each_LOBSITE=self.testLOBSITE_list[i].split(":")
                lobname=each_LOBSITE[0]
                ##GET THE CORRECT URL#####
                adminurl=GetConfig.get_Test_AdminUrl(lobname)
                tableturl=GetConfig.get_Test_Tablet(lobname)
                hostindex=GetConfig.get_Test_Hostindex(lobname)
                ##GET THE CORRECT URL#####
                #######Get lob database name########
                if lobname in self.AllSpecialLobs_list:
                    lobname_database=GetConfig.get_DatabaseName_ByLobName(lobname)
                else:
                    lobname_database=lobname
                #######Get lob database name########
                
                #Get Site to test
                site_list=each_LOBSITE[1].split("*")
                for n in range(0,len(site_list)):
                    sitename=site_list[n]
                    GetConfig.print_StartTest_message(lobname, sitename)
                    #######Get Site database name########
                    lob_site=lobname+':'+sitename
                    if lob_site in self.AllSpecialSites_list:
                        sitename_database=GetConfig.get_DatabaseName_BySiteName(lob_site)
                    else:
                        sitename_database=sitename
                    #######Get Site database name########
                    
                    L.Login_tablet(tableturl, lobname, sitename, self.OMuserid, self.OMpassword)
                    time.sleep(Gl.waittime)
                    #step14.01 Get a tl hrid for testing
                    THomepage.click_Myteaminfocircle()
                    
                    TL_hrid=MTpage.get_eachhrid(1)
                    print TL_hrid
                    TL_NAME=MTpage.get_eachusername(1)
                    print TL_NAME
                    L.logout_tablet()
                    
                    #step14.01 login admin to get tl's password
                    TLInfo=GetTL.get_TLandAgentInfofromAdmin(adminurl, lobname, sitename, self.OMuserid, self.OMpassword,TL_hrid)
                    TLpassword=TLInfo["Password"]
                    #step14.02 TL login tablet
                    L.Login_tablet(tableturl, lobname, sitename, TL_hrid, TLpassword)
                    THomepage.click_TL_Myteaminfocircle()                 
   
                    #THomepage.click_Myteaminfocircle()
                    #sql_OM_name="select firstname, lastname from account where hr_id=66776677"
                    #OMNameInDB=HMysql.Get_datafromDB(self.hostindex, lobname, sitename, self.dbuser, self.dbpassword, sql_OM_name)
                    #a=OMNameInDB[1][0]
                    #OMName=a[0]+" "+a[1]
                    assert Hpage.get_HeaderTittle()==self.PageTitle1
                    assert Hpage.get_loginLob()==lobname
                    assert Hpage.get_loginSite()==sitename
                    assert Hpage.get_loginName()==TL_NAME
                    assert Hpage.get_loginRole()==self.UserRole
                    #assert Hpage.settingButtonexisted()==self.SettingButtonExisting
                    assert Hpage.backbuttonexisted()==self.BackButtonExisting
                    assert MTpage.Nametitleexisting()==self.Titleexisting
                    assert MTpage.hridtitleexisting()==self.Titleexisting
                    assert MTpage.roletitleexisting()==self.Titleexisting
                    assert MTpage.activateddateexisting()==self.Titleexisting
                    
                    #step10 click back button to return home page
                    Hpage.click_backbutton()
                    
                    CheckTablet.Check_TabletHomepageCircle_TL(lobname)
                     
                    #step11.1 enter myteaminfo page again 
                    Tablet=TabletHomepage()  
                    Tablet.click_TL_Myteaminfocircle()
                    #step11.2 click setting button 
                    Hpage.click_settingButton()                    
                    print "changepassword:", Hpage.ChangePasword_existing()
                    assert Hpage.ChangePasword_existing()=='Change Password'
                    print "Logout:", Hpage.Logout_existing()
                    assert Hpage.Logout_existing()=='Logout'
                    #click change password to enter change password page
                    Hpage.click_changePasswordLink()
                    assert Hpage.get_HeaderTittle()==self.PageTitle2
                    #step11.3 click Cancel button at change password page
                    Changepassword=ChangePasswordPage()
                    Changepassword.click_Cancelbutton()
                    Tablet.click_TL_Myteaminfocircle()
                    #step12
                    
                    print MTpage.get_TLnumber()
                    currentdate=GetConfig.get_ServerCurrentDate().replace("-","/")
                    AGENTnumber=MTpage.get_TLnumber()
                    AllAGENTInfo_page=[]
                    for i in range(1,AGENTnumber+1):
                        MTpage.get_eachusername(i)
                        MTpage.get_eachhrid(i)
                        AGENTinfo=[MTpage.get_eachusername(i),MTpage.get_eachhrid(i)]
                        AllAGENTInfo_page.append(AGENTinfo)
                    
                    sql_AGENT_list="select * from (SELECT rt.hr_id tl_hr_id,rtl.firstname tl_first_name,rtl.lastname tl_last_name,rt.team_id as rt_teamID,r.hr_id as agentHRID,rag.firstname as agentFirstName,rag.lastname as agentLastName FROM roster_teamleaders rt JOIN roster rtl ON rt.history_id = rtl.history_id AND rt.hr_id = rtl.hr_id LEFT JOIN roster r ON rt.history_id=r.history_id AND rt.team_id=r.team_id JOIN roster rag ON r.history_id = rag.history_id AND r.hr_id = rag.hr_id WHERE rt.history_id=(SELECT id FROM upload_history uh WHERE TYPE='2' AND uh.active_time=(SELECT MAX(active_time) FROM upload_history WHERE TYPE='2' AND DATE(data_date)<="+"'"+currentdate+"')) group  by  tl_hr_id, tl_first_name,  tl_last_name, rt_teamID,agentHRID, agentFirstName, agentLastName) s  where tl_hr_id<>agentHRID and tl_hr_id="+"'"+TL_hrid+"';"
                    AGENTlistInDB=HMysql.Get_datafromDB(hostindex, lobname_database, sitename_database, self.dbuser, self.dbpassword, sql_AGENT_list)
                    print "AGENTlistInDB:", AGENTlistInDB
                    AGENTlist=AGENTlistInDB[1]
                    AllAGENTInfo_DB=[]
                    for i in range(0,len(AGENTlist)):
                        AGENT_name=AGENTlist[i][5]+" "+AGENTlist[i][6]
                        print AGENT_name
                        AGENT_hrid=AGENTlist[i][4]
                        print AGENT_hrid
                        AGENT_info=[AGENT_name,AGENT_hrid]
                        AllAGENTInfo_DB.append(AGENT_info)
                    
                    print "AllAGENTInfo_page:", AllAGENTInfo_page
                    print "AllAGENTInfo_DB:", AllAGENTInfo_DB 
                    assert len(AllAGENTInfo_page)==len(AllAGENTInfo_DB)
                    for item in AllAGENTInfo_page:
                        assert item in AllAGENTInfo_DB
                      
                    Deletefile.delete_MyteamFile(self.downloadpath)
                    MTpage.click_exportbutton()
                    
                    #Step1.2:Get Myteaminfo from excel
                    #GetMyTeamContent.Get_TotalUserNumber(self.filename, self.sheetname)
                    print '=============================get myteaminfo from excel==============================='
                    filename_prefix='myteam'
                    sheetname='My Team'
                    TotaluserNumber=GetMyTeamContent.Get_TotalUserNumber(filename_prefix, sheetname)
                    print TotaluserNumber
                    Header_excel=GetMyTeamContent.Get_MyTeamHeader(filename_prefix, sheetname)
                    #Check header
                    CheckTablet.Check_MyTeamInfo_Header(Header_excel)
                    AllAGENTInfo_excel=[]
                    for i in range(i,TotaluserNumber+1):
                        AGENT_hrid_excel=GetMyTeamContent.Get_HRID(filename_prefix, sheetname)
                    print 'AGENT hrid:', AGENT_hrid_excel
                    
                    OneUser=[]
                    for name in AGENT_hrid_excel:
                        OneUser=[name, AGENT_hrid_excel[name]]
                        AllAGENTInfo_excel.append(OneUser)
                    print AllAGENTInfo_excel
                    assert len(AllAGENTInfo_page)==len(AllAGENTInfo_excel)
                    for item in AllAGENTInfo_page:
                        assert item in AllAGENTInfo_excel    
                        
                    L.logout_tablet()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()