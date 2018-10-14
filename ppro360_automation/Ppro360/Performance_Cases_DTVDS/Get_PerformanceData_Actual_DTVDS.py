'''
Created on 2017.9.20

@author: yalan.yin
'''
from Tablet_pages.PerformancPage import PerformancePage

class Get_PerformanceData_Actual_DTVDS(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    def get_DTVDS_Goal_Actual(self):
        Ppage=PerformancePage()
        CloseRate=Ppage.get_anyKPIValueOfTotal(1,2)[0]
        VideoActivations=Ppage.get_anyKPIValueOfTotal(1,3)[0]
        IPPBAttachRate=Ppage.get_anyKPIValueOfTotal(1,4)[0]
        IPPBGrossSales=Ppage.get_anyKPIValueOfTotal(1,5)[0]
        MobilitySales=Ppage.get_anyKPIValueOfTotal(1,6)[0]
        OverallCallExp=Ppage.get_anyKPIValueOfTotal(1,7)[0]
        CC=Ppage.get_anyKPIValueOfTotal(1,8)[0]
        NFCR=Ppage.get_anyKPIValueOfTotal(1,9)[0]
        AHT=Ppage.get_anyKPIValueOfTotal(1,10)[0]
        CancelRate=Ppage.get_anyKPIValueOfTotal(1,11)[0]
        Achiev=Ppage.get_anyKPIValueOfTotal(1,12)[0]
        Goal_KPI={'CancelRate':CancelRate,'NFCR':NFCR,'CC':CC,'VideoActivations':VideoActivations,'OverallCallExp':OverallCallExp,'IPPBAttachRate':IPPBAttachRate,'IPPBGrossSales':IPPBGrossSales,'AHT':AHT,'CloseRate':CloseRate,'MobilitySales':MobilitySales,'Achiev':Achiev}
        return Goal_KPI
 
    def get_DTVDS_SITE_Data_(self):
        Ppage=PerformancePage()
        CloseRate=Ppage.get_anyKPIValueOfTotal(2,2)
        VideoActivations=Ppage.get_anyKPIValueOfTotal(2,3)
        IPPBAttachRate=Ppage.get_anyKPIValueOfTotal(2,4)
        IPPBGrossSales=Ppage.get_anyKPIValueOfTotal(2,5)
        MobilitySales=Ppage.get_anyKPIValueOfTotal(2,6)
        OverallCallExp=Ppage.get_anyKPIValueOfTotal(2,7)
        CC=Ppage.get_anyKPIValueOfTotal(2,8)
        NFCR=Ppage.get_anyKPIValueOfTotal(2,9)
        AHT=Ppage.get_anyKPIValueOfTotal(2,10)
        CancelRate=Ppage.get_anyKPIValueOfTotal(2,11)
        Achiev=Ppage.get_anyKPIValueOfTotal(2,12)
        SITE_KPI={'CancelRate':CancelRate,'NFCR':NFCR,'CC':CC,'VideoActivations':VideoActivations,'OverallCallExp':OverallCallExp,'IPPBAttachRate':IPPBAttachRate,'IPPBGrossSales':IPPBGrossSales,'AHT':AHT,'CloseRate':CloseRate,'MobilitySales':MobilitySales,'Achiev':Achiev}
        return SITE_KPI
    
    def get_DTVDS_TEAM_Data_(self):
        Ppage=PerformancePage()
        CloseRate=Ppage.get_anyKPIValueOfTotal(3,2)
        VideoActivations=Ppage.get_anyKPIValueOfTotal(3,3)
        IPPBAttachRate=Ppage.get_anyKPIValueOfTotal(3,4)
        IPPBGrossSales=Ppage.get_anyKPIValueOfTotal(3,5)
        MobilitySales=Ppage.get_anyKPIValueOfTotal(3,6)
        OverallCallExp=Ppage.get_anyKPIValueOfTotal(3,7)
        CC=Ppage.get_anyKPIValueOfTotal(3,8)
        NFCR=Ppage.get_anyKPIValueOfTotal(3,9)
        AHT=Ppage.get_anyKPIValueOfTotal(3,10)
        CancelRate=Ppage.get_anyKPIValueOfTotal(3,11)
        Achiev=Ppage.get_anyKPIValueOfTotal(3,12)
        TEAM_KPI={'CancelRate':CancelRate,'NFCR':NFCR,'CC':CC,'VideoActivations':VideoActivations,'OverallCallExp':OverallCallExp,'IPPBAttachRate':IPPBAttachRate,'IPPBGrossSales':IPPBGrossSales,'AHT':AHT,'CloseRate':CloseRate,'MobilitySales':MobilitySales,'Achiev':Achiev}
        return TEAM_KPI
 
    def get_Achievement_Data(self,lineindex): #this method may be not used
        Ppage=PerformancePage()
        Achievement_Data=Ppage.get_anyKPIValueOfTotal(lineindex, 12)
        return Achievement_Data
 
    def get_DTVDS_Agent_KPI_Actual(self,TLindex,Agentindex):
        Ppage=PerformancePage()
        CloseRate=Ppage.get_anyKPIofAgent_OM(TLindex, Agentindex, 2)
        VideoActivations=Ppage.get_anyKPIofAgent_OM(TLindex, Agentindex, 3)
        IPPBAttachRate=Ppage.get_anyKPIofAgent_OM(TLindex, Agentindex, 4)
        IPPBGrossSales=Ppage.get_anyKPIofAgent_OM(TLindex, Agentindex, 5)
        MobilitySales=Ppage.get_anyKPIofAgent_OM(TLindex, Agentindex, 6)
        OverallCallExp=Ppage.get_anyKPIofAgent_OM(TLindex, Agentindex, 7)
        CC=Ppage.get_anyKPIofAgent_OM(TLindex, Agentindex, 8)
        NFCR=Ppage.get_anyKPIofAgent_OM(TLindex, Agentindex, 9)
        AHT=Ppage.get_anyKPIofAgent_OM(TLindex, Agentindex, 10)
        CancelRate=Ppage.get_anyKPIofAgent_OM(TLindex, Agentindex, 11)        
        Achiev=Ppage.get_anyKPIofAgent_OM(TLindex, Agentindex, 12)
        Agent_KPI={'CancelRate':CancelRate,'NFCR':NFCR,'CC':CC,'VideoActivations':VideoActivations,'OverallCallExp':OverallCallExp,'IPPBAttachRate':IPPBAttachRate,'IPPBGrossSales':IPPBGrossSales,'AHT':AHT,'CloseRate':CloseRate,'MobilitySales':MobilitySales,'Achiev':Achiev}
        return Agent_KPI
    
    def get_DTVDS_TL_KPI_Actual(self,TLindex):
        Ppage=PerformancePage()
        CloseRate=Ppage.get_anyKPIofTL(TLindex, 2)
        VideoActivations=Ppage.get_anyKPIofTL(TLindex, 3)
        IPPBAttachRate=Ppage.get_anyKPIofTL(TLindex, 4)
        IPPBGrossSales=Ppage.get_anyKPIofTL(TLindex, 5)
        MobilitySales=Ppage.get_anyKPIofTL(TLindex, 6)
        OverallCallExp=Ppage.get_anyKPIofTL(TLindex, 7)
        CC=Ppage.get_anyKPIofTL(TLindex, 8)
        NFCR=Ppage.get_anyKPIofTL(TLindex, 9)
        AHT=Ppage.get_anyKPIofTL(TLindex, 10)
        CancelRate=Ppage.get_anyKPIofTL(TLindex, 11)
        Achiev=Ppage.get_anyKPIofTL(TLindex, 12)
        Agent_KPI={'CancelRate':CancelRate,'NFCR':NFCR,'CC':CC,'VideoActivations':VideoActivations,'OverallCallExp':OverallCallExp,'IPPBAttachRate':IPPBAttachRate,'IPPBGrossSales':IPPBGrossSales,'AHT':AHT,'CloseRate':CloseRate,'MobilitySales':MobilitySales,'Achiev':Achiev}
        return Agent_KPI
    
    def get_DTVDS_AgentKPI_Agent_Actual(self):
        Ppage=PerformancePage()
        CloseRate=Ppage.get_anyKPIofAgent_Agent(2)
        VideoActivations=Ppage.get_anyKPIofAgent_Agent(3)
        IPPBAttachRate=Ppage.get_anyKPIofAgent_Agent(4)
        IPPBGrossSales=Ppage.get_anyKPIofAgent_Agent(5)
        MobilitySales=Ppage.get_anyKPIofAgent_Agent(6)
        OverallCallExp=Ppage.get_anyKPIofAgent_Agent(7)
        CC=Ppage.get_anyKPIofAgent_Agent(8)
        NFCR=Ppage.get_anyKPIofAgent_Agent(9)
        AHT=Ppage.get_anyKPIofAgent_Agent(10)
        CancelRate=Ppage.get_anyKPIofAgent_Agent(11)
        Achiev=Ppage.get_anyKPIofAgent_Agent(12)
        Agent_KPI={'CancelRate':CancelRate,'NFCR':NFCR,'CC':CC,'VideoActivations':VideoActivations,'OverallCallExp':OverallCallExp,'IPPBAttachRate':IPPBAttachRate,'IPPBGrossSales':IPPBGrossSales,'AHT':AHT,'CloseRate':CloseRate,'MobilitySales':MobilitySales,'Achiev':Achiev}
        return Agent_KPI
    
    def get_DTVDS_AgentKPI_TL_Actual(self,Agentindex):
        Ppage=PerformancePage()
        CloseRate=Ppage.get_anyKPIofAgent_TL(Agentindex, 2)
        VideoActivations=Ppage.get_anyKPIofAgent_TL(Agentindex, 3)
        IPPBAttachRate=Ppage.get_anyKPIofAgent_TL(Agentindex, 4)
        IPPBGrossSales=Ppage.get_anyKPIofAgent_TL(Agentindex, 5)
        MobilitySales=Ppage.get_anyKPIofAgent_TL(Agentindex, 6)
        OverallCallExp=Ppage.get_anyKPIofAgent_TL(Agentindex, 7)
        CC=Ppage.get_anyKPIofAgent_TL(Agentindex, 8)
        NFCR=Ppage.get_anyKPIofAgent_TL(Agentindex, 9)
        AHT=Ppage.get_anyKPIofAgent_TL(Agentindex, 10)
        CancelRate=Ppage.get_anyKPIofAgent_TL(Agentindex, 11)
        Achiev=Ppage.get_anyKPIofAgent_TL(Agentindex, 12)
        Agent_KPI={'CancelRate':CancelRate,'NFCR':NFCR,'CC':CC,'VideoActivations':VideoActivations,'OverallCallExp':OverallCallExp,'IPPBAttachRate':IPPBAttachRate,'IPPBGrossSales':IPPBGrossSales,'AHT':AHT,'CloseRate':CloseRate,'MobilitySales':MobilitySales,'Achiev':Achiev}
        return Agent_KPI

        