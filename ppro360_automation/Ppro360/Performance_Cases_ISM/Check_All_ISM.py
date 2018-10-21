'''
Created on 2018.8.14

@author: Sissi.liu
'''

from Tablet_pages.PerformancPage import PerformancePage
from Performance_Cases_ISM.Get_PerformanceData_Actual_ISM import Get_PerformanceData_Actual_ISM

class Check_All_ISM(object):



    def __init__(self):
        '''
        Constructor
        '''
        self.kpikey=['NumberOfSurveys','OverallScore','eg7d_Calls','eg7d_Transfers','eg7d_OneAndDone7Day','eg7d_Rpt7Day','eg7d_7DREPEATS','AHT',
                     'Transfers','Hold','Adjustments','Wireless','Broadband','Achiev']
        self.agent_list=["Agent 1","Agent 2","Agent 3","Agent 4","Agent 5","Agent 6","Agent 7","Agent 8","Agent 9","Agent 10","Agent 11"]
        
        
    def Check_Goal(self,Expected_GoalDic,Actual_GoalDic):
        for key in self.kpikey:
            assert Actual_GoalDic[key]==Expected_GoalDic[key],"KPI of Goal:Actual %s doesn't equal Expected %s!"%(Actual_GoalDic[key],Expected_GoalDic[key])

     
    def Check_TL1Achive(self,Expected_KPIofTl1): 
        Ppage=PerformancePage()
        GetPData_Actual=Get_PerformanceData_Actual_ISM()
        
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
                Actual_Achiev_TL1=GetPData_Actual.get_ISM_TL_KPI_Actual(lineindex)["Achiev"][0]
                Tl1_line=lineindex#For Step4
                break
            lineindex=lineindex+1
            flag=Ppage.TL_line_exist(lineindex)

        
        #Step3.3:assert Expected==Actual
        assert Actual_Achiev_TL1==Expected_Achi_Tl1,"TL1's achievement:Actual %s doesn't equal Expected %s!"%(Actual_Achiev_TL1,Expected_Achi_Tl1)        
        '''Actual_Achiev_TL1'''
        return Tl1_line
    
    
    def Check_AllAgentofTL1(self,Tl1_line,TimeTab,Expected_AgentAchiev):
        Ppage=PerformancePage()
        GetPData_Actual=Get_PerformanceData_Actual_ISM()
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
            Agent_Achiev=Ppage.get_anyKPIofAgent_OM(TLindex, Agentindex, 15)[0]
            Actual_AgentAchiev[Agent_Name]=Agent_Achiev
            if Agent_Name=='Agent 8' or Agent_Name=='Agent 11':
                Agent_KPI=GetPData_Actual.get_ISM_Agent_KPI_Actual(TLindex, Agentindex)
                Actual_AgentKPI[Agent_Name]=Agent_KPI#For Step5 and Step6
            Agentindex=Agentindex+1
            flag=Ppage.Agent_line_exist_OM(TLindex, Agentindex)
           
        print "=================4.Actual_All Agents' Achiev of Tl1=============="
        print Agentindex
        print Actual_AgentAchiev
        #Step4.3:assert Expected==Actual
        for key in self.agent_list:
            if TimeTab!="LastTwoMonth":
                assert Expected_AgentAchiev[key][0]==Actual_AgentAchiev[key][0], "%s Achiev of tl1- %s:Actual %s doesn't equal Expected %s!"%(TimeTab,key,Expected_AgentAchiev[key][0],Actual_AgentAchiev[key][0])
            else:
                assert Expected_AgentAchiev["Agent 9"][0]==Actual_AgentAchiev["Agent 9"][0], "%s Achiev of tl1- Agent 9:Actual %s doesn't equal Expected %s!"%(TimeTab,Expected_AgentAchiev[key][0],Actual_AgentAchiev[key][0])
                assert Expected_AgentAchiev["Agent 10"][0]==Actual_AgentAchiev["Agent 10"][0], "%s Achiev of tl1- Agent 10:Actual %s doesn't equal Expected %s!"%(TimeTab,Expected_AgentAchiev[key][0],Actual_AgentAchiev[key][0])
                assert Expected_AgentAchiev["Agent 11"][0]==Actual_AgentAchiev["Agent 11"][0], "%s Achiev of tl1- Agent 11:Actual %s doesn't equal Expected %s!"%(TimeTab,Expected_AgentAchiev[key][0],Actual_AgentAchiev[key][0])
        
        return Actual_AgentKPI
    
    
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
            
            for key in self.kpikey:
                #0 is KPI value
                assert Actual_KPIofAgent8[key][0]==Expected_KPIofAgent8[key][0],"KPI %s of Agent8:Actual %s doesn't equal Expected %s!"%(key,Actual_KPIofAgent8[key][0],Expected_KPIofAgent8[key][0])
                #1 is KPI status
                assert Actual_KPIofAgent8[key][1]==Expected_KPIofAgent8[key][1],"KPI status %s of Agent8:Actual %s doesn't equal Expected %s!"%(key,Actual_KPIofAgent8[key][0],Expected_KPIofAgent8[key][0]) 
    
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
        
        for key in self.kpikey:
            #0 is KPI value
            assert Actual_KPIofAgent11[key][0]==Expected_KPIofAgent11[key][0],"KPI %s of Agent8:Actual %s doesn't equal Expected %s!"%(key,Actual_KPIofAgent11[key][0],Expected_KPIofAgent11[key][0])
            #1 is KPI status
            assert Actual_KPIofAgent11[key][1]==Expected_KPIofAgent11[key][1],"KPI status %s of Agent8:Actual %s doesn't equal Expected %s!"%(key,Actual_KPIofAgent11[key][0],Expected_KPIofAgent11[key][0]) 
    
            