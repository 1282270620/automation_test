'''
Created on 20171010

@author: luming.zhao
'''

import unittest
from Performance_Cases_DTVSS.Get_PerformanceData_Expected_DTVSS import Get_PerformanceData_Expected_DTVSS
from Performance_Cases_DTVSS.Get_PerformanceData_Actual_DTVSS import Get_PerformanceData_Actual_DTVSS
from public_method import Gl
from public_method.Get_configration_data import Get_configration_data
from public_method.Login import Login
from Tablet_pages.TabletHomepage import TabletHomepage
from Tablet_pages.PerformancPage import PerformancePage
import time
from public_method.Get_AllRoleAccountForTest import Get_AllRoleAccountForTest


class DTVSS_Performance_Agent(unittest.TestCase):


    def setUp(self):
        self.caseID="DTVSS_Performance_Agent"
        GetData=Get_configration_data()
        #Get URL 
        self.tableturl=GetData.get_TabletUrl()
        #Get OM account
        OMaccount=GetData.get_OMaccount()
        self.OMuserid=OMaccount["OMuserid"]
        self.OMpassword=OMaccount["OMpassword"]
        #TL2's name
        ''' Name='Tl1 Test' '''
        self.TL_name='Tl1 Test'
        self.TL_userid='321170'
        #Agent14's name
        ''' Name='Agent 11' '''
        self.Agent_name='Agent 11'
        self.Agent_userid='321062'
        #Get all lobs from CSV
        self.testLOBSITE_list=GetData.get_LOBSITEtoTest(self.caseID)
        
        #Yesterday,WTD,MTD for DTVRCX
        self.tablist=Gl.Multi_timetab#["yesterday","Week-to-Day","Month-to-Day"]
        


    def tearDown(self):
        #Gl.driver.quit() 
        pass


    def test_DTVSS_Performance_OM(self):
        GetConfig=Get_configration_data()
        L=Login()
        Get_account=Get_AllRoleAccountForTest()
        THomepage=TabletHomepage()
        Ppage=PerformancePage()
        GetPData_Actual=Get_PerformanceData_Actual_DTVSS()
        
        #Get Goal Expected
        GetPData_Expected=Get_PerformanceData_Expected_DTVSS()
        lineindex=2#The goal is in the row 3 of excel file,so linedex is 2
        Expected_GoalDic=GetPData_Expected.get_DTVSS_Goal_Expected(lineindex)
        
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
                    TL1_Info=Get_account.Get_MyTeamInfo(lineindex)
                    TL1_name=TL1_Info['Name']
                    TL1_password=TL1_Info['Password']
                    L.logout_tablet()
                    if TL1_name!=self.TL_name:
                        print "!!!!!!!!!!TL1 is not incorrect, please check it!!!!!!!!!"
                    else:
                        #Agent14's user id and password
                        L.Login_tablet(self.tableturl, lobname, sitename, self.TL_userid, TL1_password)
                        THomepage.click_TL_Myteaminfocircle()
                        lineindex=Get_account.Get_lineindex(self.Agent_userid)
                        Agent11_Info=Get_account.Get_MyTeamInfo(lineindex)
                        Agent11_name=Agent11_Info['Name']
                        Agent11_password=Agent11_Info['Password']
                        L.logout_tablet()
                        if Agent11_name!=self.Agent_name:
                            print "!!!!!!!!!!Agent11 is not incorrect, please check it!!!!!!!!!"
                        else:
        
                            #Step0.1:All data has been ready manually
                            #Step0.3:Login with OM to do upload work
                            L.Login_tablet(self.tableturl, lobname, sitename, self.Agent_userid, Agent11_password)
                            Achiev_PerformanceCircle=THomepage.get_Achiev_performancecircle()
                            THomepage.click_performancecircle()
                            Achiev_TEAM_Monthly=GetPData_Actual.get_DTVSS_TEAM_Data_()['Achiev'][0]
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
                                Actual_GoalDic=GetPData_Actual.get_DTVSS_Goal_Actual()#GET ACTUAL GOAL FORM PERFORMANCE PAGE
                                assert Expected_GoalDic["ActivationRateModify"]==Actual_GoalDic["ActivationRateModify"]
                                assert Expected_GoalDic["CancelTransfer"]==Actual_GoalDic["CancelTransfer"]
                                assert Expected_GoalDic["CancelIVR"]==Actual_GoalDic["CancelIVR"]
                                assert Expected_GoalDic["IPBBNet"]==Actual_GoalDic["IPBBNet"]
                                print "Expected_GoalDic[IPBBNet]==Actual_GoalDic[IPBBNet]:",Expected_GoalDic["IPBBNet"],Actual_GoalDic["IPBBNet"]
                                assert Expected_GoalDic["MobilityGrossSales"]==Actual_GoalDic["MobilityGrossSales"]
                                assert Expected_GoalDic["AgentSatisfaction"]==Actual_GoalDic["AgentSatisfaction"]

                                
                                
                                '''Prepare Data for the following test '''
                                if self.tablist[ywm]=="LastTwoMonth":
                                    Expected_KPIofSITEDic=GetPData_Expected.get_DTVSS_Performance_Data_Expected(121)#For Step2
                                    Expected_KPIofTl1=GetPData_Expected.get_DTVSS_Performance_Data_Expected(120)#For Step3
                                    Expected_KPIofAgent11=GetPData_Expected.get_DTVSS_Performance_Data_Expected(119)#For Step6
                                elif self.tablist[ywm]=="LastMonth":
                                    Expected_KPIofSITEDic=GetPData_Expected.get_DTVSS_Performance_Data_Expected(110)#For Step2
                                    Expected_KPIofTl1=GetPData_Expected.get_DTVSS_Performance_Data_Expected(108)#For Step3
                                    Expected_KPIofAgent11=GetPData_Expected.get_DTVSS_Performance_Data_Expected(107)#For Step6
                                elif self.tablist[ywm]=="Yesterday":
                                    Expected_KPIofSITEDic=GetPData_Expected.get_DTVSS_Performance_Data_Expected(27)#For Step2
                                    Expected_KPIofTl1=GetPData_Expected.get_DTVSS_Performance_Data_Expected(16)#For Step3
                                    Expected_KPIofAgent11=GetPData_Expected.get_DTVSS_Performance_Data_Expected(15)#For Step4
                                    
                                elif self.tablist[ywm]== "Week-to-Date":
                                    Expected_KPIofSITEDic=GetPData_Expected.get_DTVSS_Performance_Data_Expected(70)#For Step2
                                    Expected_KPIofTl1=GetPData_Expected.get_DTVSS_Performance_Data_Expected(68)#For Step3
                                    Expected_KPIofAgent11=GetPData_Expected.get_DTVSS_Performance_Data_Expected(67)#For Step4
                                elif self.tablist[ywm]=="Month-to-Date":
                                    Expected_KPIofSITEDic=GetPData_Expected.get_DTVSS_Performance_Data_Expected(90)#For Step2
                                    Expected_KPIofTl1=GetPData_Expected.get_DTVSS_Performance_Data_Expected(88)#For Step3
                                    Expected_KPIofAgent11=GetPData_Expected.get_DTVSS_Performance_Data_Expected(87)#For Step4
                                
                                #Step2:Verify KPI of SITES
                                print "=================2.Verify Each KPI of site, color, achievement=============="
                                '''Expected_KPIofSITEDic is from above.'''
                                print Expected_KPIofSITEDic
                                #Step2.2:Get the Actual KPI of site
                                '''Actual_KPIofSITEDic is from blow.''' 
                                Actual_KPIofSITEDic=GetPData_Actual.get_DTVSS_SITE_Data_()
                                print Actual_KPIofSITEDic
                                #Step2.3:assert Expected==Actual
                                assert Expected_KPIofSITEDic["ActivationRateModify"][0]==Actual_KPIofSITEDic["ActivationRateModify"][0]#0 is KPI value
                                assert Expected_KPIofSITEDic["ActivationRateModify"][1]==Actual_KPIofSITEDic["ActivationRateModify"][1]#1 is KPI status
                                assert Expected_KPIofSITEDic["CancelTransfer"][0]==Actual_KPIofSITEDic["CancelTransfer"][0]#0 is KPI value
                                assert Expected_KPIofSITEDic["CancelTransfer"][1]==Actual_KPIofSITEDic["CancelTransfer"][1]#1 is KPI status
                                assert Expected_KPIofSITEDic["CancelIVR"][0]==Actual_KPIofSITEDic["CancelIVR"][0]#0 is KPI value
                                assert Expected_KPIofSITEDic["CancelIVR"][1]==Actual_KPIofSITEDic["CancelIVR"][1]#1 is KPI status
                                assert Expected_KPIofSITEDic["IPBBNet"][0]==Actual_KPIofSITEDic["IPBBNet"][0]#0 is KPI value
                                assert Expected_KPIofSITEDic["IPBBNet"][1]==Actual_KPIofSITEDic["IPBBNet"][1]#1 is KPI status
                                assert Expected_KPIofSITEDic["MobilityGrossSales"][0]==Actual_KPIofSITEDic["MobilityGrossSales"][0]#0 is KPI value
                                assert Expected_KPIofSITEDic["MobilityGrossSales"][1]==Actual_KPIofSITEDic["MobilityGrossSales"][1]#1 is KPI status
                                assert Expected_KPIofSITEDic["AgentSatisfaction"][0]==Actual_KPIofSITEDic["AgentSatisfaction"][0]#0 is KPI value
                                #assert Expected_KPIofSITEDic["AgentSatisfaction"][1]==Actual_KPIofSITEDic["AgentSatisfaction"][1]#1 is KPI status
                                assert Expected_KPIofSITEDic["Achiev"][0]==Actual_KPIofSITEDic["Achiev"][0]#0 is KPI value
                                ''' Achiev has no KPI sort '''
                                
                                if self.tablist[ywm]!="LastTwoMonth":
                                    #Step3:Verify achievement of Tl1
                                    print "=================3.Verify TEAM (TL1's) KPI.=============="
                                    #Step3.1:Get the Expected achievement of Tl1
                                    '''Expected_KPIofTl2 is from above, and  Expected_Achi_Tl1 is from below'''
                                    print Expected_KPIofTl1
                                    #Step3.2:Get the Actual achievement of Tl2(TEAM)
                                    Actual_KPIofTl1=GetPData_Actual.get_DTVSS_TEAM_Data_()
                                    print Actual_KPIofTl1
                                    
                                    #Step3.3:assert Expected==Actual
                                    assert Expected_KPIofTl1["ActivationRateModify"][0]==Actual_KPIofTl1["ActivationRateModify"][0]#0 is KPI value
                                    assert Expected_KPIofTl1["ActivationRateModify"][1]==Actual_KPIofTl1["ActivationRateModify"][1]#1 is KPI status
                                    assert Expected_KPIofTl1["CancelTransfer"][0]==Actual_KPIofTl1["CancelTransfer"][0]#0 is KPI value
                                    assert Expected_KPIofTl1["CancelTransfer"][1]==Actual_KPIofTl1["CancelTransfer"][1]#1 is KPI status
                                    assert Expected_KPIofTl1["CancelIVR"][0]==Actual_KPIofTl1["CancelIVR"][0]#0 is KPI value
                                    assert Expected_KPIofTl1["CancelIVR"][1]==Actual_KPIofTl1["CancelIVR"][1]#1 is KPI status
                                    assert Expected_KPIofTl1["IPBBNet"][0]==Actual_KPIofTl1["IPBBNet"][0]#0 is KPI value
                                    assert Expected_KPIofTl1["IPBBNet"][1]==Actual_KPIofTl1["IPBBNet"][1]#1 is KPI status
                                    assert Expected_KPIofTl1["MobilityGrossSales"][0]==Actual_KPIofTl1["MobilityGrossSales"][0]#0 is KPI value
                                    assert Expected_KPIofTl1["MobilityGrossSales"][1]==Actual_KPIofTl1["MobilityGrossSales"][1]#1 is KPI status
                                    assert Expected_KPIofTl1["AgentSatisfaction"][0]==Actual_KPIofTl1["AgentSatisfaction"][0]#0 is KPI value
                                    #assert Expected_KPIofTl2["AgentSatisfaction"][1]==Actual_KPIofTl2["AgentSatisfaction"][1]#1 is KPI status
                                    assert Expected_KPIofTl1["Achiev"][0]==Actual_KPIofTl1["Achiev"][0]#0 is KPI value
                                

                                
                                    #Step4:Verify achievement of all Tl1's Agents 
                                    print "=================4.Verify Agent14's all KPIs=============="                       
                                    #Step4.1:Get the Expected achievement of all Tl1's Agents
                                    print "=================4.Expected Agent14's all KPIs==============" 
                                    print Expected_KPIofAgent11
                                   
                                    #Step4.2:Get the Actual achievement of all Tl1's Agents
                                    print "=================4.Actual Agent14's all KPIs=============="
                                    Actual_KPIofAgent11=GetPData_Actual.get_DTVSS_AgentKPI_Agent_Actual()
                                    print Actual_KPIofAgent11
                                    
                                    #Step4.3:assert Expected==Actual
                                    assert Expected_KPIofAgent11["ActivationRateModify"][0]==Actual_KPIofAgent11["ActivationRateModify"][0]#0 is KPI value
                                    assert Expected_KPIofAgent11["ActivationRateModify"][1]==Actual_KPIofAgent11["ActivationRateModify"][1]#1 is KPI status
                                    assert Expected_KPIofAgent11["CancelTransfer"][0]==Actual_KPIofAgent11["CancelTransfer"][0]#0 is KPI value
                                    assert Expected_KPIofAgent11["CancelTransfer"][1]==Actual_KPIofAgent11["CancelTransfer"][1]#1 is KPI status
                                    assert Expected_KPIofAgent11["CancelIVR"][0]==Actual_KPIofAgent11["CancelIVR"][0]#0 is KPI value
                                    assert Expected_KPIofAgent11["CancelIVR"][1]==Actual_KPIofAgent11["CancelIVR"][1]#1 is KPI status
                                    assert Expected_KPIofAgent11["IPBBNet"][0]==Actual_KPIofAgent11["IPBBNet"][0]#0 is KPI value
                                    assert Expected_KPIofAgent11["IPBBNet"][1]==Actual_KPIofAgent11["IPBBNet"][1]#1 is KPI status
                                    assert Expected_KPIofAgent11["MobilityGrossSales"][0]==Actual_KPIofAgent11["MobilityGrossSales"][0]#0 is KPI value
                                    assert Expected_KPIofAgent11["MobilityGrossSales"][1]==Actual_KPIofAgent11["MobilityGrossSales"][1]#1 is KPI status
                                    assert Expected_KPIofAgent11["AgentSatisfaction"][0]==Actual_KPIofAgent11["AgentSatisfaction"][0]#0 is KPI value
                                    #assert Expected_KPIofAgent11["AgentSatisfaction"][1]==Actual_KPIofAgent11["AgentSatisfaction"][1]#1 is KPI status
                            L.logout_tablet()
                               


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()