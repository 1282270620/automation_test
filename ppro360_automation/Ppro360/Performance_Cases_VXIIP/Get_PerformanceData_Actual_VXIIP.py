'''
Created on Apr 7, 2017

@author: symbio
'''
from Tablet_pages.PerformancPage import PerformancePage
class Get_PerformanceData_Actual_VXIIP():
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    def get_VXIIP_Goal_Actual(self):
                                            
        Ppage=PerformancePage()
        VOC_Number=Ppage.get_anyKPIValueOfTotal(1,2)[0]
        VOC_OverallScore=Ppage.get_anyKPIValueOfTotal(1,3)[0]
        SevenDayRepeats_Repeats=Ppage.get_anyKPIValueOfTotal(1,4)[0]
        SevenDayRepeats_ManagedCalls=Ppage.get_anyKPIValueOfTotal(1,5)[0]
        SevenDayRepeats_RepeatRate=Ppage.get_anyKPIValueOfTotal(1,6)[0]
        Productivity_AHT=Ppage.get_anyKPIValueOfTotal(1,7)[0]
        Transfers=Ppage.get_anyKPIValueOfTotal(1,8)[0]
        Adjustment=Ppage.get_anyKPIValueOfTotal(1,9)[0]
        AdjustmentPerCall=Ppage.get_anyKPIValueOfTotal(1,10)[0]
        Wireless=Ppage.get_anyKPIValueOfTotal(1,11)[0]
        Broadband=Ppage.get_anyKPIValueOfTotal(1,12)[0]
        DTV=Ppage.get_anyKPIValueOfTotal(1,13)[0]
        DTV_BB_VOIP_IPTV=Ppage.get_anyKPIValueOfTotal(1,14)[0]
        Achiev=Ppage.get_anyKPIValueOfTotal(1,15)[0]
        Goal_KPI={"VOC_Number":VOC_Number,"VOC_OverallScore":VOC_OverallScore,"SevenDayRepeats_Repeats":SevenDayRepeats_Repeats,
                  "SevenDayRepeats_ManagedCalls":SevenDayRepeats_ManagedCalls,"SevenDayRepeats_RepeatRate":SevenDayRepeats_RepeatRate,
                  "Productivity_AHT":Productivity_AHT,"Transfers":Transfers,"Adjustment":Adjustment,"AdjustmentPerCall":AdjustmentPerCall,
                  "Wireless":Wireless,"Broadband":Broadband,"DTV":DTV,"DTV_BB_VOIP_IPTV":DTV_BB_VOIP_IPTV,"Achiev":Achiev}
        return Goal_KPI
    def get_VXIIP_SITE_Data_(self):#site:lineindex=2
        Ppage=PerformancePage()
        VOC_Number=Ppage.get_anyKPIValueOfTotal(2,2)
        VOC_OverallScore=Ppage.get_anyKPIValueOfTotal(2,3)
        SevenDayRepeats_Repeats=Ppage.get_anyKPIValueOfTotal(2,4)
        SevenDayRepeats_ManagedCalls =Ppage.get_anyKPIValueOfTotal(2,5)
        SevenDayRepeats_RepeatRate=Ppage.get_anyKPIValueOfTotal(2,6)
        Productivity_AHT=Ppage.get_anyKPIValueOfTotal(2,7)
        Transfers=Ppage.get_anyKPIValueOfTotal(2,8)
        Adjustment=Ppage.get_anyKPIValueOfTotal(2,9)
        AdjustmentPerCall=Ppage.get_anyKPIValueOfTotal(2,10)
        Wireless=Ppage.get_anyKPIValueOfTotal(2,11)
        Broadband=Ppage.get_anyKPIValueOfTotal(2,12)
        DTV=Ppage.get_anyKPIValueOfTotal(2,13)
        DTV_BB_VOIP_IPTV=Ppage.get_anyKPIValueOfTotal(2,14)
        Achiev=Ppage.get_anyKPIValueOfTotal(2,15)
        SITE_KPI={"VOC_Number":VOC_Number,"VOC_OverallScore":VOC_OverallScore,"SevenDayRepeats_Repeats":SevenDayRepeats_Repeats,
                  "SevenDayRepeats_ManagedCalls":SevenDayRepeats_ManagedCalls,"SevenDayRepeats_RepeatRate":SevenDayRepeats_RepeatRate,
                  "Productivity_AHT":Productivity_AHT,"Transfers":Transfers,"Adjustment":Adjustment,"AdjustmentPerCall":AdjustmentPerCall,
                  "Wireless":Wireless,"Broadband":Broadband,"DTV":DTV,"DTV_BB_VOIP_IPTV":DTV_BB_VOIP_IPTV,"Achiev":Achiev}
        return SITE_KPI
    def get_VXIIP_TEAM_Data_(self):#TEAM:lineindex=3
        Ppage=PerformancePage()
        VOC_Number=Ppage.get_anyKPIValueOfTotal(3,2)
        VOC_OverallScore=Ppage.get_anyKPIValueOfTotal(3,3)
        SevenDayRepeats_Repeats=Ppage.get_anyKPIValueOfTotal(3,4)
        SevenDayRepeats_ManagedCalls =Ppage.get_anyKPIValueOfTotal(3,5)
        SevenDayRepeats_RepeatRate=Ppage.get_anyKPIValueOfTotal(3,6)
        Productivity_AHT=Ppage.get_anyKPIValueOfTotal(3,7)
        Transfers=Ppage.get_anyKPIValueOfTotal(3,8)
        Adjustment=Ppage.get_anyKPIValueOfTotal(3,9)
        AdjustmentPerCall=Ppage.get_anyKPIValueOfTotal(3,10)
        Wireless=Ppage.get_anyKPIValueOfTotal(3,11)
        Broadband=Ppage.get_anyKPIValueOfTotal(3,12)
        DTV=Ppage.get_anyKPIValueOfTotal(3,13)
        DTV_BB_VOIP_IPTV=Ppage.get_anyKPIValueOfTotal(3,14)
        Achiev=Ppage.get_anyKPIValueOfTotal(3,15)
        TEAM_KPI={"VOC_Number":VOC_Number,"VOC_OverallScore":VOC_OverallScore,"SevenDayRepeats_Repeats":SevenDayRepeats_Repeats,
                  "SevenDayRepeats_ManagedCalls":SevenDayRepeats_ManagedCalls,"SevenDayRepeats_RepeatRate":SevenDayRepeats_RepeatRate,
                  "Productivity_AHT":Productivity_AHT,"Transfers":Transfers,"Adjustment":Adjustment,"AdjustmentPerCall":AdjustmentPerCall,
                  "Wireless":Wireless,"Broadband":Broadband,"DTV":DTV,"DTV_BB_VOIP_IPTV":DTV_BB_VOIP_IPTV,"Achiev":Achiev}
        return TEAM_KPI
    
    
    def get_Achievement_Data(self,lineindex):
        Ppage=PerformancePage()
        Achievement_Data=Ppage.get_anyKPIValueOfTotal(lineindex, 15)
        return Achievement_Data
    
    def get_VXIIP_Agent_KPI_Actual(self,TLindex,Agentindex):
        Ppage=PerformancePage()
        VOC_Number=Ppage.get_anyKPIofAgent_OM(TLindex,Agentindex,2)
        VOC_OverallScore=Ppage.get_anyKPIofAgent_OM(TLindex,Agentindex,3)
        SevenDayRepeats_Repeats=Ppage.get_anyKPIofAgent_OM(TLindex,Agentindex,4)
        SevenDayRepeats_ManagedCalls =Ppage.get_anyKPIofAgent_OM(TLindex,Agentindex,5)
        SevenDayRepeats_RepeatRate=Ppage.get_anyKPIofAgent_OM(TLindex,Agentindex,6)
        Productivity_AHT=Ppage.get_anyKPIofAgent_OM(TLindex,Agentindex,7)
        Transfers=Ppage.get_anyKPIofAgent_OM(TLindex,Agentindex,8)
        Adjustment=Ppage.get_anyKPIofAgent_OM(TLindex,Agentindex,9)
        AdjustmentPerCall=Ppage.get_anyKPIofAgent_OM(TLindex,Agentindex,10)
        Wireless=Ppage.get_anyKPIofAgent_OM(TLindex,Agentindex,11)
        Broadband=Ppage.get_anyKPIofAgent_OM(TLindex,Agentindex,12)
        DTV=Ppage.get_anyKPIofAgent_OM(TLindex,Agentindex,13)
        DTV_BB_VOIP_IPTV=Ppage.get_anyKPIofAgent_OM(TLindex,Agentindex,14)
        Achiev=Ppage.get_anyKPIofAgent_OM(TLindex,Agentindex,15)

        Agent_KPI={"VOC_Number":VOC_Number,"VOC_OverallScore":VOC_OverallScore,"SevenDayRepeats_Repeats":SevenDayRepeats_Repeats,
                  "SevenDayRepeats_ManagedCalls":SevenDayRepeats_ManagedCalls,"SevenDayRepeats_RepeatRate":SevenDayRepeats_RepeatRate,
                  "Productivity_AHT":Productivity_AHT,"Transfers":Transfers,"Adjustment":Adjustment,"AdjustmentPerCall":AdjustmentPerCall,
                  "Wireless":Wireless,"Broadband":Broadband,"DTV":DTV,"DTV_BB_VOIP_IPTV":DTV_BB_VOIP_IPTV,"Achiev":Achiev}
        return Agent_KPI
    
    def get_VXIIP_TL_KPI_Actual(self,TLindex):
        Ppage=PerformancePage()
        VOC_Number=Ppage.get_anyKPIofTL(TLindex,2)
        VOC_OverallScore=Ppage.get_anyKPIofTL(TLindex,3)
        SevenDayRepeats_Repeats=Ppage.get_anyKPIofTL(TLindex,4)
        SevenDayRepeats_ManagedCalls =Ppage.get_anyKPIofTL(TLindex,5)
        SevenDayRepeats_RepeatRate=Ppage.get_anyKPIofTL(TLindex,6)
        Productivity_AHT=Ppage.get_anyKPIofTL(TLindex,7)
        Transfers=Ppage.get_anyKPIofTL(TLindex,8)
        Adjustment=Ppage.get_anyKPIofTL(TLindex,9)
        AdjustmentPerCall=Ppage.get_anyKPIofTL(TLindex,10)
        Wireless=Ppage.get_anyKPIofTL(TLindex,11)
        Broadband=Ppage.get_anyKPIofTL(TLindex,12)
        DTV=Ppage.get_anyKPIofTL(TLindex,13)
        DTV_BB_VOIP_IPTV=Ppage.get_anyKPIofTL(TLindex,14)
        Achiev=Ppage.get_anyKPIofTL(TLindex,15)
        Agent_KPI={"VOC_Number":VOC_Number,"VOC_OverallScore":VOC_OverallScore,"SevenDayRepeats_Repeats":SevenDayRepeats_Repeats,
                  "SevenDayRepeats_ManagedCalls":SevenDayRepeats_ManagedCalls,"SevenDayRepeats_RepeatRate":SevenDayRepeats_RepeatRate,
                  "Productivity_AHT":Productivity_AHT,"Transfers":Transfers,"Adjustment":Adjustment,"AdjustmentPerCall":AdjustmentPerCall,
                  "Wireless":Wireless,"Broadband":Broadband,"DTV":DTV,"DTV_BB_VOIP_IPTV":DTV_BB_VOIP_IPTV,"Achiev":Achiev}
        return Agent_KPI
    def get_VXIIP_AgentKPI_Agent_Actual(self):
        Ppage=PerformancePage()
        VOC_Number=Ppage.get_anyKPIofAgent_Agent(2)
        VOC_OverallScore=Ppage.get_anyKPIofAgent_Agent(3)
        SevenDayRepeats_Repeats=Ppage.get_anyKPIofAgent_Agent(4)
        SevenDayRepeats_ManagedCalls =Ppage.get_anyKPIofAgent_Agent(5)
        SevenDayRepeats_RepeatRate=Ppage.get_anyKPIofAgent_Agent(6)
        Productivity_AHT=Ppage.get_anyKPIofAgent_Agent(7)
        Transfers=Ppage.get_anyKPIofAgent_Agent(8)
        Adjustment=Ppage.get_anyKPIofAgent_Agent(9)
        AdjustmentPerCall=Ppage.get_anyKPIofAgent_Agent(10)
        Wireless=Ppage.get_anyKPIofAgent_Agent(11)
        Broadband=Ppage.get_anyKPIofAgent_Agent(12)
        DTV=Ppage.get_anyKPIofAgent_Agent(13)
        DTV_BB_VOIP_IPTV=Ppage.get_anyKPIofAgent_Agent(14)
        Achiev=Ppage.get_anyKPIofAgent_Agent(15)
        Agent_KPI={"VOC_Number":VOC_Number,"VOC_OverallScore":VOC_OverallScore,"SevenDayRepeats_Repeats":SevenDayRepeats_Repeats,
                  "SevenDayRepeats_ManagedCalls":SevenDayRepeats_ManagedCalls,"SevenDayRepeats_RepeatRate":SevenDayRepeats_RepeatRate,
                  "Productivity_AHT":Productivity_AHT,"Transfers":Transfers,"Adjustment":Adjustment,"AdjustmentPerCall":AdjustmentPerCall,
                  "Wireless":Wireless,"Broadband":Broadband,"DTV":DTV,"DTV_BB_VOIP_IPTV":DTV_BB_VOIP_IPTV,"Achiev":Achiev}
        return Agent_KPI
    
    def get_VXIIP_AgentKPI_TL_Actual(self,Agentindex):
        Ppage=PerformancePage()
        VOC_Number=Ppage.get_anyKPIofAgent_TL(Agentindex,2)
        VOC_OverallScore=Ppage.get_anyKPIofAgent_TL(Agentindex,3)
        SevenDayRepeats_Repeats=Ppage.get_anyKPIofAgent_TL(Agentindex,4)
        SevenDayRepeats_ManagedCalls =Ppage.get_anyKPIofAgent_TL(Agentindex,5)
        SevenDayRepeats_RepeatRate=Ppage.get_anyKPIofAgent_TL(Agentindex,6)
        Productivity_AHT=Ppage.get_anyKPIofAgent_TL(Agentindex,7)
        Transfers=Ppage.get_anyKPIofAgent_TL(Agentindex,8)
        Adjustment=Ppage.get_anyKPIofAgent_TL(Agentindex,9)
        AdjustmentPerCall=Ppage.get_anyKPIofAgent_TL(Agentindex,10)
        Wireless=Ppage.get_anyKPIofAgent_TL(Agentindex,11)
        Broadband=Ppage.get_anyKPIofAgent_TL(Agentindex,12)
        DTV=Ppage.get_anyKPIofAgent_TL(Agentindex,13)
        DTV_BB_VOIP_IPTV=Ppage.get_anyKPIofAgent_TL(Agentindex,14)
        Achiev=Ppage.get_anyKPIofAgent_TL(Agentindex,15)

        Agent_KPI={"VOC_Number":VOC_Number,"VOC_OverallScore":VOC_OverallScore,"SevenDayRepeats_Repeats":SevenDayRepeats_Repeats,
                  "SevenDayRepeats_ManagedCalls":SevenDayRepeats_ManagedCalls,"SevenDayRepeats_RepeatRate":SevenDayRepeats_RepeatRate,
                  "Productivity_AHT":Productivity_AHT,"Transfers":Transfers,"Adjustment":Adjustment,"AdjustmentPerCall":AdjustmentPerCall,
                  "Wireless":Wireless,"Broadband":Broadband,"DTV":DTV,"DTV_BB_VOIP_IPTV":DTV_BB_VOIP_IPTV,"Achiev":Achiev}
        return Agent_KPI
    
    
   
        
        