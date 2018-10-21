'''
Created on 2018.8.13

@author: Sissi.liu
'''
from Tablet_pages.PerformancPage import PerformancePage

class Get_PerformanceData_Actual_ISM(object):
    '''
    classdocs
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
    
    def get_ISM_Goal_Actual(self):
        Ppage = PerformancePage()
        
        NumberOfSurveys=Ppage.get_anyGoalValue(2)
        OverallScore=Ppage.get_anyGoalValue(3)
        eg7d_Calls=Ppage.get_anyGoalValue(4)
        eg7d_Transfers=Ppage.get_anyGoalValue(5)
        eg7d_OneAndDone7Day=Ppage.get_anyGoalValue(6)
        eg7d_Rpt7Day=Ppage.get_anyGoalValue(7)
        eg7d_7DREPEATS=Ppage.get_anyGoalValue(8)
        AHT=Ppage.get_anyGoalValue(9)
        Transfers=Ppage.get_anyGoalValue(10)
        Hold=Ppage.get_anyGoalValue(11)
        Adjustments=Ppage.get_anyGoalValue(12)
        Wireless=Ppage.get_anyGoalValue(13)
        Broadband=Ppage.get_anyGoalValue(14)
        Achiev=Ppage.get_anyGoalValue(15)
                
        Goal_KPI={'NumberOfSurveys':NumberOfSurveys,'OverallScore':OverallScore,'eg7d_Calls':eg7d_Calls,'eg7d_Transfers':eg7d_Transfers,'eg7d_OneAndDone7Day':eg7d_OneAndDone7Day,
                  'eg7d_Rpt7Day':eg7d_Rpt7Day,'eg7d_7DREPEATS':eg7d_7DREPEATS,'AHT':AHT,'Transfers':Transfers,'Hold':Hold,'Adjustments':Adjustments,
                  'Wireless':Wireless,'Broadband':Broadband,'Achiev':Achiev}
        return Goal_KPI;
    
    def get_ISM_TL_KPI_Actual(self,TLindex):
        Ppage=PerformancePage()
                
        NumberOfSurveys=Ppage.get_anyKPIofTL(TLindex, 2)
        OverallScore=Ppage.get_anyKPIofTL(TLindex, 3)
        eg7d_Calls=Ppage.get_anyKPIofTL(TLindex, 4)
        eg7d_Transfers=Ppage.get_anyKPIofTL(TLindex, 5)
        eg7d_OneAndDone7Day=Ppage.get_anyKPIofTL(TLindex, 6)
        eg7d_Rpt7Day=Ppage.get_anyKPIofTL(TLindex, 7)
        eg7d_7DREPEATS=Ppage.get_anyKPIofTL(TLindex, 8)
        AHT=Ppage.get_anyKPIofTL(TLindex, 9)
        Transfers=Ppage.get_anyKPIofTL(TLindex, 10)
        Hold=Ppage.get_anyKPIofTL(TLindex, 11)
        Adjustments=Ppage.get_anyKPIofTL(TLindex, 12)
        Wireless=Ppage.get_anyKPIofTL(TLindex, 13)
        Broadband=Ppage.get_anyKPIofTL(TLindex, 14)
        Achiev=Ppage.get_anyKPIofTL(TLindex, 15)
        
        TL_KPI={'NumberOfSurveys':NumberOfSurveys,'OverallScore':OverallScore,'eg7d_Calls':eg7d_Calls,'eg7d_Transfers':eg7d_Transfers,'eg7d_OneAndDone7Day':eg7d_OneAndDone7Day,
                  'eg7d_Rpt7Day':eg7d_Rpt7Day,'eg7d_7DREPEATS':eg7d_7DREPEATS,'AHT':AHT,'Transfers':Transfers,'Hold':Hold,'Adjustments':Adjustments,
                  'Wireless':Wireless,'Broadband':Broadband,'Achiev':Achiev}
        return TL_KPI
    
    
    def get_ISM_Agent_KPI_Actual(self, TLindex, Agentindex):
        Ppage=PerformancePage()
        
        NumberOfSurveys=Ppage.get_anyKPIofAgent_OM(TLindex,Agentindex,2)
        OverallScore=Ppage.get_anyKPIofAgent_OM(TLindex,Agentindex,3)
        eg7d_Calls=Ppage.get_anyKPIofAgent_OM(TLindex,Agentindex,4)
        eg7d_Transfers=Ppage.get_anyKPIofAgent_OM(TLindex,Agentindex,5)
        eg7d_OneAndDone7Day=Ppage.get_anyKPIofAgent_OM(TLindex,Agentindex,6)
        eg7d_Rpt7Day=Ppage.get_anyKPIofAgent_OM(TLindex,Agentindex,7)
        eg7d_7DREPEATS=Ppage.get_anyKPIofAgent_OM(TLindex,Agentindex,8)
        AHT=Ppage.get_anyKPIofAgent_OM(TLindex,Agentindex,9)
        Transfers=Ppage.get_anyKPIofAgent_OM(TLindex,Agentindex,10)
        Hold=Ppage.get_anyKPIofAgent_OM(TLindex,Agentindex,11)
        Adjustments=Ppage.get_anyKPIofAgent_OM(TLindex,Agentindex,12)
        Wireless=Ppage.get_anyKPIofAgent_OM(TLindex,Agentindex,13)
        Broadband=Ppage.get_anyKPIofAgent_OM(TLindex,Agentindex,14)
        Achiev=Ppage.get_anyKPIofAgent_OM(TLindex,Agentindex,15)
                
        Agent_KPI={'NumberOfSurveys':NumberOfSurveys,'OverallScore':OverallScore,'eg7d_Calls':eg7d_Calls,'eg7d_Transfers':eg7d_Transfers,'eg7d_OneAndDone7Day':eg7d_OneAndDone7Day,
                  'eg7d_Rpt7Day':eg7d_Rpt7Day,'eg7d_7DREPEATS':eg7d_7DREPEATS,'AHT':AHT,'Transfers':Transfers,'Hold':Hold,'Adjustments':Adjustments,
                  'Wireless':Wireless,'Broadband':Broadband,'Achiev':Achiev}
        
        return Agent_KPI