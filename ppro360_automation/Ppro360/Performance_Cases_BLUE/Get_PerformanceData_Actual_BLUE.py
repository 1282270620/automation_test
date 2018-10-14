'''
Created on Apr 7, 2017

@author: symbio
'''
from Tablet_pages.PerformancPage import PerformancePage
class Get_PerformanceData_Actual_BLUE():
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    def get_BLUE_Goal_Actual(self):
        Ppage=PerformancePage()
        Goal_lsit=Ppage.get_AllKPIsofGoal_list(14)
        for i in range(0,len(Goal_lsit)):
            if '\n' in Goal_lsit[i]:
                Goal_lsit[i]=Goal_lsit[i].split('\n')
        VOC=Goal_lsit[1]
        SevenDayRepeats=Goal_lsit[2]
        AHT=Goal_lsit[3]
               
        Transfer=Goal_lsit[4]
        
        a=Goal_lsit[5][0].replace("$","")
        b=Goal_lsit[5][1].replace("$","")
        DTV=[a,b]
        
        c=Goal_lsit[6][0].replace("$","")
        d=Goal_lsit[6][1].replace("$","")
        IPBB=[c,d]
        
        
        VOIP=Goal_lsit[7]
        
        e=Goal_lsit[8][0].replace("$","")
        f=Goal_lsit[8][1].replace("$","")
        Wireless=[e,f]
        
        Adjustment=Goal_lsit[9]
        
        Achiev=Goal_lsit[10]
        
        Goal_KPI={"VOC":VOC,"SevenDayRepeats":SevenDayRepeats,"AHT":AHT,"Transfer":Transfer,"DTV":DTV,"IPBB":IPBB,
                  "VOIP":VOIP,"Wireless":Wireless,"Adjustment":Adjustment,"Achiev":Achiev}
        return Goal_KPI
    def get_BLUE_SITE_Data_(self):#site:lineindex=2
        Ppage=PerformancePage()
        VOC=Ppage.get_anyKPIValueOfTotal(2,2)
        SevenDayRepeats=Ppage.get_anyKPIValueOfTotal(2,3)
        AHT=Ppage.get_anyKPIValueOfTotal(2,4)
        Transfer=Ppage.get_anyKPIValueOfTotal(2,5)
        DTV=Ppage.get_anyKPIValueOfTotal(2,6)
        IPBB=Ppage.get_anyKPIValueOfTotal(2,7)
        VOIP=Ppage.get_anyKPIValueOfTotal(2,8)
        Wireless=Ppage.get_anyKPIValueOfTotal(2,9)
        Adjustment=Ppage.get_anyKPIValueOfTotal(2,10)
        Achiev=Ppage.get_anyKPIValueOfTotal(2,11)
        SITE_KPI={"VOC":VOC,"SevenDayRepeats":SevenDayRepeats,"AHT":AHT,"Transfer":Transfer,"DTV":DTV,"IPBB":IPBB,
                  "VOIP":VOIP,"Wireless":Wireless,"Adjustment":Adjustment,"Achiev":Achiev}
        return SITE_KPI
    def get_BLUE_TEAM_Data_(self):#TEAM:lineindex=3
        Ppage=PerformancePage()
        VOC=Ppage.get_anyKPIValueOfTotal(3,2)
        SevenDayRepeats=Ppage.get_anyKPIValueOfTotal(3,3)
        AHT=Ppage.get_anyKPIValueOfTotal(3,4)
        Transfer=Ppage.get_anyKPIValueOfTotal(3,5)
        DTV=Ppage.get_anyKPIValueOfTotal(3,6)
        IPBB=Ppage.get_anyKPIValueOfTotal(3,7)
        VOIP=Ppage.get_anyKPIValueOfTotal(3,8)
        Wireless=Ppage.get_anyKPIValueOfTotal(3,9)
        Adjustment=Ppage.get_anyKPIValueOfTotal(3,10)
        Achiev=Ppage.get_anyKPIValueOfTotal(3,11)
        TEAM_KPI={"VOC":VOC,"SevenDayRepeats":SevenDayRepeats,"AHT":AHT,"Transfer":Transfer,"DTV":DTV,"IPBB":IPBB,
                  "VOIP":VOIP,"Wireless":Wireless,"Adjustment":Adjustment,"Achiev":Achiev}
        return TEAM_KPI
    
    
    def get_Achievement_Data(self,lineindex):
        Ppage=PerformancePage()
        Achievement_Data=Ppage.get_anyKPIValueOfTotal(lineindex, 11)
        return Achievement_Data
    
    def get_BLUE_Agent_KPI_Actual(self,TLindex,Agentindex):
        Ppage=PerformancePage()
        VOC=Ppage.get_anyKPIofAgent_OM(TLindex, Agentindex,2)
        SevenDayRepeats=Ppage.get_anyKPIofAgent_OM(TLindex, Agentindex,3)
        AHT=Ppage.get_anyKPIofAgent_OM(TLindex, Agentindex,4)
        Transfer=Ppage.get_anyKPIofAgent_OM(TLindex, Agentindex,5)
        DTV=Ppage.get_anyKPIofAgent_OM(TLindex, Agentindex,6)
        IPBB=Ppage.get_anyKPIofAgent_OM(TLindex, Agentindex,7)
        VOIP=Ppage.get_anyKPIofAgent_OM(TLindex, Agentindex,8)
        Wireless=Ppage.get_anyKPIofAgent_OM(TLindex, Agentindex,9)
        Adjustment=Ppage.get_anyKPIofAgent_OM(TLindex, Agentindex,10)
        Achiev=Ppage.get_anyKPIofAgent_OM(TLindex, Agentindex,11)
        Agent_KPI={"VOC":VOC,"SevenDayRepeats":SevenDayRepeats,"AHT":AHT,"Transfer":Transfer,"DTV":DTV,"IPBB":IPBB,
                  "VOIP":VOIP,"Wireless":Wireless,"Adjustment":Adjustment,"Achiev":Achiev}
        return Agent_KPI
    
    
    
    
    def get_BLUE_TL_KPI_Actual(self,TLindex):
        Ppage=PerformancePage()
        VOC=Ppage.get_anyKPIofTL(TLindex,2)
        SevenDayRepeats=Ppage.get_anyKPIofTL(TLindex,3)
        AHT=Ppage.get_anyKPIofTL(TLindex,4)
        Transfer=Ppage.get_anyKPIofTL(TLindex,5)
        DTV=Ppage.get_anyKPIofTL(TLindex,6)
        IPBB=Ppage.get_anyKPIofTL(TLindex,7)
        VOIP=Ppage.get_anyKPIofTL(TLindex,8)
        Wireless=Ppage.get_anyKPIofTL(TLindex,9)
        Adjustment=Ppage.get_anyKPIofTL(TLindex,10)
        Achiev=Ppage.get_anyKPIofTL(TLindex,11)

        Agent_KPI={"VOC":VOC,"SevenDayRepeats":SevenDayRepeats,"AHT":AHT,"Transfer":Transfer,"DTV":DTV,"IPBB":IPBB,
                  "VOIP":VOIP,"Wireless":Wireless,"Adjustment":Adjustment,"Achiev":Achiev}
        
        for key in Agent_KPI:
            if '\n' in Agent_KPI[key]:
                Agent_KPI[key]=Agent_KPI[key].split('\n')
                Agent_KPI[key][1]=Agent_KPI[key][1].replace('(','').replace(')','')
                
        return Agent_KPI
    def get_BLUE_AgentKPI_Agent_Actual(self):
        Ppage=PerformancePage()
        VOC=Ppage.get_anyKPIofAgent_Agent(2)
        SevenDayRepeats=Ppage.get_anyKPIofAgent_Agent(3)
        AHT=Ppage.get_anyKPIofAgent_Agent(4)
        Transfer=Ppage.get_anyKPIofAgent_Agent(5)
        DTV=Ppage.get_anyKPIofAgent_Agent(6)
        IPBB=Ppage.get_anyKPIofAgent_Agent(7)
        VOIP=Ppage.get_anyKPIofAgent_Agent(8)
        Wireless=Ppage.get_anyKPIofAgent_Agent(9)
        Adjustment=Ppage.get_anyKPIofAgent_Agent(10)
        Achiev=Ppage.get_anyKPIofAgent_Agent(11)
        Agent_KPI={"VOC":VOC,"SevenDayRepeats":SevenDayRepeats,"AHT":AHT,"Transfer":Transfer,"DTV":DTV,"IPBB":IPBB,
                  "VOIP":VOIP,"Wireless":Wireless,"Adjustment":Adjustment,"Achiev":Achiev}
        return Agent_KPI
    
    def get_BLUE_AgentKPI_TL_Actual(self,Agentindex):
        Ppage=PerformancePage()
        VOC=Ppage.get_anyKPIofAgent_TL(Agentindex,2)
        SevenDayRepeats=Ppage.get_anyKPIofAgent_TL(Agentindex,3)
        AHT=Ppage.get_anyKPIofAgent_TL(Agentindex,4)
        Transfer=Ppage.get_anyKPIofAgent_TL(Agentindex,5)
        DTV=Ppage.get_anyKPIofAgent_TL(Agentindex,6)
        IPBB=Ppage.get_anyKPIofAgent_TL(Agentindex,7)
        VOIP=Ppage.get_anyKPIofAgent_TL(Agentindex,8)
        Wireless=Ppage.get_anyKPIofAgent_TL(Agentindex,9)
        Adjustment=Ppage.get_anyKPIofAgent_TL(Agentindex,10)
        Achiev=Ppage.get_anyKPIofAgent_TL(Agentindex,11)
        Agent_KPI={"VOC":VOC,"SevenDayRepeats":SevenDayRepeats,"AHT":AHT,"Transfer":Transfer,"DTV":DTV,"IPBB":IPBB,
                  "VOIP":VOIP,"Wireless":Wireless,"Adjustment":Adjustment,"Achiev":Achiev}
        return Agent_KPI
    
  
        
        
        