'''
Created on Apr 7, 2017

@author: symbio
'''
from Tablet_pages.PerformancPage import PerformancePage
class Get_PerformanceData_Actual_CENTURYLINK():
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    def get_CENTURYLINK_Goal_Actual(self):
                                            
        Ppage=PerformancePage()
        AttainmenttoGoal_HSI=Ppage.get_anyKPIValueOfTotal(1,2)[0]
        B2P=Ppage.get_anyKPIValueOfTotal(1,3)[0]
        AHT=Ppage.get_anyKPIValueOfTotal(1,4)[0]
        Hold=Ppage.get_anyKPIValueOfTotal(1,5)[0]
        AbsAbsenteeism=Ppage.get_anyKPIValueOfTotal(1,6)[0]
        AvgQAScore=Ppage.get_anyKPIValueOfTotal(1,7)[0]
        QACalls=Ppage.get_anyKPIValueOfTotal(1,8)[0]
        ofAutoFails=Ppage.get_anyKPIValueOfTotal(1,9)[0]
        MixClose_HSI=Ppage.get_anyKPIValueOfTotal(1,10)[0]
        AttainmenttoGoal_HSI_1=Ppage.get_anyKPIValueOfTotal(1,11)[0]
        MixClose_TV=Ppage.get_anyKPIValueOfTotal(1,12)[0]
        AttainmenttoGoal_TV=Ppage.get_anyKPIValueOfTotal(1,13)[0]
        AttachRate_DTV=Ppage.get_anyKPIValueOfTotal(1,14)[0]
        MixClose_PhoneLines=Ppage.get_anyKPIValueOfTotal(1,15)[0]
        MixClose_Ease=Ppage.get_anyKPIValueOfTotal(1,16)[0]
        ACDCalls=Ppage.get_anyKPIValueOfTotal(1,17)[0]
        AHTIneligible=Ppage.get_anyKPIValueOfTotal(1,18)[0]
        QualifiedCloseRate=Ppage.get_anyKPIValueOfTotal(1,19)[0]
        Achiev=Ppage.get_anyKPIValueOfTotal(1,20)[0]
        Goal_KPI={"AttainmenttoGoal_HSI":AttainmenttoGoal_HSI,"B2P":B2P,"AHT":AHT,"Hold":Hold,"AbsAbsenteeism":AbsAbsenteeism,
                  "AvgQAScore":AvgQAScore,"QACalls":QACalls,"ofAutoFails":ofAutoFails,"MixClose_HSI":MixClose_HSI,
                  "AttainmenttoGoal_HSI_1":AttainmenttoGoal_HSI_1,"MixClose_TV":MixClose_TV,"AttainmenttoGoal_TV":AttainmenttoGoal_TV,
                  "AttachRate_DTV":AttachRate_DTV,"MixClose_PhoneLines":MixClose_PhoneLines,"MixClose_Ease":MixClose_Ease,
                  "ACDCalls":ACDCalls,"AHTIneligible":AHTIneligible,"QualifiedCloseRate":QualifiedCloseRate,"Achiev":Achiev}
        return Goal_KPI
    def get_CENTURYLINK_SITE_Data_(self):#site:lineindex=2
        Ppage=PerformancePage()
        AttainmenttoGoal_HSI=Ppage.get_anyKPIValueOfTotal(2,2)
        B2P=Ppage.get_anyKPIValueOfTotal(2,3)
        AHT=Ppage.get_anyKPIValueOfTotal(2,4)
        Hold=Ppage.get_anyKPIValueOfTotal(2,5)
        AbsAbsenteeism=Ppage.get_anyKPIValueOfTotal(2,6)
        AvgQAScore=Ppage.get_anyKPIValueOfTotal(2,7)
        QACalls=Ppage.get_anyKPIValueOfTotal(2,8)
        ofAutoFails=Ppage.get_anyKPIValueOfTotal(2,9)
        MixClose_HSI=Ppage.get_anyKPIValueOfTotal(2,10)
        AttainmenttoGoal_HSI_1=Ppage.get_anyKPIValueOfTotal(2,11)
        MixClose_TV=Ppage.get_anyKPIValueOfTotal(2,12)
        AttainmenttoGoal_TV=Ppage.get_anyKPIValueOfTotal(2,13)
        AttachRate_DTV=Ppage.get_anyKPIValueOfTotal(2,14)
        MixClose_PhoneLines=Ppage.get_anyKPIValueOfTotal(2,15)
        MixClose_Ease=Ppage.get_anyKPIValueOfTotal(2,16)
        ACDCalls=Ppage.get_anyKPIValueOfTotal(2,17)
        AHTIneligible=Ppage.get_anyKPIValueOfTotal(2,18)
        QualifiedCloseRate=Ppage.get_anyKPIValueOfTotal(2,19)
        Achiev=Ppage.get_anyKPIValueOfTotal(2,20)

        SITE_KPI={"AttainmenttoGoal_HSI":AttainmenttoGoal_HSI,"B2P":B2P,"AHT":AHT,"Hold":Hold,"AbsAbsenteeism":AbsAbsenteeism,
                  "AvgQAScore":AvgQAScore,"QACalls":QACalls,"ofAutoFails":ofAutoFails,"MixClose_HSI":MixClose_HSI,
                  "AttainmenttoGoal_HSI_1":AttainmenttoGoal_HSI_1,"MixClose_TV":MixClose_TV,"AttainmenttoGoal_TV":AttainmenttoGoal_TV,
                  "AttachRate_DTV":AttachRate_DTV,"MixClose_PhoneLines":MixClose_PhoneLines,"MixClose_Ease":MixClose_Ease,
                  "ACDCalls":ACDCalls,"AHTIneligible":AHTIneligible,"QualifiedCloseRate":QualifiedCloseRate,"Achiev":Achiev}
        return SITE_KPI
    def get_CENTURYLINK_TEAM_Data_(self):#TEAM:lineindex=3
        Ppage=PerformancePage()
        AttainmenttoGoal_HSI=Ppage.get_anyKPIValueOfTotal(3,2)
        B2P=Ppage.get_anyKPIValueOfTotal(3,3)
        AHT=Ppage.get_anyKPIValueOfTotal(3,4)
        Hold=Ppage.get_anyKPIValueOfTotal(3,5)
        AbsAbsenteeism=Ppage.get_anyKPIValueOfTotal(3,6)
        AvgQAScore=Ppage.get_anyKPIValueOfTotal(3,7)
        QACalls=Ppage.get_anyKPIValueOfTotal(3,8)
        ofAutoFails=Ppage.get_anyKPIValueOfTotal(3,9)
        MixClose_HSI=Ppage.get_anyKPIValueOfTotal(3,10)
        AttainmenttoGoal_HSI_1=Ppage.get_anyKPIValueOfTotal(3,11)
        MixClose_TV=Ppage.get_anyKPIValueOfTotal(3,12)
        AttainmenttoGoal_TV=Ppage.get_anyKPIValueOfTotal(3,13)
        AttachRate_DTV=Ppage.get_anyKPIValueOfTotal(3,14)
        MixClose_PhoneLines=Ppage.get_anyKPIValueOfTotal(3,15)
        MixClose_Ease=Ppage.get_anyKPIValueOfTotal(3,16)
        ACDCalls=Ppage.get_anyKPIValueOfTotal(3,17)
        AHTIneligible=Ppage.get_anyKPIValueOfTotal(3,18)
        QualifiedCloseRate=Ppage.get_anyKPIValueOfTotal(3,19)
        Achiev=Ppage.get_anyKPIValueOfTotal(3,20)

        TEAM_KPI={"AttainmenttoGoal_HSI":AttainmenttoGoal_HSI,"B2P":B2P,"AHT":AHT,"Hold":Hold,"AbsAbsenteeism":AbsAbsenteeism,
                  "AvgQAScore":AvgQAScore,"QACalls":QACalls,"ofAutoFails":ofAutoFails,"MixClose_HSI":MixClose_HSI,
                  "AttainmenttoGoal_HSI_1":AttainmenttoGoal_HSI_1,"MixClose_TV":MixClose_TV,"AttainmenttoGoal_TV":AttainmenttoGoal_TV,
                  "AttachRate_DTV":AttachRate_DTV,"MixClose_PhoneLines":MixClose_PhoneLines,"MixClose_Ease":MixClose_Ease,
                  "ACDCalls":ACDCalls,"AHTIneligible":AHTIneligible,"QualifiedCloseRate":QualifiedCloseRate,"Achiev":Achiev}
        return TEAM_KPI
    
    
    def get_Achievement_Data(self,lineindex):
        Ppage=PerformancePage()
        Achievement_Data=Ppage.get_anyKPIValueOfTotal(lineindex, 8)
        return Achievement_Data
    
    def get_CENTURYLINK_Agent_KPI_Actual(self,TLindex,Agentindex):
        Ppage=PerformancePage()
        AttainmenttoGoal_HSI=Ppage.get_anyKPIofAgent_OM(TLindex,Agentindex,2)
        B2P=Ppage.get_anyKPIofAgent_OM(TLindex,Agentindex,3)
        AHT=Ppage.get_anyKPIofAgent_OM(TLindex,Agentindex,4)
        Hold=Ppage.get_anyKPIofAgent_OM(TLindex,Agentindex,5)
        AbsAbsenteeism=Ppage.get_anyKPIofAgent_OM(TLindex,Agentindex,6)
        AvgQAScore=Ppage.get_anyKPIofAgent_OM(TLindex,Agentindex,7)
        QACalls=Ppage.get_anyKPIofAgent_OM(TLindex,Agentindex,8)
        ofAutoFails=Ppage.get_anyKPIofAgent_OM(TLindex,Agentindex,9)
        MixClose_HSI=Ppage.get_anyKPIofAgent_OM(TLindex,Agentindex,10)
        AttainmenttoGoal_HSI_1=Ppage.get_anyKPIofAgent_OM(TLindex,Agentindex,11)
        MixClose_TV=Ppage.get_anyKPIofAgent_OM(TLindex,Agentindex,12)
        AttainmenttoGoal_TV=Ppage.get_anyKPIofAgent_OM(TLindex,Agentindex,13)
        AttachRate_DTV=Ppage.get_anyKPIofAgent_OM(TLindex,Agentindex,14)
        MixClose_PhoneLines=Ppage.get_anyKPIofAgent_OM(TLindex,Agentindex,15)
        MixClose_Ease=Ppage.get_anyKPIofAgent_OM(TLindex,Agentindex,16)
        ACDCalls=Ppage.get_anyKPIofAgent_OM(TLindex,Agentindex,17)
        AHTIneligible=Ppage.get_anyKPIofAgent_OM(TLindex,Agentindex,18)
        QualifiedCloseRate=Ppage.get_anyKPIofAgent_OM(TLindex,Agentindex,19)
        Achiev=Ppage.get_anyKPIofAgent_OM(TLindex,Agentindex,20)

        Agent_KPI={"AttainmenttoGoal_HSI":AttainmenttoGoal_HSI,"B2P":B2P,"AHT":AHT,"Hold":Hold,"AbsAbsenteeism":AbsAbsenteeism,
                  "AvgQAScore":AvgQAScore,"QACalls":QACalls,"ofAutoFails":ofAutoFails,"MixClose_HSI":MixClose_HSI,
                  "AttainmenttoGoal_HSI_1":AttainmenttoGoal_HSI_1,"MixClose_TV":MixClose_TV,"AttainmenttoGoal_TV":AttainmenttoGoal_TV,
                  "AttachRate_DTV":AttachRate_DTV,"MixClose_PhoneLines":MixClose_PhoneLines,"MixClose_Ease":MixClose_Ease,
                  "ACDCalls":ACDCalls,"AHTIneligible":AHTIneligible,"QualifiedCloseRate":QualifiedCloseRate,"Achiev":Achiev}
        return Agent_KPI
    
    def get_CENTURYLINK_TL_KPI_Actual(self,TLindex):
        Ppage=PerformancePage()
        AttainmenttoGoal_HSI=Ppage.get_anyKPIofTL(TLindex,2)
        B2P=Ppage.get_anyKPIofTL(TLindex,3)
        AHT=Ppage.get_anyKPIofTL(TLindex,4)
        Hold=Ppage.get_anyKPIofTL(TLindex,5)
        AbsAbsenteeism=Ppage.get_anyKPIofTL(TLindex,6)
        AvgQAScore=Ppage.get_anyKPIofTL(TLindex,7)
        QACalls=Ppage.get_anyKPIofTL(TLindex,8)
        ofAutoFails=Ppage.get_anyKPIofTL(TLindex,9)
        MixClose_HSI=Ppage.get_anyKPIofTL(TLindex,10)
        AttainmenttoGoal_HSI_1=Ppage.get_anyKPIofTL(TLindex,11)
        MixClose_TV=Ppage.get_anyKPIofTL(TLindex,12)
        AttainmenttoGoal_TV=Ppage.get_anyKPIofTL(TLindex,13)
        AttachRate_DTV=Ppage.get_anyKPIofTL(TLindex,14)
        MixClose_PhoneLines=Ppage.get_anyKPIofTL(TLindex,15)
        MixClose_Ease=Ppage.get_anyKPIofTL(TLindex,16)
        ACDCalls=Ppage.get_anyKPIofTL(TLindex,17)
        AHTIneligible=Ppage.get_anyKPIofTL(TLindex,18)
        QualifiedCloseRate=Ppage.get_anyKPIofTL(TLindex,19)
        Achiev=Ppage.get_anyKPIofTL(TLindex,20)
        Agent_KPI={"AttainmenttoGoal_HSI":AttainmenttoGoal_HSI,"B2P":B2P,"AHT":AHT,"Hold":Hold,"AbsAbsenteeism":AbsAbsenteeism,
                  "AvgQAScore":AvgQAScore,"QACalls":QACalls,"ofAutoFails":ofAutoFails,"MixClose_HSI":MixClose_HSI,
                  "AttainmenttoGoal_HSI_1":AttainmenttoGoal_HSI_1,"MixClose_TV":MixClose_TV,"AttainmenttoGoal_TV":AttainmenttoGoal_TV,
                  "AttachRate_DTV":AttachRate_DTV,"MixClose_PhoneLines":MixClose_PhoneLines,"MixClose_Ease":MixClose_Ease,
                  "ACDCalls":ACDCalls,"AHTIneligible":AHTIneligible,"QualifiedCloseRate":QualifiedCloseRate,"Achiev":Achiev}
        return Agent_KPI
    def get_CENTURYLINK_AgentKPI_Agent_Actual(self):
        Ppage=PerformancePage()
        AttainmenttoGoal_HSI=Ppage.get_anyKPIofAgent_Agent(2)
        B2P=Ppage.get_anyKPIofAgent_Agent(3)
        AHT=Ppage.get_anyKPIofAgent_Agent(4)
        Hold=Ppage.get_anyKPIofAgent_Agent(5)
        AbsAbsenteeism=Ppage.get_anyKPIofAgent_Agent(6)
        AvgQAScore=Ppage.get_anyKPIofAgent_Agent(7)
        QACalls=Ppage.get_anyKPIofAgent_Agent(8)
        ofAutoFails=Ppage.get_anyKPIofAgent_Agent(9)
        MixClose_HSI=Ppage.get_anyKPIofAgent_Agent(10)
        AttainmenttoGoal_HSI_1=Ppage.get_anyKPIofAgent_Agent(11)
        MixClose_TV=Ppage.get_anyKPIofAgent_Agent(12)
        AttainmenttoGoal_TV=Ppage.get_anyKPIofAgent_Agent(13)
        AttachRate_DTV=Ppage.get_anyKPIofAgent_Agent(14)
        MixClose_PhoneLines=Ppage.get_anyKPIofAgent_Agent(15)
        MixClose_Ease=Ppage.get_anyKPIofAgent_Agent(16)
        ACDCalls=Ppage.get_anyKPIofAgent_Agent(17)
        AHTIneligible=Ppage.get_anyKPIofAgent_Agent(18)
        QualifiedCloseRate=Ppage.get_anyKPIofAgent_Agent(19)
        Achiev=Ppage.get_anyKPIofAgent_Agent(20)
        Agent_KPI={"AttainmenttoGoal_HSI":AttainmenttoGoal_HSI,"B2P":B2P,"AHT":AHT,"Hold":Hold,"AbsAbsenteeism":AbsAbsenteeism,
                  "AvgQAScore":AvgQAScore,"QACalls":QACalls,"ofAutoFails":ofAutoFails,"MixClose_HSI":MixClose_HSI,
                  "AttainmenttoGoal_HSI_1":AttainmenttoGoal_HSI_1,"MixClose_TV":MixClose_TV,"AttainmenttoGoal_TV":AttainmenttoGoal_TV,
                  "AttachRate_DTV":AttachRate_DTV,"MixClose_PhoneLines":MixClose_PhoneLines,"MixClose_Ease":MixClose_Ease,
                  "ACDCalls":ACDCalls,"AHTIneligible":AHTIneligible,"QualifiedCloseRate":QualifiedCloseRate,"Achiev":Achiev}
        return Agent_KPI
    
    def get_CENTURYLINK_AgentKPI_TL_Actual(self,Agentindex):
        Ppage=PerformancePage()
        AttainmenttoGoal_HSI=Ppage.get_anyKPIofAgent_TL(Agentindex,2)
        B2P=Ppage.get_anyKPIofAgent_TL(Agentindex,3)
        AHT=Ppage.get_anyKPIofAgent_TL(Agentindex,4)
        Hold=Ppage.get_anyKPIofAgent_TL(Agentindex,5)
        AbsAbsenteeism=Ppage.get_anyKPIofAgent_TL(Agentindex,6)
        AvgQAScore=Ppage.get_anyKPIofAgent_TL(Agentindex,7)
        QACalls=Ppage.get_anyKPIofAgent_TL(Agentindex,8)
        ofAutoFails=Ppage.get_anyKPIofAgent_TL(Agentindex,9)
        MixClose_HSI=Ppage.get_anyKPIofAgent_TL(Agentindex,10)
        AttainmenttoGoal_HSI_1=Ppage.get_anyKPIofAgent_TL(Agentindex,11)
        MixClose_TV=Ppage.get_anyKPIofAgent_TL(Agentindex,12)
        AttainmenttoGoal_TV=Ppage.get_anyKPIofAgent_TL(Agentindex,13)
        AttachRate_DTV=Ppage.get_anyKPIofAgent_TL(Agentindex,14)
        MixClose_PhoneLines=Ppage.get_anyKPIofAgent_TL(Agentindex,15)
        MixClose_Ease=Ppage.get_anyKPIofAgent_TL(Agentindex,16)
        ACDCalls=Ppage.get_anyKPIofAgent_TL(Agentindex,17)
        AHTIneligible=Ppage.get_anyKPIofAgent_TL(Agentindex,18)
        QualifiedCloseRate=Ppage.get_anyKPIofAgent_TL(Agentindex,19)
        Achiev=Ppage.get_anyKPIofAgent_TL(Agentindex,20)
        Agent_KPI={"AttainmenttoGoal_HSI":AttainmenttoGoal_HSI,"B2P":B2P,"AHT":AHT,"Hold":Hold,"AbsAbsenteeism":AbsAbsenteeism,
                  "AvgQAScore":AvgQAScore,"QACalls":QACalls,"ofAutoFails":ofAutoFails,"MixClose_HSI":MixClose_HSI,
                  "AttainmenttoGoal_HSI_1":AttainmenttoGoal_HSI_1,"MixClose_TV":MixClose_TV,"AttainmenttoGoal_TV":AttainmenttoGoal_TV,
                  "AttachRate_DTV":AttachRate_DTV,"MixClose_PhoneLines":MixClose_PhoneLines,"MixClose_Ease":MixClose_Ease,
                  "ACDCalls":ACDCalls,"AHTIneligible":AHTIneligible,"QualifiedCloseRate":QualifiedCloseRate,"Achiev":Achiev}
        return Agent_KPI
    
    
   
        
        