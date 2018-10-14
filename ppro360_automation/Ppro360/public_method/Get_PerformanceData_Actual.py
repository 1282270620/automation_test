'''
Created on Apr 7, 2017

@author: symbio
'''
from Tablet_pages.PerformancPage import PerformancePage
class Get_PerformanceData_Actual():
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    def get_LCBB_Goal_Actual(self):
        Ppage=PerformancePage()
        AHT=Ppage.get_anyKPIValueOfTotal(1,2)[0]
        HoldTime=Ppage.get_anyKPIValueOfTotal(1,3)[0]
        ACW=Ppage.get_anyKPIValueOfTotal(1,4)[0]
        Transfers=Ppage.get_anyKPIValueOfTotal(1,5)[0]
        VOC=Ppage.get_anyKPIValueOfTotal(1,6)[0]
        SOAR=Ppage.get_anyKPIValueOfTotal(1,7)[0]
        Achiev=Ppage.get_anyKPIValueOfTotal(1,8)[0]
        Goal_KPI={"AHT":AHT,"HoldTime":HoldTime,"ACW":ACW,"Transfers":Transfers,"VOC":VOC,"SOAR":SOAR,"Achiev":Achiev}
        return Goal_KPI
    def get_LCBB_SITE_Data_(self):#site:lineindex=2
        Ppage=PerformancePage()
        AHT=Ppage.get_anyKPIValueOfTotal(2,2)
        HoldTime=Ppage.get_anyKPIValueOfTotal(2,3)
        ACW=Ppage.get_anyKPIValueOfTotal(2,4)
        Transfers=Ppage.get_anyKPIValueOfTotal(2,5)
        VOC=Ppage.get_anyKPIValueOfTotal(2,6)
        SOAR=Ppage.get_anyKPIValueOfTotal(2,7)
        Achiev=Ppage.get_anyKPIValueOfTotal(2,8)
        SITE_KPI={"AHT":AHT,"HoldTime":HoldTime,"ACW":ACW,"Transfers":Transfers,"VOC":VOC,"SOAR":SOAR,"Achiev":Achiev}
        return SITE_KPI
    def get_LCBB_TEAM_Data_(self):#TEAM:lineindex=3
        Ppage=PerformancePage()
        AHT=Ppage.get_anyKPIValueOfTotal(3,2)
        HoldTime=Ppage.get_anyKPIValueOfTotal(3,3)
        ACW=Ppage.get_anyKPIValueOfTotal(3,4)
        Transfers=Ppage.get_anyKPIValueOfTotal(3,5)
        VOC=Ppage.get_anyKPIValueOfTotal(3,6)
        SOAR=Ppage.get_anyKPIValueOfTotal(3,7)
        Achiev=Ppage.get_anyKPIValueOfTotal(3,8)
        TEAM_KPI={"AHT":AHT,"HoldTime":HoldTime,"ACW":ACW,"Transfers":Transfers,"VOC":VOC,"SOAR":SOAR,"Achiev":Achiev}
        return TEAM_KPI
    
    
    def get_Achievement_Data(self,lineindex):
        Ppage=PerformancePage()
        Achievement_Data=Ppage.get_anyKPIValueOfTotal(lineindex, 8)
        return Achievement_Data
    
    def get_LCBB_Agent_KPI_Actual(self,TLindex,Agentindex):
        Ppage=PerformancePage()
        AHT=Ppage.get_anyKPIofAgent_OM(TLindex, Agentindex, 2)
        HoldTime=Ppage.get_anyKPIofAgent_OM(TLindex, Agentindex, 3)
        ACW=Ppage.get_anyKPIofAgent_OM(TLindex, Agentindex, 4)
        Transfers=Ppage.get_anyKPIofAgent_OM(TLindex, Agentindex, 5)
        VOC=Ppage.get_anyKPIofAgent_OM(TLindex, Agentindex, 6)
        SOAR=Ppage.get_anyKPIofAgent_OM(TLindex, Agentindex, 7)
        Achiev=Ppage.get_anyKPIofAgent_OM(TLindex, Agentindex, 8)
        Agent_KPI={"AHT":AHT,"HoldTime":HoldTime,"ACW":ACW,"Transfers":Transfers,"VOC":VOC,"SOAR":SOAR,"Achiev":Achiev}
        return Agent_KPI
    
    def get_LCBB_TL_KPI_Actual(self,TLindex):
        Ppage=PerformancePage()
        AHT=Ppage.get_anyKPIofTL(TLindex, 2)
        HoldTime=Ppage.get_anyKPIofTL(TLindex, 3)
        ACW=Ppage.get_anyKPIofTL(TLindex, 4)
        Transfers=Ppage.get_anyKPIofTL(TLindex, 5)
        VOC=Ppage.get_anyKPIofTL(TLindex, 6)
        SOAR=Ppage.get_anyKPIofTL(TLindex, 7)
        Achiev=Ppage.get_anyKPIofTL(TLindex, 8)
        Agent_KPI={"AHT":AHT,"HoldTime":HoldTime,"ACW":ACW,"Transfers":Transfers,"VOC":VOC,"SOAR":SOAR,"Achiev":Achiev}
        return Agent_KPI
    def get_LCBB_AgentKPI_Agent_Actual(self):
        Ppage=PerformancePage()
        AHT=Ppage.get_anyKPIofAgent_Agent(2)
        HoldTime=Ppage.get_anyKPIofAgent_Agent(3)
        ACW=Ppage.get_anyKPIofAgent_Agent(4)
        Transfers=Ppage.get_anyKPIofAgent_Agent(5)
        VOC=Ppage.get_anyKPIofAgent_Agent(6)
        SOAR=Ppage.get_anyKPIofAgent_Agent(7)
        Achiev=Ppage.get_anyKPIofAgent_Agent(8)
        Agent_KPI={"AHT":AHT,"HoldTime":HoldTime,"ACW":ACW,"Transfers":Transfers,"VOC":VOC,"SOAR":SOAR,"Achiev":Achiev}
        return Agent_KPI
    
    def get_LCBB_AgentKPI_TL_Actual(self,Agentindex):
        Ppage=PerformancePage()
        AHT=Ppage.get_anyKPIofAgent_TL(Agentindex, 2)
        HoldTime=Ppage.get_anyKPIofAgent_TL(Agentindex,3)
        ACW=Ppage.get_anyKPIofAgent_TL(Agentindex,4)
        Transfers=Ppage.get_anyKPIofAgent_TL(Agentindex,5)
        VOC=Ppage.get_anyKPIofAgent_TL(Agentindex,6)
        SOAR=Ppage.get_anyKPIofAgent_TL(Agentindex,7)
        Achiev=Ppage.get_anyKPIofAgent_TL(Agentindex,8)
        Agent_KPI={"AHT":AHT,"HoldTime":HoldTime,"ACW":ACW,"Transfers":Transfers,"VOC":VOC,"SOAR":SOAR,"Achiev":Achiev}
        return Agent_KPI
    
    
    '''
    def get_Tl_name(self,lineindex):
        Ppage=PerformancePage()
        Title_name=Ppage.get_anyKPIValueOfTotal(lineindex, 1)
        #Title_name=Ppage.get_anyKPIValue(lineindex, 1)
        print Title_name
        return Title_name
        '''
        
        
        