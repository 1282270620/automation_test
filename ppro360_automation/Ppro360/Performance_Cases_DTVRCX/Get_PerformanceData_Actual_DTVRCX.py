'''
Created on Apr 7, 2017

@author: symbio
'''
from Tablet_pages.PerformancPage import PerformancePage
class Get_PerformanceData_Actual_DTVRCX():
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    def get_DTVRCX_Goal_Actual(self):
        Ppage=PerformancePage()
        CombinedGoalRate=Ppage.get_anyKPIValueOfTotal(1,2)[0]
        WBAttainmant=Ppage.get_anyKPIValueOfTotal(1,3)[0]
        CCTAttainmant=Ppage.get_anyKPIValueOfTotal(1,4)[0]
        DISCAttainmant=Ppage.get_anyKPIValueOfTotal(1,5)[0]
        IPBBGrossSales=Ppage.get_anyKPIValueOfTotal(1,6)[0]
        BroadbandAttachRate=Ppage.get_anyKPIValueOfTotal(1,7)[0]
        AgentSatisfaction=Ppage.get_anyKPIValueOfTotal(1,8)[0]
        Achiev=Ppage.get_anyKPIValueOfTotal(1,9)[0]
        Goal_KPI={"CombinedGoalRate":CombinedGoalRate,"WBAttainmant":WBAttainmant,"CCTAttainmant":CCTAttainmant,"DISCAttainmant":DISCAttainmant,"IPBBGrossSales":IPBBGrossSales,"BroadbandAttachRate":BroadbandAttachRate,"AgentSatisfaction":AgentSatisfaction,"Achiev":Achiev}
        return Goal_KPI
    def get_DTVRCX_SITE_Data_(self):#site:lineindex=2
        Ppage=PerformancePage()
        CombinedGoalRate=Ppage.get_anyKPIValueOfTotal(2,2)
        WBAttainmant=Ppage.get_anyKPIValueOfTotal(2,3)
        CCTAttainmant=Ppage.get_anyKPIValueOfTotal(2,4)
        DISCAttainmant=Ppage.get_anyKPIValueOfTotal(2,5)
        IPBBGrossSales=Ppage.get_anyKPIValueOfTotal(2,6)
        BroadbandAttachRate=Ppage.get_anyKPIValueOfTotal(2,7)
        AgentSatisfaction=Ppage.get_anyKPIValueOfTotal(2,8)
        Achiev=Ppage.get_anyKPIValueOfTotal(2,9)
        SITE_KPI={"CombinedGoalRate":CombinedGoalRate,"WBAttainmant":WBAttainmant,"CCTAttainmant":CCTAttainmant,"DISCAttainmant":DISCAttainmant,"IPBBGrossSales":IPBBGrossSales,"BroadbandAttachRate":BroadbandAttachRate,"AgentSatisfaction":AgentSatisfaction,"Achiev":Achiev}
        return SITE_KPI
	'''
    def get_DTVRCX_TEAM_Data_(self):#TEAM:lineindex=3
        Ppage=PerformancePage()
        CombinedGoalRate=Ppage.get_anyKPIValueOfTotal(3,2)
        WBAttainmant=Ppage.get_anyKPIValueOfTotal(3,3)
        CCTAttainmant=Ppage.get_anyKPIValueOfTotal(3,4)
        DISCAttainmant=Ppage.get_anyKPIValueOfTotal(3,5)
        IPBBGrossSales=Ppage.get_anyKPIValueOfTotal(3,6)
        BroadbandAttachRate=Ppage.get_anyKPIValueOfTotal(3,7)
        AgentSatisfaction=Ppage.get_anyKPIValueOfTotal(3,8)
        Achiev=Ppage.get_anyKPIValueOfTotal(3,9)
        TEAM_KPI={"CombinedGoalRate":CombinedGoalRate,"WBAttainmant":WBAttainmant,"CCTAttainmant":CCTAttainmant,"DISCAttainmant":DISCAttainmant,"IPBBGrossSales":IPBBGrossSales,"BroadbandAttachRate":BroadbandAttachRate,"AgentSatisfaction":AgentSatisfaction,"Achiev":Achiev}
        return TEAM_KPI
    '''
    
    def get_Achievement_Data(self,lineindex):
        Ppage=PerformancePage()
        Achievement_Data=Ppage.get_anyKPIValueOfTotal(lineindex, 9)
        return Achievement_Data
    
    def get_DTVRCX_Agent_KPI_Actual(self,TLindex,Agentindex):
        Ppage=PerformancePage()
        CombinedGoalRate=Ppage.get_anyKPIofAgent_OM(TLindex, Agentindex, 2)
        WBAttainmant=Ppage.get_anyKPIofAgent_OM(TLindex, Agentindex, 3)
        CCTAttainmant=Ppage.get_anyKPIofAgent_OM(TLindex, Agentindex, 4)
        DISCAttainmant=Ppage.get_anyKPIofAgent_OM(TLindex, Agentindex, 5)
        IPBBGrossSales=Ppage.get_anyKPIofAgent_OM(TLindex, Agentindex, 6)
        BroadbandAttachRate=Ppage.get_anyKPIofAgent_OM(TLindex, Agentindex, 7)
        AgentSatisfaction=Ppage.get_anyKPIofAgent_OM(TLindex, Agentindex, 8)
        Achiev=Ppage.get_anyKPIofAgent_OM(TLindex, Agentindex, 9)
        Agent_KPI={"CombinedGoalRate":CombinedGoalRate,"WBAttainmant":WBAttainmant,"CCTAttainmant":CCTAttainmant,"DISCAttainmant":DISCAttainmant,"IPBBGrossSales":IPBBGrossSales,"BroadbandAttachRate":BroadbandAttachRate,"AgentSatisfaction":AgentSatisfaction,"Achiev":Achiev}
        return Agent_KPI
    
    def get_DTVRCX_TL_KPI_Actual(self,TLindex):
        Ppage=PerformancePage()
        CombinedGoalRate=Ppage.get_anyKPIofTL(TLindex, 2)
        WBAttainmant=Ppage.get_anyKPIofTL(TLindex, 3)
        CCTAttainmant=Ppage.get_anyKPIofTL(TLindex, 4)
        DISCAttainmant=Ppage.get_anyKPIofTL(TLindex, 5)
        IPBBGrossSales=Ppage.get_anyKPIofTL(TLindex, 6)
        BroadbandAttachRate=Ppage.get_anyKPIofTL(TLindex, 7)
        AgentSatisfaction=Ppage.get_anyKPIofTL(TLindex, 8)
        Achiev=Ppage.get_anyKPIofTL(TLindex, 9)
        Agent_KPI={"CombinedGoalRate":CombinedGoalRate,"WBAttainmant":WBAttainmant,"CCTAttainmant":CCTAttainmant,"DISCAttainmant":DISCAttainmant,"IPBBGrossSales":IPBBGrossSales,"BroadbandAttachRate":BroadbandAttachRate,"AgentSatisfaction":AgentSatisfaction,"Achiev":Achiev}
        return Agent_KPI
    def get_DTVRCX_AgentKPI_Agent_Actual(self):
        Ppage=PerformancePage()
        CombinedGoalRate=Ppage.get_anyKPIofAgent_Agent(2)
        WBAttainmant=Ppage.get_anyKPIofAgent_Agent(3)
        CCTAttainmant=Ppage.get_anyKPIofAgent_Agent(4)
        DISCAttainmant=Ppage.get_anyKPIofAgent_Agent(5)
        IPBBGrossSales=Ppage.get_anyKPIofAgent_Agent(6)
        BroadbandAttachRate=Ppage.get_anyKPIofAgent_Agent(7)
        AgentSatisfaction=Ppage.get_anyKPIofAgent_Agent(8)
        Achiev=Ppage.get_anyKPIofAgent_Agent(9)
        Agent_KPI={"CombinedGoalRate":CombinedGoalRate,"WBAttainmant":WBAttainmant,"CCTAttainmant":CCTAttainmant,"DISCAttainmant":DISCAttainmant,"IPBBGrossSales":IPBBGrossSales,"BroadbandAttachRate":BroadbandAttachRate,"AgentSatisfaction":AgentSatisfaction,"Achiev":Achiev}
        return Agent_KPI
    
    def get_DTVRCX_AgentKPI_TL_Actual(self,Agentindex):
        Ppage=PerformancePage()
        CombinedGoalRate=Ppage.get_anyKPIofAgent_TL(Agentindex, 2)
        WBAttainmant=Ppage.get_anyKPIofAgent_TL(Agentindex,3)
        CCTAttainmant=Ppage.get_anyKPIofAgent_TL(Agentindex,4)
        DISCAttainmant=Ppage.get_anyKPIofAgent_TL(Agentindex,5)
        IPBBGrossSales=Ppage.get_anyKPIofAgent_TL(Agentindex,6)
        BroadbandAttachRate=Ppage.get_anyKPIofAgent_TL(Agentindex,7)
        AgentSatisfaction=Ppage.get_anyKPIofAgent_TL(Agentindex,8)
        Achiev=Ppage.get_anyKPIofAgent_TL(Agentindex,9)
        Agent_KPI={"CombinedGoalRate":CombinedGoalRate,"WBAttainmant":WBAttainmant,"CCTAttainmant":CCTAttainmant,"DISCAttainmant":DISCAttainmant,"IPBBGrossSales":IPBBGrossSales,"BroadbandAttachRate":BroadbandAttachRate,"AgentSatisfaction":AgentSatisfaction,"Achiev":Achiev}
        return Agent_KPI
    
    
 
        
        