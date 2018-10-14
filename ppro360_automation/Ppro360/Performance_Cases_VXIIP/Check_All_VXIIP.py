'''
Created on Apr 10, 2018

@author: symbio
'''
from Tablet_pages.PerformancPage import PerformancePage
from Performance_Cases_VXIIP.Get_PerformanceData_Actual_VXIIP import Get_PerformanceData_Actual_VXIIP

class Check_All_VXIIP(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    def Check_Goal(self,Expected_GoalDic,Actual_GoalDic):
        assert Expected_GoalDic["VOC_Number"]==Actual_GoalDic["VOC_Number"]
        assert Expected_GoalDic["VOC_OverallScore"]==Actual_GoalDic["VOC_OverallScore"]
        assert Expected_GoalDic["SevenDayRepeats_Repeats"]==Actual_GoalDic["SevenDayRepeats_Repeats"]
        assert Expected_GoalDic["SevenDayRepeats_ManagedCalls"]==Actual_GoalDic["SevenDayRepeats_ManagedCalls"]
        assert Expected_GoalDic["SevenDayRepeats_RepeatRate"]==Actual_GoalDic["SevenDayRepeats_RepeatRate"]
        assert Expected_GoalDic["Productivity_AHT"]==Actual_GoalDic["Productivity_AHT"]
        assert Expected_GoalDic["Transfers"]==Actual_GoalDic["Transfers"]
        assert Expected_GoalDic["Adjustment"]==Actual_GoalDic["Adjustment"]
        assert Expected_GoalDic["AdjustmentPerCall"]==Actual_GoalDic["AdjustmentPerCall"]
        assert Expected_GoalDic["Wireless"]==Actual_GoalDic["Wireless"]
        assert Expected_GoalDic["Broadband"]==Actual_GoalDic["Broadband"]
        assert Expected_GoalDic["DTV"]==Actual_GoalDic["DTV"]
        assert Expected_GoalDic["DTV_BB_VOIP_IPTV"]==Actual_GoalDic["DTV_BB_VOIP_IPTV"]
    def Check_Site(self,Expected_KPIofSITEDic,Actual_KPIofSITEDic):
        #Step2:Verify KPI of SITES
        print "=================2.Verify Each KPI of site, color, achievement=============="
        '''Expected_KPIofSITEDic is from above.'''
        print Expected_KPIofSITEDic
        #Step2.2:Get the Actual KPI of site
        '''Expected_KPIofSITEDic is from blow.''' 
        
        print Actual_KPIofSITEDic
        assert Expected_KPIofSITEDic["VOC_Number"][0]==Actual_KPIofSITEDic["VOC_Number"][0]#0 is KPI value
        assert Expected_KPIofSITEDic["VOC_Number"][1]==Actual_KPIofSITEDic["VOC_Number"][1]#1 is KPI status
        assert Expected_KPIofSITEDic["VOC_OverallScore"][0]==Actual_KPIofSITEDic["VOC_OverallScore"][0]#0 is KPI value
        assert Expected_KPIofSITEDic["VOC_OverallScore"][1]==Actual_KPIofSITEDic["VOC_OverallScore"][1]#1 is KPI status
        assert Expected_KPIofSITEDic["SevenDayRepeats_Repeats"][0]==Actual_KPIofSITEDic["SevenDayRepeats_Repeats"][0]#0 is KPI value
        assert Expected_KPIofSITEDic["SevenDayRepeats_Repeats"][1]==Actual_KPIofSITEDic["SevenDayRepeats_Repeats"][1]#1 is KPI status
        assert Expected_KPIofSITEDic["SevenDayRepeats_ManagedCalls"][0]==Actual_KPIofSITEDic["SevenDayRepeats_ManagedCalls"][0]#0 is KPI value
        assert Expected_KPIofSITEDic["SevenDayRepeats_ManagedCalls"][1]==Actual_KPIofSITEDic["SevenDayRepeats_ManagedCalls"][1]#1 is KPI status
        assert Expected_KPIofSITEDic["SevenDayRepeats_RepeatRate"][0]==Actual_KPIofSITEDic["SevenDayRepeats_RepeatRate"][0]#0 is KPI value
        assert Expected_KPIofSITEDic["SevenDayRepeats_RepeatRate"][1]==Actual_KPIofSITEDic["SevenDayRepeats_RepeatRate"][1]#1 is KPI status
        assert Expected_KPIofSITEDic["Productivity_AHT"][0]==Actual_KPIofSITEDic["Productivity_AHT"][0]#0 is KPI value
        assert Expected_KPIofSITEDic["Productivity_AHT"][1]==Actual_KPIofSITEDic["Productivity_AHT"][1]#1 is KPI status
        assert Expected_KPIofSITEDic["Transfers"][0]==Actual_KPIofSITEDic["Transfers"][0]#0 is KPI value
        assert Expected_KPIofSITEDic["Transfers"][1]==Actual_KPIofSITEDic["Transfers"][1]#1 is KPI status
        assert Expected_KPIofSITEDic["Adjustment"][0]==Actual_KPIofSITEDic["Adjustment"][0]#0 is KPI value
        assert Expected_KPIofSITEDic["Adjustment"][1]==Actual_KPIofSITEDic["Adjustment"][1]#1 is KPI status
        assert Expected_KPIofSITEDic["AdjustmentPerCall"][0]==Actual_KPIofSITEDic["AdjustmentPerCall"][0]#0 is KPI value
        assert Expected_KPIofSITEDic["AdjustmentPerCall"][1]==Actual_KPIofSITEDic["AdjustmentPerCall"][1]#1 is KPI status
        assert Expected_KPIofSITEDic["Wireless"][0]==Actual_KPIofSITEDic["Wireless"][0]#0 is KPI value
        assert Expected_KPIofSITEDic["Wireless"][1]==Actual_KPIofSITEDic["Wireless"][1]#1 is KPI status
        assert Expected_KPIofSITEDic["Broadband"][0]==Actual_KPIofSITEDic["Broadband"][0]#0 is KPI value
        assert Expected_KPIofSITEDic["Broadband"][1]==Actual_KPIofSITEDic["Broadband"][1]#1 is KPI status
        assert Expected_KPIofSITEDic["DTV"][0]==Actual_KPIofSITEDic["DTV"][0]#0 is KPI value
        assert Expected_KPIofSITEDic["DTV"][1]==Actual_KPIofSITEDic["DTV"][1]#1 is KPI status
        assert Expected_KPIofSITEDic["DTV_BB_VOIP_IPTV"][0]==Actual_KPIofSITEDic["DTV_BB_VOIP_IPTV"][0]#0 is KPI value
        assert Expected_KPIofSITEDic["DTV_BB_VOIP_IPTV"][1]==Actual_KPIofSITEDic["DTV_BB_VOIP_IPTV"][1]#1 is KPI status
        assert Expected_KPIofSITEDic["Achiev"][0]==Actual_KPIofSITEDic["Achiev"][0]#0 is KPI value   
        
    def Check_TL1Achive(self,Expected_KPIofTl1):
        Ppage=PerformancePage()
        GetPData_Actual=Get_PerformanceData_Actual_VXIIP()
        #Get Goal Expected
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
                Actual_Achiev_TL1=GetPData_Actual.get_VXIIP_TL_KPI_Actual(lineindex)["Achiev"][0]
                Tl1_line=lineindex#For Step4
                break
            lineindex=lineindex+1
            flag=Ppage.TL_line_exist(lineindex)
       
        '''Actual_Achiev_TL1'''
        return Tl1_line
        #Step3.3:assert Expected==Actual
        assert Expected_Achi_Tl1==Actual_Achiev_TL1
    
    
    def Check_AllAgentofTL1(self,Tl1_line,TimeTab,Expected_AgentAchiev):
        Ppage=PerformancePage()
        GetPData_Actual=Get_PerformanceData_Actual_VXIIP()
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
            Agent_Achiev=Ppage.get_anyKPIofAgent_OM(TLindex, Agentindex, 12)[0]
            Actual_AgentAchiev[Agent_Name]=Agent_Achiev
            if Agent_Name=='Agent 8' or Agent_Name=='Agent 11':
                Agent_KPI=GetPData_Actual.get_VXIIP_Agent_KPI_Actual(TLindex, Agentindex)
                Actual_AgentKPI[Agent_Name]=Agent_KPI#For Step5 and Step6
            Agentindex=Agentindex+1
            flag=Ppage.Agent_line_exist_OM(TLindex, Agentindex)
           
        print "=================4.Actual_All Agents' Achiev of Tl1=============="
        print Agentindex
        print Actual_AgentAchiev
        return Actual_AgentKPI
        #Step4.3:assert Expected==Actual
        if TimeTab!="LastTwoMonth":
            assert Expected_AgentAchiev["Agent 1"][0]==Actual_AgentAchiev["Agent 1"][0]
            assert Expected_AgentAchiev["Agent 2"][0]==Actual_AgentAchiev["Agent 2"][0]
            assert Expected_AgentAchiev["Agent 3"][0]==Actual_AgentAchiev["Agent 3"][0]
            assert Expected_AgentAchiev["Agent 4"][0]==Actual_AgentAchiev["Agent 4"][0]
            assert Expected_AgentAchiev["Agent 5"][0]==Actual_AgentAchiev["Agent 5"][0]
            assert Expected_AgentAchiev["Agent 6"][0]==Actual_AgentAchiev["Agent 6"][0]
            assert Expected_AgentAchiev["Agent 7"][0]==Actual_AgentAchiev["Agent 7"][0]
            assert Expected_AgentAchiev["Agent 8"][0]==Actual_AgentAchiev["Agent 8"][0] 
        assert Expected_AgentAchiev["Agent 9"][0]==Actual_AgentAchiev["Agent 9"][0]
        assert Expected_AgentAchiev["Agent 10"][0]==Actual_AgentAchiev["Agent 10"][0]
        assert Expected_AgentAchiev["Agent 11"][0]==Actual_AgentAchiev["Agent 11"][0]
        
        
    def Check_Agent8(self,Timetab,Expected_KPIofAgent8,Actual_AgentKPI):
        if Timetab!="LastTwoMonth":
            
            #Step5:Verify Agent8:check each KPI value, color.
            print "=================5.Verify Agent8:check each KPI value, color==============" 
            #Step5.1:Get the Expected KPI value and color for Agent8
            print "=================5.1 Expected KPI value and color of Agent8=============="
            print Expected_KPIofAgent8
            #Step5.2:Get the Actual KPI and color for Agent8
            print "=================5.2 Actual KPI value and color of Agent8=============="
            print Actual_AgentKPI
            Actual_KPIofAgent8=Actual_AgentKPI['Agent 8']
            print Actual_KPIofAgent8
            assert Expected_KPIofAgent8["VOC_Number"][0]==Actual_KPIofAgent8["VOC_Number"][0]#0 is KPI value
            assert Expected_KPIofAgent8["VOC_Number"][1]==Actual_KPIofAgent8["VOC_Number"][1]#1 is KPI status
            assert Expected_KPIofAgent8["VOC_OverallScore"][0]==Actual_KPIofAgent8["VOC_OverallScore"][0]#0 is KPI value
            assert Expected_KPIofAgent8["VOC_OverallScore"][1]==Actual_KPIofAgent8["VOC_OverallScore"][1]#1 is KPI status
            assert Expected_KPIofAgent8["SevenDayRepeats_Repeats"][0]==Actual_KPIofAgent8["SevenDayRepeats_Repeats"][0]#0 is KPI value
            assert Expected_KPIofAgent8["SevenDayRepeats_Repeats"][1]==Actual_KPIofAgent8["SevenDayRepeats_Repeats"][1]#1 is KPI status
            assert Expected_KPIofAgent8["SevenDayRepeats_ManagedCalls"][0]==Actual_KPIofAgent8["SevenDayRepeats_ManagedCalls"][0]#0 is KPI value
            assert Expected_KPIofAgent8["SevenDayRepeats_ManagedCalls"][1]==Actual_KPIofAgent8["SevenDayRepeats_ManagedCalls"][1]#1 is KPI status
            assert Expected_KPIofAgent8["SevenDayRepeats_RepeatRate"][0]==Actual_KPIofAgent8["SevenDayRepeats_RepeatRate"][0]#0 is KPI value
            assert Expected_KPIofAgent8["SevenDayRepeats_RepeatRate"][1]==Actual_KPIofAgent8["SevenDayRepeats_RepeatRate"][1]#1 is KPI status
            assert Expected_KPIofAgent8["Productivity_AHT"][0]==Actual_KPIofAgent8["Productivity_AHT"][0]#0 is KPI value
            assert Expected_KPIofAgent8["Productivity_AHT"][1]==Actual_KPIofAgent8["Productivity_AHT"][1]#1 is KPI status
            assert Expected_KPIofAgent8["Transfers"][0]==Actual_KPIofAgent8["Transfers"][0]#0 is KPI value
            assert Expected_KPIofAgent8["Transfers"][1]==Actual_KPIofAgent8["Transfers"][1]#1 is KPI status
            assert Expected_KPIofAgent8["Adjustment"][0]==Actual_KPIofAgent8["Adjustment"][0]#0 is KPI value
            assert Expected_KPIofAgent8["Adjustment"][1]==Actual_KPIofAgent8["Adjustment"][1]#1 is KPI status
            assert Expected_KPIofAgent8["AdjustmentPerCall"][0]==Actual_KPIofAgent8["AdjustmentPerCall"][0]#0 is KPI value
            assert Expected_KPIofAgent8["AdjustmentPerCall"][1]==Actual_KPIofAgent8["AdjustmentPerCall"][1]#1 is KPI status
            assert Expected_KPIofAgent8["Wireless"][0]==Actual_KPIofAgent8["Wireless"][0]#0 is KPI value
            assert Expected_KPIofAgent8["Wireless"][1]==Actual_KPIofAgent8["Wireless"][1]#1 is KPI status
            assert Expected_KPIofAgent8["Broadband"][0]==Actual_KPIofAgent8["Broadband"][0]#0 is KPI value
            assert Expected_KPIofAgent8["Broadband"][1]==Actual_KPIofAgent8["Broadband"][1]#1 is KPI status
            assert Expected_KPIofAgent8["DTV"][0]==Actual_KPIofAgent8["DTV"][0]#0 is KPI value
            assert Expected_KPIofAgent8["DTV"][1]==Actual_KPIofAgent8["DTV"][1]#1 is KPI status
            assert Expected_KPIofAgent8["DTV_BB_VOIP_IPTV"][0]==Actual_KPIofAgent8["DTV_BB_VOIP_IPTV"][0]#0 is KPI value
            assert Expected_KPIofAgent8["DTV_BB_VOIP_IPTV"][1]==Actual_KPIofAgent8["DTV_BB_VOIP_IPTV"][1]#1 is KPI status
            assert Expected_KPIofAgent8["Achiev"][0]==Actual_KPIofAgent8["Achiev"][0]#0 is KPI value
            assert Expected_KPIofAgent8["Achiev"][1]==Actual_KPIofAgent8["Achiev"][1]#1 is KPI status
    
    def Check_Agent11(self,Expected_KPIofAgent11,Actual_AgentKPI):
        #Step6:Verify Agent11:check each KPI value, color.
        print "=================6.Verify Agent11:check each KPI value, color=============="
        #Step6.1:Get the Expected KPI value and color for Agent8
        print "=================6.1 Expected KPI value and color of Agent11=============="
        print Expected_KPIofAgent11
        #Step6.2:Get the Actual KPI and color for Agent8
        print "=================6.2 Actual KPI value and color of Agent11=============="
        Actual_KPIofAgent11=Actual_AgentKPI['Agent 11']
        print Actual_KPIofAgent11
        assert Expected_KPIofAgent11["VOC_Number"][0]==Actual_KPIofAgent11["VOC_Number"][0]#0 is KPI value
        assert Expected_KPIofAgent11["VOC_Number"][1]==Actual_KPIofAgent11["VOC_Number"][1]#1 is KPI status
        assert Expected_KPIofAgent11["VOC_OverallScore"][0]==Actual_KPIofAgent11["VOC_OverallScore"][0]#0 is KPI value
        assert Expected_KPIofAgent11["VOC_OverallScore"][1]==Actual_KPIofAgent11["VOC_OverallScore"][1]#1 is KPI status
        assert Expected_KPIofAgent11["SevenDayRepeats_Repeats"][0]==Actual_KPIofAgent11["SevenDayRepeats_Repeats"][0]#0 is KPI value
        assert Expected_KPIofAgent11["SevenDayRepeats_Repeats"][1]==Actual_KPIofAgent11["SevenDayRepeats_Repeats"][1]#1 is KPI status
        assert Expected_KPIofAgent11["SevenDayRepeats_ManagedCalls"][0]==Actual_KPIofAgent11["SevenDayRepeats_ManagedCalls"][0]#0 is KPI value
        assert Expected_KPIofAgent11["SevenDayRepeats_ManagedCalls"][1]==Actual_KPIofAgent11["SevenDayRepeats_ManagedCalls"][1]#1 is KPI status
        assert Expected_KPIofAgent11["SevenDayRepeats_RepeatRate"][0]==Actual_KPIofAgent11["SevenDayRepeats_RepeatRate"][0]#0 is KPI value
        assert Expected_KPIofAgent11["SevenDayRepeats_RepeatRate"][1]==Actual_KPIofAgent11["SevenDayRepeats_RepeatRate"][1]#1 is KPI status
        assert Expected_KPIofAgent11["Productivity_AHT"][0]==Actual_KPIofAgent11["Productivity_AHT"][0]#0 is KPI value
        assert Expected_KPIofAgent11["Productivity_AHT"][1]==Actual_KPIofAgent11["Productivity_AHT"][1]#1 is KPI status
        assert Expected_KPIofAgent11["Transfers"][0]==Actual_KPIofAgent11["Transfers"][0]#0 is KPI value
        assert Expected_KPIofAgent11["Transfers"][1]==Actual_KPIofAgent11["Transfers"][1]#1 is KPI status
        assert Expected_KPIofAgent11["Adjustment"][0]==Actual_KPIofAgent11["Adjustment"][0]#0 is KPI value
        assert Expected_KPIofAgent11["Adjustment"][1]==Actual_KPIofAgent11["Adjustment"][1]#1 is KPI status
        assert Expected_KPIofAgent11["AdjustmentPerCall"][0]==Actual_KPIofAgent11["AdjustmentPerCall"][0]#0 is KPI value
        assert Expected_KPIofAgent11["AdjustmentPerCall"][1]==Actual_KPIofAgent11["AdjustmentPerCall"][1]#1 is KPI status
        assert Expected_KPIofAgent11["Wireless"][0]==Actual_KPIofAgent11["Wireless"][0]#0 is KPI value
        assert Expected_KPIofAgent11["Wireless"][1]==Actual_KPIofAgent11["Wireless"][1]#1 is KPI status
        assert Expected_KPIofAgent11["Broadband"][0]==Actual_KPIofAgent11["Broadband"][0]#0 is KPI value
        assert Expected_KPIofAgent11["Broadband"][1]==Actual_KPIofAgent11["Broadband"][1]#1 is KPI status
        assert Expected_KPIofAgent11["DTV"][0]==Actual_KPIofAgent11["DTV"][0]#0 is KPI value
        assert Expected_KPIofAgent11["DTV"][1]==Actual_KPIofAgent11["DTV"][1]#1 is KPI status
        assert Expected_KPIofAgent11["DTV_BB_VOIP_IPTV"][0]==Actual_KPIofAgent11["DTV_BB_VOIP_IPTV"][0]#0 is KPI value
        assert Expected_KPIofAgent11["DTV_BB_VOIP_IPTV"][1]==Actual_KPIofAgent11["DTV_BB_VOIP_IPTV"][1]#1 is KPI status
        assert Expected_KPIofAgent11["Achiev"][0]==Actual_KPIofAgent11["Achiev"][0]#0 is KPI value
        assert Expected_KPIofAgent11["Achiev"][1]==Actual_KPIofAgent11["Achiev"][1]#1 is KPI status
    