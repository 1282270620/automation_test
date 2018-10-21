'''
Created on 2018.8.13

@author: Sissi.liu
'''

from public_method.Get_file import Get_file
from public_method.KPI_method import KPI_method

class Get_PerformanceData_Expected_ISM(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.ISM_Performance_Sheetiname="ISM"
        
    def get_ISM_Goal_Expected(self,lineindex):
        Getfile=Get_file()
        table=Getfile.Get_performance_sheet_Info(self.ISM_Performance_Sheetiname)
        KPIMethod=KPI_method()        
        
        NumberOfSurveys=table.row_values(lineindex)[2]
        OverallScore=table.row_values(lineindex)[5]
        eg7d_Calls=table.row_values(lineindex)[8]
        eg7d_Transfers=table.row_values(lineindex)[11]
        eg7d_OneAndDone7Day=table.row_values(lineindex)[14]
        eg7d_Rpt7Day=table.row_values(lineindex)[17]
        eg7d_7DREPEATS=table.row_values(lineindex)[19]
        AHT=table.row_values(lineindex)[32]
        Transfers=table.row_values(lineindex)[24]
        Hold=table.row_values(lineindex)[27]
        Adjustments=table.row_values(lineindex)[37]
        Wireless=table.row_values(lineindex)[40]
        Broadband=table.row_values(lineindex)[43]
        Achiev=table.row_values(lineindex)[45]
                
        Goal_KPI={'NumberOfSurveys':NumberOfSurveys,'OverallScore':OverallScore,'eg7d_Calls':eg7d_Calls,'eg7d_Transfers':eg7d_Transfers,'eg7d_OneAndDone7Day':eg7d_OneAndDone7Day,
                  'eg7d_Rpt7Day':eg7d_Rpt7Day,'eg7d_7DREPEATS':eg7d_7DREPEATS,'AHT':AHT,'Transfers':Transfers,'Hold':Hold,'Adjustments':Adjustments,
                  'Wireless':Wireless,'Broadband':Broadband,'Achiev':Achiev}
        
        for key in Goal_KPI:
            #if key=='AHT' or key=='Adjustments':
            if key in ("AHT","NumberOfSurveys","eg7d_Calls","eg7d_Transfers","eg7d_OneAndDone7Day","eg7d_Rpt7Day","Adjustments","Wireless","Broadband"):
                Decimal_digits='0.00'
                Goal_KPI[key]=str(KPIMethod.Change_Decimal_digits(Goal_KPI[key],Decimal_digits))#If not str, the value of AHT will be Decimal('650.00')
            else:
                Goal_KPI[key]=KPIMethod.Decimal_To_Percentage(Goal_KPI[key])
        return Goal_KPI;
    
    def get_ISM_Performance_Data_Expected(self,lineindex):
        
        Getfile=Get_file()
        table=Getfile.Get_performance_sheet_Info(self.ISM_Performance_Sheetiname)
        KPIMethod=KPI_method()
        Name_value=table.row_values(lineindex)[0]
        Name_status=''
        Name=[Name_value,Name_status]
        
        NumberOfSurveys_value=table.row_values(lineindex)[2]
        NumberOfSurveys_status=table.row_values(lineindex)[3]
        NumberOfSurveys=[NumberOfSurveys_value, NumberOfSurveys_status]        
        
        OverallScore_value=table.row_values(lineindex)[5]
        OverallScore_status=table.row_values(lineindex)[6]
        OverallScore=[OverallScore_value, OverallScore_status]
        
        eg7d_Calls_value=table.row_values(lineindex)[8]
        eg7d_Calls_status=table.row_values(lineindex)[9]
        eg7d_Calls=[eg7d_Calls_value, eg7d_Calls_status]
        
        eg7d_Transfers_value=table.row_values(lineindex)[11]
        eg7d_Transfers_status=table.row_values(lineindex)[12]
        eg7d_Transfers=[eg7d_Transfers_value, eg7d_Transfers_status]
        
        eg7d_OneAndDone7Day_value=table.row_values(lineindex)[14]
        eg7d_OneAndDone7Day_status=table.row_values(lineindex)[15]
        eg7d_OneAndDone7Day=[eg7d_OneAndDone7Day_value, eg7d_OneAndDone7Day_status]
        
        eg7d_Rpt7Day_value=table.row_values(lineindex)[17]
        eg7d_Rpt7Day_status=table.row_values(lineindex)[18]
        eg7d_Rpt7Day=[eg7d_Rpt7Day_value, eg7d_Rpt7Day_status]
        
        eg7d_7DREPEATS_value=table.row_values(lineindex)[19]
        eg7d_7DREPEATS_status=table.row_values(lineindex)[20]
        eg7d_7DREPEATS=[eg7d_7DREPEATS_value, eg7d_7DREPEATS_status]
        
        AHT_value=table.row_values(lineindex)[32]
        AHT_status=table.row_values(lineindex)[33]
        AHT=[AHT_value, AHT_status]
        
        Transfers_value=table.row_values(lineindex)[24]
        Transfers_status=table.row_values(lineindex)[25]
        Transfers=[Transfers_value, Transfers_status]
        
        Hold_value=table.row_values(lineindex)[27]
        Hold_status=table.row_values(lineindex)[28]
        Hold=[Hold_value, Hold_status]
        
        Adjustments_value=table.row_values(lineindex)[37]
        Adjustments_status=table.row_values(lineindex)[38]
        Adjustments=[Adjustments_value, Adjustments_status]
        
        Wireless_value=table.row_values(lineindex)[40]
        Wireless_status=table.row_values(lineindex)[41]
        Wireless=[Wireless_value, Wireless_status]
        
        Broadband_value=table.row_values(lineindex)[43]
        Broadband_status=table.row_values(lineindex)[44]
        Broadband=[Broadband_value, Broadband_status]
        
        Achiev_value=table.row_values(lineindex)[45]
        Achiev_status=table.row_values(lineindex)[46]
        Achiev=[Achiev_value, Achiev_status]
        
        Eachline_KPI={"Name":Name,'NumberOfSurveys':NumberOfSurveys,'OverallScore':OverallScore,'eg7d_Calls':eg7d_Calls,'eg7d_Transfers':eg7d_Transfers,'eg7d_OneAndDone7Day':eg7d_OneAndDone7Day,
                  'eg7d_Rpt7Day':eg7d_Rpt7Day,'eg7d_7DREPEATS':eg7d_7DREPEATS,'AHT':AHT,'Transfers':Transfers,'Hold':Hold,'Adjustments':Adjustments,
                  'Wireless':Wireless,'Broadband':Broadband,'Achiev':Achiev}
        for key in Eachline_KPI:
            if key in ("AHT","NumberOfSurveys","eg7d_Calls","eg7d_Transfers","eg7d_OneAndDone7Day","eg7d_Rpt7Day","Adjustments","Wireless","Broadband"):
                Decimal_digits='0.00'
                Eachline_KPI[key][0]=str(KPIMethod.Change_Decimal_digits(Eachline_KPI[key][0],Decimal_digits))#If not str, the value of AHT will be Decimal('650.00')
            elif key!="Name":
                Eachline_KPI[key][0]=KPIMethod.Decimal_To_Percentage(Eachline_KPI[key][0])
        
        return Eachline_KPI
    
    
    def Get_ManyAgentAchiev_Expected(self,start_lineindex,end_lineindex):
        Agent_Achiev_Dic={}
        for lineindex in range(start_lineindex,end_lineindex+1):
            AllKPI_OneAgent=self.get_ISM_Performance_Data_Expected(lineindex)
            AgentName=AllKPI_OneAgent["Name"][0]
            Achiv_Agent=AllKPI_OneAgent["Achiev"][0]
            Agent_Achiev_Dic[AgentName]=Achiv_Agent   
        return Agent_Achiev_Dic