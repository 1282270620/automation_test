'''
Created on Apr 7, 2017

@author: symbio
'''
from Tablet_pages.PerformancPage import PerformancePage
class Get_PerformanceData_Actual_UBIZICM():
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    def get_UBIZICM_Goal_Actual(self):
        Ppage=PerformancePage()
        AvgHoldTime=Ppage.get_anyKPIValueOfTotal(1,2)[0]
        IBAHT=Ppage.get_anyKPIValueOfTotal(1,3)[0]
        CaseTocall=Ppage.get_anyKPIValueOfTotal(1,4)[0]
        Misdirects=Ppage.get_anyKPIValueOfTotal(1,5)[0]
        Ghosts=Ppage.get_anyKPIValueOfTotal(1,6)[0]
        SwitchTransfer=Ppage.get_anyKPIValueOfTotal(1,7)[0]
        DailyRepeatRate=Ppage.get_anyKPIValueOfTotal(1,8)[0]
        DispatchRateByCTV=Ppage.get_anyKPIValueOfTotal(1,9)[0]
        WFEComplianceRate=Ppage.get_anyKPIValueOfTotal(1,10)[0]
        R3AllIn=Ppage.get_anyKPIValueOfTotal(1,11)[0]
        R30AllIn=Ppage.get_anyKPIValueOfTotal(1,12)[0]
        R7AllIn=Ppage.get_anyKPIValueOfTotal(1,13)[0]
        Achiev=Ppage.get_anyKPIValueOfTotal(1,14)[0]
        Goal_KPI={"AvgHoldTime":AvgHoldTime,"IBAHT":IBAHT,"CaseTocall":CaseTocall,"Misdirects":Misdirects,"Ghosts":Ghosts,
                  "SwitchTransfer":SwitchTransfer,"DailyRepeatRate":DailyRepeatRate,"DispatchRateByCTV":DispatchRateByCTV,
                  "WFEComplianceRate":WFEComplianceRate,"R3AllIn":R3AllIn,"R30AllIn":R30AllIn,"R7AllIn":R7AllIn,"Achiev":Achiev}
        return Goal_KPI
    def get_UBIZICM_SITE_Data_(self):#site:lineindex=2
        Ppage=PerformancePage()
        AvgHoldTime=Ppage.get_anyKPIValueOfTotal(2,2)
        IBAHT=Ppage.get_anyKPIValueOfTotal(2,3)
        CaseTocall=Ppage.get_anyKPIValueOfTotal(2,4)
        Misdirects=Ppage.get_anyKPIValueOfTotal(2,5)
        Ghosts=Ppage.get_anyKPIValueOfTotal(2,6)
        SwitchTransfer=Ppage.get_anyKPIValueOfTotal(2,7)
        DailyRepeatRate=Ppage.get_anyKPIValueOfTotal(2,8)
        DispatchRateByCTV=Ppage.get_anyKPIValueOfTotal(2,9)
        WFEComplianceRate=Ppage.get_anyKPIValueOfTotal(2,10)
        R3AllIn=Ppage.get_anyKPIValueOfTotal(2,11)
        R30AllIn=Ppage.get_anyKPIValueOfTotal(2,12)
        R7AllIn=Ppage.get_anyKPIValueOfTotal(2,13)
        Achiev=Ppage.get_anyKPIValueOfTotal(2,14)
        SITE_KPI={"AvgHoldTime":AvgHoldTime,"IBAHT":IBAHT,"CaseTocall":CaseTocall,"Misdirects":Misdirects,"Ghosts":Ghosts,
                  "SwitchTransfer":SwitchTransfer,"DailyRepeatRate":DailyRepeatRate,"DispatchRateByCTV":DispatchRateByCTV,
                  "WFEComplianceRate":WFEComplianceRate,"R3AllIn":R3AllIn,"R30AllIn":R30AllIn,"R7AllIn":R7AllIn,"Achiev":Achiev}
        return SITE_KPI
    def get_UBIZICM_TEAM_Data_(self):#TEAM:lineindex=3
        Ppage=PerformancePage()
        AvgHoldTime=Ppage.get_anyKPIValueOfTotal(3,2)
        IBAHT=Ppage.get_anyKPIValueOfTotal(3,3)
        CaseTocall=Ppage.get_anyKPIValueOfTotal(3,4)
        Misdirects=Ppage.get_anyKPIValueOfTotal(3,5)
        Ghosts=Ppage.get_anyKPIValueOfTotal(3,6)
        SwitchTransfer=Ppage.get_anyKPIValueOfTotal(3,7)
        DailyRepeatRate=Ppage.get_anyKPIValueOfTotal(3,8)
        DispatchRateByCTV=Ppage.get_anyKPIValueOfTotal(3,9)
        WFEComplianceRate=Ppage.get_anyKPIValueOfTotal(3,10)
        R3AllIn=Ppage.get_anyKPIValueOfTotal(3,11)
        R30AllIn=Ppage.get_anyKPIValueOfTotal(3,12)
        R7AllIn=Ppage.get_anyKPIValueOfTotal(3,13)
        Achiev=Ppage.get_anyKPIValueOfTotal(3,14)
        TEAM_KPI={"AvgHoldTime":AvgHoldTime,"IBAHT":IBAHT,"CaseTocall":CaseTocall,"Misdirects":Misdirects,"Ghosts":Ghosts,
                  "SwitchTransfer":SwitchTransfer,"DailyRepeatRate":DailyRepeatRate,"DispatchRateByCTV":DispatchRateByCTV,
                  "WFEComplianceRate":WFEComplianceRate,"R3AllIn":R3AllIn,"R30AllIn":R30AllIn,"R7AllIn":R7AllIn,"Achiev":Achiev}
        return TEAM_KPI
    
    
    def get_Achievement_Data(self,lineindex):
        Ppage=PerformancePage()
        Achievement_Data=Ppage.get_anyKPIValueOfTotal(lineindex, 8)
        return Achievement_Data
    
    def get_UBIZICM_Agent_KPI_Actual(self,TLindex,Agentindex):
        Ppage=PerformancePage()
        AvgHoldTime=Ppage.get_anyKPIofAgent_OM(TLindex, Agentindex, 2)
        IBAHT=Ppage.get_anyKPIofAgent_OM(TLindex, Agentindex, 3)
        CaseTocall=Ppage.get_anyKPIofAgent_OM(TLindex, Agentindex, 4)
        Misdirects=Ppage.get_anyKPIofAgent_OM(TLindex, Agentindex, 5)
        Ghosts=Ppage.get_anyKPIofAgent_OM(TLindex, Agentindex, 6)
        SwitchTransfer=Ppage.get_anyKPIofAgent_OM(TLindex, Agentindex, 7)
        DailyRepeatRate=Ppage.get_anyKPIofAgent_OM(TLindex, Agentindex, 8)
        DispatchRateByCTV=Ppage.get_anyKPIofAgent_OM(TLindex, Agentindex, 9)
        WFEComplianceRate=Ppage.get_anyKPIofAgent_OM(TLindex, Agentindex,10)
        R3AllIn=Ppage.get_anyKPIofAgent_OM(TLindex, Agentindex,11)
        R30AllIn=Ppage.get_anyKPIofAgent_OM(TLindex, Agentindex,12)
        R7AllIn=Ppage.get_anyKPIofAgent_OM(TLindex, Agentindex,13)
        Achiev=Ppage.get_anyKPIofAgent_OM(TLindex, Agentindex,14)
        
        Agent_KPI={"AvgHoldTime":AvgHoldTime,"IBAHT":IBAHT,"CaseTocall":CaseTocall,"Misdirects":Misdirects,"Ghosts":Ghosts,
                  "SwitchTransfer":SwitchTransfer,"DailyRepeatRate":DailyRepeatRate,"DispatchRateByCTV":DispatchRateByCTV,
                  "WFEComplianceRate":WFEComplianceRate,"R3AllIn":R3AllIn,"R30AllIn":R30AllIn,"R7AllIn":R7AllIn,"Achiev":Achiev}
        return Agent_KPI
    
    def get_UBIZICM_TL_KPI_Actual(self,TLindex):
        Ppage=PerformancePage()
        AvgHoldTime=Ppage.get_anyKPIofTL(TLindex, 2)
        IBAHT=Ppage.get_anyKPIofTL(TLindex,3)
        CaseTocall=Ppage.get_anyKPIofTL(TLindex, 4)
        Misdirects=Ppage.get_anyKPIofTL(TLindex, 5)
        Ghosts=Ppage.get_anyKPIofTL(TLindex, 6)
        SwitchTransfer=Ppage.get_anyKPIofTL(TLindex, 7)
        DailyRepeatRate=Ppage.get_anyKPIofTL(TLindex, 8)
        DispatchRateByCTV=Ppage.get_anyKPIofTL(TLindex, 9)
        WFEComplianceRate=Ppage.get_anyKPIofTL(TLindex,10)
        R3AllIn=Ppage.get_anyKPIofTL(TLindex,11)
        R30AllIn=Ppage.get_anyKPIofTL(TLindex,12)
        R7AllIn=Ppage.get_anyKPIofTL(TLindex,13)
        Achiev=Ppage.get_anyKPIofTL(TLindex,14)
        Agent_KPI={"AvgHoldTime":AvgHoldTime,"IBAHT":IBAHT,"CaseTocall":CaseTocall,"Misdirects":Misdirects,"Ghosts":Ghosts,
                  "SwitchTransfer":SwitchTransfer,"DailyRepeatRate":DailyRepeatRate,"DispatchRateByCTV":DispatchRateByCTV,
                  "WFEComplianceRate":WFEComplianceRate,"R3AllIn":R3AllIn,"R30AllIn":R30AllIn,"R7AllIn":R7AllIn,"Achiev":Achiev}
        return Agent_KPI
    def get_UBIZICM_AgentKPI_Agent_Actual(self):
        Ppage=PerformancePage()
        AvgHoldTime=Ppage.get_anyKPIofAgent_Agent(2)
        IBAHT=Ppage.get_anyKPIofAgent_Agent(3)
        CaseTocall=Ppage.get_anyKPIofAgent_Agent(4)
        Misdirects=Ppage.get_anyKPIofAgent_Agent(5)
        Ghosts=Ppage.get_anyKPIofAgent_Agent(6)
        SwitchTransfer=Ppage.get_anyKPIofAgent_Agent(7)
        DailyRepeatRate=Ppage.get_anyKPIofAgent_Agent(8)
        DispatchRateByCTV=Ppage.get_anyKPIofAgent_Agent(9)
        WFEComplianceRate=Ppage.get_anyKPIofAgent_Agent(10)
        R3AllIn=Ppage.get_anyKPIofAgent_Agent(11)
        R30AllIn=Ppage.get_anyKPIofAgent_Agent(12)
        R7AllIn=Ppage.get_anyKPIofAgent_Agent(13)
        Achiev=Ppage.get_anyKPIofAgent_Agent(14)
        Agent_KPI={"AvgHoldTime":AvgHoldTime,"IBAHT":IBAHT,"CaseTocall":CaseTocall,"Misdirects":Misdirects,"Ghosts":Ghosts,
                  "SwitchTransfer":SwitchTransfer,"DailyRepeatRate":DailyRepeatRate,"DispatchRateByCTV":DispatchRateByCTV,
                  "WFEComplianceRate":WFEComplianceRate,"R3AllIn":R3AllIn,"R30AllIn":R30AllIn,"R7AllIn":R7AllIn,"Achiev":Achiev}
        return Agent_KPI
    
    def get_UBIZICM_AgentKPI_TL_Actual(self,Agentindex):
        Ppage=PerformancePage()
        AvgHoldTime=Ppage.get_anyKPIofAgent_TL(Agentindex,2)
        IBAHT=Ppage.get_anyKPIofAgent_TL(Agentindex,3)
        CaseTocall=Ppage.get_anyKPIofAgent_TL(Agentindex,4)
        Misdirects=Ppage.get_anyKPIofAgent_TL(Agentindex,5)
        Ghosts=Ppage.get_anyKPIofAgent_TL(Agentindex,6)
        SwitchTransfer=Ppage.get_anyKPIofAgent_TL(Agentindex,7)
        DailyRepeatRate=Ppage.get_anyKPIofAgent_TL(Agentindex,8)
        DispatchRateByCTV=Ppage.get_anyKPIofAgent_TL(Agentindex,9)
        WFEComplianceRate=Ppage.get_anyKPIofAgent_TL(Agentindex,10)
        R3AllIn=Ppage.get_anyKPIofAgent_TL(Agentindex,11)
        R30AllIn=Ppage.get_anyKPIofAgent_TL(Agentindex,12)
        R7AllIn=Ppage.get_anyKPIofAgent_TL(Agentindex,13)
        Achiev=Ppage.get_anyKPIofAgent_TL(Agentindex,14)
        Agent_KPI={"AvgHoldTime":AvgHoldTime,"IBAHT":IBAHT,"CaseTocall":CaseTocall,"Misdirects":Misdirects,"Ghosts":Ghosts,
                  "SwitchTransfer":SwitchTransfer,"DailyRepeatRate":DailyRepeatRate,"DispatchRateByCTV":DispatchRateByCTV,
                  "WFEComplianceRate":WFEComplianceRate,"R3AllIn":R3AllIn,"R30AllIn":R30AllIn,"R7AllIn":R7AllIn,"Achiev":Achiev}
        return Agent_KPI
    
    
   
        
        