'''
Created on 2017.9.6

@author: yalan.yin
'''
from Tablet_pages.PerformancPage import PerformancePage

class Get_PerformanceData_Actual_DBS(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    def get_DBS_Goal_Actual(self):
        Ppage=PerformancePage()
        R30=Ppage.get_anyKPIValueOfTotal(1,2)[0]
        R7=Ppage.get_anyKPIValueOfTotal(1,3)[0]
        Transfers=Ppage.get_anyKPIValueOfTotal(1,4)[0]
        AHT=Ppage.get_anyKPIValueOfTotal(1,5)[0]
        CloseRate=Ppage.get_anyKPIValueOfTotal(1,6)[0]
        VOC=Ppage.get_anyKPIValueOfTotal(1,7)[0]
        Achiev=Ppage.get_anyKPIValueOfTotal(1,8)[0]
        Goal_KPI={'R30':R30,'R7':R7,'Transfers':Transfers,'AHT':AHT,'CloseRate':CloseRate,'VOC':VOC,'Achiev':Achiev}
        return Goal_KPI
 
    def get_DBS_SITE_Data_(self):
        Ppage=PerformancePage()
        R30=Ppage.get_anyKPIValueOfTotal(2,2)
        R7=Ppage.get_anyKPIValueOfTotal(2,3)
        Transfers=Ppage.get_anyKPIValueOfTotal(2,4)
        AHT=Ppage.get_anyKPIValueOfTotal(2,5)
        CloseRate=Ppage.get_anyKPIValueOfTotal(2,6)
        VOC=Ppage.get_anyKPIValueOfTotal(2,7)
        Achiev=Ppage.get_anyKPIValueOfTotal(2,8)
        SITE_KPI={'R30':R30,'R7':R7,'Transfers':Transfers,'AHT':AHT,'CloseRate':CloseRate,'VOC':VOC,'Achiev':Achiev}
        return SITE_KPI
    def get_DBS_TEAM_Data_(self):
        Ppage=PerformancePage()
        R30=Ppage.get_anyKPIValueOfTotal(3,2)
        R7=Ppage.get_anyKPIValueOfTotal(3,3)
        Transfers=Ppage.get_anyKPIValueOfTotal(3,4)
        AHT=Ppage.get_anyKPIValueOfTotal(3,5)
        CloseRate=Ppage.get_anyKPIValueOfTotal(3,6)
        VOC=Ppage.get_anyKPIValueOfTotal(3,7)
        Achiev=Ppage.get_anyKPIValueOfTotal(3,8)
        TEAM_KPI={'R30':R30,'R7':R7,'Transfers':Transfers,'AHT':AHT,'CloseRate':CloseRate,'VOC':VOC,'Achiev':Achiev}
        return TEAM_KPI
 
    def get_Achievement_Data(self,lineindex): #this method may be not used
        Ppage=PerformancePage()
        Achievement_Data=Ppage.get_anyKPIValueOfTotal(lineindex, 8)
        return Achievement_Data
 
    def get_DBS_Agent_KPI_Actual(self,TLindex,Agentindex):
        Ppage=PerformancePage()
        R30=Ppage.get_anyKPIofAgent_OM(TLindex, Agentindex, 2)
        R7=Ppage.get_anyKPIofAgent_OM(TLindex, Agentindex, 3)
        Transfers=Ppage.get_anyKPIofAgent_OM(TLindex, Agentindex, 4)
        AHT=Ppage.get_anyKPIofAgent_OM(TLindex, Agentindex, 5)
        CloseRate=Ppage.get_anyKPIofAgent_OM(TLindex, Agentindex, 6)
        VOC=Ppage.get_anyKPIofAgent_OM(TLindex, Agentindex, 7)
        Achiev=Ppage.get_anyKPIofAgent_OM(TLindex, Agentindex, 8)
        Agent_KPI={'R30':R30,'R7':R7,'Transfers':Transfers,'AHT':AHT,'CloseRate':CloseRate,'VOC':VOC,'Achiev':Achiev}
        return Agent_KPI
    
    def get_DBS_TL_KPI_Actual(self,TLindex):
        Ppage=PerformancePage()
        R30=Ppage.get_anyKPIofTL(TLindex, 2)
        R7=Ppage.get_anyKPIofTL(TLindex, 3)
        Transfers=Ppage.get_anyKPIofTL(TLindex, 4)
        AHT=Ppage.get_anyKPIofTL(TLindex, 5)
        CloseRate=Ppage.get_anyKPIofTL(TLindex, 6)
        VOC=Ppage.get_anyKPIofTL(TLindex, 7)
        Achiev=Ppage.get_anyKPIofTL(TLindex, 8)
        Agent_KPI={'R30':R30,'R7':R7,'Transfers':Transfers,'AHT':AHT,'CloseRate':CloseRate,'VOC':VOC,'Achiev':Achiev}
        return Agent_KPI
    
    def get_DBS_AgentKPI_Agent_Actual(self):
        Ppage=PerformancePage()
        R30=Ppage.get_anyKPIofAgent_Agent(2)
        R7=Ppage.get_anyKPIofAgent_Agent(3)
        Transfers=Ppage.get_anyKPIofAgent_Agent(4)
        AHT=Ppage.get_anyKPIofAgent_Agent(5)
        CloseRate=Ppage.get_anyKPIofAgent_Agent(6)
        VOC=Ppage.get_anyKPIofAgent_Agent(7)
        Achiev=Ppage.get_anyKPIofAgent_Agent(8)
        Agent_KPI={'R30':R30,'R7':R7,'Transfers':Transfers,'AHT':AHT,'CloseRate':CloseRate,'VOC':VOC,'Achiev':Achiev}
        return Agent_KPI
    
    def get_DBS_AgentKPI_TL_Actual(self,Agentindex):
        Ppage=PerformancePage()
        R30=Ppage.get_anyKPIofAgent_TL(Agentindex, 2)
        R7=Ppage.get_anyKPIofAgent_TL(Agentindex, 3)
        Transfers=Ppage.get_anyKPIofAgent_TL(Agentindex, 4)
        AHT=Ppage.get_anyKPIofAgent_TL(Agentindex, 5)
        CloseRate=Ppage.get_anyKPIofAgent_TL(Agentindex, 6)
        VOC=Ppage.get_anyKPIofAgent_TL(Agentindex, 7)
        Achiev=Ppage.get_anyKPIofAgent_TL(Agentindex, 8)
        Agent_KPI={'R30':R30,'R7':R7,'Transfers':Transfers,'AHT':AHT,'CloseRate':CloseRate,'VOC':VOC,'Achiev':Achiev}
        return Agent_KPI

    