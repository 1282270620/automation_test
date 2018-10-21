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
from Tablet_pages.OutlierPage import OutlierPage
from Tablet_pages.HeaderPage import HeaderPage
from public_method.Get_AllRoleAccountForTest import Get_AllRoleAccountForTest
from public_method.HandleMySQL import HandleMySQL
from public_method.KPI_method import KPI_method
import time

class TLEnterOutlier(unittest.TestCase):


    def setUp(self):
        self.caseID="TLEnterOutlier"
        GetData=Get_configration_data()
        #Get URL 
        self.tableturl=GetData.get_TabletUrl()
        self.adminurl=GetData.get_AdminUrl()

        #Get OM account
        OMaccount=GetData.get_OMaccount()
        self.OMuserid=OMaccount["OMuserid"]
        self.OMpassword=OMaccount["OMpassword"]
        self.role="L1"
        #Get all lobs from CSV
        self.testLOBSITE_list=GetData.get_LOBSITEtoTest(self.caseID)
        self.host=GetData.get_StageDatabaseHost()
        
        self.dbuser=GetData.get_StageDatabaseUser()
        self.dbpassword=GetData.get_StageDatabasePassword()
        self.tablist=["Yesterday","Week-to-Date","Month-to-Date","LastTwoMonth","LastMonth"]

    def tearDown(self):
        #Gl.driver.quit() 
        pass


    def test_TLEnterOutlier(self):
        GetConfig=Get_configration_data()
        Tablet=TabletHomepage()
        L=Login()
        OPPage=OutlierPage()
        Getaccount=Get_AllRoleAccountForTest()
        HMysql=HandleMySQL()
        MTpage=MyTeamInfoPage()
        KPIMethod=KPI_method()
        
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
                    
                    #TL login tablet to enter 'Outlier' 
                    L.Login_tablet(self.tableturl, lobname, sitename, TL_hrid, TLpassword)
                                        
                    Tablet.click_TL_outliercircle()
                    #check role is L1                    
                    Header=HeaderPage()
                    assert Header.get_loginRole()==self.role
                    
                    
                    for ywm in range(0,len(self.tablist)):
                        OPPage.click_timetab_MyAchievement(ywm+1)                        
                
                        print "*********************Start********************",
                        print self.tablist[ywm],
                        print "is in testing:"
                        time.sleep(Gl.waittime)
                        
                        if self.tablist[ywm]=="Yesterday":
                            #yesterday check arrows:Weight, Goal, Your Team
                            #yesterday check KPI name 
                            #yesterday check Goal, Your Team KPI Value
                            
                        else:
                            #other tab check section top 20%
                            
                            #other tab check section bottom 20%
                        
                        
                        #Step1:Verify Only shown KPIs with weight values<>0 + Achievement
                        print "=================1.Verify Each KPI of Weight=============="
                        sql_weightname="select title from kpiscore_weight where score_weight !='0';"
                        WeightValuetlist1=HMysql.Get_datafromDB(self.hostindex, lobname, sitename, self.dbuser, self.dbpassword, sql_weightname) #WeightValuetlist1 is Weight value!=0
                        TotalWeightnameFromDB=WeightValuetlist1[1]
                        WeightDB=TotalWeightnameFromDB[0]
                        print "TotalWeightnameFromDB is :" , TotalWeightnameFromDB
                        TotalWeightnametablet=OPPage.get_weightname_page()
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