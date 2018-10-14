'''
Created on Apr 5, 2017

@author: symbio
'''

from public_method.Get_file import Get_file
from public_method.KPI_method import KPI_method

class Get_PerformanceData_Expected_DTVRCX():
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.DTVRCX_Performance_Sheetiname="DTVRCX"
        
    def get_DTVRCX_Performance_Data_Expected(self,lineindex): 
        '''
        Can get all data include all KPI of site,tl,agent
        The range of linenumber_Yesterday:TL1~5-18,TL2~19-23
        The range of linenumber_WTD:60-77
        The range of linenumber_MTD:82-99
        The range of linenumber_LASTMONTH:106-123
        The range of linenumber_LASTTWOMONTH:130-134
        '''
        Getfile=Get_file()
        table=Getfile.Get_performance_sheet_Info(self.DTVRCX_Performance_Sheetiname)
        KPIMethod=KPI_method()
        Name_value=table.row_values(lineindex)[0]
        Name_status=''
        Name=[Name_value,Name_status]
        
        CombinedGoalRate_value=table.row_values(lineindex)[4]
        CombinedGoalRate_status=table.row_values(lineindex)[5]
        CombinedGoalRate=[CombinedGoalRate_value,CombinedGoalRate_status]
        
        WBAttainmant_value=table.row_values(lineindex)[8]
        WBAttainmant_status=table.row_values(lineindex)[9]
        WBAttainmant=[WBAttainmant_value,WBAttainmant_status]
        
        CCTAttainmant_value=table.row_values(lineindex)[12]
        CCTAttainmant_status=table.row_values(lineindex)[13]
        CCTAttainmant=[CCTAttainmant_value,CCTAttainmant_status]
        
        DISCAttainmant_value=table.row_values(lineindex)[16]
        DISCAttainmant_status=table.row_values(lineindex)[17]
        DISCAttainmant=[DISCAttainmant_value,DISCAttainmant_status]
        
        IPBBGrossSales_value=table.row_values(lineindex)[19]
        IPBBGrossSales_status=table.row_values(lineindex)[20]
        IPBBGrossSales=[IPBBGrossSales_value,IPBBGrossSales_status]
        
        BroadbandAttachRate_value=table.row_values(lineindex)[23]
        BroadbandAttachRate_status=table.row_values(lineindex)[24]
        BroadbandAttachRate=[BroadbandAttachRate_value,BroadbandAttachRate_status]
        
        AgentSatisfaction_value=table.row_values(lineindex)[25]
        AgentSatisfaction_status=table.row_values(lineindex)[26]
        AgentSatisfaction=[AgentSatisfaction_value,AgentSatisfaction_status]
        
        Achiev_value=table.row_values(lineindex)[27]
        Achiev__status=table.row_values(lineindex)[28]
        Achiev=[Achiev_value,Achiev__status]
       
        Eachline_KPI={"Name":Name,"CombinedGoalRate":CombinedGoalRate,"WBAttainmant":WBAttainmant,"CCTAttainmant":CCTAttainmant,"DISCAttainmant":DISCAttainmant,"IPBBGrossSales":IPBBGrossSales,"BroadbandAttachRate":BroadbandAttachRate,"AgentSatisfaction":AgentSatisfaction,"Achiev":Achiev}
        for key in Eachline_KPI:
            if key=="IPBBGrossSales":
                Decimal_digits='0.00'
                Eachline_KPI[key][0]=str(KPIMethod.Change_Decimal_digits(Eachline_KPI[key][0],Decimal_digits))#If not str, the value of AHT will be Decimal('650.00')
            elif key!="Name":
                Eachline_KPI[key][0]=KPIMethod.Decimal_To_Percentage(Eachline_KPI[key][0])
        
        return Eachline_KPI
    
    

    def get_DTVRCX_Goal_Expected(self,lineindex): 
        Getfile=Get_file()
        table=Getfile.Get_performance_sheet_Info(self.DTVRCX_Performance_Sheetiname)
        KPIMethod=KPI_method()
        CombinedGoalRate=table.row_values(lineindex)[1]
        WBAttainmant=table.row_values(lineindex)[6]
        CCTAttainmant=table.row_values(lineindex)[10]
        DISCAttainmant=table.row_values(lineindex)[14]
        IPBBGrossSales=table.row_values(lineindex)[18]
        BroadbandAttachRate=table.row_values(lineindex)[21]
        AgentSatisfaction=table.row_values(lineindex)[25]
        Achiev=table.row_values(lineindex)[27]
        Goal_KPI={"CombinedGoalRate":CombinedGoalRate,"WBAttainmant":WBAttainmant,"CCTAttainmant":CCTAttainmant,"DISCAttainmant":DISCAttainmant,"IPBBGrossSales":IPBBGrossSales,"BroadbandAttachRate":BroadbandAttachRate,"AgentSatisfaction":AgentSatisfaction,"Achiev":Achiev}
        for key in Goal_KPI:
            if key=="IPBBGrossSales":
                Decimal_digits='0.00'
                Goal_KPI[key]=str(KPIMethod.Change_Decimal_digits(Goal_KPI[key],Decimal_digits))#If not str, the value of AHT will be Decimal('650.00')
            else:
                Goal_KPI[key]=KPIMethod.Decimal_To_Percentage(Goal_KPI[key])
        return Goal_KPI
    
    
            
    def Get_ManyAgentAchiev_Expected(self,start_lineindex,end_lineindex):
        Agent_Achiev_Dic={}
        for lineindex in range(start_lineindex,end_lineindex+1):
            AllKPI_OneAgent=self.get_DTVRCX_Performance_Data_Expected(lineindex)
            AgentName=AllKPI_OneAgent["Name"][0]
            Achiv_Agent=AllKPI_OneAgent["Achiev"][0]
            Agent_Achiev_Dic[AgentName]=Achiv_Agent   
        return Agent_Achiev_Dic
    
    def Get_AllAgentName_Expected(self,start_lineindex,end_lineindex):
        AllAgentName_List=[]
        Agent_Achiev_Dic=self.Get_ManyAgentAchiev_Expected(start_lineindex, end_lineindex)
        for key in Agent_Achiev_Dic:
            AllAgentName_List.append(key)
            
        return AllAgentName_List
    
    
  
    
    
    
    
    
    
