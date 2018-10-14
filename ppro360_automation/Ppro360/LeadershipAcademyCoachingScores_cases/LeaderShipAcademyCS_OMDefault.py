'''
Created on Jun 14, 2018

@author: Sabrina Guo
'''
import unittest
from public_method.Get_configration_data import Get_configration_data
from Tablet_pages.TabletHomepage import TabletHomepage
from public_method.Login import Login
from public_method.Check_Tablet import Check_Tablet
from public_method.HandleMySQL import HandleMySQL
from public_method.LeadershipDate_Actual import LeadershipDate_Actual
from Tablet_pages.LeadershipAcademyCoachingScoresPage import  LeadershipAcademyCoachingScoresPage


class LeaderShipAcademyCS_OMDefault(unittest.TestCase):


    def setUp(self):
        self.caseID="LeaderShipAcademyCS_OMDefault"
        GetData=Get_configration_data()
        
        #Get LOBs have no LSACS
        self.LOBs_NoLSACS_list=GetData.get_LOBHasNoLSACS_list()
        #Get OM account
        OMaccount=GetData.get_OMaccount()
        self.OMuserid=OMaccount["OMuserid"]
        self.OMpassword=OMaccount["OMpassword"]
        self.role="L3"
        #Get all lobs from CSV
        self.testLOBSITE_list=GetData.get_LOBSITEtoTest(self.caseID)
        
        #Database info
        self.host=GetData.get_StageDatabaseHost()
        self.dbuser=GetData.get_StageDatabaseUser()
        self.dbpassword=GetData.get_StageDatabasePassword()
        
        #Info of configuration
        self.sqlsheetname="SQLs"
        self.sql_SiteData="Sql_Site_LeaderShipAcademyCoachingScores"
        self.sql_TeamData="Sql_TL_ByOM_LeaderShipAcademyCoachingScores"
        self.sql_agentsAndTLs="Sql_AllAgentsAndTLsOfL3_LeaderShipAcademyCoachingScores"
        self.sql_AgentData="Sql_Agent_ByOM_LeaderShipAcademyCoachingScores"
        #KPInumber
        self.KPInumber=7
        #Special lobname
        self.AllSpecialLobs_list=GetData.get_Allspeciallobs_ByDataBase()
        #Special sitename
        self.AllSpecialSites_list=GetData.get_Allspecialsites_ByDataBase()


    def tearDown(self):
        #Gl.driver.quit()
        pass



    def test_LeaderShipAcademyCS_OMDefault(self):
        Tablet=TabletHomepage()
        GetConfig=Get_configration_data()
        L=Login()
        #LSACoachingScores=LeadershipAcademyCoachingScoresPage()
        CheckTablet=Check_Tablet()
        HMysql=HandleMySQL()
        Lactual=LeadershipDate_Actual()
        LSACoachingScores=LeadershipAcademyCoachingScoresPage()
        #Test several LOBs
        for i in range(0,len(self.testLOBSITE_list)):
            Flag=GetConfig.get_LOBSITE_STATUS(self.testLOBSITE_list[i])
            if Flag==True:
                each_LOBSITE=self.testLOBSITE_list[i].split(":")
                lobname=each_LOBSITE[0]
                ##GET THE CORRECT URL#####
                tableturl=GetConfig.get_Test_Tablet(lobname)
                hostindex=GetConfig.get_Test_Hostindex(lobname)
                ##GET THE CORRECT URL#####
                #######Get lob database name########
                if lobname in self.AllSpecialLobs_list:
                    lobname_database=GetConfig.get_DatabaseName_ByLobName(lobname)
                else:
                    lobname_database=lobname
                #######Get lob database name########
                if lobname in self.LOBs_NoLSACS_list:
                    print lobname," does not have LeadershipAcademyCoachingScores module."
                else:
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
                        #Step0:Login tablet system and find out a Agent for testing    
                        L.Login_tablet(tableturl, lobname, sitename, self.OMuserid, self.OMpassword)
                        Tablet.click_LeadershipAcademyCoachingScores_OM()
                        
                        #Step1:Check all Default values of Conditions
                        CheckTablet.Check_DefaultValuesOfQueryConditions_LeaderShipAcademyCoachingScores()
                        
                        #Step2:Check All agents and Tls of this site
                        #Step2.1:Get all accounts from DataBase
                        Sql_agentsandTLs=GetConfig.get_sql_content(self.sqlsheetname, self.sql_agentsAndTLs)
                        AllaccountsInfo_DataBase=HMysql.Get_datafromDB(hostindex, lobname_database, sitename_database, self.dbuser, self.dbpassword, Sql_agentsandTLs)
                        Allaccounts_DataBase=list(AllaccountsInfo_DataBase[1])
                        AllTLs_DataBase=[]
                        AllAgents_DataBase=[]
                        for item in Allaccounts_DataBase:
                            name=item[0]+" "+item[1]
                            if item[3]=="TL":
                                AllTLs_DataBase.append(name)
                            else:
                                AllAgents_DataBase.append(name)
                        print "AllTls:",AllTLs_DataBase
                        print "AllAgents:",AllAgents_DataBase

                        #Step2.2: Get all accounts from Page
                        AllTLInfo=LSACoachingScores.get_AllTLs_Leadershippage_ByL3()
                        print AllTLInfo
                        TLnumber=AllTLInfo[1]
                        AllTLs_FromPage=AllTLInfo[0]
                        #AllAgents_FromPage=LSACoachingScores.get_AllAgents_Leadershippage_ByL3(TLnumber)
                        AllInfoOfAgent_FromPage=LSACoachingScores.get_AllAgents_Leadershippage_ByL3(TLnumber,self.KPInumber)
                        print AllInfoOfAgent_FromPage
                        AllAgents_FromPage=AllInfoOfAgent_FromPage[0]
                        print AllAgents_FromPage
                        AllTLs_DataBase.sort()
                        AllTLs_FromPage.sort()
                        CheckTablet.CheckData_DataBaseAndPage(AllTLs_DataBase, AllTLs_FromPage)
                        AllAgents_DataBase.sort()
                        AllAgents_FromPage.sort()
                        print AllAgents_DataBase
                        print AllAgents_FromPage
                        CheckTablet.CheckData_DataBaseAndPage(AllAgents_DataBase, AllAgents_FromPage)
                        
                        #Step3: Check Default site data of half a year 
                        #Step3.1:Get data from page
                        DataLSACS_FromPage=Lactual.get_page_teamandsite_Actual(1)
                        KPInumber=len(DataLSACS_FromPage)
                        print DataLSACS_FromPage
                        #Step3.2: Get data from DB
                        #Get lastsixmonthdate TLHrid
                        Current_Date=GetConfig.get_LocalCurrentTime()
                        LastSixMonth_Date=GetConfig.get_TheDateOfLastAnyMonth(6, "Local")
                        Sql_Site=GetConfig.get_sql_content(self.sqlsheetname, self.sql_SiteData).replace("LastSixMonth_Date",LastSixMonth_Date).replace("Current_Date",Current_Date)
                        #print Sql_Site
                        Datalist=HMysql.Get_datafromDB(hostindex, lobname_database, sitename_database, self.dbuser, self.dbpassword, Sql_Site)
                        DataLSACS_DataBase=list(Datalist[1][0][0:KPInumber])
                        print DataLSACS_DataBase
                        CheckTablet.CheckData_DataBaseAndPage(DataLSACS_DataBase, DataLSACS_FromPage)
                        
                        #Step4: Check Default each team's data of half a year
                        AllTLvalue_FromPage=LSACoachingScores.get_AllTLvalue_ByL3(TLnumber,self.KPInumber)
                        print AllTLvalue_FromPage
                        AllTLvalue_DataBase={}
                        #for i in range(0,len(AllTLvalue_FromPage)):
                        for key in AllTLvalue_FromPage:
                            TLHrid=key
                            #KPInumber=len(AllTLvalue_FromPage[key])
                            #TLHrid=AllTLvalue_FromPage[i][0]
                            Sql_teamdata=GetConfig.get_sql_content(self.sqlsheetname, self.sql_TeamData).replace("LastSixMonth_Date",LastSixMonth_Date).replace("TLHrid",TLHrid).replace("Current_Date",Current_Date)
                            TeamDatalist=HMysql.Get_datafromDB(hostindex, lobname_database, sitename_database, self.dbuser, self.dbpassword, Sql_teamdata)
                            #print Sql_Site
                            TeamData=list(TeamDatalist[1][0][0:self.KPInumber])
                            #print TeamData
                            AllTLvalue_DataBase[TLHrid]=TeamData
                        print AllTLvalue_DataBase
                        
                        for key in AllTLvalue_FromPage:
                            CheckTablet.CheckData_DataBaseAndPage(AllTLvalue_DataBase[key], AllTLvalue_FromPage[key])
                            
                        #Step5: Check Default The first three agents' data of each Team half a year
                        TheFirstThreeAgentsValueOfAllTls_FromPage=AllInfoOfAgent_FromPage[1]#For Step5
                        print TheFirstThreeAgentsValueOfAllTls_FromPage
                        TheFirstThreeAgentsValueOfAllTls_DataBase={}
                        for key in TheFirstThreeAgentsValueOfAllTls_FromPage:
                            AgentHrid=key
                            Sql_AgentData=GetConfig.get_sql_content(self.sqlsheetname, self.sql_AgentData).replace("LastSixMonth_Date",LastSixMonth_Date).replace("AgentHrid",AgentHrid).replace("Current_Date",Current_Date)
                            AgentDatalist=HMysql.Get_datafromDB(hostindex, lobname_database, sitename_database, self.dbuser, self.dbpassword, Sql_AgentData)
                            AgentData=list(AgentDatalist[1][0][0:self.KPInumber])
                            TheFirstThreeAgentsValueOfAllTls_DataBase[AgentHrid]=AgentData
                        print TheFirstThreeAgentsValueOfAllTls_DataBase
                        for key in TheFirstThreeAgentsValueOfAllTls_FromPage:
                            CheckTablet.CheckData_DataBaseAndPage(TheFirstThreeAgentsValueOfAllTls_DataBase[key],TheFirstThreeAgentsValueOfAllTls_FromPage[key])
                        
                        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_LeaderShipAcademyCS_OMDefault']
    unittest.main()