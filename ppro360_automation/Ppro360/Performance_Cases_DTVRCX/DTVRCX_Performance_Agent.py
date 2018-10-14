'''
Created on Apr 5, 2017

@author: symbio
'''
import unittest
from Performance_Cases_DTVRCX.Get_PerformanceData_Actual_DTVRCX import Get_PerformanceData_Actual_DTVRCX
from Performance_Cases_DTVRCX.Get_PerformanceData_Expected_DTVRCX import Get_PerformanceData_Expected_DTVRCX
from public_method import Gl
from public_method.Get_configration_data import Get_configration_data
from public_method.Login import Login
from Tablet_pages.TabletHomepage import TabletHomepage
from Tablet_pages.PerformancPage import PerformancePage
import time
from public_method.Get_AllRoleAccountForTest import Get_AllRoleAccountForTest


class DTVRCX_Performance_Agent(unittest.TestCase):


    def setUp(self):
        self.caseID="DTVRCX_Performance_Agent"
        GetData=Get_configration_data()
        #Get URL 
        self.tableturl=GetData.get_TabletUrl()
        #Get OM account
        OMaccount=GetData.get_OMaccount()
        self.OMuserid=OMaccount["OMuserid"]
        self.OMpassword=OMaccount["OMpassword"]
        #TL2's name
        ''' Name='Tl2 Test' '''
        self.TL_name='Tl2 Test'
        self.TL_userid='300016'
        #Agent14's name
        ''' Name='Agent 14' '''
        self.Agent_name='Agent 14'
        self.Agent_userid='300119'
        #Get all lobs from CSV
        self.testLOBSITE_list=GetData.get_LOBSITEtoTest(self.caseID)
        
        #Yesterday,WTD,MTD for DTVRCX
        self.tablist=Gl.Multi_timetab#["yesterday","Week-to-Day","Month-to-Day"]
        


    def tearDown(self):
        #Gl.driver.quit() 
        pass


    def test_DTVRCX_Performance_OM(self):
        GetConfig=Get_configration_data()
        L=Login()
        Get_account=Get_AllRoleAccountForTest()
        THomepage=TabletHomepage()
        Ppage=PerformancePage()
        GetPData_Actual=Get_PerformanceData_Actual_DTVRCX()
        
        #Get Goal Expected
        GetPData_Expected=Get_PerformanceData_Expected_DTVRCX()
        lineindex=2#The goal is in the row 3 of excel file,so linedex is 2
        Expected_GoalDic=GetPData_Expected.get_DTVRCX_Goal_Expected(lineindex)
        
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
                    
                    #Get TL2's account
                    L.Login_tablet(self.tableturl, lobname, sitename, self.OMuserid, self.OMpassword)
                    THomepage.click_Myteaminfocircle()
                    lineindex=Get_account.Get_lineindex(self.TL_userid)
                    TL2_Info=Get_account.Get_MyTeamInfo(lineindex)
                    TL2_name=TL2_Info['Name']
                    TL2_password=TL2_Info['Password']
                    L.logout_tablet()
                    if TL2_name!=self.TL_name:
                        print "!!!!!!!!!!TL2 is not incorrect, please check it!!!!!!!!!"
                    else:
                        #Agent14's user id and password
                        L.Login_tablet(self.tableturl, lobname, sitename, self.TL_userid, TL2_password)
                        THomepage.click_TL_Myteaminfocircle()
                        lineindex=Get_account.Get_lineindex(self.Agent_userid)
                        Agent14_Info=Get_account.Get_MyTeamInfo(lineindex)
                        Agent14_name=Agent14_Info['Name']
                        Agent14_password=Agent14_Info['Password']
                        L.logout_tablet()
                        if Agent14_name!=self.Agent_name:
                            print "!!!!!!!!!!Agent14 is not incorrect, please check it!!!!!!!!!"
                        else:
        
                            #Step0.1:All data has been ready manually
                            #Step0.3:Login with OM to do upload work
                            L.Login_tablet(self.tableturl, lobname, sitename, self.Agent_userid, Agent14_password)
                            Achiev_PerformanceCircle=THomepage.get_Achiev_performancecircle()
                            THomepage.click_performancecircle()
                            Achiev_TEAM_Monthly=GetPData_Actual.get_DTVRCX_TEAM_Data_()['Achiev'][0]
                            print "=================The value is the same as SITE KPI of monthly report page.=============="                    
                            assert Achiev_PerformanceCircle==Achiev_TEAM_Monthly
                            
                            for ywm in range(0,len(self.tablist)):
                                Ppage.click_timetab_performance(ywm+1)
                                '''
                                if self.tablist[ywm]=="yesterday":
                                    Ppage.click_ytd()
                                elif self.tablist[ywm]== "Week-to-Day":
                                    Ppage.click_wtd()
                                elif self.tablist[ywm]=="Month-to-Day":
                                    Ppage.click_mtd()'''
                                
                                print "*********************Start********************",
                                print self.tablist[ywm],
                                print "is in testing:"
                                time.sleep(Gl.waittime)
                                #Step1:Verify Goal
                                print "=================1.Verify Each KPI of Goal=============="
                                Actual_GoalDic=GetPData_Actual.get_DTVRCX_Goal_Actual()#GET ACTUAL GOAL FORM PERFORMANCE PAGE
                                assert Expected_GoalDic["CombinedGoalRate"]==Actual_GoalDic["CombinedGoalRate"]
                                assert Expected_GoalDic["WBAttainmant"]==Actual_GoalDic["WBAttainmant"]
                                assert Expected_GoalDic["CCTAttainmant"]==Actual_GoalDic["CCTAttainmant"]
                                assert Expected_GoalDic["DISCAttainmant"]==Actual_GoalDic["DISCAttainmant"]
                                assert Expected_GoalDic["IPBBGrossSales"]==Actual_GoalDic["IPBBGrossSales"]
                                assert Expected_GoalDic["BroadbandAttachRate"]==Actual_GoalDic["BroadbandAttachRate"]
                                assert Expected_GoalDic["AgentSatisfaction"]==Actual_GoalDic["AgentSatisfaction"]
                                assert Expected_GoalDic['Achiev']==Actual_GoalDic["Achiev"]
                                
                                
                                '''Prepare Data for the following test '''
                                if self.tablist[ywm]=="LastTwoMonth":
                                    Expected_KPIofSITEDic=GetPData_Expected.get_DTVRCX_Performance_Data_Expected(134)#For Step2
                                elif self.tablist[ywm]=="LastMonth":
                                    Expected_KPIofSITEDic=GetPData_Expected.get_DTVRCX_Performance_Data_Expected(123)#For Step2
                                    Expected_KPIofTl2=GetPData_Expected.get_DTVRCX_Performance_Data_Expected(122)#For Step3
                                    Expected_KPIofAgent14=GetPData_Expected.get_DTVRCX_Performance_Data_Expected(121)#For Step6
                                elif self.tablist[ywm]=="Yesterday":
                                    Expected_KPIofSITEDic=GetPData_Expected.get_DTVRCX_Performance_Data_Expected(23)#For Step2
                                    Expected_KPIofTl2=GetPData_Expected.get_DTVRCX_Performance_Data_Expected(22)#For Step3
                                    Expected_KPIofAgent14=GetPData_Expected.get_DTVRCX_Performance_Data_Expected(21)#For Step4
                                    
                                elif self.tablist[ywm]== "Week-to-Date":
                                    Expected_KPIofSITEDic=GetPData_Expected.get_DTVRCX_Performance_Data_Expected(77)#For Step2
                                    Expected_KPIofTl2=GetPData_Expected.get_DTVRCX_Performance_Data_Expected(76)#For Step3
                                    Expected_KPIofAgent14=GetPData_Expected.get_DTVRCX_Performance_Data_Expected(75)#For Step4
                                elif self.tablist[ywm]=="Month-to-Date":
                                    Expected_KPIofSITEDic=GetPData_Expected.get_DTVRCX_Performance_Data_Expected(99)#For Step2
                                    Expected_KPIofTl2=GetPData_Expected.get_DTVRCX_Performance_Data_Expected(98)#For Step3
                                    Expected_KPIofAgent14=GetPData_Expected.get_DTVRCX_Performance_Data_Expected(97)#For Step4
                                
                                #Step2:Verify KPI of SITES
                                print "=================2.Verify Each KPI of site, color, achievement=============="
                                '''Expected_KPIofSITEDic is from above.'''
                                print Expected_KPIofSITEDic
                                #Step2.2:Get the Actual KPI of site
                                '''Actual_KPIofSITEDic is from blow.''' 
                                Actual_KPIofSITEDic=GetPData_Actual.get_DTVRCX_SITE_Data_()
                                print Actual_KPIofSITEDic
                                #Step2.3:assert Expected==Actual
                                assert Expected_KPIofSITEDic["CombinedGoalRate"][0]==Actual_KPIofSITEDic["CombinedGoalRate"][0]#0 is KPI value
                                assert Expected_KPIofSITEDic["CombinedGoalRate"][1]==Actual_KPIofSITEDic["CombinedGoalRate"][1]#1 is KPI status
                                assert Expected_KPIofSITEDic["WBAttainmant"][0]==Actual_KPIofSITEDic["WBAttainmant"][0]#0 is KPI value
                                assert Expected_KPIofSITEDic["WBAttainmant"][1]==Actual_KPIofSITEDic["WBAttainmant"][1]#1 is KPI status
                                assert Expected_KPIofSITEDic["CCTAttainmant"][0]==Actual_KPIofSITEDic["CCTAttainmant"][0]#0 is KPI value
                                assert Expected_KPIofSITEDic["CCTAttainmant"][1]==Actual_KPIofSITEDic["CCTAttainmant"][1]#1 is KPI status
                                assert Expected_KPIofSITEDic["DISCAttainmant"][0]==Actual_KPIofSITEDic["DISCAttainmant"][0]#0 is KPI value
                                assert Expected_KPIofSITEDic["DISCAttainmant"][1]==Actual_KPIofSITEDic["DISCAttainmant"][1]#1 is KPI status
                                assert Expected_KPIofSITEDic["IPBBGrossSales"][0]==Actual_KPIofSITEDic["IPBBGrossSales"][0]#0 is KPI value
                                assert Expected_KPIofSITEDic["IPBBGrossSales"][1]==Actual_KPIofSITEDic["IPBBGrossSales"][1]#1 is KPI status
                                assert Expected_KPIofSITEDic["BroadbandAttachRate"][0]==Actual_KPIofSITEDic["BroadbandAttachRate"][0]#0 is KPI value
                                assert Expected_KPIofSITEDic["BroadbandAttachRate"][1]==Actual_KPIofSITEDic["BroadbandAttachRate"][1]#1 is KPI status
                                assert Expected_KPIofSITEDic["AgentSatisfaction"][0]==Actual_KPIofSITEDic["AgentSatisfaction"][0]#0 is KPI value
                                assert Expected_KPIofSITEDic["AgentSatisfaction"][1]==Actual_KPIofSITEDic["AgentSatisfaction"][1]#1 is KPI status
                                assert Expected_KPIofSITEDic["Achiev"][0]==Actual_KPIofSITEDic["Achiev"][0]#0 is KPI value
                                ''' Achiev has no KPI sort '''
                                
                                if self.tablist[ywm]!="LastTwoMonth":
                                    #Step3:Verify achievement of Tl1
                                    print "=================3.Verify TEAM (TL2's) KPI.=============="
                                    #Step3.1:Get the Expected achievement of Tl1
                                    '''Expected_KPIofTl2 is from above, and  Expected_Achi_Tl2 is from below'''
                                    print Expected_KPIofTl2
                                    #Step3.2:Get the Actual achievement of Tl2(TEAM)
                                    Actual_KPIofTl2=GetPData_Actual.get_DTVRCX_TEAM_Data_()
                                    print Actual_KPIofTl2
                                    
                                    #Step3.3:assert Expected==Actual
                                    assert Expected_KPIofTl2["CombinedGoalRate"][0]==Actual_KPIofTl2["CombinedGoalRate"][0]#0 is KPI value
                                    assert Expected_KPIofTl2["CombinedGoalRate"][1]==Actual_KPIofTl2["CombinedGoalRate"][1]#1 is KPI status
                                    assert Expected_KPIofTl2["WBAttainmant"][0]==Actual_KPIofTl2["WBAttainmant"][0]#0 is KPI value
                                    assert Expected_KPIofTl2["WBAttainmant"][1]==Actual_KPIofTl2["WBAttainmant"][1]#1 is KPI status
                                    assert Expected_KPIofTl2["CCTAttainmant"][0]==Actual_KPIofTl2["CCTAttainmant"][0]#0 is KPI value
                                    assert Expected_KPIofTl2["CCTAttainmant"][1]==Actual_KPIofTl2["CCTAttainmant"][1]#1 is KPI status
                                    assert Expected_KPIofTl2["DISCAttainmant"][0]==Actual_KPIofTl2["DISCAttainmant"][0]#0 is KPI value
                                    assert Expected_KPIofTl2["DISCAttainmant"][1]==Actual_KPIofTl2["DISCAttainmant"][1]#1 is KPI status
                                    assert Expected_KPIofTl2["IPBBGrossSales"][0]==Actual_KPIofTl2["IPBBGrossSales"][0]#0 is KPI value
                                    assert Expected_KPIofTl2["IPBBGrossSales"][1]==Actual_KPIofTl2["IPBBGrossSales"][1]#1 is KPI status
                                    assert Expected_KPIofTl2["BroadbandAttachRate"][0]==Actual_KPIofTl2["BroadbandAttachRate"][0]#0 is KPI value
                                    assert Expected_KPIofTl2["BroadbandAttachRate"][1]==Actual_KPIofTl2["BroadbandAttachRate"][1]#1 is KPI status
                                    assert Expected_KPIofTl2["AgentSatisfaction"][0]==Actual_KPIofTl2["AgentSatisfaction"][0]#0 is KPI value
                                    assert Expected_KPIofTl2["AgentSatisfaction"][1]==Actual_KPIofTl2["AgentSatisfaction"][1]#1 is KPI status
                                    assert Expected_KPIofTl2["Achiev"][0]==Actual_KPIofTl2["Achiev"][0]#0 is KPI value
                                

                                
                                    #Step4:Verify achievement of all Tl1's Agents 
                                    print "=================4.Verify Agent14's all KPIs=============="                       
                                    #Step4.1:Get the Expected achievement of all Tl1's Agents
                                    print "=================4.Expected Agent14's all KPIs==============" 
                                    print Expected_KPIofAgent14
                                   
                                    #Step4.2:Get the Actual achievement of all Tl1's Agents
                                    print "=================4.Actual Agent14's all KPIs=============="
                                    Actual_KPIofAgent14=GetPData_Actual.get_DTVRCX_AgentKPI_Agent_Actual()
                                    print Actual_KPIofAgent14
                                    
                                    #Step4.3:assert Expected==Actual
                                    assert Expected_KPIofAgent14["CombinedGoalRate"][0]==Actual_KPIofAgent14["CombinedGoalRate"][0]#0 is KPI value
                                    assert Expected_KPIofAgent14["CombinedGoalRate"][1]==Actual_KPIofAgent14["CombinedGoalRate"][1]#1 is KPI status
                                    assert Expected_KPIofAgent14["WBAttainmant"][0]==Actual_KPIofAgent14["WBAttainmant"][0]#0 is KPI value
                                    assert Expected_KPIofAgent14["WBAttainmant"][1]==Actual_KPIofAgent14["WBAttainmant"][1]#1 is KPI status
                                    assert Expected_KPIofAgent14["CCTAttainmant"][0]==Actual_KPIofAgent14["CCTAttainmant"][0]#0 is KPI value
                                    assert Expected_KPIofAgent14["CCTAttainmant"][1]==Actual_KPIofAgent14["CCTAttainmant"][1]#1 is KPI status
                                    assert Expected_KPIofAgent14["DISCAttainmant"][0]==Actual_KPIofAgent14["DISCAttainmant"][0]#0 is KPI value
                                    assert Expected_KPIofAgent14["DISCAttainmant"][1]==Actual_KPIofAgent14["DISCAttainmant"][1]#1 is KPI status
                                    assert Expected_KPIofAgent14["IPBBGrossSales"][0]==Actual_KPIofAgent14["IPBBGrossSales"][0]#0 is KPI value
                                    assert Expected_KPIofAgent14["IPBBGrossSales"][1]==Actual_KPIofAgent14["IPBBGrossSales"][1]#1 is KPI status
                                    assert Expected_KPIofAgent14["BroadbandAttachRate"][0]==Actual_KPIofAgent14["BroadbandAttachRate"][0]#0 is KPI value
                                    assert Expected_KPIofAgent14["BroadbandAttachRate"][1]==Actual_KPIofAgent14["BroadbandAttachRate"][1]#1 is KPI status
                                    assert Expected_KPIofAgent14["AgentSatisfaction"][0]==Actual_KPIofAgent14["AgentSatisfaction"][0]#0 is KPI value
                                    assert Expected_KPIofAgent14["AgentSatisfaction"][1]==Actual_KPIofAgent14["AgentSatisfaction"][1]#1 is KPI status
                            L.logout_tablet()
                               


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()