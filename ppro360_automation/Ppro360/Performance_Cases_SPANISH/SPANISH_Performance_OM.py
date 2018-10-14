'''
Created on Apr 5, 2017

@author: symbio
'''
import unittest
#from public_method.Get_PerformanceData_Expected import Get_PerformanceData_Expected
#from public_method.Get_PerformanceData_Actual import Get_PerformanceData_Actual
from Performance_Cases_SPANISH.Get_PerformanceData_Actual_SPANISH import Get_PerformanceData_Actual_SPANISH
from Performance_Cases_SPANISH.Get_PerformanceData_Expected_SPANISH import Get_PerformanceData_Expected_SPANISH

from public_method import Gl
from public_method.Get_configration_data import Get_configration_data
from public_method.Login import Login
from Tablet_pages.TabletHomepage import TabletHomepage
from Tablet_pages.PerformancPage import PerformancePage
import time


class SPANISH_Performance_OM(unittest.TestCase):


    def setUp(self):
        self.caseID="SPANISH_Performance_OM"
        GetData=Get_configration_data()
        #Get URL 
        self.tableturl=GetData.get_TabletUrl()
        #Get OM account
        OMaccount=GetData.get_OMaccount()
        self.OMuserid=OMaccount["OMuserid"]
        self.OMpassword=OMaccount["OMpassword"]
        #Get all lobs from CSV
        self.testLOBSITE_list=GetData.get_LOBSITEtoTest(self.caseID)
        
        #Yesterday,WTD,MTD for SPANISH
        self.tablist=Gl.Less_timetab#["LastTwoMonth","LastMonth","Month-to-Date"]#
        


    def tearDown(self):
        #Gl.driver.quit() 
        pass


    def test_SPANISH_Performance_OM(self):
        GetConfig=Get_configration_data()
        L=Login()
        THomepage=TabletHomepage()
        Ppage=PerformancePage()
        GetPData_Actual=Get_PerformanceData_Actual_SPANISH()
        #Get Goal Expected
        GetPData_Expected=Get_PerformanceData_Expected_SPANISH()
        '''
        lineindex=2#The goal is in the row 3 of excel file,so linedex is 2
        Expected_GoalDic=GetPData_Expected.get_SPANISH_Goal_Expected(lineindex)
        print "Expected_GoalDic:"
        print Expected_GoalDic'''
        
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
                    Achiev_SITE_Monthly=GetPData_Actual.get_SPANISH_SITE_Data_()['Achiev'][0]
                    print "=================The value is the same as SITE KPI of monthly report page.=============="                    
                    assert Achiev_PerformanceCircle==Achiev_SITE_Monthly
                     
                    #for ywm in range(0,len(self.tablist)):
                    for ywm in range(2,3):
                        Ppage.click_timetab_performance(ywm+1)
                        
                        print "*********************Start********************",
                        print self.tablist[ywm],
                        print "is in testing:"
                        time.sleep(Gl.waittime)
                        #Step1:Verify Goal
                        
                        
                        '''Prepare Data for the following test '''
                        if self.tablist[ywm]=="LastTwoMonth":#date2
                            Expected_GoalDic=GetPData_Expected.get_SPANISH_Goal_Expected(85)
                            Expected_KPIofSITEDic=GetPData_Expected.get_SPANISH_Performance_Data_Expected(116)#For Step2
                            Expected_KPIofTl1=GetPData_Expected.get_SPANISH_Performance_Data_Expected(95)#For Step3
                            Expected_AgentAchiev=GetPData_Expected.Get_ManyAgentAchiev_Expected(89, 93)#For Step4
                            Expected_KPIofAgent11=GetPData_Expected.get_SPANISH_Performance_Data_Expected(93)#For Step6
                            
                        elif self.tablist[ywm]=="LastMonth":#date1
                            Expected_GoalDic=GetPData_Expected.get_SPANISH_Goal_Expected(2)
                            Expected_KPIofSITEDic=GetPData_Expected.get_SPANISH_Performance_Data_Expected(40)#For Step2
                            Expected_KPIofTl1=GetPData_Expected.get_SPANISH_Performance_Data_Expected(28)#For Step3
                            Expected_AgentAchiev=GetPData_Expected.Get_ManyAgentAchiev_Expected(6, 26)#For Step4
                            Expected_KPIofAgent8=GetPData_Expected.get_SPANISH_Performance_Data_Expected(20)#For Step5
                            Expected_KPIofAgent11=GetPData_Expected.get_SPANISH_Performance_Data_Expected(26)#For Step6
                        
                        elif self.tablist[ywm]=="Month-to-Date":#date3
                            Expected_GoalDic=GetPData_Expected.get_SPANISH_Goal_Expected(102)
                            Expected_KPIofSITEDic=GetPData_Expected.get_SPANISH_Performance_Data_Expected(116)#For Step2
                            Expected_KPIofTl1=GetPData_Expected.get_SPANISH_Performance_Data_Expected(114)#For Step3
                            Expected_AgentAchiev=GetPData_Expected.Get_ManyAgentAchiev_Expected(106, 112)#For Step4
                            Expected_KPIofAgent8=GetPData_Expected.get_SPANISH_Performance_Data_Expected(106)#For Step5
                            Expected_KPIofAgent11=GetPData_Expected.get_SPANISH_Performance_Data_Expected(112)#For Step6
                        
                        
                        print "Expected_GoalDic:"
                        print Expected_GoalDic
                        print "=================1.Verify Each KPI of Goal=============="
                        Actual_GoalDic=GetPData_Actual.get_SPANISH_Goal_Actual()#GET ACTUAL GOAL FORM PERFORMANCE PAGE
                        
                        print "Actual_GoalDic:"
                        print Actual_GoalDic
                        for key in Expected_GoalDic:
                            if type(Expected_GoalDic[key])==list and Expected_GoalDic[key][0]==Expected_GoalDic[key][1]=='N/A':
                                Expected_GoalDic[key]='N/A'
                        assert Expected_GoalDic["NetRevenue_Attain"]==Actual_GoalDic["NetRevenue_Attain"]
                        assert Expected_GoalDic["HSIAIPDSL_Actual"]==Actual_GoalDic["HSIAIPDSL_Actual"]
                        assert Expected_GoalDic["HSIAIPDSL_Attain"]==Actual_GoalDic["HSIAIPDSL_Attain"]
                        assert Expected_GoalDic["CRFT_Actual"]==Actual_GoalDic["CRFT_Actual"]
                        assert Expected_GoalDic["CRFT_Attain"]==Actual_GoalDic["CRFT_Attain"]
                        assert Expected_GoalDic["OpsAht"]==Actual_GoalDic["OpsAht"]
                        assert Expected_GoalDic["VOIP_Actual"]==Actual_GoalDic["VOIP_Actual"]
                        assert Expected_GoalDic["VOIP_Attain"]==Actual_GoalDic["VOIP_Attain"]
                        assert Expected_GoalDic["WLS_Actual"]==Actual_GoalDic["WLS_Actual"]
                        assert Expected_GoalDic["WLS_Attain"]==Actual_GoalDic["WLS_Attain"]
                        assert Expected_GoalDic["Achiev"]==Actual_GoalDic["Achiev"]

                        #Step2:Verify KPI of SITES
                        print "=================2.Verify Each KPI of site, color, achievement=============="
                        '''Expected_KPIofSITEDic is from above.'''
                        print Expected_KPIofSITEDic
                        #Step2.2:Get the Actual KPI of site
                        '''Expected_KPIofSITEDic is from blow.''' 
                        Actual_KPIofSITEDic=GetPData_Actual.get_SPANISH_SITE_Data_()
                        print Actual_KPIofSITEDic
                        #Step2.3:assert Expected==Actual
                        assert Expected_KPIofSITEDic["NetRevenue_Actual"][0]==Actual_KPIofSITEDic["NetRevenue_Actual"][0]
                        assert Expected_KPIofSITEDic["NetRevenue_Actual"][1]==Actual_KPIofSITEDic["NetRevenue_Actual"][1]
                        assert Expected_KPIofSITEDic["NetRevenue_Attain"][0]==Actual_KPIofSITEDic["NetRevenue_Attain"][0]
                        assert Expected_KPIofSITEDic["NetRevenue_Attain"][1]==Actual_KPIofSITEDic["NetRevenue_Attain"][1]
                        assert Expected_KPIofSITEDic["HSIAIPDSL_Actual"][0]==Actual_KPIofSITEDic["HSIAIPDSL_Actual"][0]
                        assert Expected_KPIofSITEDic["HSIAIPDSL_Actual"][1]==Actual_KPIofSITEDic["HSIAIPDSL_Actual"][1]
                        assert Expected_KPIofSITEDic["HSIAIPDSL_Attain"][0]==Actual_KPIofSITEDic["HSIAIPDSL_Attain"][0]
                        assert Expected_KPIofSITEDic["HSIAIPDSL_Attain"][1]==Actual_KPIofSITEDic["HSIAIPDSL_Attain"][1]
                        assert Expected_KPIofSITEDic["CRFT_Actual"][0]==Actual_KPIofSITEDic["CRFT_Actual"][0]
                        assert Expected_KPIofSITEDic["CRFT_Actual"][1]==Actual_KPIofSITEDic["CRFT_Actual"][1]
                        assert Expected_KPIofSITEDic["CRFT_Attain"][0]==Actual_KPIofSITEDic["CRFT_Attain"][0]
                        assert Expected_KPIofSITEDic["CRFT_Attain"][1]==Actual_KPIofSITEDic["CRFT_Attain"][1]
                        assert Expected_KPIofSITEDic["OpsAht"][0]==Actual_KPIofSITEDic["OpsAht"][0]
                        assert Expected_KPIofSITEDic["OpsAht"][1]==Actual_KPIofSITEDic["OpsAht"][1]
                        assert Expected_KPIofSITEDic["VOIP_Actual"][0]==Actual_KPIofSITEDic["VOIP_Actual"][0]
                        assert Expected_KPIofSITEDic["VOIP_Actual"][1]==Actual_KPIofSITEDic["VOIP_Actual"][1]
                        assert Expected_KPIofSITEDic["VOIP_Attain"][0]==Actual_KPIofSITEDic["VOIP_Attain"][0]
                        assert Expected_KPIofSITEDic["VOIP_Attain"][1]==Actual_KPIofSITEDic["VOIP_Attain"][1]
                        assert Expected_KPIofSITEDic["WLS_Actual"][0]==Actual_KPIofSITEDic["WLS_Actual"][0]
                        assert Expected_KPIofSITEDic["WLS_Actual"][1]==Actual_KPIofSITEDic["WLS_Actual"][1]
                        assert Expected_KPIofSITEDic["WLS_Attain"][0]==Actual_KPIofSITEDic["WLS_Attain"][0]
                        assert Expected_KPIofSITEDic["WLS_Attain"][1]==Actual_KPIofSITEDic["WLS_Attain"][1]
                        assert Expected_KPIofSITEDic["Achiev"][0]==Actual_KPIofSITEDic["Achiev"][0]
                        ''' Achiev has no KPI sort '''
                        
                        
                        #Step3:Verify achievement of Tl1
                        print "=================3.Verify TL1's achievement.=============="
                        #Step3.1:Get the Expected achievement of Tl1
                        '''Expected_KPIofTl1 is from above, and  Expected_Achi_Tl1 is from below'''
                        #Expected_Achi_Tl1=Expected_KPIofTl1["Achiev"][0]
                        #Step3.2:Get the Actual achievement of Tl1
                        flag=True
                        lineindex=1
                        while flag==True:
                            TL_name=Ppage.get_anyKPIofTL(lineindex, 1)[0]
                            if TL_name=='Tl1 Test':
                                Actual_KPIofTl1=GetPData_Actual.get_SPANISH_TL_KPI_Actual(lineindex)
                                #Actual_Achiev_TL1=GetPData_Actual.get_SPANISH_TL_KPI_Actual(lineindex)["Achiev"][0]
                                Tl1_line=lineindex#For Step4
                                break
                            lineindex=lineindex+1
                            flag=Ppage.TL_line_exist(lineindex)
                       
                        '''Actual_Achiev_TL1'''
                        #Step3.3:assert Expected==Actual
                        #assert Expected_Achi_Tl1==Actual_Achiev_TL1
                        print Expected_KPIofTl1
                        print Actual_KPIofTl1
                        
                        
                        
                        assert Expected_KPIofTl1["NetRevenue_Actual"][0]==Actual_KPIofTl1["NetRevenue_Actual"][0]
                        assert Expected_KPIofTl1["NetRevenue_Actual"][1]==Actual_KPIofTl1["NetRevenue_Actual"][1]
                        assert Expected_KPIofTl1["NetRevenue_Attain"][0]==Actual_KPIofTl1["NetRevenue_Attain"][0]
                        assert Expected_KPIofTl1["NetRevenue_Attain"][1]==Actual_KPIofTl1["NetRevenue_Attain"][1]
                        assert Expected_KPIofTl1["HSIAIPDSL_Actual"][0]==Actual_KPIofTl1["HSIAIPDSL_Actual"][0]
                        assert Expected_KPIofTl1["HSIAIPDSL_Actual"][1]==Actual_KPIofTl1["HSIAIPDSL_Actual"][1]
                        assert Expected_KPIofTl1["HSIAIPDSL_Attain"][0]==Actual_KPIofTl1["HSIAIPDSL_Attain"][0]
                        assert Expected_KPIofTl1["HSIAIPDSL_Attain"][1]==Actual_KPIofTl1["HSIAIPDSL_Attain"][1]
                        assert Expected_KPIofTl1["CRFT_Actual"][0]==Actual_KPIofTl1["CRFT_Actual"][0]
                        assert Expected_KPIofTl1["CRFT_Actual"][1]==Actual_KPIofTl1["CRFT_Actual"][1]
                        assert Expected_KPIofTl1["CRFT_Attain"][0]==Actual_KPIofTl1["CRFT_Attain"][0]
                        assert Expected_KPIofTl1["CRFT_Attain"][1]==Actual_KPIofTl1["CRFT_Attain"][1]
                        assert Expected_KPIofTl1["OpsAht"][0]==Actual_KPIofTl1["OpsAht"][0]
                        assert Expected_KPIofTl1["OpsAht"][1]==Actual_KPIofTl1["OpsAht"][1]
                        assert Expected_KPIofTl1["VOIP_Actual"][0]==Actual_KPIofTl1["VOIP_Actual"][0]
                        assert Expected_KPIofTl1["VOIP_Actual"][1]==Actual_KPIofTl1["VOIP_Actual"][1]
                        assert Expected_KPIofTl1["VOIP_Attain"][0]==Actual_KPIofTl1["VOIP_Attain"][0]
                        assert Expected_KPIofTl1["VOIP_Attain"][1]==Actual_KPIofTl1["VOIP_Attain"][1]
                        assert Expected_KPIofTl1["WLS_Actual"][0]==Actual_KPIofTl1["WLS_Actual"][0]
                        assert Expected_KPIofTl1["WLS_Actual"][1]==Actual_KPIofTl1["WLS_Actual"][1]
                        assert Expected_KPIofTl1["WLS_Attain"][0]==Actual_KPIofTl1["WLS_Attain"][0]##????
                        assert Expected_KPIofTl1["WLS_Attain"][1]==Actual_KPIofTl1["WLS_Attain"][1]
                        assert Expected_KPIofTl1["Achiev"][0]==Actual_KPIofTl1["Achiev"][0]
                        
                        
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
                            Agent_Achiev=Ppage.get_anyKPIofAgent_OM(TLindex, Agentindex, 13)[0]
                            Actual_AgentAchiev[Agent_Name]=Agent_Achiev
                            if Agent_Name=='Agent 8' or Agent_Name=='Agent 11':
                                Agent_KPI=GetPData_Actual.get_SPANISH_Agent_KPI_Actual(TLindex, Agentindex)
                                Actual_AgentKPI[Agent_Name]=Agent_KPI#For Step5 and Step6
                            Agentindex=Agentindex+1
                            flag=Ppage.Agent_line_exist_OM(TLindex, Agentindex)
                            
                        print "=================4.Actual_All Agents' Achiev of Tl1=============="
                        print Agentindex
                        print Actual_AgentAchiev
                        #Step4.3:assert Expected==Actual
                        if self.tablist[ywm] not in ["LastTwoMonth","Month-to-Date"] :
                            assert Expected_AgentAchiev["Agent 1"][0]==Actual_AgentAchiev["Agent 1"][0]
                            assert Expected_AgentAchiev["Agent 2"][0]==Actual_AgentAchiev["Agent 2"][0]
                            assert Expected_AgentAchiev["Agent 3"][0]==Actual_AgentAchiev["Agent 3"][0]
                            assert Expected_AgentAchiev["Agent 4"][0]==Actual_AgentAchiev["Agent 4"][0]
                            assert Expected_AgentAchiev["Agent 5"][0]==Actual_AgentAchiev["Agent 5"][0]
                            assert Expected_AgentAchiev["Agent 6"][0]==Actual_AgentAchiev["Agent 6"][0]
                            assert Expected_AgentAchiev["Agent 7"][0]==Actual_AgentAchiev["Agent 7"][0]
                        if self.tablist[ywm] != "LastTwoMonth":
                            assert Expected_AgentAchiev["Agent 8"][0]==Actual_AgentAchiev["Agent 8"][0]
                        assert Expected_AgentAchiev["Agent 9"][0]==Actual_AgentAchiev["Agent 9"][0]
                        assert Expected_AgentAchiev["Agent 10"][0]==Actual_AgentAchiev["Agent 10"][0]
                        assert Expected_AgentAchiev["Agent 11"][0]==Actual_AgentAchiev["Agent 11"][0]
                        
                        
                        #Step5:Verify Agent8:check each KPI value, color.
                        print "=================5.Verify Agent8:check each KPI value, color==============" 
                        #Step5.1:Get the Expected KPI value and color for Agent8
                        print "=================5.1 Expected KPI value and color of Agent8=============="
                        if self.tablist[ywm] != "LastTwoMonth":
                            print Expected_KPIofAgent8
                            #Step5.2:Get the Actual KPI and color for Agent8
                            print "=================5.2 Actual KPI value and color of Agent8=============="
                            Actual_KPIofAgent8=Actual_AgentKPI['Agent 8']
                            print Actual_KPIofAgent8
                            assert Expected_KPIofAgent8["NetRevenue_Actual"][0]==Actual_KPIofAgent8["NetRevenue_Actual"][0]
                            assert Expected_KPIofAgent8["NetRevenue_Actual"][1]==Actual_KPIofAgent8["NetRevenue_Actual"][1]
                            assert Expected_KPIofAgent8["NetRevenue_Attain"][0]==Actual_KPIofAgent8["NetRevenue_Attain"][0]
                            assert Expected_KPIofAgent8["NetRevenue_Attain"][1]==Actual_KPIofAgent8["NetRevenue_Attain"][1]
                            assert Expected_KPIofAgent8["HSIAIPDSL_Actual"][0]==Actual_KPIofAgent8["HSIAIPDSL_Actual"][0]
                            assert Expected_KPIofAgent8["HSIAIPDSL_Actual"][1]==Actual_KPIofAgent8["HSIAIPDSL_Actual"][1]
                            assert Expected_KPIofAgent8["HSIAIPDSL_Attain"][0]==Actual_KPIofAgent8["HSIAIPDSL_Attain"][0]
                            assert Expected_KPIofAgent8["HSIAIPDSL_Attain"][1]==Actual_KPIofAgent8["HSIAIPDSL_Attain"][1]
                            assert Expected_KPIofAgent8["CRFT_Actual"][0]==Actual_KPIofAgent8["CRFT_Actual"][0]
                            assert Expected_KPIofAgent8["CRFT_Actual"][1]==Actual_KPIofAgent8["CRFT_Actual"][1]
                            assert Expected_KPIofAgent8["CRFT_Attain"][0]==Actual_KPIofAgent8["CRFT_Attain"][0]
                            assert Expected_KPIofAgent8["CRFT_Attain"][1]==Actual_KPIofAgent8["CRFT_Attain"][1]
                            assert Expected_KPIofAgent8["OpsAht"][0]==Actual_KPIofAgent8["OpsAht"][0]
                            assert Expected_KPIofAgent8["OpsAht"][1]==Actual_KPIofAgent8["OpsAht"][1]
                            assert Expected_KPIofAgent8["VOIP_Actual"][0]==Actual_KPIofAgent8["VOIP_Actual"][0]
                            assert Expected_KPIofAgent8["VOIP_Actual"][1]==Actual_KPIofAgent8["VOIP_Actual"][1]
                            assert Expected_KPIofAgent8["VOIP_Attain"][0]==Actual_KPIofAgent8["VOIP_Attain"][0]
                            assert Expected_KPIofAgent8["VOIP_Attain"][1]==Actual_KPIofAgent8["VOIP_Attain"][1]
                            assert Expected_KPIofAgent8["WLS_Actual"][0]==Actual_KPIofAgent8["WLS_Actual"][0]
                            assert Expected_KPIofAgent8["WLS_Actual"][1]==Actual_KPIofAgent8["WLS_Actual"][1]
                            assert Expected_KPIofAgent8["WLS_Attain"][0]==Actual_KPIofAgent8["WLS_Attain"][0]
                            assert Expected_KPIofAgent8["WLS_Attain"][1]==Actual_KPIofAgent8["WLS_Attain"][1]

                        
                        
                        #Step6:Verify Agent11:check each KPI value, color.
                        print "=================6.Verify Agent11:check each KPI value, color=============="
                        #Step6.1:Get the Expected KPI value and color for Agent8
                        print "=================6.1 Expected KPI value and color of Agent11=============="
                        print Expected_KPIofAgent11
                        #Step6.2:Get the Actual KPI and color for Agent8
                        print "=================6.2 Actual KPI value and color of Agent11=============="
                        Actual_KPIofAgent11=Actual_AgentKPI['Agent 11']
                        print Actual_KPIofAgent11
                        assert Expected_KPIofAgent11["NetRevenue_Actual"][0]==Actual_KPIofAgent11["NetRevenue_Actual"][0]
                        assert Expected_KPIofAgent11["NetRevenue_Actual"][1]==Actual_KPIofAgent11["NetRevenue_Actual"][1]
                        assert Expected_KPIofAgent11["NetRevenue_Attain"][0]==Actual_KPIofAgent11["NetRevenue_Attain"][0]
                        assert Expected_KPIofAgent11["NetRevenue_Attain"][1]==Actual_KPIofAgent11["NetRevenue_Attain"][1]
                        assert Expected_KPIofAgent11["HSIAIPDSL_Actual"][0]==Actual_KPIofAgent11["HSIAIPDSL_Actual"][0]
                        assert Expected_KPIofAgent11["HSIAIPDSL_Actual"][1]==Actual_KPIofAgent11["HSIAIPDSL_Actual"][1]
                        assert Expected_KPIofAgent11["HSIAIPDSL_Attain"][0]==Actual_KPIofAgent11["HSIAIPDSL_Attain"][0]
                        assert Expected_KPIofAgent11["HSIAIPDSL_Attain"][1]==Actual_KPIofAgent11["HSIAIPDSL_Attain"][1]
                        assert Expected_KPIofAgent11["CRFT_Actual"][0]==Actual_KPIofAgent11["CRFT_Actual"][0]
                        assert Expected_KPIofAgent11["CRFT_Actual"][1]==Actual_KPIofAgent11["CRFT_Actual"][1]
                        assert Expected_KPIofAgent11["CRFT_Attain"][0]==Actual_KPIofAgent11["CRFT_Attain"][0]
                        assert Expected_KPIofAgent11["CRFT_Attain"][1]==Actual_KPIofAgent11["CRFT_Attain"][1]
                        assert Expected_KPIofAgent11["OpsAht"][0]==Actual_KPIofAgent11["OpsAht"][0]
                        assert Expected_KPIofAgent11["OpsAht"][1]==Actual_KPIofAgent11["OpsAht"][1]
                        assert Expected_KPIofAgent11["VOIP_Actual"][0]==Actual_KPIofAgent11["VOIP_Actual"][0]
                        assert Expected_KPIofAgent11["VOIP_Actual"][1]==Actual_KPIofAgent11["VOIP_Actual"][1]
                        assert Expected_KPIofAgent11["VOIP_Attain"][0]==Actual_KPIofAgent11["VOIP_Attain"][0]
                        assert Expected_KPIofAgent11["VOIP_Attain"][1]==Actual_KPIofAgent11["VOIP_Attain"][1]
                        assert Expected_KPIofAgent11["WLS_Actual"][0]==Actual_KPIofAgent11["WLS_Actual"][0]
                        assert Expected_KPIofAgent11["WLS_Actual"][1]==Actual_KPIofAgent11["WLS_Actual"][1]
                        assert Expected_KPIofAgent11["WLS_Attain"][0]==Actual_KPIofAgent11["WLS_Attain"][0]
                        assert Expected_KPIofAgent11["WLS_Attain"][1]==Actual_KPIofAgent11["WLS_Attain"][1]

                    L.logout_tablet()    


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()