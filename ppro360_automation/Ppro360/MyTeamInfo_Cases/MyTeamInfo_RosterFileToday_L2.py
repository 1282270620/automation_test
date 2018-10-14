'''
Created on 2018.5.25

@author: yalan.yin
'''
import unittest
from public_method.Get_configration_data import Get_configration_data
from public_method.Login import Login
from public_method import Gl
from Tablet_pages.HeaderPage import HeaderPage
from Tablet_pages.TabletHomepage import TabletHomepage
from Tablet_pages.MyTeamInfoPage import MyTeamInfoPage
from public_method.HandleMySQL import HandleMySQL
from public_method.Deleteexistfile import Deleteexistfile
from public_method.Get_MyTeamContent import Get_MyTeamContent
from public_method.Get_AllRoleAccountForTest import Get_AllRoleAccountForTest
import time



class MyTeamInfo_RosterFileToday_L2(unittest.TestCase):


    def setUp(self):
        #Case ID
        self.caseID="MyTeamInfo_RosterFileToday_L2"
        
        GetData=Get_configration_data()
        #Get OM account
        OMaccount=GetData.get_OMaccount()
        self.OMuserid=OMaccount["OMuserid"]
        self.OMpassword=OMaccount["OMpassword"]
        #Get TL account
        
        
        #Get all lobs from CSV
        self.testLOBSITE_list=GetData.get_LOBSITEtoTest(self.caseID)
        self.UserRole="L2"
        #self.UserName='Antonette Corpus'
        self.PageTitle1='My Team'
        self.PageTitle2='Change Password'
        self.SettingButtonExisting='nav-btn-icon fa fa-cog'
        self.BackButtonExisting='nav-btn-text-inner'
        self.Titleexisting='text-center'
        #Database info
        self.host=GetData.get_StageDatabaseHost()
        #self.L2_hrid=900001
        self.dbuser=GetData.get_StageDatabaseUser()
        self.dbpassword=GetData.get_StageDatabasePassword()
        #Get default download path
        self.downloadpath=GetData.get_DefaultDownloadPath()
        #Myteam file prefix
        self.filename="myteam"
        
        self.sheetname="My Team"
        self.role="L2"
        #Special lobname
        self.AllSpecialLobs_list=GetData.get_Allspeciallobs_ByDataBase()
        #Special sitename
        self.AllSpecialSites_list=GetData.get_Allspecialsites_ByDataBase()


    def tearDown(self):
        #Gl.driver.quit()
        pass


    def test_MyTeamInfo_RosterFileToday_L2(self):
        HMysql=HandleMySQL()
        L=Login()
        THomepage=TabletHomepage()
        Hpage=HeaderPage()
        GetConfig=Get_configration_data()
        MTpage=MyTeamInfoPage()
        Deletefile=Deleteexistfile()
        GetMyTeamContent=Get_MyTeamContent()
        GetL2=Get_AllRoleAccountForTest()
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
                    #L.Login_admin(self.adminurl, lobname, sitename, self.OMuserid, self.OMpassword)
                    time.sleep(Gl.waittime)
                    #AdminPage.Enter_BrowseTLAgentAccounts()

                    L2Info=GetL2.get_TLandAgentInfofromAdmin_Byrole(adminurl, lobname, sitename, self.OMuserid, self.OMpassword, self.role)
                    print "L2Info:", L2Info
                    
                    
                    
                    #step14.01 login admin to get tl's password
                    #L2Info=GetTL.get_TLandAgentInfofromAdmin(self.adminurl, lobname, sitename, self.OMuserid, self.OMpassword,self.L2_hrid)
                    L2_hrid=L2Info["Hrid"]
                    L2password=L2Info["Password"]
                    L2Name=L2Info["Name"]
                    #step14.02 TL login tablet
                    L.Login_tablet(tableturl, lobname, sitename, L2_hrid, L2password)
                    THomepage.click_Myteaminfocircle()                
   
                    #THomepage.click_Myteaminfocircle()
                    #sql_OM_name="select firstname, lastname from account where hr_id=66776677"
                    #OMNameInDB=HMysql.Get_datafromDB(self.hostindex, lobname, sitename, self.dbuser, self.dbpassword, sql_OM_name)
                    #a=OMNameInDB[1][0]
                    #OMName=a[0]+" "+a[1]
                    assert Hpage.get_HeaderTittle()==self.PageTitle1
                    assert Hpage.get_loginLob()==lobname
                    assert Hpage.get_loginSite()==sitename
                    assert Hpage.get_loginName()==L2Name
                    assert Hpage.get_loginRole()==self.UserRole
                    #assert Hpage.settingButtonexisted()==self.SettingButtonExisting
                    assert Hpage.backbuttonexisted()==self.BackButtonExisting
                    assert MTpage.Nametitleexisting()==self.Titleexisting
                    assert MTpage.hridtitleexisting()==self.Titleexisting
                    assert MTpage.roletitleexisting()==self.Titleexisting
                    assert MTpage.activateddateexisting()==self.Titleexisting
                    
                    print MTpage.get_TLnumber()
                    #currentdate=GetConfig.get_ServerCurrentDate().replace("-","/")
                    AGENTnumber=MTpage.get_TLnumber()
                    AllAGENTInfo_page=[]
                    for i in range(1,AGENTnumber+1):
                        MTpage.get_eachusername(i)
                        MTpage.get_eachhrid(i)
                        AGENTinfo=[MTpage.get_eachusername(i),MTpage.get_eachhrid(i)]
                        AllAGENTInfo_page.append(AGENTinfo)
                    
                    sql_AGENT_list="select  t.firstname tl_firstname, t.lastname tl_lastname,t.hr_id tl_hrid, 'L1' as Title,u.active_time from  manager l2 join manager t on l2.id=t.parent_id  join upload_history u on t.history_id=u.id where l2.history_id=(SELECT id FROM upload_history uh WHERE TYPE='2' AND uh.active_time=(SELECT MAX(active_time) FROM upload_history WHERE TYPE='2' AND DATE(data_date)<=now())) and l2.hr_id=900001;"
                    AGENTlistInDB=HMysql.Get_datafromDB(hostindex, lobname_database, sitename_database, self.dbuser, self.dbpassword, sql_AGENT_list)
                    print "AGENTlistInDB:", AGENTlistInDB
                    AGENTlist=AGENTlistInDB[1]
                    AllAGENTInfo_DB=[]
                    for i in range(0,len(AGENTlist)):
                        AGENT_name=AGENTlist[i][0]+" "+AGENTlist[i][1]
                        print AGENT_name
                        AGENT_hrid=AGENTlist[i][2]
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
                    Header_onpage=['Name','HR ID','Title','Activated Date']
                    Header_excel=GetMyTeamContent.Get_MyTeamHeader(filename_prefix, sheetname)
                    print "hearder_excel:", Header_excel
                    assert Header_onpage==Header_excel
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