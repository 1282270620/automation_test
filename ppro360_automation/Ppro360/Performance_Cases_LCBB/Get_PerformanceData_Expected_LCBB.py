'''
Created on Apr 5, 2017

@author: symbio
'''
from public_method.Get_file import Get_file
from public_method.KPI_method import KPI_method

class Get_PerformanceData_Expected_LCBB():
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.LCBB_Performance_Sheetiname="LCBB"
        
    def get_LCBB_Performance_Data_Expected(self,lineindex): 
        '''
        Can get all data include all KPI of site,tl,agent
        The range of linenumber_Yesterday:TL1~5-16,TL2~21-25
        The range of linenumber_WTD:60-73
        The range of linenumber_MTD:78-91
        '''
        #table=self.Get_sheet_Info(self.LCBB_Performance_Sheetiname)
        Getfile=Get_file()
        table=Getfile.Get_performance_sheet_Info(self.LCBB_Performance_Sheetiname)
        KPIMethod=KPI_method()
        Name_value=table.row_values(lineindex)[0]
        Name_status=''
        Name=[Name_value,Name_status]
        
        AHT_value=table.row_values(lineindex)[5]
        AHT_status=table.row_values(lineindex)[6]
        AHT=[AHT_value,AHT_status]
        
        HoldTime_value=table.row_values(lineindex)[9]
        HoldTime_status=table.row_values(lineindex)[10]
        HoldTime=[HoldTime_value,HoldTime_status]
        
        ACW_value=table.row_values(lineindex)[14]
        ACW_status=table.row_values(lineindex)[15]
        ACW=[ACW_value,ACW_status]
        
        Transfers_value=table.row_values(lineindex)[18]
        Transfers_status=table.row_values(lineindex)[19]
        Transfers=[Transfers_value,Transfers_status]
        
        VOC_value=table.row_values(lineindex)[23]
        VOC_status=table.row_values(lineindex)[24]
        VOC=[VOC_value,VOC_status]
        
        SOAR_value=table.row_values(lineindex)[26]
        SOAR_status=table.row_values(lineindex)[27]
        SOAR=[SOAR_value,SOAR_status]
        
        
        Achiev_value=table.row_values(lineindex)[28]
        Achiev__status=''
        Achiev=[Achiev_value,Achiev__status]
        
        Eachline_KPI={"Name":Name,"AHT":AHT,"HoldTime":HoldTime,"ACW":ACW,"Transfers":Transfers,"VOC":VOC,"SOAR":SOAR,"Achiev":Achiev}
        for key in Eachline_KPI:
            if key=="AHT":
                Decimal_digits='0.00'
                Eachline_KPI[key][0]=str(KPIMethod.Change_Decimal_digits(Eachline_KPI[key][0],Decimal_digits))#If not str, the value of AHT will be Decimal('650.00')
            elif key!="Name":
                Eachline_KPI[key][0]=KPIMethod.Decimal_To_Percentage(Eachline_KPI[key][0])
        
        return Eachline_KPI
    
    

    def get_LCBB_Goal_Expected(self,lineindex): 
        #table=self.Get_sheet_Info(self.LCBB_Performance_Sheetiname)
        Getfile=Get_file()
        table=Getfile.Get_performance_sheet_Info(self.LCBB_Performance_Sheetiname)
        KPIMethod=KPI_method()
        AHT=table.row_values(lineindex)[1]
        HoldTime=table.row_values(lineindex)[7]
        ACW=table.row_values(lineindex)[11]
        Transfers=table.row_values(lineindex)[16]
        VOC=table.row_values(lineindex)[20]
        SOAR=table.row_values(lineindex)[25]
        Achiev='N/A'
        Goal_KPI={"AHT":AHT,"HoldTime":HoldTime,"ACW":ACW,"Transfers":Transfers,"VOC":VOC,"SOAR":SOAR,"Achiev":Achiev}
        for key in Goal_KPI:
            if key=="AHT":
                Decimal_digits='0.00'
                Goal_KPI[key]=str(KPIMethod.Change_Decimal_digits(Goal_KPI[key],Decimal_digits))#If not str, the value of AHT will be Decimal('650.00')
            else:
                Goal_KPI[key]=KPIMethod.Decimal_To_Percentage(Goal_KPI[key])
        return Goal_KPI
    
            
    def Get_ManyAgentAchiev_Expected(self,start_lineindex,end_lineindex):
        Agent_Achiev_Dic={}
        for lineindex in range(start_lineindex,end_lineindex+1):
            AllKPI_OneAgent=self.get_LCBB_Performance_Data_Expected(lineindex)
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
    
    
