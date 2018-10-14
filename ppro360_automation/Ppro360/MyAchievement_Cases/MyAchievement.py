'''
Created on 2018.6.21

@author: yalan.yin
'''
import unittest
from public_method import Gl
from public_method.Get_configration_data import Get_configration_data
from public_method.Login import Login
from Tablet_pages.TabletHomepage import TabletHomepage
from public_method.KPI_method import KPI_method
from OutlierTrendViewMyAchievement_Pages.MyAchievementPage import MyAchievementPage
from public_method.Get_AllRoleAccountForTest import Get_AllRoleAccountForTest
from Tablet_pages.HeaderPage import HeaderPage
from public_method.HandleMySQL import HandleMySQL
from OutlierTrendViewMyAchievement_Pages.AgentPerformancePage import AgentPerformancePage
from Tablet_pages.PerformancPage import PerformancePage
import time
from public_method.Check_Tablet import Check_Tablet


class Test(unittest.TestCase):


    def setUp(self):
        self.caseID="MyAchievement"
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

        #Get OM account
        OMaccount=GetData.get_OMaccount()
        self.OMuserid=OMaccount["OMuserid"]
        self.OMpassword=OMaccount["OMpassword"]
        #Get all lobs from CSV
        self.testLOBSITE_list=GetData.get_LOBSITEtoTest(self.caseID)
        self.host=GetData.get_StageDatabaseHost()
        #self.hostindex=92
        #Get AWS hostindex
        self.AWS_hostindex=93
        #Get VXI hostindex
        self.VXI_hostindex=92
        self.dbuser=GetData.get_StageDatabaseUser()
        self.dbpassword=GetData.get_StageDatabasePassword()
        #Yesterday,WTD,MTD for LCBB
        self.tablist=Gl.Multi_timetab#["yesterday","Week-to-Day","Month-to-Day"]#
        self.role='Agent'
        self.LoggedUserRole="AGENT"
        self.PageTitle1='My Achievement'


    def tearDown(self):
        pass


    def testName(self):
        L=Login()
        MAPage=MyAchievementPage()
        HMysql=HandleMySQL()
        KPIMethod=KPI_method()
        THomepage=TabletHomepage()
        Hpage=HeaderPage()
        GetConfig=Get_configration_data()
        GetAgent=Get_AllRoleAccountForTest()
        AP=AgentPerformancePage()
        Ppage=PerformancePage()
        CT=Check_Tablet()
        for i in range(0,len(self.testLOBSITE_list)):
            Flag=GetConfig.get_LOBSITE_STATUS(self.testLOBSITE_list[i])
            if Flag==True:
                each_LOBSITE=self.testLOBSITE_list[i].split(":")
                lobname=each_LOBSITE[0]
                if lobname in self.AWSLOBs_list:
                    tableturl=self.AWS_tableturl
                    hostindex=self.AWS_hostindex
                    Adminurl=self.AWS_adminurl
                elif lobname in self.VXILOBs_list:
                    tableturl=self.VXI_tableturl
                    hostindex=self.VXI_hostindex
                    Adminurl=self.VXI_adminurl
                #Get Site to test
                site_list=each_LOBSITE[1].split("*")
                for n in range(0,len(site_list)):
                    sitename=site_list[n]
                    GetConfig.print_StartTest_message(lobname, sitename)
                    #L.Login_admin(self.adminurl, lobname, sitename, self.OMuserid, self.OMpassword)
                    time.sleep(Gl.waittime)
                    #AdminPage.Enter_BrowseTLAgentAccounts()

                    AgentInfo=GetAgent.get_TLandAgentInfofromAdmin_Byrole(Adminurl, lobname, sitename, self.OMuserid, self.OMpassword, self.role)
                    print "AgentInfo:", AgentInfo
                    
                    
                    
                    #step14.01 login admin to get tl's password
                    #L2Info=GetTL.get_TLandAgentInfofromAdmin(self.adminurl, lobname, sitename, self.OMuserid, self.OMpassword,self.L2_hrid)
                    Agent_hrid=AgentInfo["Hrid"]
                    Agentpassword=AgentInfo["Password"]
                    AgentName=AgentInfo["Name"]
                    #step14.02 TL login tablet
                    L.Login_tablet(tableturl, lobname, sitename, Agent_hrid, Agentpassword)
                   
                    #Ppage.click_backbutton()
                    THomepage.click_MyAchievementcircle()
                   
                    
                    print "Start===========Check the UI of My Achievement============"
                    assert Hpage.get_HeaderTittle()==self.PageTitle1
                    assert Hpage.get_loginLob()==lobname
                    assert Hpage.get_loginSite()==sitename
                    assert Hpage.get_loginName()==AgentName
                    assert Hpage.get_loginRole()==self.LoggedUserRole
                    #assert Hpage.settingButtonexisted()==self.SettingButtonExisting
                    #assert Hpage.backbuttonexisted()==self.BackButtonExisting
                    print "=============check UI successfully==========================="
                    
                    for ywm in range(0,len(self.tablist)):                      
                        MAPage.click_timetab_MyAchievement(ywm+1)
                        print "*********************Start********************",
                        print self.tablist[ywm],
                        print "is in testing:"
                        time.sleep(Gl.waittime)
                        #Step1:Verify Only shown KPIs with weight values<>0 + Achievement
                        print "=================1.Verify Each KPI of Weight=============="
                        sql_weightname="select title from kpiscore_weight where score_weight !='0';"
                        WeightValuetlist1=HMysql.Get_datafromDB(hostindex, lobname, sitename, self.dbuser, self.dbpassword, sql_weightname) #WeightValuetlist1 is Weight value!=0
                        print ' WeightValuetlist1:', WeightValuetlist1
                        TotalWeightnameFromDB=WeightValuetlist1[1]
                        WeightKPINameDBlist=[]
                        for i in range(0,len(TotalWeightnameFromDB)):
                            OneKPIName=TotalWeightnameFromDB[i][0]
                            WeightKPINameDBlist.append(OneKPIName)
                            print 'WeightKPINameDBlist:',WeightKPINameDBlist
    
                        TotalWeightnametablet=MAPage.get_weightname_page()
                        print "TotalWeightnametablet is :" ,TotalWeightnametablet
                        assert len(TotalWeightnametablet)==len(WeightKPINameDBlist)
                        for item in WeightKPINameDBlist:
                            assert item in TotalWeightnametablet
                        print "=================assert weight kpi name successfully======================="
                        
                        sql_weightvalue="select score_weight from kpiscore_weight  where score_weight !='0';"
                        WeightValuetlist2=HMysql.Get_datafromDB(self.hostindex, lobname, sitename, self.dbuser, self.dbpassword, sql_weightvalue) #WeightValuetlist1 is Weight value!=0
                        #Total_Weightnumber_database=WeightValuesnot0
                        WeightValueFromDB=WeightValuetlist2[1]
                        print 'WeightValueFromDB:',WeightValueFromDB
                        WeightKPIValueDBlist=[]
                        for i in range(0,len(WeightValueFromDB)):
                            OneKPIValue=KPIMethod.Decimal_To_Percentage(WeightValueFromDB[i][0])
                            WeightKPIValueDBlist.append(OneKPIValue)
                            print 'WeightKPIValueDBlist:',WeightKPIValueDBlist
                        WeightValue_tablet=MAPage.get_WeightKPI_page()
                        print "WeightValue_tablet",WeightValue_tablet
                        assert len(WeightKPIValueDBlist)==len(WeightValue_tablet)
                        for item in WeightKPIValueDBlist:
                            assert item in WeightValue_tablet
                        print "=================assert weight value successfully======================="                        
                        MAPage.click_back()
                        THomepage.click_performancecircle()
                        print '======================get goal/team/agent kpi value from performance Page=========================='
                        Ppage.click_timetab_performance(ywm+1)
                        print "*********************Start********************",
                        print "Get values from",
                        print self.tablist[ywm],
                        time.sleep(Gl.waittime)
        
                        Kpinumber=Ppage.get_KPInumber()
                        kpiname=Ppage.get_KPIname_list(Kpinumber)
                        print "kpiname:",kpiname
                        
                        #AllGoalValue_OnPerformancePage=AP.get_GoalValue_page()
                        AllGoalValue_OnPerformancePage=Ppage.get_AllKPIsofGoal_list(Kpinumber)
                        
                        print 'AllGoalValue_OnPerformancePage:', AllGoalValue_OnPerformancePage
                        GoalDic1={}
                        for i in range(0,len(AllGoalValue_OnPerformancePage)-1):
                            GoalDic1[kpiname[i]]=AllGoalValue_OnPerformancePage[i+1]
                            
                        #AllTeamValue_OnperformancePage=AP.get_TeamValue_page()
                        AllTeamValue_OnperformancePage=Ppage.get_AllKPIsofTeam_list(Kpinumber)
                        print "AllTeamValue_OnperformancePage:", AllTeamValue_OnperformancePage
                        TeamValueOnPerformance=[]
                        for i in range(1,len(AllTeamValue_OnperformancePage)):
                            TeamValue=AllTeamValue_OnperformancePage[i][0]
                            TeamValueOnPerformance.append(TeamValue)
                            print "Team value on Performance page:", TeamValueOnPerformance
                        TeamDic1={}
                        for i in range(0,len(TeamValueOnPerformance)):
                            TeamDic1[kpiname[i]]=TeamValueOnPerformance[i]
                            print TeamDic1
                        AllAgentValue_OnPerformancePage=AP.get_AgentValue_page()
                        print 'AllAgentValue_OnPerformancePage:',AllAgentValue_OnPerformancePage
                        AgentDic1={}
                        for i in range(0,len(AllAgentValue_OnPerformancePage)):
                            
                            AgentDic1[kpiname[i]]=AllAgentValue_OnPerformancePage[i]
                            
                        
                        
                        Ppage.click_backbutton()
                        THomepage.click_MyAchievementcircle()
                        MAPage.click_timetab_MyAchievement(ywm+1)
                        AllKpiName_MApage=MAPage.get_allkpiname_page()
                        print "AllKpiName_MApage:", AllKpiName_MApage
                        GoalValue_MyAchievePage=MAPage.get_GoalKPI_page()
                        print "GoalValue_MyAchievePage:",GoalValue_MyAchievePage
                        GoalDic2={}
                        for i in range(0,len(GoalValue_MyAchievePage)):
                            GoalDic2[AllKpiName_MApage[i]]=GoalValue_MyAchievePage[i]
                            
                        TeamValue_MyAchivementPage=MAPage.get_YourTeamKPI_page()
                        print 'TeamValue_MyAchivementPage:', TeamValue_MyAchivementPage
                        TeamDic2={}
                        for i in range(0,len(TeamValue_MyAchivementPage)):
                            TeamDic2[AllKpiName_MApage[i]]=TeamValue_MyAchivementPage[i]
                        AgentValue_MyAchievePage=MAPage.get_AgentValue_page()
                        print 'AgentValue_MyAchievePage:', AgentValue_MyAchievePage
                        AgentDic2={}
                        for i in range(0,len(AgentValue_MyAchievePage)):
                            AgentDic2[AllKpiName_MApage[i]]=AgentValue_MyAchievePage[i]
                        for item in AllKpiName_MApage:
                            print "GoalDic1:", GoalDic1
                            print "GoalDic2:", GoalDic2
                            assert GoalDic1[item]==GoalDic2[item]
                            print "TeamDic1:", TeamDic1
                            print "TeamDic2", TeamDic2
                            assert TeamDic1[item]==TeamDic2[item]
                            #assert AgentDic1[item]==GoalDic2[item]
                        
                        
                        
                    MAPage.click_back()
                    CT.Check_TabletHomepageCircle_Agent(lobname)
                    
                    
                    


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()