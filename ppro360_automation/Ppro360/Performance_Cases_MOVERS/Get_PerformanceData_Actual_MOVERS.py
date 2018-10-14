'''
Created on Apr 7, 2017

@author: symbio
'''
from Tablet_pages.PerformancPage import PerformancePage
class Get_PerformanceData_Actual_MOVERS():
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    def get_MOVERS_Goal_Actual(self):
                                            
        Ppage=PerformancePage()
        
        LoyaltyRate=Ppage.get_anyGoalValue(2)
        BroadbandGrossSales=Ppage.get_anyGoalValue(3)
        DisconnectRate=Ppage.get_anyGoalValue(4)
        VOC=Ppage.get_anyGoalValue(5)
        MobilityGrossSales=Ppage.get_anyGoalValue(6)
        DTVNowActivations=Ppage.get_anyGoalValue(7)
        AHT=Ppage.get_anyGoalValue(8)
        B2P=Ppage.get_anyGoalValue(9)
        ABS=Ppage.get_anyGoalValue(10)
        Achiev=Ppage.get_anyGoalValue(11)
        
        Goal_KPI={"LoyaltyRate":LoyaltyRate,"BroadbandGrossSales":BroadbandGrossSales,"DisconnectRate":DisconnectRate,"VOC":VOC,
                  "MobilityGrossSales":MobilityGrossSales,"DTVNowActivations":DTVNowActivations,"AHT":AHT,"B2P":B2P,"ABS":ABS,
                  "Achiev":Achiev}
        return Goal_KPI
    def get_MOVERS_SITE_Data_(self):#site:lineindex=2
        Ppage=PerformancePage()
        LoyaltyRate=Ppage.get_anyKPIValueOfTotal(2,2)
        BroadbandGrossSales=Ppage.get_anyKPIValueOfTotal(2,3)
        DisconnectRate=Ppage.get_anyKPIValueOfTotal(2,4)
        VOC=Ppage.get_anyKPIValueOfTotal(2,5)
        MobilityGrossSales=Ppage.get_anyKPIValueOfTotal(2,6)
        DTVNowActivations=Ppage.get_anyKPIValueOfTotal(2,7)
        AHT=Ppage.get_anyKPIValueOfTotal(2,8)
        B2P=Ppage.get_anyKPIValueOfTotal(2,9)
        ABS=Ppage.get_anyKPIValueOfTotal(2,10)
        Achiev=Ppage.get_anyKPIValueOfTotal(2,11)
        SITE_KPI={"LoyaltyRate":LoyaltyRate,"BroadbandGrossSales":BroadbandGrossSales,"DisconnectRate":DisconnectRate,"VOC":VOC,
                  "MobilityGrossSales":MobilityGrossSales,"DTVNowActivations":DTVNowActivations,"AHT":AHT,"B2P":B2P,"ABS":ABS,
                  "Achiev":Achiev}
        return SITE_KPI
    def get_MOVERS_TEAM_Data_(self):#TEAM:lineindex=3
        Ppage=PerformancePage()
        LoyaltyRate=Ppage.get_anyKPIValueOfTotal(3,2)
        BroadbandGrossSales=Ppage.get_anyKPIValueOfTotal(3,3)
        DisconnectRate=Ppage.get_anyKPIValueOfTotal(3,4)
        VOC=Ppage.get_anyKPIValueOfTotal(3,5)
        MobilityGrossSales=Ppage.get_anyKPIValueOfTotal(3,6)
        DTVNowActivations=Ppage.get_anyKPIValueOfTotal(3,7)
        AHT=Ppage.get_anyKPIValueOfTotal(3,8)
        B2P=Ppage.get_anyKPIValueOfTotal(3,9)
        ABS=Ppage.get_anyKPIValueOfTotal(3,10)
        Achiev=Ppage.get_anyKPIValueOfTotal(3,11)
        TEAM_KPI={"LoyaltyRate":LoyaltyRate,"BroadbandGrossSales":BroadbandGrossSales,"DisconnectRate":DisconnectRate,"VOC":VOC,
                  "MobilityGrossSales":MobilityGrossSales,"DTVNowActivations":DTVNowActivations,"AHT":AHT,"B2P":B2P,"ABS":ABS,
                  "Achiev":Achiev}
        return TEAM_KPI
    
    
    def get_Achievement_Data(self,lineindex):
        Ppage=PerformancePage()
        Achievement_Data=Ppage.get_anyKPIValueOfTotal(lineindex, 8)
        return Achievement_Data
    
    def get_MOVERS_Agent_KPI_Actual(self,TLindex,Agentindex):
        Ppage=PerformancePage()
        LoyaltyRate=Ppage.get_anyKPIofAgent_OM(TLindex,Agentindex,2)
        BroadbandGrossSales=Ppage.get_anyKPIofAgent_OM(TLindex,Agentindex,3)
        DisconnectRate=Ppage.get_anyKPIofAgent_OM(TLindex,Agentindex,4)
        VOC=Ppage.get_anyKPIofAgent_OM(TLindex,Agentindex,5)
        MobilityGrossSales=Ppage.get_anyKPIofAgent_OM(TLindex,Agentindex,6)
        DTVNowActivations=Ppage.get_anyKPIofAgent_OM(TLindex,Agentindex,7)
        AHT=Ppage.get_anyKPIofAgent_OM(TLindex,Agentindex,8)
        B2P=Ppage.get_anyKPIofAgent_OM(TLindex,Agentindex,9)
        ABS=Ppage.get_anyKPIofAgent_OM(TLindex,Agentindex,10)
        Achiev=Ppage.get_anyKPIofAgent_OM(TLindex,Agentindex,11)

        
        Agent_KPI={"LoyaltyRate":LoyaltyRate,"BroadbandGrossSales":BroadbandGrossSales,"DisconnectRate":DisconnectRate,"VOC":VOC,
                  "MobilityGrossSales":MobilityGrossSales,"DTVNowActivations":DTVNowActivations,"AHT":AHT,"B2P":B2P,"ABS":ABS,
                  "Achiev":Achiev}
        return Agent_KPI
    
    def get_MOVERS_TL_KPI_Actual(self,TLindex):
        Ppage=PerformancePage()
        LoyaltyRate=Ppage.get_anyKPIofTL(TLindex,2)
        BroadbandGrossSales=Ppage.get_anyKPIofTL(TLindex,3)
        DisconnectRate=Ppage.get_anyKPIofTL(TLindex,4)
        VOC=Ppage.get_anyKPIofTL(TLindex,5)
        MobilityGrossSales=Ppage.get_anyKPIofTL(TLindex,6)
        DTVNowActivations=Ppage.get_anyKPIofTL(TLindex,7)
        AHT=Ppage.get_anyKPIofTL(TLindex,8)
        B2P=Ppage.get_anyKPIofTL(TLindex,9)
        ABS=Ppage.get_anyKPIofTL(TLindex,10)
        Achiev=Ppage.get_anyKPIofTL(TLindex,11)
        Agent_KPI={"LoyaltyRate":LoyaltyRate,"BroadbandGrossSales":BroadbandGrossSales,"DisconnectRate":DisconnectRate,"VOC":VOC,
                  "MobilityGrossSales":MobilityGrossSales,"DTVNowActivations":DTVNowActivations,"AHT":AHT,"B2P":B2P,"ABS":ABS,
                  "Achiev":Achiev}
        return Agent_KPI
    def get_MOVERS_AgentKPI_Agent_Actual(self):
        Ppage=PerformancePage()
        LoyaltyRate=Ppage.get_anyKPIofAgent_Agent(2)
        BroadbandGrossSales=Ppage.get_anyKPIofAgent_Agent(3)
        DisconnectRate=Ppage.get_anyKPIofAgent_Agent(4)
        VOC=Ppage.get_anyKPIofAgent_Agent(5)
        MobilityGrossSales=Ppage.get_anyKPIofAgent_Agent(6)
        DTVNowActivations=Ppage.get_anyKPIofAgent_Agent(7)
        AHT=Ppage.get_anyKPIofAgent_Agent(8)
        B2P=Ppage.get_anyKPIofAgent_Agent(9)
        ABS=Ppage.get_anyKPIofAgent_Agent(10)
        Achiev=Ppage.get_anyKPIofAgent_Agent(11)
        Agent_KPI={"LoyaltyRate":LoyaltyRate,"BroadbandGrossSales":BroadbandGrossSales,"DisconnectRate":DisconnectRate,"VOC":VOC,
                  "MobilityGrossSales":MobilityGrossSales,"DTVNowActivations":DTVNowActivations,"AHT":AHT,"B2P":B2P,"ABS":ABS,
                  "Achiev":Achiev}
        return Agent_KPI
    
    def get_MOVERS_AgentKPI_TL_Actual(self,Agentindex):
        Ppage=PerformancePage()
        LoyaltyRate=Ppage.get_anyKPIofAgent_TL(Agentindex,2)
        BroadbandGrossSales=Ppage.get_anyKPIofAgent_TL(Agentindex,3)
        DisconnectRate=Ppage.get_anyKPIofAgent_TL(Agentindex,4)
        VOC=Ppage.get_anyKPIofAgent_TL(Agentindex,5)
        MobilityGrossSales=Ppage.get_anyKPIofAgent_TL(Agentindex,6)
        DTVNowActivations=Ppage.get_anyKPIofAgent_TL(Agentindex,7)
        AHT=Ppage.get_anyKPIofAgent_TL(Agentindex,8)
        B2P=Ppage.get_anyKPIofAgent_TL(Agentindex,9)
        ABS=Ppage.get_anyKPIofAgent_TL(Agentindex,10)
        Achiev=Ppage.get_anyKPIofAgent_TL(Agentindex,11)
        Agent_KPI={"LoyaltyRate":LoyaltyRate,"BroadbandGrossSales":BroadbandGrossSales,"DisconnectRate":DisconnectRate,"VOC":VOC,
                  "MobilityGrossSales":MobilityGrossSales,"DTVNowActivations":DTVNowActivations,"AHT":AHT,"B2P":B2P,"ABS":ABS,
                  "Achiev":Achiev}
        return Agent_KPI
    
        
        
        