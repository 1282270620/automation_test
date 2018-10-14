'''
Created on Apr 10, 2018

@author: symbio
'''
from Tablet_pages.PerformancPage import PerformancePage
from Performance_Cases_MOVERS.Get_PerformanceData_Actual_MOVERS import Get_PerformanceData_Actual_MOVERS

class Check_All_MOVERS(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    def Check_Goal(self,Expected_GoalDic,Actual_GoalDic):
        print Expected_GoalDic
        for key in Actual_GoalDic:
            if key in ["BroadbandGrossSales","MobilityGrossSales","DTVNowActivations"]:
                Actual_GoalDic[key]=Actual_GoalDic[key].split("\n")
                #Actual_GoalDic[key][1]=Actual_GoalDic[key][1][1:-1]
        #print Actual_GoalDic
        assert Expected_GoalDic["LoyaltyRate"]==Actual_GoalDic["LoyaltyRate"]
        assert Expected_GoalDic["BroadbandGrossSales"]==Actual_GoalDic["BroadbandGrossSales"]
        assert Expected_GoalDic["DisconnectRate"]==Actual_GoalDic["DisconnectRate"]
        assert Expected_GoalDic["VOC"]==Actual_GoalDic["VOC"]
        assert Expected_GoalDic["MobilityGrossSales"]==Actual_GoalDic["MobilityGrossSales"]
        assert Expected_GoalDic["DTVNowActivations"]==Actual_GoalDic["DTVNowActivations"]
        assert Expected_GoalDic["AHT"]==Actual_GoalDic["AHT"]
        assert Expected_GoalDic["B2P"]==Actual_GoalDic["B2P"]
        assert Expected_GoalDic["ABS"]==Actual_GoalDic["ABS"]
        assert Expected_GoalDic["Achiev"]==Actual_GoalDic["Achiev"]
    def Check_Site(self,Expected_KPIofSITEDic,Actual_KPIofSITEDic):
        #Step2:Verify KPI of SITES
        print "=================2.Verify Each KPI of site, color, achievement=============="
        '''Expected_KPIofSITEDic is from above.'''
        print Expected_KPIofSITEDic
        #Step2.2:Get the Actual KPI of site
        '''Expected_KPIofSITEDic is from blow.''' 
        
        print Actual_KPIofSITEDic
        for key in Actual_KPIofSITEDic:
            if key in ["BroadbandGrossSales","MobilityGrossSales","DTVNowActivations"]:
                Actual_KPIofSITEDic[key][0]=Actual_KPIofSITEDic[key][0].split("\n")
                Actual_KPIofSITEDic[key][0][1]=Actual_KPIofSITEDic[key][0][1][1:-1]
        assert Expected_KPIofSITEDic["LoyaltyRate"][0]==Actual_KPIofSITEDic["LoyaltyRate"][0]#0 is KPI value
        assert Expected_KPIofSITEDic["LoyaltyRate"][1]==Actual_KPIofSITEDic["LoyaltyRate"][1]#1 is KPI status
        assert Expected_KPIofSITEDic["BroadbandGrossSales"][0]==Actual_KPIofSITEDic["BroadbandGrossSales"][0]#0 is KPI value
        assert Expected_KPIofSITEDic["BroadbandGrossSales"][1]==Actual_KPIofSITEDic["BroadbandGrossSales"][1]#1 is KPI status
        assert Expected_KPIofSITEDic["DisconnectRate"][0]==Actual_KPIofSITEDic["DisconnectRate"][0]#0 is KPI value
        assert Expected_KPIofSITEDic["DisconnectRate"][1]==Actual_KPIofSITEDic["DisconnectRate"][1]#1 is KPI status
        assert Expected_KPIofSITEDic["VOC"][0]==Actual_KPIofSITEDic["VOC"][0]#0 is KPI value
        assert Expected_KPIofSITEDic["VOC"][1]==Actual_KPIofSITEDic["VOC"][1]#1 is KPI status
        assert Expected_KPIofSITEDic["MobilityGrossSales"][0]==Actual_KPIofSITEDic["MobilityGrossSales"][0]#0 is KPI value
        assert Expected_KPIofSITEDic["MobilityGrossSales"][1]==Actual_KPIofSITEDic["MobilityGrossSales"][1]#1 is KPI status
        assert Expected_KPIofSITEDic["DTVNowActivations"][0]==Actual_KPIofSITEDic["DTVNowActivations"][0]#0 is KPI value
        assert Expected_KPIofSITEDic["DTVNowActivations"][1]==Actual_KPIofSITEDic["DTVNowActivations"][1]#1 is KPI status
        assert Expected_KPIofSITEDic["AHT"][0]==Actual_KPIofSITEDic["AHT"][0]#0 is KPI value
        assert Expected_KPIofSITEDic["AHT"][1]==Actual_KPIofSITEDic["AHT"][1]#1 is KPI status
        assert Expected_KPIofSITEDic["B2P"][0]==Actual_KPIofSITEDic["B2P"][0]#0 is KPI value
        assert Expected_KPIofSITEDic["B2P"][1]==Actual_KPIofSITEDic["B2P"][1]#1 is KPI status
        assert Expected_KPIofSITEDic["ABS"][0]==Actual_KPIofSITEDic["ABS"][0]#0 is KPI value
        assert Expected_KPIofSITEDic["ABS"][1]==Actual_KPIofSITEDic["ABS"][1]#1 is KPI status
        assert Expected_KPIofSITEDic["Achiev"][0]==Actual_KPIofSITEDic["Achiev"][0]#0 is KPI value
        assert Expected_KPIofSITEDic["Achiev"][1]==Actual_KPIofSITEDic["Achiev"][1]#1 is KPI status
        
    def Check_TL1Achive(self,Expected_KPIofTl1):
        Ppage=PerformancePage()
        GetPData_Actual=Get_PerformanceData_Actual_MOVERS()
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
                Actual_Achiev_TL1=GetPData_Actual.get_MOVERS_TL_KPI_Actual(lineindex)["Achiev"][0]
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
        GetPData_Actual=Get_PerformanceData_Actual_MOVERS()
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
                Agent_KPI=GetPData_Actual.get_MOVERS_Agent_KPI_Actual(TLindex, Agentindex)
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
            assert Expected_KPIofAgent8["LoyaltyRate"][0]==Actual_KPIofAgent8["LoyaltyRate"][0]#0 is KPI value
            assert Expected_KPIofAgent8["LoyaltyRate"][1]==Actual_KPIofAgent8["LoyaltyRate"][1]#1 is KPI status
            assert Expected_KPIofAgent8["BroadbandGrossSales"][0]==Actual_KPIofAgent8["BroadbandGrossSales"][0]#0 is KPI value
            assert Expected_KPIofAgent8["BroadbandGrossSales"][1]==Actual_KPIofAgent8["BroadbandGrossSales"][1]#1 is KPI status
            assert Expected_KPIofAgent8["DisconnectRate"][0]==Actual_KPIofAgent8["DisconnectRate"][0]#0 is KPI value
            assert Expected_KPIofAgent8["DisconnectRate"][1]==Actual_KPIofAgent8["DisconnectRate"][1]#1 is KPI status
            assert Expected_KPIofAgent8["VOC"][0]==Actual_KPIofAgent8["VOC"][0]#0 is KPI value
            assert Expected_KPIofAgent8["VOC"][1]==Actual_KPIofAgent8["VOC"][1]#1 is KPI status
            assert Expected_KPIofAgent8["MobilityGrossSales"][0]==Actual_KPIofAgent8["MobilityGrossSales"][0]#0 is KPI value
            assert Expected_KPIofAgent8["MobilityGrossSales"][1]==Actual_KPIofAgent8["MobilityGrossSales"][1]#1 is KPI status
            assert Expected_KPIofAgent8["DTVNowActivations"][0]==Actual_KPIofAgent8["DTVNowActivations"][0]#0 is KPI value
            assert Expected_KPIofAgent8["DTVNowActivations"][1]==Actual_KPIofAgent8["DTVNowActivations"][1]#1 is KPI status
            assert Expected_KPIofAgent8["AHT"][0]==Actual_KPIofAgent8["AHT"][0]#0 is KPI value
            assert Expected_KPIofAgent8["AHT"][1]==Actual_KPIofAgent8["AHT"][1]#1 is KPI status
            assert Expected_KPIofAgent8["B2P"][0]==Actual_KPIofAgent8["B2P"][0]#0 is KPI value
            assert Expected_KPIofAgent8["B2P"][1]==Actual_KPIofAgent8["B2P"][1]#1 is KPI status
            assert Expected_KPIofAgent8["ABS"][0]==Actual_KPIofAgent8["ABS"][0]#0 is KPI value
            assert Expected_KPIofAgent8["ABS"][1]==Actual_KPIofAgent8["ABS"][1]#1 is KPI status
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
        assert Expected_KPIofAgent11["LoyaltyRate"][0]==Actual_KPIofAgent11["LoyaltyRate"][0]#0 is KPI value
        assert Expected_KPIofAgent11["LoyaltyRate"][1]==Actual_KPIofAgent11["LoyaltyRate"][1]#1 is KPI status
        assert Expected_KPIofAgent11["BroadbandGrossSales"][0]==Actual_KPIofAgent11["BroadbandGrossSales"][0]#0 is KPI value
        assert Expected_KPIofAgent11["BroadbandGrossSales"][1]==Actual_KPIofAgent11["BroadbandGrossSales"][1]#1 is KPI status
        assert Expected_KPIofAgent11["DisconnectRate"][0]==Actual_KPIofAgent11["DisconnectRate"][0]#0 is KPI value
        assert Expected_KPIofAgent11["DisconnectRate"][1]==Actual_KPIofAgent11["DisconnectRate"][1]#1 is KPI status
        assert Expected_KPIofAgent11["VOC"][0]==Actual_KPIofAgent11["VOC"][0]#0 is KPI value
        assert Expected_KPIofAgent11["VOC"][1]==Actual_KPIofAgent11["VOC"][1]#1 is KPI status
        assert Expected_KPIofAgent11["MobilityGrossSales"][0]==Actual_KPIofAgent11["MobilityGrossSales"][0]#0 is KPI value
        assert Expected_KPIofAgent11["MobilityGrossSales"][1]==Actual_KPIofAgent11["MobilityGrossSales"][1]#1 is KPI status
        assert Expected_KPIofAgent11["DTVNowActivations"][0]==Actual_KPIofAgent11["DTVNowActivations"][0]#0 is KPI value
        assert Expected_KPIofAgent11["DTVNowActivations"][1]==Actual_KPIofAgent11["DTVNowActivations"][1]#1 is KPI status
        assert Expected_KPIofAgent11["AHT"][0]==Actual_KPIofAgent11["AHT"][0]#0 is KPI value
        assert Expected_KPIofAgent11["AHT"][1]==Actual_KPIofAgent11["AHT"][1]#1 is KPI status
        assert Expected_KPIofAgent11["B2P"][0]==Actual_KPIofAgent11["B2P"][0]#0 is KPI value
        assert Expected_KPIofAgent11["B2P"][1]==Actual_KPIofAgent11["B2P"][1]#1 is KPI status
        assert Expected_KPIofAgent11["ABS"][0]==Actual_KPIofAgent11["ABS"][0]#0 is KPI value
        assert Expected_KPIofAgent11["ABS"][1]==Actual_KPIofAgent11["ABS"][1]#1 is KPI status
        assert Expected_KPIofAgent11["Achiev"][0]==Actual_KPIofAgent11["Achiev"][0]#0 is KPI value
        assert Expected_KPIofAgent11["Achiev"][1]==Actual_KPIofAgent11["Achiev"][1]#1 is KPI status
    