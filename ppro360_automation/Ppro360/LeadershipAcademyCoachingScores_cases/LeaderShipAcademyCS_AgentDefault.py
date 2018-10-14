'''
Created on Jun 13, 2018

@author: Sabrina Guo
'''
import unittest
from public_method.Get_configration_data import Get_configration_data
from public_method.Get_AllRoleAccountForTest import Get_AllRoleAccountForTest
from Tablet_pages.TabletHomepage import TabletHomepage
from public_method.Login import Login
from public_method.Check_Tablet import Check_Tablet
from public_method.HandleMySQL import HandleMySQL
from public_method.LeadershipDate_Actual import LeadershipDate_Actual
class LeaderShipAcademyCS_AgentDefault(unittest.TestCase):


    def setUp(self):
        self.caseID="LeaderShipAcademyCS_AgentDefault"
        GetData=Get_configration_data()
        
        #Get LOBs have no LSACS
        self.LOBs_NoLSACS_list=GetData.get_LOBHasNoLSACS_list()
        #Get OM account
        OMaccount=GetData.get_OMaccount()
        self.OMuserid=OMaccount["OMuserid"]
        self.OMpassword=OMaccount["OMpassword"]
        self.role="Agent"
        #Get all lobs from CSV
        self.testLOBSITE_list=GetData.get_LOBSITEtoTest(self.caseID)
        
        #Database info
        self.host=GetData.get_StageDatabaseHost()
        self.dbuser=GetData.get_StageDatabaseUser()
        self.dbpassword=GetData.get_StageDatabasePassword()
        
        #Info of configuration
        self.sqlsheetname="SQLs"
        self.sqlitemname="Sql_Site_LeaderShipAcademyCoachingScores"
        #Special lobname
        self.AllSpecialLobs_list=GetData.get_Allspeciallobs_ByDataBase()
        #Special sitename
        self.AllSpecialSites_list=GetData.get_Allspecialsites_ByDataBase()


    def tearDown(self):
        pass
        #Gl.driver.quit()
        


    def test_LeaderShipAcademyCS_AgentDefault(self):
        Tablet=TabletHomepage()
        GetAgent=Get_AllRoleAccountForTest()
        GetConfig=Get_configration_data()
        L=Login()
        #LSACoachingScores=LeadershipAcademyCoachingScoresPage()
        CheckTablet=Check_Tablet()
        HMysql=HandleMySQL()
        Lactual=LeadershipDate_Actual()
        #Test several LOBs
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
                        AgentInfo=GetAgent.get_TLandAgentInfofromAdmin_Byrole(adminurl, lobname, sitename, self.OMuserid, self.OMpassword, self.role)
                        AgentHrid=AgentInfo["Hrid"]
                        AgentPassword=AgentInfo["Password"]

                        L.Login_tablet(tableturl, lobname, sitename, AgentHrid, AgentPassword)
                        Tablet.click_LeadershipAcademyCoachingScores_Agent()
                        
                        #Step1:Check all Default values of Conditions
                        CheckTablet.Check_DefaultValuesOfQueryConditions_LeaderShipAcademyCoachingScores()
                        
                        #Step2: Check Default data of half a year 
                        #Step2.1: Get data from DB
                        #Get lastsixmonthdate
                        Current_Date=GetConfig.get_LocalCurrentTime()
                        LastSixMonth_Date=GetConfig.get_TheDateOfLastAnyMonth(6, "Local")
                        Sql_Site=GetConfig.get_sql_content(self.sqlsheetname, self.sqlitemname).replace("LastSixMonth_Date",LastSixMonth_Date).replace("Current_Date",Current_Date)
                        print Sql_Site
                        Datalist=HMysql.Get_datafromDB(hostindex, lobname_database, sitename_database, self.dbuser, self.dbpassword, Sql_Site)
                        DataLSACS_DataBase=list(Datalist[1][0][0:7])
                        print DataLSACS_DataBase
                        #Step2.2:Get data from page
                        DataLSACS_FromPage=Lactual.get_page_teamandsite_Actual(1)
                        print DataLSACS_FromPage
                        CheckTablet.CheckData_DataBaseAndPage(DataLSACS_DataBase, DataLSACS_FromPage)
                    
                        
                        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_LeaderShipAcademyCS_AgentDefault']
    unittest.main()