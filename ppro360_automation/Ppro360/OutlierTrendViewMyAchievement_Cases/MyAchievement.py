'''
Created on 20180301

@author: luming.zhao
The case is in sheet 'OutlierTrendViewMyAchievement' at line 95-112

'''


import unittest
from public_method import Gl
from public_method.Get_configration_data import Get_configration_data
from public_method.Login import Login
from Tablet_pages.TabletHomepage import TabletHomepage
from Tablet_pages.MyTeamInfoPage import MyTeamInfoPage
from OutlierTrendViewMyAchievement_Pages.MyAchievementPage import MyAchievementPage
from public_method.Get_AllRoleAccountForTest import Get_AllRoleAccountForTest
from public_method.HandleMySQL import HandleMySQL
from CoachingAndTriadCoaching_Pages.BasicInfoforCoaching import BasicInfoforCoaching
from AdminSystem_Pages.AdminHomepage import AdminHomepage
from public_method.KPI_method import KPI_method
from decimal import getcontext, Decimal
#import numpy
import time

class MyAchievement(unittest.TestCase):


    def setUp(self):
        self.caseID="MyAchievement"
        GetData=Get_configration_data()
        #Get URL 
        self.tableturl=GetData.get_TabletUrl()
        self.adminurl=GetData.get_AdminUrl()

        #Get OM account
        OMaccount=GetData.get_OMaccount()
        self.OMuserid=OMaccount["OMuserid"]
        self.OMpassword=OMaccount["OMpassword"]
        #Get all lobs from CSV
        self.testLOBSITE_list=GetData.get_LOBSITEtoTest(self.caseID)
        self.host=GetData.get_StageDatabaseHost()
        self.hostindex=92
        self.dbuser=GetData.get_StageDatabaseUser()
        self.dbpassword=GetData.get_StageDatabasePassword()
        #Yesterday,WTD,MTD for LCBB
        self.tablist=Gl.Multi_timetab#["yesterday","Week-to-Day","Month-to-Day"]#
        self.Adminurl=GetData.get_AdminUrl()
        


    def tearDown(self):
        #Gl.driver.quit() 
        pass


    def test_MyAchievement(self):
        GetConfig=Get_configration_data()
        Tablet=TabletHomepage()
        L=Login()
        MAPage=MyAchievementPage()
        Getaccount=Get_AllRoleAccountForTest()
        HMysql=HandleMySQL()
        BasicInfo=BasicInfoforCoaching()
        MTpage=MyTeamInfoPage()
        KPIMethod=KPI_method()
        #Expected_WeightDic=MAPage.get_MyAchWeight_data_Expected()
        #Header=HeaderPage()

        
        


        
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
                    #Login with OM to find TL account
                    L.Login_tablet(self.tableturl, lobname, sitename, self.OMuserid, self.OMpassword)
                    time.sleep(Gl.waittime)
                    Tablet.click_Myteaminfocircle()
                    TL_hrid=MTpage.get_eachhrid(1)
                    print TL_hrid
                    TL_NAME=MTpage.get_eachusername(1)
                    print TL_NAME
                    L.logout_tablet()
                    #Login admin system to find TL's password
                    TLInfo=Getaccount.get_TLandAgentInfofromAdmin(self.adminurl, lobname, sitename, self.OMuserid, self.OMpassword,TL_hrid)
                    TLpassword=TLInfo["Password"]
                    print TLpassword
                    #TL login tablet to find Agent account
                    L.Login_tablet(self.tableturl, lobname, sitename, TL_hrid, TLpassword)
                    Tablet.click_TL_Myteaminfocircle() 
                    Agent_hrid=MTpage.get_eachhrid(1)
                    print Agent_hrid
                    Agent_NAME=MTpage.get_eachusername(1)
                    print Agent_NAME
                    L.logout_tablet()
                    #Login admin system to find Agent's password
                    AgentInfo=Getaccount.get_TLandAgentInfofromAdmin(self.adminurl, lobname, sitename, self.OMuserid, self.OMpassword,Agent_hrid)
                    Agentpassword=AgentInfo["Password"]
                    print Agentpassword
                    #Agent login tablet to enter 'Myahievement' 
                    L.Login_tablet(self.tableturl, lobname, sitename, Agent_hrid, Agentpassword)
                                        
                    Tablet.click_performancecircle()
                    TeamKPI=MAPage.get_PTeamKPI_page()
                    print TeamKPI
                    GoalKPI=MAPage.get_GoalKPI_page()
                    print GoalKPI
                    Tablet.click_Back()
                    
                    Tablet.click_MyAchievementcircle()
                    

                    
                    print "Start===========Check the UI of My Achievement============"                    

                    
                    for ywm in range(0,len(self.tablist)):
                        MAPage.click_timetab_MyAchievement(ywm+1)
                        
                
                        print "*********************Start********************",
                        print self.tablist[ywm],
                        print "is in testing:"
                        time.sleep(Gl.waittime)
                        #Step1:Verify Only shown KPIs with weight values<>0 + Achievement
                        print "=================1.Verify Each KPI of Weight=============="
                        sql_weightname="select title from kpiscore_weight where score_weight !='0';"
                        WeightValuetlist1=HMysql.Get_datafromDB(self.hostindex, lobname, sitename, self.dbuser, self.dbpassword, sql_weightname) #WeightValuetlist1 is Weight value!=0
                        TotalWeightnameFromDB=WeightValuetlist1[1]
                        WeightDB=TotalWeightnameFromDB[0]
                        print "TotalWeightnameFromDB is :" , TotalWeightnameFromDB
                        TotalWeightnametablet=MAPage.get_weightname_page()
                        print "TotalWeightnametablet is :" ,TotalWeightnametablet
                        '''a=0
                        while a<10:
                            if WeightDB[a]==None:
                                if TotalWeightnametablet[a]=="N/A":
                                    print "WeightDB and tablet dispaly N/A"
                            if WeightDB[a]!=None:
                               WeightDBF=float(WeightDB[a])
                                WeightDBD=Decimal(WeightDBF).quantize(Decimal('0.000'))    
                                WeightDBvalue=round(WeightDBD,2)
                                WeighttabletF=float(TotalWeightnumbertablet[a])
                                WeighttabletD=Decimal(WeighttabletF).quantize(Decimal('0.000'))  
                                Weighttablevalue=round(WeighttabletD,2)
                                assert WeightDBvalue==Weighttablevalue
                                print WeightDBvalue
                                print Weighttablevalue
                            a=a+1 
                                WeightDBValueX=KPIMethod.Decimal_To_Percentage(WeightDB[a])
                                print WeightDBValueX'''
                                            
                        print "Total_Weightnumber_database : ",len(TotalWeightnameFromDB)
                        print "Total_Weightnumber_tablet : ",len(TotalWeightnametablet)
                        assert len(TotalWeightnameFromDB)==len(TotalWeightnametablet)
                        
                        
                        sql_weightvalue="select score_weight from kpiscore_weight  where score_weight !='0';"
                        WeightValuetlist2=HMysql.Get_datafromDB(self.hostindex, lobname, sitename, self.dbuser, self.dbpassword, sql_weightvalue) #WeightValuetlist1 is Weight value!=0
                        #Total_Weightnumber_database=WeightValuesnot0
                        WeightValueFromDB=WeightValuetlist2[1]
                        DBWeight=WeightValueFromDB[0]
                        print "WeightValueFromDB is :" , WeightValueFromDB
                        WeightValue_tablet=MAPage.get_WeightKPI_page()
                        print "WeightValue_tablet",WeightValue_tablet
                        #KPIMethod.Decimal_To_Percentage(WeightValueFromDB)

                        a=0
                        WeightDBD=KPIMethod.Decimal_To_Percentage(DBWeight[a])  
                        a=a+1
                        print WeightDBD
                      
                        # check each KPI's Goal value is the same as performance dashboard page.
                        print "=================1.Verify Each KPI of GOAL=============="
                       
                        sql_goalvalue="select * from goal" #some LOB is 'goal_site'
                        GoalValueList=HMysql.Get_datafromDB(self.hostindex, lobname, sitename, self.dbuser, self.dbpassword, sql_goalvalue)
                        GoalValue_tablet=MAPage.get_GoalKPI_page()
                        print "GoalValue_tablet is :",GoalValue_tablet
                        print "GoalValue_performance is:",GoalKPI
                        
                        GoalValueFromDB=GoalValueList[1]
                        #DBGoal=GoalValueFromDB[0]
                        print "GoalValueFromDB is :" ,GoalValueFromDB

                        '''
                        b=0
                        GoalDBD=KPIMethod.Decimal_To_Percentage(DBGoal[b])
                        b=b+1
                        print GoalDBD
                       '''
                        
                        # check each KPI's TEAM value is the same as performance dashboard  page.
                        print "=================1.Verify Each KPI of TEAM=============="
                        TEAMValue_tablet=MAPage.get_YourTeamKPI_page()
                        print "TEAMValue_tablet is :",TEAMValue_tablet
                        print "TEAMValue_performance is:",TeamKPI
                        
                    # 6.Click BACK button form top left page.
                    Tablet.click_Back()
                    #Back to home page with page title 'Performance Pro 360'Shonw icons:
                    assert Tablet.get_performancename() == "Performance"#Verify performance displayed
                    assert Tablet.get_MyAchievementname() == "My Achievement"#Verify Coaching displayed
                    assert Tablet.get_Agent_coachingname()=="Coaching" #when agent login,coaching circle behind 'My Achievement' circle.
                    assert Tablet.get_LeadershipAcademyCoachingScoresname_Agent()=="Leadership Academy Coaching Scores"
                    print "ALL module shonw these icons"    
                     

                    #L.logout_tablet()    


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()