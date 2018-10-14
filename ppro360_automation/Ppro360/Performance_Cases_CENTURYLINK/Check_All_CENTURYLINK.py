'''
Created on Apr 10, 2018

@author: symbio
'''
from Tablet_pages.PerformancPage import PerformancePage
from Performance_Cases_CENTURYLINK.Get_PerformanceData_Actual_CENTURYLINK import Get_PerformanceData_Actual_CENTURYLINK
class Check_All_CENTURYLINK(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    def Check_Goal(self,Expected_GoalDic,Actual_GoalDic):
        assert Expected_GoalDic["AttainmenttoGoal_HSI"]==Actual_GoalDic["AttainmenttoGoal_HSI"]
        assert Expected_GoalDic["B2P"]==Actual_GoalDic["B2P"]
        assert Expected_GoalDic["AHT"]==Actual_GoalDic["AHT"]
        assert Expected_GoalDic["Hold"]==Actual_GoalDic["Hold"]
        assert Expected_GoalDic["AbsAbsenteeism"]==Actual_GoalDic["AbsAbsenteeism"]
        assert Expected_GoalDic["AvgQAScore"]==Actual_GoalDic["AvgQAScore"]
        assert Expected_GoalDic["QACalls"]==Actual_GoalDic["QACalls"]
        assert Expected_GoalDic["ofAutoFails"]==Actual_GoalDic["ofAutoFails"]
        assert Expected_GoalDic["MixClose_HSI"]==Actual_GoalDic["MixClose_HSI"]
        assert Expected_GoalDic["AttainmenttoGoal_HSI"]==Actual_GoalDic["AttainmenttoGoal_HSI"]
        assert Expected_GoalDic["MixClose_TV"]==Actual_GoalDic["MixClose_TV"]
        assert Expected_GoalDic["AttainmenttoGoal_TV"]==Actual_GoalDic["AttainmenttoGoal_TV"]
        assert Expected_GoalDic["AttachRate_DTV"]==Actual_GoalDic["AttachRate_DTV"]
        assert Expected_GoalDic["MixClose_PhoneLines"]==Actual_GoalDic["MixClose_PhoneLines"]
        assert Expected_GoalDic["MixClose_Ease"]==Actual_GoalDic["MixClose_Ease"]
        assert Expected_GoalDic["ACDCalls"]==Actual_GoalDic["ACDCalls"]
        assert Expected_GoalDic["AHTIneligible"]==Actual_GoalDic["AHTIneligible"]
        assert Expected_GoalDic["QualifiedCloseRate"]==Actual_GoalDic["QualifiedCloseRate"]
    def Check_Site(self,Expected_KPIofSITEDic,Actual_KPIofSITEDic):
        #Step2:Verify KPI of SITES
        print "=================2.Verify Each KPI of site, color, achievement=============="
        '''Expected_KPIofSITEDic is from above.'''
        print Expected_KPIofSITEDic
        #Step2.2:Get the Actual KPI of site
        '''Expected_KPIofSITEDic is from blow.''' 
        
        print Actual_KPIofSITEDic
        assert Expected_KPIofSITEDic["AttainmenttoGoal_HSI"][0]==Actual_KPIofSITEDic["AttainmenttoGoal_HSI"][0]#0 is KPI value
        assert Expected_KPIofSITEDic["AttainmenttoGoal_HSI"][1]==Actual_KPIofSITEDic["AttainmenttoGoal_HSI"][1]#1 is KPI status
        assert Expected_KPIofSITEDic["B2P"][0]==Actual_KPIofSITEDic["B2P"][0]#0 is KPI value
        assert Expected_KPIofSITEDic["B2P"][1]==Actual_KPIofSITEDic["B2P"][1]#1 is KPI status
        assert Expected_KPIofSITEDic["AHT"][0]==Actual_KPIofSITEDic["AHT"][0]#0 is KPI value
        assert Expected_KPIofSITEDic["AHT"][1]==Actual_KPIofSITEDic["AHT"][1]#1 is KPI status
        assert Expected_KPIofSITEDic["Hold"][0]==Actual_KPIofSITEDic["Hold"][0]#0 is KPI value
        assert Expected_KPIofSITEDic["Hold"][1]==Actual_KPIofSITEDic["Hold"][1]#1 is KPI status
        assert Expected_KPIofSITEDic["AbsAbsenteeism"][0]==Actual_KPIofSITEDic["AbsAbsenteeism"][0]#0 is KPI value
        assert Expected_KPIofSITEDic["AbsAbsenteeism"][1]==Actual_KPIofSITEDic["AbsAbsenteeism"][1]#1 is KPI status
        assert Expected_KPIofSITEDic["AvgQAScore"][0]==Actual_KPIofSITEDic["AvgQAScore"][0]#0 is KPI value
        assert Expected_KPIofSITEDic["AvgQAScore"][1]==Actual_KPIofSITEDic["AvgQAScore"][1]#1 is KPI status
        assert Expected_KPIofSITEDic["QACalls"][0]==Actual_KPIofSITEDic["QACalls"][0]#0 is KPI value
        assert Expected_KPIofSITEDic["QACalls"][1]==Actual_KPIofSITEDic["QACalls"][1]#1 is KPI status
        assert Expected_KPIofSITEDic["ofAutoFails"][0]==Actual_KPIofSITEDic["ofAutoFails"][0]#0 is KPI value
        assert Expected_KPIofSITEDic["ofAutoFails"][1]==Actual_KPIofSITEDic["ofAutoFails"][1]#1 is KPI status
        assert Expected_KPIofSITEDic["MixClose_HSI"][0]==Actual_KPIofSITEDic["MixClose_HSI"][0]#0 is KPI value
        assert Expected_KPIofSITEDic["MixClose_HSI"][1]==Actual_KPIofSITEDic["MixClose_HSI"][1]#1 is KPI status
        assert Expected_KPIofSITEDic["AttainmenttoGoal_HSI"][0]==Actual_KPIofSITEDic["AttainmenttoGoal_HSI"][0]#0 is KPI value
        assert Expected_KPIofSITEDic["AttainmenttoGoal_HSI"][1]==Actual_KPIofSITEDic["AttainmenttoGoal_HSI"][1]#1 is KPI status
        assert Expected_KPIofSITEDic["MixClose_TV"][0]==Actual_KPIofSITEDic["MixClose_TV"][0]#0 is KPI value
        assert Expected_KPIofSITEDic["MixClose_TV"][1]==Actual_KPIofSITEDic["MixClose_TV"][1]#1 is KPI status
        assert Expected_KPIofSITEDic["AttainmenttoGoal_TV"][0]==Actual_KPIofSITEDic["AttainmenttoGoal_TV"][0]#0 is KPI value
        assert Expected_KPIofSITEDic["AttainmenttoGoal_TV"][1]==Actual_KPIofSITEDic["AttainmenttoGoal_TV"][1]#1 is KPI status
        assert Expected_KPIofSITEDic["AttachRate_DTV"][0]==Actual_KPIofSITEDic["AttachRate_DTV"][0]#0 is KPI value
        assert Expected_KPIofSITEDic["AttachRate_DTV"][1]==Actual_KPIofSITEDic["AttachRate_DTV"][1]#1 is KPI status
        assert Expected_KPIofSITEDic["MixClose_PhoneLines"][0]==Actual_KPIofSITEDic["MixClose_PhoneLines"][0]#0 is KPI value
        assert Expected_KPIofSITEDic["MixClose_PhoneLines"][1]==Actual_KPIofSITEDic["MixClose_PhoneLines"][1]#1 is KPI status
        assert Expected_KPIofSITEDic["MixClose_Ease"][0]==Actual_KPIofSITEDic["MixClose_Ease"][0]#0 is KPI value
        assert Expected_KPIofSITEDic["MixClose_Ease"][1]==Actual_KPIofSITEDic["MixClose_Ease"][1]#1 is KPI status
        assert Expected_KPIofSITEDic["ACDCalls"][0]==Actual_KPIofSITEDic["ACDCalls"][0]#0 is KPI value
        assert Expected_KPIofSITEDic["ACDCalls"][1]==Actual_KPIofSITEDic["ACDCalls"][1]#1 is KPI status
        assert Expected_KPIofSITEDic["AHTIneligible"][0]==Actual_KPIofSITEDic["AHTIneligible"][0]#0 is KPI value
        assert Expected_KPIofSITEDic["AHTIneligible"][1]==Actual_KPIofSITEDic["AHTIneligible"][1]#1 is KPI status
        assert Expected_KPIofSITEDic["QualifiedCloseRate"][0]==Actual_KPIofSITEDic["QualifiedCloseRate"][0]#0 is KPI value
        assert Expected_KPIofSITEDic["QualifiedCloseRate"][1]==Actual_KPIofSITEDic["QualifiedCloseRate"][1]#1 is KPI status
        assert Expected_KPIofSITEDic["Achiev"][0]==Actual_KPIofSITEDic["Achiev"][0]#0 is KPI value   
        
    def Check_TL1Achive(self,Expected_KPIofTl1):
        Ppage=PerformancePage()
        GetPData_Actual=Get_PerformanceData_Actual_CENTURYLINK()
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
                Actual_Achiev_TL1=GetPData_Actual.get_CENTURYLINK_TL_KPI_Actual(lineindex)["Achiev"][0]
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
        GetPData_Actual=Get_PerformanceData_Actual_CENTURYLINK()
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
            Agent_Achiev=Ppage.get_anyKPIofAgent_OM(TLindex, Agentindex, 20)[0]
            Actual_AgentAchiev[Agent_Name]=Agent_Achiev
            if Agent_Name=='Agent 8' or Agent_Name=='Agent 11':
                Agent_KPI=GetPData_Actual.get_CENTURYLINK_Agent_KPI_Actual(TLindex, Agentindex)
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
            assert Expected_KPIofAgent8["AttainmenttoGoal_HSI"][0]==Actual_KPIofAgent8["AttainmenttoGoal_HSI"][0]#0 is KPI value
            assert Expected_KPIofAgent8["AttainmenttoGoal_HSI"][1]==Actual_KPIofAgent8["AttainmenttoGoal_HSI"][1]#1 is KPI status
            assert Expected_KPIofAgent8["B2P"][0]==Actual_KPIofAgent8["B2P"][0]#0 is KPI value
            assert Expected_KPIofAgent8["B2P"][1]==Actual_KPIofAgent8["B2P"][1]#1 is KPI status
            assert Expected_KPIofAgent8["AHT"][0]==Actual_KPIofAgent8["AHT"][0]#0 is KPI value
            assert Expected_KPIofAgent8["AHT"][1]==Actual_KPIofAgent8["AHT"][1]#1 is KPI status
            assert Expected_KPIofAgent8["Hold"][0]==Actual_KPIofAgent8["Hold"][0]#0 is KPI value
            assert Expected_KPIofAgent8["Hold"][1]==Actual_KPIofAgent8["Hold"][1]#1 is KPI status
            assert Expected_KPIofAgent8["AbsAbsenteeism"][0]==Actual_KPIofAgent8["AbsAbsenteeism"][0]#0 is KPI value
            assert Expected_KPIofAgent8["AbsAbsenteeism"][1]==Actual_KPIofAgent8["AbsAbsenteeism"][1]#1 is KPI status
            assert Expected_KPIofAgent8["AvgQAScore"][0]==Actual_KPIofAgent8["AvgQAScore"][0]#0 is KPI value
            assert Expected_KPIofAgent8["AvgQAScore"][1]==Actual_KPIofAgent8["AvgQAScore"][1]#1 is KPI status
            assert Expected_KPIofAgent8["QACalls"][0]==Actual_KPIofAgent8["QACalls"][0]#0 is KPI value
            assert Expected_KPIofAgent8["QACalls"][1]==Actual_KPIofAgent8["QACalls"][1]#1 is KPI status
            assert Expected_KPIofAgent8["ofAutoFails"][0]==Actual_KPIofAgent8["ofAutoFails"][0]#0 is KPI value
            assert Expected_KPIofAgent8["ofAutoFails"][1]==Actual_KPIofAgent8["ofAutoFails"][1]#1 is KPI status
            assert Expected_KPIofAgent8["MixClose_HSI"][0]==Actual_KPIofAgent8["MixClose_HSI"][0]#0 is KPI value
            assert Expected_KPIofAgent8["MixClose_HSI"][1]==Actual_KPIofAgent8["MixClose_HSI"][1]#1 is KPI status
            assert Expected_KPIofAgent8["AttainmenttoGoal_HSI"][0]==Actual_KPIofAgent8["AttainmenttoGoal_HSI"][0]#0 is KPI value
            assert Expected_KPIofAgent8["AttainmenttoGoal_HSI"][1]==Actual_KPIofAgent8["AttainmenttoGoal_HSI"][1]#1 is KPI status
            assert Expected_KPIofAgent8["MixClose_TV"][0]==Actual_KPIofAgent8["MixClose_TV"][0]#0 is KPI value
            assert Expected_KPIofAgent8["MixClose_TV"][1]==Actual_KPIofAgent8["MixClose_TV"][1]#1 is KPI status
            assert Expected_KPIofAgent8["AttainmenttoGoal_TV"][0]==Actual_KPIofAgent8["AttainmenttoGoal_TV"][0]#0 is KPI value
            assert Expected_KPIofAgent8["AttainmenttoGoal_TV"][1]==Actual_KPIofAgent8["AttainmenttoGoal_TV"][1]#1 is KPI status
            assert Expected_KPIofAgent8["AttachRate_DTV"][0]==Actual_KPIofAgent8["AttachRate_DTV"][0]#0 is KPI value
            assert Expected_KPIofAgent8["AttachRate_DTV"][1]==Actual_KPIofAgent8["AttachRate_DTV"][1]#1 is KPI status
            assert Expected_KPIofAgent8["MixClose_PhoneLines"][0]==Actual_KPIofAgent8["MixClose_PhoneLines"][0]#0 is KPI value
            assert Expected_KPIofAgent8["MixClose_PhoneLines"][1]==Actual_KPIofAgent8["MixClose_PhoneLines"][1]#1 is KPI status
            assert Expected_KPIofAgent8["MixClose_Ease"][0]==Actual_KPIofAgent8["MixClose_Ease"][0]#0 is KPI value
            assert Expected_KPIofAgent8["MixClose_Ease"][1]==Actual_KPIofAgent8["MixClose_Ease"][1]#1 is KPI status
            assert Expected_KPIofAgent8["ACDCalls"][0]==Actual_KPIofAgent8["ACDCalls"][0]#0 is KPI value
            assert Expected_KPIofAgent8["ACDCalls"][1]==Actual_KPIofAgent8["ACDCalls"][1]#1 is KPI status
            assert Expected_KPIofAgent8["AHTIneligible"][0]==Actual_KPIofAgent8["AHTIneligible"][0]#0 is KPI value
            assert Expected_KPIofAgent8["AHTIneligible"][1]==Actual_KPIofAgent8["AHTIneligible"][1]#1 is KPI status
            assert Expected_KPIofAgent8["QualifiedCloseRate"][0]==Actual_KPIofAgent8["QualifiedCloseRate"][0]#0 is KPI value
            assert Expected_KPIofAgent8["QualifiedCloseRate"][1]==Actual_KPIofAgent8["QualifiedCloseRate"][1]#1 is KPI status
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
        assert Expected_KPIofAgent11["AttainmenttoGoal_HSI"][0]==Actual_KPIofAgent11["AttainmenttoGoal_HSI"][0]#0 is KPI value
        assert Expected_KPIofAgent11["AttainmenttoGoal_HSI"][1]==Actual_KPIofAgent11["AttainmenttoGoal_HSI"][1]#1 is KPI status
        assert Expected_KPIofAgent11["B2P"][0]==Actual_KPIofAgent11["B2P"][0]#0 is KPI value
        assert Expected_KPIofAgent11["B2P"][1]==Actual_KPIofAgent11["B2P"][1]#1 is KPI status
        assert Expected_KPIofAgent11["AHT"][0]==Actual_KPIofAgent11["AHT"][0]#0 is KPI value
        assert Expected_KPIofAgent11["AHT"][1]==Actual_KPIofAgent11["AHT"][1]#1 is KPI status
        assert Expected_KPIofAgent11["Hold"][0]==Actual_KPIofAgent11["Hold"][0]#0 is KPI value
        assert Expected_KPIofAgent11["Hold"][1]==Actual_KPIofAgent11["Hold"][1]#1 is KPI status
        assert Expected_KPIofAgent11["AbsAbsenteeism"][0]==Actual_KPIofAgent11["AbsAbsenteeism"][0]#0 is KPI value
        assert Expected_KPIofAgent11["AbsAbsenteeism"][1]==Actual_KPIofAgent11["AbsAbsenteeism"][1]#1 is KPI status
        assert Expected_KPIofAgent11["AvgQAScore"][0]==Actual_KPIofAgent11["AvgQAScore"][0]#0 is KPI value
        assert Expected_KPIofAgent11["AvgQAScore"][1]==Actual_KPIofAgent11["AvgQAScore"][1]#1 is KPI status
        assert Expected_KPIofAgent11["QACalls"][0]==Actual_KPIofAgent11["QACalls"][0]#0 is KPI value
        assert Expected_KPIofAgent11["QACalls"][1]==Actual_KPIofAgent11["QACalls"][1]#1 is KPI status
        assert Expected_KPIofAgent11["ofAutoFails"][0]==Actual_KPIofAgent11["ofAutoFails"][0]#0 is KPI value
        assert Expected_KPIofAgent11["ofAutoFails"][1]==Actual_KPIofAgent11["ofAutoFails"][1]#1 is KPI status
        assert Expected_KPIofAgent11["MixClose_HSI"][0]==Actual_KPIofAgent11["MixClose_HSI"][0]#0 is KPI value
        assert Expected_KPIofAgent11["MixClose_HSI"][1]==Actual_KPIofAgent11["MixClose_HSI"][1]#1 is KPI status
        assert Expected_KPIofAgent11["AttainmenttoGoal_HSI"][0]==Actual_KPIofAgent11["AttainmenttoGoal_HSI"][0]#0 is KPI value
        assert Expected_KPIofAgent11["AttainmenttoGoal_HSI"][1]==Actual_KPIofAgent11["AttainmenttoGoal_HSI"][1]#1 is KPI status
        assert Expected_KPIofAgent11["MixClose_TV"][0]==Actual_KPIofAgent11["MixClose_TV"][0]#0 is KPI value
        assert Expected_KPIofAgent11["MixClose_TV"][1]==Actual_KPIofAgent11["MixClose_TV"][1]#1 is KPI status
        assert Expected_KPIofAgent11["AttainmenttoGoal_TV"][0]==Actual_KPIofAgent11["AttainmenttoGoal_TV"][0]#0 is KPI value
        assert Expected_KPIofAgent11["AttainmenttoGoal_TV"][1]==Actual_KPIofAgent11["AttainmenttoGoal_TV"][1]#1 is KPI status
        assert Expected_KPIofAgent11["AttachRate_DTV"][0]==Actual_KPIofAgent11["AttachRate_DTV"][0]#0 is KPI value
        assert Expected_KPIofAgent11["AttachRate_DTV"][1]==Actual_KPIofAgent11["AttachRate_DTV"][1]#1 is KPI status
        assert Expected_KPIofAgent11["MixClose_PhoneLines"][0]==Actual_KPIofAgent11["MixClose_PhoneLines"][0]#0 is KPI value
        assert Expected_KPIofAgent11["MixClose_PhoneLines"][1]==Actual_KPIofAgent11["MixClose_PhoneLines"][1]#1 is KPI status
        assert Expected_KPIofAgent11["MixClose_Ease"][0]==Actual_KPIofAgent11["MixClose_Ease"][0]#0 is KPI value
        assert Expected_KPIofAgent11["MixClose_Ease"][1]==Actual_KPIofAgent11["MixClose_Ease"][1]#1 is KPI status
        assert Expected_KPIofAgent11["ACDCalls"][0]==Actual_KPIofAgent11["ACDCalls"][0]#0 is KPI value
        assert Expected_KPIofAgent11["ACDCalls"][1]==Actual_KPIofAgent11["ACDCalls"][1]#1 is KPI status
        assert Expected_KPIofAgent11["AHTIneligible"][0]==Actual_KPIofAgent11["AHTIneligible"][0]#0 is KPI value
        assert Expected_KPIofAgent11["AHTIneligible"][1]==Actual_KPIofAgent11["AHTIneligible"][1]#1 is KPI status
        assert Expected_KPIofAgent11["QualifiedCloseRate"][0]==Actual_KPIofAgent11["QualifiedCloseRate"][0]#0 is KPI value
        assert Expected_KPIofAgent11["QualifiedCloseRate"][1]==Actual_KPIofAgent11["QualifiedCloseRate"][1]#1 is KPI status
        assert Expected_KPIofAgent11["Achiev"][0]==Actual_KPIofAgent11["Achiev"][0]#0 is KPI value
        assert Expected_KPIofAgent11["Achiev"][1]==Actual_KPIofAgent11["Achiev"][1]#1 is KPI status
    