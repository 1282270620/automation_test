'''
Created on Apr 5, 2017

@author: symbio
'''
import unittest
#from public_method.Get_PerformanceData_Expected import Get_PerformanceData_Expected
#from public_method.Get_PerformanceData_Actual import Get_PerformanceData_Actual
from Performance_Cases_BLUE.Get_PerformanceData_Actual_BLUE import Get_PerformanceData_Actual_BLUE
from Performance_Cases_BLUE.Get_PerformanceData_Expected_BLUE import Get_PerformanceData_Expected_BLUE

from public_method import Gl
from public_method.Get_configration_data import Get_configration_data
from public_method.Login import Login
from Tablet_pages.TabletHomepage import TabletHomepage
from Tablet_pages.PerformancPage import PerformancePage
import time


class BLUE_Performance_OM(unittest.TestCase):


    def setUp(self):
        self.caseID="BLUE_Performance_OM"
        GetData=Get_configration_data()
        #Get URL 
        self.tableturl=GetData.get_TabletUrl()
        #Get OM account
        OMaccount=GetData.get_OMaccount()
        self.OMuserid=OMaccount["OMuserid"]
        self.OMpassword=OMaccount["OMpassword"]
        #Get all lobs from CSV
        self.testLOBSITE_list=GetData.get_LOBSITEtoTest(self.caseID)
        
        #Yesterday,WTD,MTD for BLUE
        self.tablist=Gl.Less_timetab#["LastTwoMonth","LastMonth","Month-to-Date"]#
        


    def tearDown(self):
        #Gl.driver.quit() 
        pass


    def test_BLUE_Performance_OM(self):
        GetConfig=Get_configration_data()
        L=Login()
        THomepage=TabletHomepage()
        Ppage=PerformancePage()
        GetPData_Actual=Get_PerformanceData_Actual_BLUE()
        #Get Goal Expected
        GetPData_Expected=Get_PerformanceData_Expected_BLUE()
        '''
        lineindex=2#The goal is in the row 3 of excel file,so linedex is 2
        Expected_GoalDic=GetPData_Expected.get_BLUE_Goal_Expected(lineindex)
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
                    Achiev_SITE_Monthly=GetPData_Actual.get_BLUE_SITE_Data_()['Achiev'][0]
                    print "=================The value is the same as SITE KPI of monthly report page.=============="                    
                    assert Achiev_PerformanceCircle==Achiev_SITE_Monthly
                     
                    for ywm in range(0,len(self.tablist)):
                        Ppage.click_timetab_performance(ywm+1)
                        
                        print "*********************Start********************",
                        print self.tablist[ywm],
                        print "is in testing:"
                        time.sleep(Gl.waittime)
                        #Step1:Verify Goal
                        
                        '''
                        assert Expected_GoalDic["CRFT"]==Actual_GoalDic["CRFT"]
                        assert Expected_GoalDic["SevenDayRepeats"]==Actual_GoalDic["SevenDayRepeats"]
                        assert Expected_GoalDic["NetRevenue_Chargeback"]==Actual_GoalDic["NetRevenue_Chargeback"]
                        assert Expected_GoalDic["NetRevenue_Net"]==Actual_GoalDic["NetRevenue_Net"]
                        assert Expected_GoalDic["Broadband_Chargeback"]==Actual_GoalDic["Broadband_Chargeback"]
                        assert Expected_GoalDic["Broadband_Net"]==Actual_GoalDic["Broadband_Net"]
                        assert Expected_GoalDic["DTV_Chargeback"]==Actual_GoalDic["DTV_Chargeback"]
                        assert Expected_GoalDic["DTV_Net"]==Actual_GoalDic["DTV_Net"]
                        assert Expected_GoalDic["IPTV"]==Actual_GoalDic["IPTV"]
                        assert Expected_GoalDic["VOIP"]==Actual_GoalDic["VOIP"]
                        assert Expected_GoalDic["Wireless"]==Actual_GoalDic["Wireless"]
                        assert Expected_GoalDic["IPTV_VOIP_Wireless"]==Actual_GoalDic["IPTV_VOIP_Wireless"]
                        assert Expected_GoalDic["Achiev"]==Actual_GoalDic["Achiev"]'''
                        
                        '''Prepare Data for the following test '''
                        if self.tablist[ywm]=="LastTwoMonth":
                            Expected_GoalDic=GetPData_Expected.get_BLUE_Goal_Expected(81)
                            Expected_KPIofSITEDic=GetPData_Expected.get_BLUE_Performance_Data_Expected(40)#For Step2
                            Expected_KPIofTl1=GetPData_Expected.get_BLUE_Performance_Data_Expected(91)#For Step3
                            Expected_AgentAchiev=GetPData_Expected.Get_ManyAgentAchiev_Expected(131, 134)#For Step4
                            Expected_KPIofAgent8=GetPData_Expected.get_BLUE_Performance_Data_Expected(131)#For Step5
                            Expected_KPIofAgent11=GetPData_Expected.get_BLUE_Performance_Data_Expected(134)#For Step6
                            
                        elif self.tablist[ywm]=="LastMonth":
                            Expected_GoalDic=GetPData_Expected.get_BLUE_Goal_Expected(2)
                            Expected_KPIofSITEDic=GetPData_Expected.get_BLUE_Site_Expected(124)#For Step2
                            Expected_KPIofTl1=GetPData_Expected.get_BLUE_Performance_Data_Expected(118)#For Step3
                            Expected_AgentAchiev=GetPData_Expected.Get_ManyAgentAchiev_Expected(107, 117)#For Step4
                            Expected_KPIofAgent8=GetPData_Expected.get_BLUE_Performance_Data_Expected(114)#For Step5
                            Expected_KPIofAgent11=GetPData_Expected.get_BLUE_Performance_Data_Expected(117)#For Step6
                        
                        elif self.tablist[ywm]=="Month-to-Date":
                            Expected_GoalDic=GetPData_Expected.get_BLUE_Goal_Expected(98)
                            Expected_KPIofSITEDic=GetPData_Expected.get_BLUE_Site_Expected(99)#For Step2
                            Expected_KPIofTl1=GetPData_Expected.get_BLUE_Performance_Data_Expected(93)#For Step3
                            Expected_AgentAchiev=GetPData_Expected.Get_ManyAgentAchiev_Expected(82, 92)#For Step4
                            Expected_KPIofAgent8=GetPData_Expected.get_BLUE_Performance_Data_Expected(89)#For Step5
                            Expected_KPIofAgent11=GetPData_Expected.get_BLUE_Performance_Data_Expected(92)#For Step6
                        
                        
                        print "Expected_GoalDic:"
                        print Expected_GoalDic
                        print "=================1.Verify Each KPI of Goal=============="
                        Actual_GoalDic=GetPData_Actual.get_BLUE_Goal_Actual()#GET ACTUAL GOAL FORM PERFORMANCE PAGE
                        
                        print "Actual_GoalDic:"
                        print Actual_GoalDic
                        assert Expected_GoalDic["CRFT"]==Actual_GoalDic["CRFT"]
                        assert Expected_GoalDic["SevenDayRepeats"]==Actual_GoalDic["SevenDayRepeats"]
                        if Expected_GoalDic["NetRevenue_Chargeback"][0]==Expected_GoalDic["NetRevenue_Chargeback"][1]=='N/A':
                            Expected_GoalDic["NetRevenue_Chargeback"]='N/A'
                        assert Expected_GoalDic["NetRevenue_Chargeback"]==Actual_GoalDic["NetRevenue_Chargeback"]
                        assert Expected_GoalDic["NetRevenue_Net"]==Actual_GoalDic["NetRevenue_Net"]
                        assert Expected_GoalDic["Broadband_Chargeback"]==Actual_GoalDic["Broadband_Chargeback"]
                        assert Expected_GoalDic["Broadband_Net"]==Actual_GoalDic["Broadband_Net"]
                        assert Expected_GoalDic["DTV_Chargeback"]==Actual_GoalDic["DTV_Chargeback"]
                        assert Expected_GoalDic["DTV_Net"]==Actual_GoalDic["DTV_Net"]
                        assert Expected_GoalDic["IPTV"]==Actual_GoalDic["IPTV"]
                        assert Expected_GoalDic["VOIP"]==Actual_GoalDic["VOIP"]
                        assert Expected_GoalDic["Wireless"]==Actual_GoalDic["Wireless"]
                        assert Expected_GoalDic["IPTV_VOIP_Wireless"]==Actual_GoalDic["IPTV_VOIP_Wireless"]
                        assert Expected_GoalDic["Achiev"]==Actual_GoalDic["Achiev"]
                        #Step2:Verify KPI of SITES
                        print "=================2.Verify Each KPI of site, color, achievement=============="
                        '''Expected_KPIofSITEDic is from above.'''
                        print Expected_KPIofSITEDic
                        #Step2.2:Get the Actual KPI of site
                        '''Expected_KPIofSITEDic is from blow.''' 
                        Actual_KPIofSITEDic=GetPData_Actual.get_BLUE_SITE_Data_()
                        print Actual_KPIofSITEDic
                        #Step2.3:assert Expected==Actual
                        print Expected_KPIofSITEDic["CRFT"][0],Actual_KPIofSITEDic["CRFT"][0]
                        assert Expected_KPIofSITEDic["CRFT"][0]==Actual_KPIofSITEDic["CRFT"][0]
                        assert Expected_KPIofSITEDic["CRFT"][1]==Actual_KPIofSITEDic["CRFT"][1]
                        assert Expected_KPIofSITEDic["SevenDayRepeats"][0]==Actual_KPIofSITEDic["SevenDayRepeats"][0]
                        assert Expected_KPIofSITEDic["SevenDayRepeats"][1]==Actual_KPIofSITEDic["SevenDayRepeats"][1]
                        assert Expected_KPIofSITEDic["NetRevenue_Chargeback"][0]==Actual_KPIofSITEDic["NetRevenue_Chargeback"][0]
                        assert Expected_KPIofSITEDic["NetRevenue_Chargeback"][1]==Actual_KPIofSITEDic["NetRevenue_Chargeback"][1]
                        assert Expected_KPIofSITEDic["NetRevenue_Net"][0]==Actual_KPIofSITEDic["NetRevenue_Net"][0]
                        assert Expected_KPIofSITEDic["NetRevenue_Net"][1]==Actual_KPIofSITEDic["NetRevenue_Net"][1]
                        assert Expected_KPIofSITEDic["Broadband_Chargeback"][0]==Actual_KPIofSITEDic["Broadband_Chargeback"][0]
                        assert Expected_KPIofSITEDic["Broadband_Chargeback"][1]==Actual_KPIofSITEDic["Broadband_Chargeback"][1]
                        print Expected_KPIofSITEDic["Broadband_Net"][0],Actual_KPIofSITEDic["Broadband_Net"][0]
                        assert Expected_KPIofSITEDic["Broadband_Net"][0]==Actual_KPIofSITEDic["Broadband_Net"][0]
                        assert Expected_KPIofSITEDic["Broadband_Net"][1]==Actual_KPIofSITEDic["Broadband_Net"][1]
                        assert Expected_KPIofSITEDic["DTV_Chargeback"][0]==Actual_KPIofSITEDic["DTV_Chargeback"][0]
                        assert Expected_KPIofSITEDic["DTV_Chargeback"][1]==Actual_KPIofSITEDic["DTV_Chargeback"][1]
                        assert Expected_KPIofSITEDic["DTV_Net"][0]==Actual_KPIofSITEDic["DTV_Net"][0]
                        assert Expected_KPIofSITEDic["DTV_Net"][1]==Actual_KPIofSITEDic["DTV_Net"][1]
                        assert Expected_KPIofSITEDic["IPTV"][0]==Actual_KPIofSITEDic["IPTV"][0]
                        assert Expected_KPIofSITEDic["IPTV"][1]==Actual_KPIofSITEDic["IPTV"][1]
                        assert Expected_KPIofSITEDic["VOIP"][0]==Actual_KPIofSITEDic["VOIP"][0]
                        assert Expected_KPIofSITEDic["VOIP"][1]==Actual_KPIofSITEDic["VOIP"][1]
                        assert Expected_KPIofSITEDic["Wireless"][0]==Actual_KPIofSITEDic["Wireless"][0]
                        assert Expected_KPIofSITEDic["Wireless"][1]==Actual_KPIofSITEDic["Wireless"][1]
                        assert Expected_KPIofSITEDic["IPTV_VOIP_Wireless"][0]==Actual_KPIofSITEDic["IPTV_VOIP_Wireless"][0]
                        assert Expected_KPIofSITEDic["IPTV_VOIP_Wireless"][1]==Actual_KPIofSITEDic["IPTV_VOIP_Wireless"][1]
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
                                Actual_KPIofTl1=GetPData_Actual.get_BLUE_TL_KPI_Actual(lineindex)
                                #Actual_Achiev_TL1=GetPData_Actual.get_BLUE_TL_KPI_Actual(lineindex)["Achiev"][0]
                                Tl1_line=lineindex#For Step4
                                break
                            lineindex=lineindex+1
                            flag=Ppage.TL_line_exist(lineindex)
                       
                        '''Actual_Achiev_TL1'''
                        #Step3.3:assert Expected==Actual
                        #assert Expected_Achi_Tl1==Actual_Achiev_TL1
                        print Expected_KPIofTl1
                        print Actual_KPIofTl1
                        assert Expected_KPIofTl1["CRFT"][0]==Actual_KPIofTl1["CRFT"][0]
                        assert Expected_KPIofTl1["CRFT"][1]==Actual_KPIofTl1["CRFT"][1]
                        assert Expected_KPIofTl1["SevenDayRepeats"][0]==Actual_KPIofTl1["SevenDayRepeats"][0]
                        assert Expected_KPIofTl1["SevenDayRepeats"][1]==Actual_KPIofTl1["SevenDayRepeats"][1]
                        assert Expected_KPIofTl1["NetRevenue_Chargeback"][0]==Actual_KPIofTl1["NetRevenue_Chargeback"][0]
                        assert Expected_KPIofTl1["NetRevenue_Chargeback"][1]==Actual_KPIofTl1["NetRevenue_Chargeback"][1]
                        assert Expected_KPIofTl1["NetRevenue_Net"][0]==Actual_KPIofTl1["NetRevenue_Net"][0]
                        assert Expected_KPIofTl1["NetRevenue_Net"][1]==Actual_KPIofTl1["NetRevenue_Net"][1]
                        assert Expected_KPIofTl1["Broadband_Chargeback"][0]==Actual_KPIofTl1["Broadband_Chargeback"][0]
                        assert Expected_KPIofTl1["Broadband_Chargeback"][1]==Actual_KPIofTl1["Broadband_Chargeback"][1]
                        assert Expected_KPIofTl1["Broadband_Net"][1]==Actual_KPIofTl1["Broadband_Net"][1]
                        assert Expected_KPIofTl1["DTV_Chargeback"][0]==Actual_KPIofTl1["DTV_Chargeback"][0]
                        assert Expected_KPIofTl1["DTV_Chargeback"][1]==Actual_KPIofTl1["DTV_Chargeback"][1]
                        print Expected_KPIofTl1["DTV_Net"][0],Actual_KPIofTl1["DTV_Net"][0]
                        assert Expected_KPIofTl1["DTV_Net"][0]==Actual_KPIofTl1["DTV_Net"][0]
                        assert Expected_KPIofTl1["DTV_Net"][1]==Actual_KPIofTl1["DTV_Net"][1]
                        assert Expected_KPIofTl1["IPTV"][0]==Actual_KPIofTl1["IPTV"][0]
                        assert Expected_KPIofTl1["IPTV"][1]==Actual_KPIofTl1["IPTV"][1]
                        assert Expected_KPIofTl1["VOIP"][0]==Actual_KPIofTl1["VOIP"][0]
                        assert Expected_KPIofTl1["VOIP"][1]==Actual_KPIofTl1["VOIP"][1]
                        assert Expected_KPIofTl1["Wireless"][0]==Actual_KPIofTl1["Wireless"][0]
                        assert Expected_KPIofTl1["Wireless"][1]==Actual_KPIofTl1["Wireless"][1]
                        assert Expected_KPIofTl1["IPTV_VOIP_Wireless"][0]==Actual_KPIofTl1["IPTV_VOIP_Wireless"][0]
                        assert Expected_KPIofTl1["IPTV_VOIP_Wireless"][1]==Actual_KPIofTl1["IPTV_VOIP_Wireless"][1]
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
                            Agent_Achiev=Ppage.get_anyKPIofAgent_OM(TLindex, Agentindex, 8)[0]
                            Actual_AgentAchiev[Agent_Name]=Agent_Achiev
                            if Agent_Name=='Agent 8' or Agent_Name=='Agent 11':
                                Agent_KPI=GetPData_Actual.get_BLUE_Agent_KPI_Actual(TLindex, Agentindex)
                                Actual_AgentKPI[Agent_Name]=Agent_KPI#For Step5 and Step6
                            Agentindex=Agentindex+1
                            flag=Ppage.Agent_line_exist_OM(TLindex, Agentindex)
                            
                        print "=================4.Actual_All Agents' Achiev of Tl1=============="
                        print Agentindex
                        print Actual_AgentAchiev
                        #Step4.3:assert Expected==Actual
                        if self.tablist[ywm] not in ["LastTwoMonth","Month-To-Date"] :
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
                        print Expected_KPIofAgent8
                        #Step5.2:Get the Actual KPI and color for Agent8
                        print "=================5.2 Actual KPI value and color of Agent8=============="
                        Actual_KPIofAgent8=Actual_AgentKPI['Agent 8']
                        print Actual_KPIofAgent8
                        assert Expected_KPIofAgent8["AHT"][0]==Actual_KPIofAgent8["AHT"][0]#0 is KPI value
                        assert Expected_KPIofAgent8["AHT"][1]==Actual_KPIofAgent8["AHT"][1]#1 is KPI status
                        assert Expected_KPIofAgent8["HoldTime"][0]==Actual_KPIofAgent8["HoldTime"][0]#0 is KPI value
                        assert Expected_KPIofAgent8["HoldTime"][1]==Actual_KPIofAgent8["HoldTime"][1]#1 is KPI status
                        assert Expected_KPIofAgent8["ACW"][0]==Actual_KPIofAgent8["ACW"][0]#0 is KPI value
                        assert Expected_KPIofAgent8["ACW"][1]==Actual_KPIofAgent8["ACW"][1]#1 is KPI status
                        assert Expected_KPIofAgent8["Transfers"][0]==Actual_KPIofAgent8["Transfers"][0]#0 is KPI value
                        assert Expected_KPIofAgent8["Transfers"][1]==Actual_KPIofAgent8["Transfers"][1]#1 is KPI status
                        assert Expected_KPIofAgent8["VOC"][0]==Actual_KPIofAgent8["VOC"][0]#0 is KPI value
                        assert Expected_KPIofAgent8["VOC"][1]==Actual_KPIofAgent8["VOC"][1]#1 is KPI status
                        assert Expected_KPIofAgent8["SOAR"][0]==Actual_KPIofAgent8["SOAR"][0]#0 is KPI value
                        assert Expected_KPIofAgent8["SOAR"][1]==Actual_KPIofAgent8["SOAR"][1]#1 is KPI status


                        
                        
                        #Step6:Verify Agent11:check each KPI value, color.
                        print "=================6.Verify Agent11:check each KPI value, color=============="
                        #Step6.1:Get the Expected KPI value and color for Agent8
                        print "=================6.1 Expected KPI value and color of Agent11=============="
                        print Expected_KPIofAgent11
                        #Step6.2:Get the Actual KPI and color for Agent8
                        print "=================6.2 Actual KPI value and color of Agent11=============="
                        Actual_KPIofAgent11=Actual_AgentKPI['Agent 11']
                        print Actual_KPIofAgent11
                        assert Expected_KPIofAgent11["AHT"][0]==Actual_KPIofAgent11["AHT"][0]#0 is KPI value
                        assert Expected_KPIofAgent11["AHT"][1]==Actual_KPIofAgent11["AHT"][1]#1 is KPI status
                        assert Expected_KPIofAgent11["HoldTime"][0]==Actual_KPIofAgent11["HoldTime"][0]#0 is KPI value
                        assert Expected_KPIofAgent11["HoldTime"][1]==Actual_KPIofAgent11["HoldTime"][1]#1 is KPI status
                        assert Expected_KPIofAgent11["ACW"][0]==Actual_KPIofAgent11["ACW"][0]#0 is KPI value
                        assert Expected_KPIofAgent11["ACW"][1]==Actual_KPIofAgent11["ACW"][1]#1 is KPI status
                        assert Expected_KPIofAgent11["Transfers"][0]==Actual_KPIofAgent11["Transfers"][0]#0 is KPI value
                        assert Expected_KPIofAgent11["Transfers"][1]==Actual_KPIofAgent11["Transfers"][1]#1 is KPI status
                        assert Expected_KPIofAgent11["VOC"][0]==Actual_KPIofAgent11["VOC"][0]#0 is KPI value
                        assert Expected_KPIofAgent11["VOC"][1]==Actual_KPIofAgent11["VOC"][1]#1 is KPI status
                        assert Expected_KPIofAgent11["SOAR"][0]==Actual_KPIofAgent11["SOAR"][0]#0 is KPI value
                        assert Expected_KPIofAgent11["SOAR"][1]==Actual_KPIofAgent11["SOAR"][1]#1 is KPI status

                    L.logout_tablet()    


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()