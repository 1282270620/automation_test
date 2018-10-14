'''
Created on Apr 7, 2017

@author: symbio
'''
from Tablet_pages.PerformancPage import PerformancePage
class Get_PerformanceData_Actual_PAYPAL():
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    def get_PAYPAL_Goal_Actual(self):
                                            
        Ppage=PerformancePage()
        NPS=Ppage.get_anyKPIValueOfTotal(1,2)[0]
        AHT=Ppage.get_anyKPIValueOfTotal(1,3)[0]
        HP=Ppage.get_anyKPIValueOfTotal(1,4)[0]
        SGI=Ppage.get_anyKPIValueOfTotal(1,5)[0]
        TO=Ppage.get_anyKPIValueOfTotal(1,6)[0]
        KHR=Ppage.get_anyKPIValueOfTotal(1,7)[0]
        VC=Ppage.get_anyKPIValueOfTotal(1,8)[0]
        KDIPhone=Ppage.get_anyKPIValueOfTotal(1,9)[0]
        RCR=Ppage.get_anyKPIValueOfTotal(1,10)[0]
        TR=Ppage.get_anyKPIValueOfTotal(1,11)[0]
        Achiev=Ppage.get_anyKPIValueOfTotal(1,12)[0]
        Goal_KPI={"NPS":NPS,"AHT":AHT,"HP":HP,"SGI":SGI,"TO":TO,"KHR":KHR,"VC":VC,
                  "KDIPhone":KDIPhone,"RCR":RCR,"TR":TR,"Achiev":Achiev}
        return Goal_KPI
    def get_PAYPAL_SITE_Data_(self):#site:lineindex=2
        Ppage=PerformancePage()
        NPS=Ppage.get_anyKPIValueOfTotal(2,2)
        AHT=Ppage.get_anyKPIValueOfTotal(2,3)
        HP=Ppage.get_anyKPIValueOfTotal(2,4)
        SGI=Ppage.get_anyKPIValueOfTotal(2,5)
        TO=Ppage.get_anyKPIValueOfTotal(2,6)
        KHR=Ppage.get_anyKPIValueOfTotal(2,7)
        VC=Ppage.get_anyKPIValueOfTotal(2,8)
        KDIPhone=Ppage.get_anyKPIValueOfTotal(2,9)
        RCR=Ppage.get_anyKPIValueOfTotal(2,10)
        TR=Ppage.get_anyKPIValueOfTotal(2,11)
        Achiev=Ppage.get_anyKPIValueOfTotal(2,12)
        SITE_KPI={"NPS":NPS,"AHT":AHT,"HP":HP,"SGI":SGI,"TO":TO,"KHR":KHR,"VC":VC,
                  "KDIPhone":KDIPhone,"RCR":RCR,"TR":TR,"Achiev":Achiev}
        return SITE_KPI
    def get_PAYPAL_TEAM_Data_(self):#TEAM:lineindex=3
        Ppage=PerformancePage()
        NPS=Ppage.get_anyKPIValueOfTotal(3,2)
        AHT=Ppage.get_anyKPIValueOfTotal(3,3)
        HP=Ppage.get_anyKPIValueOfTotal(3,4)
        SGI=Ppage.get_anyKPIValueOfTotal(3,5)
        TO=Ppage.get_anyKPIValueOfTotal(3,6)
        KHR=Ppage.get_anyKPIValueOfTotal(3,7)
        VC=Ppage.get_anyKPIValueOfTotal(3,8)
        KDIPhone=Ppage.get_anyKPIValueOfTotal(3,9)
        RCR=Ppage.get_anyKPIValueOfTotal(3,10)
        TR=Ppage.get_anyKPIValueOfTotal(3,11)
        Achiev=Ppage.get_anyKPIValueOfTotal(3,12)
        TEAM_KPI={"NPS":NPS,"AHT":AHT,"HP":HP,"SGI":SGI,"TO":TO,"KHR":KHR,"VC":VC,
                  "KDIPhone":KDIPhone,"RCR":RCR,"TR":TR,"Achiev":Achiev}
        return TEAM_KPI
    
    
    def get_Achievement_Data(self,lineindex):
        Ppage=PerformancePage()
        Achievement_Data=Ppage.get_anyKPIValueOfTotal(lineindex, 8)
        return Achievement_Data
    
    def get_PAYPAL_Agent_KPI_Actual(self,TLindex,Agentindex):
        Ppage=PerformancePage()
        NPS=Ppage.get_anyKPIofAgent_OM(TLindex,Agentindex,2)
        AHT=Ppage.get_anyKPIofAgent_OM(TLindex,Agentindex,3)
        HP=Ppage.get_anyKPIofAgent_OM(TLindex,Agentindex,4)
        SGI=Ppage.get_anyKPIofAgent_OM(TLindex,Agentindex,5)
        TO=Ppage.get_anyKPIofAgent_OM(TLindex,Agentindex,6)
        KHR=Ppage.get_anyKPIofAgent_OM(TLindex,Agentindex,7)
        VC=Ppage.get_anyKPIofAgent_OM(TLindex,Agentindex,8)
        KDIPhone=Ppage.get_anyKPIofAgent_OM(TLindex,Agentindex,9)
        RCR=Ppage.get_anyKPIofAgent_OM(TLindex,Agentindex,10)
        TR=Ppage.get_anyKPIofAgent_OM(TLindex,Agentindex,11)
        Achiev=Ppage.get_anyKPIofAgent_OM(TLindex,Agentindex,12)

        
        Agent_KPI={"NPS":NPS,"AHT":AHT,"HP":HP,"SGI":SGI,"TO":TO,"KHR":KHR,"VC":VC,
                  "KDIPhone":KDIPhone,"RCR":RCR,"TR":TR,"Achiev":Achiev}
        return Agent_KPI
    
    def get_PAYPAL_TL_KPI_Actual(self,TLindex):
        Ppage=PerformancePage()
        NPS=Ppage.get_anyKPIofTL(TLindex,2)
        AHT=Ppage.get_anyKPIofTL(TLindex,3)
        HP=Ppage.get_anyKPIofTL(TLindex,4)
        SGI=Ppage.get_anyKPIofTL(TLindex,5)
        TO=Ppage.get_anyKPIofTL(TLindex,6)
        KHR=Ppage.get_anyKPIofTL(TLindex,7)
        VC=Ppage.get_anyKPIofTL(TLindex,8)
        KDIPhone=Ppage.get_anyKPIofTL(TLindex,9)
        RCR=Ppage.get_anyKPIofTL(TLindex,10)
        TR=Ppage.get_anyKPIofTL(TLindex,11)
        Achiev=Ppage.get_anyKPIofTL(TLindex,12)
        Agent_KPI={"NPS":NPS,"AHT":AHT,"HP":HP,"SGI":SGI,"TO":TO,"KHR":KHR,"VC":VC,
                  "KDIPhone":KDIPhone,"RCR":RCR,"TR":TR,"Achiev":Achiev}
        return Agent_KPI
    def get_PAYPAL_AgentKPI_Agent_Actual(self):
        Ppage=PerformancePage()
        NPS=Ppage.get_anyKPIofAgent_Agent(2)
        AHT=Ppage.get_anyKPIofAgent_Agent(3)
        HP=Ppage.get_anyKPIofAgent_Agent(4)
        SGI=Ppage.get_anyKPIofAgent_Agent(5)
        TO=Ppage.get_anyKPIofAgent_Agent(6)
        KHR=Ppage.get_anyKPIofAgent_Agent(7)
        VC=Ppage.get_anyKPIofAgent_Agent(8)
        KDIPhone=Ppage.get_anyKPIofAgent_Agent(9)
        RCR=Ppage.get_anyKPIofAgent_Agent(10)
        TR=Ppage.get_anyKPIofAgent_Agent(11)
        Achiev=Ppage.get_anyKPIofAgent_Agent(12)
        Agent_KPI={"NPS":NPS,"AHT":AHT,"HP":HP,"SGI":SGI,"TO":TO,"KHR":KHR,"VC":VC,
                  "KDIPhone":KDIPhone,"RCR":RCR,"TR":TR,"Achiev":Achiev}
        return Agent_KPI
    
    def get_PAYPAL_AgentKPI_TL_Actual(self,Agentindex):
        Ppage=PerformancePage()
        NPS=Ppage.get_anyKPIofAgent_TL(Agentindex,2)
        AHT=Ppage.get_anyKPIofAgent_TL(Agentindex,3)
        HP=Ppage.get_anyKPIofAgent_TL(Agentindex,4)
        SGI=Ppage.get_anyKPIofAgent_TL(Agentindex,5)
        TO=Ppage.get_anyKPIofAgent_TL(Agentindex,6)
        KHR=Ppage.get_anyKPIofAgent_TL(Agentindex,7)
        VC=Ppage.get_anyKPIofAgent_TL(Agentindex,8)
        KDIPhone=Ppage.get_anyKPIofAgent_TL(Agentindex,9)
        RCR=Ppage.get_anyKPIofAgent_TL(Agentindex,10)
        TR=Ppage.get_anyKPIofAgent_TL(Agentindex,11)
        Achiev=Ppage.get_anyKPIofAgent_TL(Agentindex,12)
        Agent_KPI={"NPS":NPS,"AHT":AHT,"HP":HP,"SGI":SGI,"TO":TO,"KHR":KHR,"VC":VC,
                  "KDIPhone":KDIPhone,"RCR":RCR,"TR":TR,"Achiev":Achiev}
        return Agent_KPI
    
    
   
        
        