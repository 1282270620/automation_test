'''
Created on 2017.10.10

@author: yalan.yin
'''
from Tablet_pages.PerformancPage import PerformancePage

class Get_PerformanceData_Actual_GREEN(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    def get_GREEN_Goal_Actual(self):
        Ppage=PerformancePage()
        Revenue=Ppage.get_anyKPIValueOfTotal(1,2)[0]
        Video=Ppage.get_anyKPIValueOfTotal(1,3)[0]
        Broadband=Ppage.get_anyKPIValueOfTotal(1,4)[0]
        Wireless=Ppage.get_anyKPIValueOfTotal(1,5)[0]
        VOIP=Ppage.get_anyKPIValueOfTotal(1,6)[0]
        VOC=Ppage.get_anyKPIValueOfTotal(1,7)[0]
        BARAttainment=Ppage.get_anyKPIValueOfTotal(1,8)[0]
        AHT=Ppage.get_anyKPIValueOfTotal(1,9)[0]
        Achiev=Ppage.get_anyKPIValueOfTotal(1,10)[0]
        Goal_KPI={'VOIP':VOIP,'Revenue':Revenue,'Video':Video,'Broadband':Broadband,'AHT':AHT,'Wireless':Wireless,'VOC':VOC,'BARAttainment':BARAttainment,'Achiev':Achiev}
        return Goal_KPI
 
    def get_GREEN_SITE_Data_(self):
        Ppage=PerformancePage()
        Revenue=Ppage.get_anyKPIValueOfTotal(2,2)
        Video=Ppage.get_anyKPIValueOfTotal(2,3)
        Broadband=Ppage.get_anyKPIValueOfTotal(2,4)
        Wireless=Ppage.get_anyKPIValueOfTotal(2,5)
        VOIP=Ppage.get_anyKPIValueOfTotal(2,6)
        VOC=Ppage.get_anyKPIValueOfTotal(2,7)
        BARAttainment=Ppage.get_anyKPIValueOfTotal(2,8)
        AHT=Ppage.get_anyKPIValueOfTotal(2,9)
        Achiev=Ppage.get_anyKPIValueOfTotal(2,10)
        SITE_KPI={'VOIP':VOIP,'Revenue':Revenue,'Video':Video,'Broadband':Broadband,'AHT':AHT,'Wireless':Wireless,'VOC':VOC,'BARAttainment':BARAttainment,'Achiev':Achiev}
        return SITE_KPI
    def get_GREEN_TEAM_Data_(self):
        Ppage=PerformancePage()
        Revenue=Ppage.get_anyKPIValueOfTotal(3,2)
        Video=Ppage.get_anyKPIValueOfTotal(3,3)
        Broadband=Ppage.get_anyKPIValueOfTotal(3,4)
        Wireless=Ppage.get_anyKPIValueOfTotal(3,5)
        VOIP=Ppage.get_anyKPIValueOfTotal(3,6)
        VOC=Ppage.get_anyKPIValueOfTotal(3,7)
        BARAttainment=Ppage.get_anyKPIValueOfTotal(3,8)
        AHT=Ppage.get_anyKPIValueOfTotal(3,9)
        Achiev=Ppage.get_anyKPIValueOfTotal(3,10)
        TEAM_KPI={'VOIP':VOIP,'Revenue':Revenue,'Video':Video,'Broadband':Broadband,'AHT':AHT,'Wireless':Wireless,'VOC':VOC,'BARAttainment':BARAttainment,'Achiev':Achiev}
        return TEAM_KPI
 
    def get_Achievement_Data(self,lineindex): #this method may be not used
        Ppage=PerformancePage()
        Achievement_Data=Ppage.get_anyKPIValueOfTotal(lineindex, 8)
        return Achievement_Data
 
    def get_GREEN_Agent_KPI_Actual(self,TLindex,Agentindex):
        Ppage=PerformancePage()
        Revenue=Ppage.get_anyKPIofAgent_OM(TLindex, Agentindex, 2)
        Video=Ppage.get_anyKPIofAgent_OM(TLindex, Agentindex, 3)
        Broadband=Ppage.get_anyKPIofAgent_OM(TLindex, Agentindex, 4)
        Wireless=Ppage.get_anyKPIofAgent_OM(TLindex, Agentindex, 5)
        VOIP=Ppage.get_anyKPIofAgent_OM(TLindex, Agentindex, 6)
        VOC=Ppage.get_anyKPIofAgent_OM(TLindex, Agentindex, 7)
        BARAttainment=Ppage.get_anyKPIofAgent_OM(TLindex, Agentindex, 8)
        AHT=Ppage.get_anyKPIofAgent_OM(TLindex, Agentindex, 9)
        Achiev=Ppage.get_anyKPIofAgent_OM(TLindex, Agentindex, 10)
        Agent_KPI={'VOIP':VOIP,'Revenue':Revenue,'Video':Video,'Broadband':Broadband,'AHT':AHT,'Wireless':Wireless,'VOC':VOC,'BARAttainment':BARAttainment,'Achiev':Achiev}
        return Agent_KPI
    
    def get_GREEN_TL_KPI_Actual(self,TLindex):
        Ppage=PerformancePage()
        Revenue=Ppage.get_anyKPIofTL(TLindex, 2)
        Video=Ppage.get_anyKPIofTL(TLindex, 3)
        Broadband=Ppage.get_anyKPIofTL(TLindex, 4)
        Wireless=Ppage.get_anyKPIofTL(TLindex, 5)
        VOIP=Ppage.get_anyKPIofTL(TLindex, 6)
        VOC=Ppage.get_anyKPIofTL(TLindex, 7)
        BARAttainment=Ppage.get_anyKPIofTL(TLindex, 8)
        AHT=Ppage.get_anyKPIofTL(TLindex, 9)
        Achiev=Ppage.get_anyKPIofTL(TLindex, 10)
        Agent_KPI={'VOIP':VOIP,'Revenue':Revenue,'Video':Video,'Broadband':Broadband,'AHT':AHT,'Wireless':Wireless,'VOC':VOC,'BARAttainment':BARAttainment,'Achiev':Achiev}
        return Agent_KPI
    
    def get_GREEN_AgentKPI_Agent_Actual(self):
        Ppage=PerformancePage()
        Revenue=Ppage.get_anyKPIofAgent_Agent(2)
        Video=Ppage.get_anyKPIofAgent_Agent(3)
        Broadband=Ppage.get_anyKPIofAgent_Agent(4)
        Wireless=Ppage.get_anyKPIofAgent_Agent(5)
        VOIP=Ppage.get_anyKPIofAgent_Agent(6)
        VOC=Ppage.get_anyKPIofAgent_Agent(7)
        BARAttainment=Ppage.get_anyKPIofAgent_Agent(8)
        AHT=Ppage.get_anyKPIofAgent_Agent(9)       
        Achiev=Ppage.get_anyKPIofAgent_Agent(10)
        Agent_KPI={'VOIP':VOIP,'Revenue':Revenue,'Video':Video,'Broadband':Broadband,'AHT':AHT,'Wireless':Wireless,'VOC':VOC,'BARAttainment':BARAttainment,'Achiev':Achiev}
        return Agent_KPI
    
    def get_GREEN_AgentKPI_TL_Actual(self,Agentindex):
        Ppage=PerformancePage()
        Revenue=Ppage.get_anyKPIofAgent_TL(Agentindex, 2)
        Video=Ppage.get_anyKPIofAgent_TL(Agentindex, 3)
        Broadband=Ppage.get_anyKPIofAgent_TL(Agentindex, 4)
        Wireless=Ppage.get_anyKPIofAgent_TL(Agentindex, 5)
        VOIP=Ppage.get_anyKPIofAgent_TL(Agentindex, 6)
        VOC=Ppage.get_anyKPIofAgent_TL(Agentindex, 7)
        AHT=Ppage.get_anyKPIofAgent_TL(Agentindex, 9)
        BARAttainment=Ppage.get_anyKPIofAgent_TL(Agentindex, 8)
        Achiev=Ppage.get_anyKPIofAgent_TL(Agentindex, 10)
        Agent_KPI={'VOIP':VOIP,'Revenue':Revenue,'Video':Video,'Broadband':Broadband,'AHT':AHT,'Wireless':Wireless,'VOC':VOC,'BARAttainment':BARAttainment,'Achiev':Achiev}
        return Agent_KPI
    