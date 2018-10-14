'''
Created on 20170918

@author: luming.zhao
'''
from Tablet_pages.PerformancPage import PerformancePage
class Get_PerformanceData_Actual_DTVSS(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    def get_DTVSS_Goal_Actual(self):
        Ppage=PerformancePage()
        ActivationRateModify=Ppage.get_anyKPIValueOfTotal(1,2)[0] 
        CancelTransfer=Ppage.get_anyKPIValueOfTotal(1,3)[0]
        CancelIVR=Ppage.get_anyKPIValueOfTotal(1,4)[0]  
        IPBBNet=Ppage.get_anyKPIValueOfTotal(1,5)[0] 
        MobilityGrossSales=Ppage.get_anyKPIValueOfTotal(1,6)[0] 
        AgentSatisfaction=Ppage.get_anyKPIValueOfTotal(1,7)[0]
        Achiev=Ppage.get_anyKPIValueOfTotal(1,8)[0]
        Goal_KPI={"ActivationRateModify":ActivationRateModify,"CancelTransfer":CancelTransfer,"CancelIVR":CancelIVR,"IPBBNet":IPBBNet,"MobilityGrossSales":MobilityGrossSales,"AgentSatisfaction":AgentSatisfaction,"Achiev":Achiev}
        return Goal_KPI
    def get_DTVSS_SITE_Data_(self):#site:lineindex=2
        Ppage=PerformancePage()
        ActivationRateModify=Ppage.get_anyKPIValueOfTotal(2,2)
        CancelTransfer=Ppage.get_anyKPIValueOfTotal(2,3)
        CancelIVR=Ppage.get_anyKPIValueOfTotal(2,4)
        IPBBNet=Ppage.get_anyKPIValueOfTotal(2,5)
        MobilityGrossSales=Ppage.get_anyKPIValueOfTotal(2,6)
        AgentSatisfaction=Ppage.get_anyKPIValueOfTotal(2,7)
        Achiev=Ppage.get_anyKPIValueOfTotal(2,8)
        SITE_KPI={"ActivationRateModify":ActivationRateModify,"CancelTransfer":CancelTransfer,"CancelIVR":CancelIVR,"IPBBNet":IPBBNet,"MobilityGrossSales":MobilityGrossSales,"AgentSatisfaction":AgentSatisfaction,"Achiev":Achiev}
        return SITE_KPI
    def get_DTVSS_TEAM_Data_(self):#TEAM:lineindex=3
        Ppage=PerformancePage()
        ActivationRateModify=Ppage.get_anyKPIValueOfTotal(3,2)
        CancelTransfer=Ppage.get_anyKPIValueOfTotal(3,3)
        CancelIVR=Ppage.get_anyKPIValueOfTotal(3,4)
        IPBBNet=Ppage.get_anyKPIValueOfTotal(3,5)
        MobilityGrossSales=Ppage.get_anyKPIValueOfTotal(3,6)
        AgentSatisfaction=Ppage.get_anyKPIValueOfTotal(3,7)
        Achiev=Ppage.get_anyKPIValueOfTotal(3,8)
        TEAM_KPI={"ActivationRateModify":ActivationRateModify,"CancelTransfer":CancelTransfer,"CancelIVR":CancelIVR,"IPBBNet":IPBBNet,"MobilityGrossSales":MobilityGrossSales,"AgentSatisfaction":AgentSatisfaction,"Achiev":Achiev}
        return TEAM_KPI
    
    
    def get_Achievement_Data(self,lineindex):
        Ppage=PerformancePage()
        Achievement_Data=Ppage.get_anyKPIValueOfTotal(lineindex, 8)
        return Achievement_Data
    
    def get_DTVSS_Agent_KPI_Actual(self,TLindex,Agentindex):
        Ppage=PerformancePage()
        ActivationRateModify=Ppage.get_anyKPIofAgent_OM(TLindex, Agentindex, 2)
        CancelTransfer=Ppage.get_anyKPIofAgent_OM(TLindex, Agentindex, 3)
        CancelIVR=Ppage.get_anyKPIofAgent_OM(TLindex, Agentindex, 4)
        IPBBNet=Ppage.get_anyKPIofAgent_OM(TLindex, Agentindex, 5)
        MobilityGrossSales=Ppage.get_anyKPIofAgent_OM(TLindex, Agentindex, 6)
        AgentSatisfaction=Ppage.get_anyKPIofAgent_OM(TLindex, Agentindex, 7)
        Achiev=Ppage.get_anyKPIofAgent_OM(TLindex, Agentindex, 8)
        Agent_KPI={"ActivationRateModify":ActivationRateModify,"CancelTransfer":CancelTransfer,"CancelIVR":CancelIVR,"IPBBNet":IPBBNet,"MobilityGrossSales":MobilityGrossSales,"AgentSatisfaction":AgentSatisfaction,"Achiev":Achiev}
        return Agent_KPI
    
    def get_DTVSS_TL_KPI_Actual(self,TLindex):
        Ppage=PerformancePage()
        ActivationRateModify=Ppage.get_anyKPIofTL(TLindex, 2)
        CancelTransfer=Ppage.get_anyKPIofTL(TLindex, 3)
        CancelIVR=Ppage.get_anyKPIofTL(TLindex, 4)
        IPBBNet=Ppage.get_anyKPIofTL(TLindex, 5)
        MobilityGrossSales=Ppage.get_anyKPIofTL(TLindex, 6)
        AgentSatisfaction=Ppage.get_anyKPIofTL(TLindex, 7)
        Achiev=Ppage.get_anyKPIofTL(TLindex, 8)
        Agent_KPI={"ActivationRateModify":ActivationRateModify,"CancelTransfer":CancelTransfer,"CancelIVR":CancelIVR,"IPBBNet":IPBBNet,"MobilityGrossSales":MobilityGrossSales,"AgentSatisfaction":AgentSatisfaction,"Achiev":Achiev}
        return Agent_KPI
    def get_DTVSS_AgentKPI_Agent_Actual(self):
        Ppage=PerformancePage()
        ActivationRateModify=Ppage.get_anyKPIofAgent_Agent(2)
        CancelTransfer=Ppage.get_anyKPIofAgent_Agent(3)
        CancelIVR=Ppage.get_anyKPIofAgent_Agent(4)
        IPBBNet=Ppage.get_anyKPIofAgent_Agent(5)
        MobilityGrossSales=Ppage.get_anyKPIofAgent_Agent(6)
        AgentSatisfaction=Ppage.get_anyKPIofAgent_Agent(7)
        Achiev=Ppage.get_anyKPIofAgent_Agent(8)
        Agent_KPI={"ActivationRateModify":ActivationRateModify,"CancelTransfer":CancelTransfer,"CancelIVR":CancelIVR,"IPBBNet":IPBBNet,"MobilityGrossSales":MobilityGrossSales,"AgentSatisfaction":AgentSatisfaction,"Achiev":Achiev}
        return Agent_KPI
    
    def get_DTVSS_AgentKPI_TL_Actual(self,Agentindex):
        Ppage=PerformancePage()
        ActivationRateModify=Ppage.get_anyKPIofAgent_TL(Agentindex, 2)
        CancelTransfer=Ppage.get_anyKPIofAgent_TL(Agentindex,3)
        CancelIVR=Ppage.get_anyKPIofAgent_TL(Agentindex,4)
        IPBBNet=Ppage.get_anyKPIofAgent_TL(Agentindex,5)
        MobilityGrossSales=Ppage.get_anyKPIofAgent_TL(Agentindex,6)
        AgentSatisfaction=Ppage.get_anyKPIofAgent_TL(Agentindex,7)
        Achiev=Ppage.get_anyKPIofAgent_TL(Agentindex,8)
        Agent_KPI={"ActivationRateModify":ActivationRateModify,"CancelTransfer":CancelTransfer,"CancelIVR":CancelIVR,"IPBBNet":IPBBNet,"MobilityGrossSales":MobilityGrossSales,"AgentSatisfaction":AgentSatisfaction,"Achiev":Achiev}
        return Agent_KPI
    
    
    '''
    def get_Tl_name(self,lineindex):
        Ppage=PerformancePage()
        Title_name=Ppage.get_anyKPIValueOfTotal(lineindex, 1)
        #Title_name=Ppage.get_anyKPIValue(lineindex, 1)
        print Title_name
        return Title_name
        '''
        
        
        