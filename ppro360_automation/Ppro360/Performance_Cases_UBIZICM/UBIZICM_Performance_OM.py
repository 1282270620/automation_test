'''
Created on Apr 5, 2017

@author: symbio
'''
import unittest
#from public_method.Get_PerformanceData_Expected import Get_PerformanceData_Expected
#from public_method.Get_PerformanceData_Actual import Get_PerformanceData_Actual
from Performance_Cases_UBIZICM.Get_PerformanceData_Actual_UBIZICM import Get_PerformanceData_Actual_UBIZICM
from Performance_Cases_UBIZICM.Get_PerformanceData_Expected_UBIZICM import Get_PerformanceData_Expected_UBIZICM

from public_method import Gl
from public_method.Get_configration_data import Get_configration_data
from public_method.Login import Login
from Tablet_pages.TabletHomepage import TabletHomepage
from Tablet_pages.PerformancPage import PerformancePage
import time


class UBIZICM_Performance_OM(unittest.TestCase):


    def setUp(self):
        self.caseID="UBIZICM_Performance_OM"
        GetData=Get_configration_data()
        #Get URL 
        self.tableturl=GetData.get_TabletUrl()
        #Get OM account
        OMaccount=GetData.get_OMaccount()
        self.OMuserid=OMaccount["OMuserid"]
        self.OMpassword=OMaccount["OMpassword"]
        #Get all lobs from CSV
        self.testLOBSITE_list=GetData.get_LOBSITEtoTest(self.caseID)
        
        #Yesterday,WTD,MTD for UBIZICM
        self.tablist=Gl.Multi_timetab#["yesterday","Week-to-Day","Month-to-Day"]#
        


    def tearDown(self):
        Gl.driver.quit() 


    def test_UBIZICM_Performance_OM(self):
        GetConfig=Get_configration_data()
        L=Login()
        THomepage=TabletHomepage()
        Ppage=PerformancePage()
        GetPData_Actual=Get_PerformanceData_Actual_UBIZICM()
        #Get Goal Expected
        GetPData_Expected=Get_PerformanceData_Expected_UBIZICM()
        lineindex=2#The goal is in the row 3 of excel file,so linedex is 2
        Expected_GoalDic=GetPData_Expected.get_UBIZICM_Goal_Expected(lineindex)
        
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
                    
                    #Step0.1:All data has been ready manually
                    #Step0.3:Login with OM to do upload work
                    L.Login_tablet(self.tableturl, lobname, sitename, self.OMuserid, self.OMpassword)
                    Achiev_PerformanceCircle=THomepage.get_Achiev_performancecircle()
                    THomepage.click_performancecircle()
                    Achiev_SITE_Monthly=GetPData_Actual.get_UBIZICM_SITE_Data_()['Achiev'][0]
                    print "=================The value is the same as SITE KPI of monthly report page.=============="                    
                    assert Achiev_PerformanceCircle==Achiev_SITE_Monthly
                    
                    for ywm in range(0,len(self.tablist)):
                        Ppage.click_timetab_performance(ywm+1)
                        
                
                        print "*********************Start********************",
                        print self.tablist[ywm],
                        print "is in testing:"
                        time.sleep(Gl.waittime)
                        #Step1:Verify Goal
                        print "=================1.Verify Each KPI of Goal=============="
                        Actual_GoalDic=GetPData_Actual.get_UBIZICM_Goal_Actual()#GET ACTUAL GOAL FORM PERFORMANCE PAGE
                        assert Expected_GoalDic["AvgHoldTime"]==Actual_GoalDic["AvgHoldTime"]
                        assert Expected_GoalDic["IBAHT"]==Actual_GoalDic["IBAHT"]
                        assert Expected_GoalDic["CaseTocall"]==Actual_GoalDic["CaseTocall"]
                        assert Expected_GoalDic["Misdirects"]==Actual_GoalDic["Misdirects"]
                        assert Expected_GoalDic["Ghosts"]==Actual_GoalDic["Ghosts"]
                        assert Expected_GoalDic["SwitchTransfer"]==Actual_GoalDic["SwitchTransfer"]
                        assert Expected_GoalDic["DailyRepeatRate"]==Actual_GoalDic["DailyRepeatRate"]
                        assert Expected_GoalDic["DispatchRateByCTV"]==Actual_GoalDic["DispatchRateByCTV"]
                        assert Expected_GoalDic["WFEComplianceRate"]==Actual_GoalDic["WFEComplianceRate"]
                        assert Expected_GoalDic["R3AllIn"]==Actual_GoalDic["R3AllIn"]
                        assert Expected_GoalDic["R30AllIn"]==Actual_GoalDic["R30AllIn"]
                        assert Expected_GoalDic["R7AllIn"]==Actual_GoalDic["R7AllIn"]
                        #assert Expected_GoalDic["Achiev"]==Actual_GoalDic["Achiev"]
                        
                        '''Prepare Data for the following test '''
                        if self.tablist[ywm]=="LastTwoMonth":
                            Expected_KPIofSITEDic=GetPData_Expected.get_UBIZICM_Performance_Data_Expected(137)#For Step2
                            Expected_KPIofTl1=GetPData_Expected.get_UBIZICM_Performance_Data_Expected(135)#For Step3
                            Expected_AgentAchiev=GetPData_Expected.Get_ManyAgentAchiev_Expected(132, 134)#For Step4
                            #Expected_KPIofAgent8=GetPData_Expected.get_UBIZICM_Performance_Data_Expected(131)#For Step5
                            Expected_KPIofAgent11=GetPData_Expected.get_UBIZICM_Performance_Data_Expected(134)#For Step6
                            
                        elif self.tablist[ywm]=="LastMonth":
                            Expected_KPIofSITEDic=GetPData_Expected.get_UBIZICM_Performance_Data_Expected(126)#For Step2
                            Expected_KPIofTl1=GetPData_Expected.get_UBIZICM_Performance_Data_Expected(120)#For Step3
                            Expected_AgentAchiev=GetPData_Expected.Get_ManyAgentAchiev_Expected(109, 119)#For Step4
                            Expected_KPIofAgent8=GetPData_Expected.get_UBIZICM_Performance_Data_Expected(116)#For Step5
                            Expected_KPIofAgent11=GetPData_Expected.get_UBIZICM_Performance_Data_Expected(119)#For Step6
                        elif self.tablist[ywm]=="Yesterday":
                            Expected_KPIofSITEDic=GetPData_Expected.get_UBIZICM_Performance_Data_Expected(25)#For Step2
                            Expected_KPIofTl1=GetPData_Expected.get_UBIZICM_Performance_Data_Expected(16)#For Step3
                            Expected_AgentAchiev=GetPData_Expected.Get_ManyAgentAchiev_Expected(5, 15)#For Step4
                            Expected_KPIofAgent8=GetPData_Expected.get_UBIZICM_Performance_Data_Expected(12)#For Step5
                            Expected_KPIofAgent11=GetPData_Expected.get_UBIZICM_Performance_Data_Expected(15)#For Step6
                            
                        elif self.tablist[ywm]== "Week-to-Date":
                            Expected_KPIofSITEDic=GetPData_Expected.get_UBIZICM_Performance_Data_Expected(81)#For Step2
                            Expected_KPIofTl1=GetPData_Expected.get_UBIZICM_Performance_Data_Expected(75)#For Step3
                            Expected_AgentAchiev=GetPData_Expected.Get_ManyAgentAchiev_Expected(64, 74)#For Step4
                            Expected_KPIofAgent8=GetPData_Expected.get_UBIZICM_Performance_Data_Expected(71)#For Step5
                            Expected_KPIofAgent11=GetPData_Expected.get_UBIZICM_Performance_Data_Expected(74)#For Step6
                        elif self.tablist[ywm]=="Month-to-Date":
                            Expected_KPIofSITEDic=GetPData_Expected.get_UBIZICM_Performance_Data_Expected(103)#For Step2
                            Expected_KPIofTl1=GetPData_Expected.get_UBIZICM_Performance_Data_Expected(97)#For Step3
                            Expected_AgentAchiev=GetPData_Expected.Get_ManyAgentAchiev_Expected(86, 96)#For Step4
                            Expected_KPIofAgent8=GetPData_Expected.get_UBIZICM_Performance_Data_Expected(93)#For Step5
                            Expected_KPIofAgent11=GetPData_Expected.get_UBIZICM_Performance_Data_Expected(96)#For Step6
                        
                        #Step2:Verify KPI of SITES
                        print "=================2.Verify Each KPI of site, color, achievement=============="
                        '''Expected_KPIofSITEDic is from above.'''
                        print Expected_KPIofSITEDic
                        #Step2.2:Get the Actual KPI of site
                        '''Expected_KPIofSITEDic is from blow.''' 
                        Actual_KPIofSITEDic=GetPData_Actual.get_UBIZICM_SITE_Data_()
                        print Actual_KPIofSITEDic
                        #Step2.3:assert Expected==Actual
                        assert Expected_KPIofSITEDic["AvgHoldTime"][0]==Actual_KPIofSITEDic["AvgHoldTime"][0]#0 is KPI value
                        assert Expected_KPIofSITEDic["AvgHoldTime"][1]==Actual_KPIofSITEDic["AvgHoldTime"][1]#1 is KPI status
                        assert Expected_KPIofSITEDic["IBAHT"][0]==Actual_KPIofSITEDic["IBAHT"][0]#0 is KPI value
                        assert Expected_KPIofSITEDic["IBAHT"][1]==Actual_KPIofSITEDic["IBAHT"][1]#1 is KPI status
                        assert Expected_KPIofSITEDic["CaseTocall"][0]==Actual_KPIofSITEDic["CaseTocall"][0]#0 is KPI value
                        assert Expected_KPIofSITEDic["CaseTocall"][1]==Actual_KPIofSITEDic["CaseTocall"][1]#1 is KPI status
                        assert Expected_KPIofSITEDic["Misdirects"][0]==Actual_KPIofSITEDic["Misdirects"][0]#0 is KPI value
                        assert Expected_KPIofSITEDic["Misdirects"][1]==Actual_KPIofSITEDic["Misdirects"][1]#1 is KPI status
                        assert Expected_KPIofSITEDic["Ghosts"][0]==Actual_KPIofSITEDic["Ghosts"][0]#0 is KPI value
                        assert Expected_KPIofSITEDic["Ghosts"][1]==Actual_KPIofSITEDic["Ghosts"][1]#1 is KPI status
                        assert Expected_KPIofSITEDic["SwitchTransfer"][0]==Actual_KPIofSITEDic["SwitchTransfer"][0]#0 is KPI value
                        assert Expected_KPIofSITEDic["SwitchTransfer"][1]==Actual_KPIofSITEDic["SwitchTransfer"][1]#1 is KPI status
                        assert Expected_KPIofSITEDic["DailyRepeatRate"][0]==Actual_KPIofSITEDic["DailyRepeatRate"][0]#0 is KPI value
                        assert Expected_KPIofSITEDic["DailyRepeatRate"][1]==Actual_KPIofSITEDic["DailyRepeatRate"][1]#1 is KPI status
                        assert Expected_KPIofSITEDic["DispatchRateByCTV"][0]==Actual_KPIofSITEDic["DispatchRateByCTV"][0]#0 is KPI value
                        assert Expected_KPIofSITEDic["DispatchRateByCTV"][1]==Actual_KPIofSITEDic["DispatchRateByCTV"][1]#1 is KPI status
                        assert Expected_KPIofSITEDic["WFEComplianceRate"][0]==Actual_KPIofSITEDic["WFEComplianceRate"][0]#0 is KPI value
                        assert Expected_KPIofSITEDic["WFEComplianceRate"][1]==Actual_KPIofSITEDic["WFEComplianceRate"][1]#1 is KPI status
                        assert Expected_KPIofSITEDic["R3AllIn"][0]==Actual_KPIofSITEDic["R3AllIn"][0]#0 is KPI value
                        assert Expected_KPIofSITEDic["R3AllIn"][1]==Actual_KPIofSITEDic["R3AllIn"][1]#1 is KPI status
                        assert Expected_KPIofSITEDic["R30AllIn"][0]==Actual_KPIofSITEDic["R30AllIn"][0]#0 is KPI value
                        assert Expected_KPIofSITEDic["R30AllIn"][1]==Actual_KPIofSITEDic["R30AllIn"][1]#1 is KPI status
                        assert Expected_KPIofSITEDic["R7AllIn"][0]==Actual_KPIofSITEDic["R7AllIn"][0]#0 is KPI value
                        assert Expected_KPIofSITEDic["R7AllIn"][1]==Actual_KPIofSITEDic["R7AllIn"][1]#1 is KPI status
                        assert Expected_KPIofSITEDic["Achiev"][0]==Actual_KPIofSITEDic["Achiev"][0]#0 is KPI value
                        
                        ''' Achiev has no KPI sort '''
                        
                        
                        #Step3:Verify achievement of Tl1
                        print "=================3.Verify TL1's achievement.=============="
                        #Step3.1:Get the Expected achievement of Tl1
                        '''Expected_KPIofTl1 is from above, and  Expected_Achi_Tl1 is from below'''
                        Expected_Achi_Tl1=Expected_KPIofTl1["Achiev"][0]
                        #Step3.2:Get the Actual achievement of Tl1
                        flag=True
                        lineindex=1
                        while flag==True:
                            TL_name=Ppage.get_anyKPIofTL(lineindex, 1)[0]
                            if TL_name=='Tl1 Test':
                                Actual_Achiev_TL1=GetPData_Actual.get_UBIZICM_TL_KPI_Actual(lineindex)["Achiev"][0]
                                Tl1_line=lineindex#For Step4
                                break
                            lineindex=lineindex+1
                            flag=Ppage.TL_line_exist(lineindex)
                       
                        '''Actual_Achiev_TL1'''
                        #Step3.3:assert Expected==Actual
                        assert Expected_Achi_Tl1==Actual_Achiev_TL1
                        
                        #Step4:Verify achievement of all Tl1's Agents 
                        print "=================4.Verify TL1's all agents achivement=============="                       
                        #Step4.1:Get the Expected achievement of all Tl1's Agents
                        print "=================4.Expected_All Agents' Achiev of Tl1==============" 
                        print Expected_AgentAchiev
                        #Step4.2:Get the Actual achievement of all Tl1's Agents
                        
                        TLindex=Tl1_line#From Step3
                        Ppage.unfold_anyTL(TLindex)#Click this TL1, then all his agents will be shown
                        flag=True
                        Agentindex=1
                        Actual_AgentAchiev={}
                        Actual_AgentKPI={}
                        while flag==True:
                            Agent_Name=Ppage.get_anyKPIofAgent_OM(TLindex, Agentindex, 1)[0]
                            Agent_Achiev=Ppage.get_anyKPIofAgent_OM(TLindex, Agentindex, 14)[0]
                            Actual_AgentAchiev[Agent_Name]=Agent_Achiev
                            if Agent_Name=='Agent 8' or Agent_Name=='Agent 11':
                                Agent_KPI=GetPData_Actual.get_UBIZICM_Agent_KPI_Actual(TLindex, Agentindex)
                                Actual_AgentKPI[Agent_Name]=Agent_KPI#For Step5 and Step6
                            Agentindex=Agentindex+1
                            flag=Ppage.Agent_line_exist_OM(TLindex, Agentindex)
                            
                        print "=================4.Actual_All Agents' Achiev of Tl1=============="
                        print Agentindex
                        print Actual_AgentAchiev
                        #Step4.3:assert Expected==Actual
                        if self.tablist[ywm]!="LastTwoMonth":
                            assert Expected_AgentAchiev["Agent 1"][0]==Actual_AgentAchiev["Agent 1"][0]
                            assert Expected_AgentAchiev["Agent 2"][0]==Actual_AgentAchiev["Agent 2"][0]
                            assert Expected_AgentAchiev["Agent 3"][0]==Actual_AgentAchiev["Agent 3"][0]
                            assert Expected_AgentAchiev["Agent 4"][0]==Actual_AgentAchiev["Agent 4"][0]
                            assert Expected_AgentAchiev["Agent 5"][0]==Actual_AgentAchiev["Agent 5"][0]
                            assert Expected_AgentAchiev["Agent 6"][0]==Actual_AgentAchiev["Agent 6"][0]
                            assert Expected_AgentAchiev["Agent 7"][0]==Actual_AgentAchiev["Agent 7"][0]
                            assert Expected_AgentAchiev["Agent 8"][0]==Actual_AgentAchiev["Agent 8"][0]
                        print Expected_AgentAchiev["Agent 9"][0]
                        print Actual_AgentAchiev["Agent 9"][0]
                        assert Expected_AgentAchiev["Agent 9"][0]==Actual_AgentAchiev["Agent 9"][0]
                        assert Expected_AgentAchiev["Agent 10"][0]==Actual_AgentAchiev["Agent 10"][0]
                        assert Expected_AgentAchiev["Agent 11"][0]==Actual_AgentAchiev["Agent 11"][0]
                        
                        if self.tablist[ywm]!="LastTwoMonth":
                            #Step5:Verify Agent8:check each KPI value, color.
                            print "=================5.Verify Agent8:check each KPI value, color==============" 
                            #Step5.1:Get the Expected KPI value and color for Agent8
                            print "=================5.1 Expected KPI value and color of Agent8=============="
                            print Expected_KPIofAgent8
                            #Step5.2:Get the Actual KPI and color for Agent8
                            print "=================5.2 Actual KPI value and color of Agent8=============="
                            Actual_KPIofAgent8=Actual_AgentKPI['Agent 8']
                            print Actual_KPIofAgent8
                            assert Expected_KPIofAgent8["AvgHoldTime"][0]==Actual_KPIofAgent8["AvgHoldTime"][0]#0 is KPI value
                            assert Expected_KPIofAgent8["AvgHoldTime"][1]==Actual_KPIofAgent8["AvgHoldTime"][1]#1 is KPI status
                            assert Expected_KPIofAgent8["IBAHT"][0]==Actual_KPIofAgent8["IBAHT"][0]#0 is KPI value
                            assert Expected_KPIofAgent8["IBAHT"][1]==Actual_KPIofAgent8["IBAHT"][1]#1 is KPI status
                            assert Expected_KPIofAgent8["CaseTocall"][0]==Actual_KPIofAgent8["CaseTocall"][0]#0 is KPI value
                            assert Expected_KPIofAgent8["CaseTocall"][1]==Actual_KPIofAgent8["CaseTocall"][1]#1 is KPI status
                            assert Expected_KPIofAgent8["Misdirects"][0]==Actual_KPIofAgent8["Misdirects"][0]#0 is KPI value
                            assert Expected_KPIofAgent8["Misdirects"][1]==Actual_KPIofAgent8["Misdirects"][1]#1 is KPI status
                            assert Expected_KPIofAgent8["Ghosts"][0]==Actual_KPIofAgent8["Ghosts"][0]#0 is KPI value
                            assert Expected_KPIofAgent8["Ghosts"][1]==Actual_KPIofAgent8["Ghosts"][1]#1 is KPI status
                            assert Expected_KPIofAgent8["SwitchTransfer"][0]==Actual_KPIofAgent8["SwitchTransfer"][0]#0 is KPI value
                            assert Expected_KPIofAgent8["SwitchTransfer"][1]==Actual_KPIofAgent8["SwitchTransfer"][1]#1 is KPI status
                            assert Expected_KPIofAgent8["DailyRepeatRate"][0]==Actual_KPIofAgent8["DailyRepeatRate"][0]#0 is KPI value
                            assert Expected_KPIofAgent8["DailyRepeatRate"][1]==Actual_KPIofAgent8["DailyRepeatRate"][1]#1 is KPI status
                            assert Expected_KPIofAgent8["DispatchRateByCTV"][0]==Actual_KPIofAgent8["DispatchRateByCTV"][0]#0 is KPI value
                            assert Expected_KPIofAgent8["DispatchRateByCTV"][1]==Actual_KPIofAgent8["DispatchRateByCTV"][1]#1 is KPI status
                            assert Expected_KPIofAgent8["WFEComplianceRate"][0]==Actual_KPIofAgent8["WFEComplianceRate"][0]#0 is KPI value
                            assert Expected_KPIofAgent8["WFEComplianceRate"][1]==Actual_KPIofAgent8["WFEComplianceRate"][1]#1 is KPI status
                            assert Expected_KPIofAgent8["R3AllIn"][0]==Actual_KPIofAgent8["R3AllIn"][0]#0 is KPI value
                            assert Expected_KPIofAgent8["R3AllIn"][1]==Actual_KPIofAgent8["R3AllIn"][1]#1 is KPI status
                            assert Expected_KPIofAgent8["R30AllIn"][0]==Actual_KPIofAgent8["R30AllIn"][0]#0 is KPI value
                            assert Expected_KPIofAgent8["R30AllIn"][1]==Actual_KPIofAgent8["R30AllIn"][1]#1 is KPI status
                            assert Expected_KPIofAgent8["R7AllIn"][0]==Actual_KPIofAgent8["R7AllIn"][0]#0 is KPI value
                            assert Expected_KPIofAgent8["R7AllIn"][1]==Actual_KPIofAgent8["R7AllIn"][1]#1 is KPI status
                            assert Expected_KPIofAgent8["Achiev"][0]==Actual_KPIofAgent8["Achiev"][0]#0 is KPI value
                            assert Expected_KPIofAgent8["Achiev"][1]==Actual_KPIofAgent8["Achiev"][1]#1 is KPI status


                        
                        
                        #Step6:Verify Agent11:check each KPI value, color.
                        print "=================6.Verify Agent11:check each KPI value, color=============="
                        #Step6.1:Get the Expected KPI value and color for Agent8
                        print "=================6.1 Expected KPI value and color of Agent11=============="
                        print Expected_KPIofAgent11
                        #Step6.2:Get the Actual KPI and color for Agent8
                        print "=================6.2 Actual KPI value and color of Agent11=============="
                        Actual_KPIofAgent11=Actual_AgentKPI['Agent 11']
                        print Actual_KPIofAgent11
                        assert Expected_KPIofAgent11["AvgHoldTime"][0]==Actual_KPIofAgent11["AvgHoldTime"][0]#0 is KPI value
                        assert Expected_KPIofAgent11["AvgHoldTime"][1]==Actual_KPIofAgent11["AvgHoldTime"][1]#1 is KPI status
                        assert Expected_KPIofAgent11["IBAHT"][0]==Actual_KPIofAgent11["IBAHT"][0]#0 is KPI value
                        assert Expected_KPIofAgent11["IBAHT"][1]==Actual_KPIofAgent11["IBAHT"][1]#1 is KPI status
                        assert Expected_KPIofAgent11["CaseTocall"][0]==Actual_KPIofAgent11["CaseTocall"][0]#0 is KPI value
                        assert Expected_KPIofAgent11["CaseTocall"][1]==Actual_KPIofAgent11["CaseTocall"][1]#1 is KPI status
                        assert Expected_KPIofAgent11["Misdirects"][0]==Actual_KPIofAgent11["Misdirects"][0]#0 is KPI value
                        assert Expected_KPIofAgent11["Misdirects"][1]==Actual_KPIofAgent11["Misdirects"][1]#1 is KPI status
                        assert Expected_KPIofAgent11["Ghosts"][0]==Actual_KPIofAgent11["Ghosts"][0]#0 is KPI value
                        assert Expected_KPIofAgent11["Ghosts"][1]==Actual_KPIofAgent11["Ghosts"][1]#1 is KPI status
                        assert Expected_KPIofAgent11["SwitchTransfer"][0]==Actual_KPIofAgent11["SwitchTransfer"][0]#0 is KPI value
                        assert Expected_KPIofAgent11["SwitchTransfer"][1]==Actual_KPIofAgent11["SwitchTransfer"][1]#1 is KPI status
                        assert Expected_KPIofAgent11["DailyRepeatRate"][0]==Actual_KPIofAgent11["DailyRepeatRate"][0]#0 is KPI value
                        assert Expected_KPIofAgent11["DailyRepeatRate"][1]==Actual_KPIofAgent11["DailyRepeatRate"][1]#1 is KPI status
                        assert Expected_KPIofAgent11["DispatchRateByCTV"][0]==Actual_KPIofAgent11["DispatchRateByCTV"][0]#0 is KPI value
                        assert Expected_KPIofAgent11["DispatchRateByCTV"][1]==Actual_KPIofAgent11["DispatchRateByCTV"][1]#1 is KPI status
                        assert Expected_KPIofAgent11["WFEComplianceRate"][0]==Actual_KPIofAgent11["WFEComplianceRate"][0]#0 is KPI value
                        assert Expected_KPIofAgent11["WFEComplianceRate"][1]==Actual_KPIofAgent11["WFEComplianceRate"][1]#1 is KPI status
                        assert Expected_KPIofAgent11["R3AllIn"][0]==Actual_KPIofAgent11["R3AllIn"][0]#0 is KPI value
                        assert Expected_KPIofAgent11["R3AllIn"][1]==Actual_KPIofAgent11["R3AllIn"][1]#1 is KPI status
                        assert Expected_KPIofAgent11["R30AllIn"][0]==Actual_KPIofAgent11["R30AllIn"][0]#0 is KPI value
                        assert Expected_KPIofAgent11["R30AllIn"][1]==Actual_KPIofAgent11["R30AllIn"][1]#1 is KPI status
                        assert Expected_KPIofAgent11["R7AllIn"][0]==Actual_KPIofAgent11["R7AllIn"][0]#0 is KPI value
                        assert Expected_KPIofAgent11["R7AllIn"][1]==Actual_KPIofAgent11["R7AllIn"][1]#1 is KPI status
                        assert Expected_KPIofAgent11["Achiev"][0]==Actual_KPIofAgent11["Achiev"][0]#0 is KPI value
                        assert Expected_KPIofAgent11["Achiev"][1]==Actual_KPIofAgent11["Achiev"][1]#1 is KPI status

                    L.logout_tablet()    


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()