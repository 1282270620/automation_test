'''
Created on 2017.9.6

@author: yalan.yin
'''
from public_method.Get_file import Get_file
from public_method.KPI_method import KPI_method


class Get_PerformanceData_Expected_DBS(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.DBS_Performance_Sheetiname="DBS"
        
    def get_DBS_Performance_Data_Expected(self,lineindex):
        '''
        Can get all data include all KPI of site,tl,agent
        The range of linenumber_Yesterday:TL1~5-16,TL2~21-25
        The range of linenumber_WTD:60-73
        The range of linenumber_MTD:78-91
        '''
        Getfile=Get_file()
        table=Getfile.Get_performance_sheet_Info(self.DBS_Performance_Sheetiname)
        KPIMethod=KPI_method()
        Name_value=table.row_values(lineindex)[0]
        Name_status=''
        Name=[Name_value,Name_status]
        
        R30_value=table.row_values(lineindex)[11]
        R30_status=table.row_values(lineindex)[12]
        R30=[R30_value,R30_status]
        
        R7_value=table.row_values(lineindex)[16]
        R7_status=table.row_values(lineindex)[17]
        R7=[R7_value,R7_status]
        
        Transfers_value=table.row_values(lineindex)[20]
        Transfers_status=table.row_values(lineindex)[21]
        Transfers=[Transfers_value,Transfers_status]
        
        AHT_value=table.row_values(lineindex)[27]
        AHT_status=table.row_values(lineindex)[28]
        AHT=[AHT_value,AHT_status]
        
        CloseRate_value=table.row_values(lineindex)[32]
        CloseRate_status=table.row_values(lineindex)[33]
        CloseRate=[CloseRate_value,CloseRate_status]
        
        VOC_value=table.row_values(lineindex)[6]
        VOC_status=table.row_values(lineindex)[7]
        VOC=[VOC_value,VOC_status]
        
        Achiev_value=table.row_values(lineindex)[35]
        Achieve_status=table.row_values(lineindex)[36]
        Achiev=[Achiev_value,Achieve_status]
        
        Eachline_KPI={"Name":Name,'R30':R30,'R7':R7,'Transfers':Transfers,'AHT':AHT,'CloseRate':CloseRate,'VOC':VOC,'Achiev':Achiev}
        for key in Eachline_KPI:
            if key=="AHT":
                Decimal_digits='0.00'
                Eachline_KPI[key][0]=str(KPIMethod.Change_Decimal_digits(Eachline_KPI[key][0],Decimal_digits))#If not str, the value of AHT will be Decimal('650.00')
            elif key!="Name":
                Eachline_KPI[key][0]=KPIMethod.Decimal_To_Percentage(Eachline_KPI[key][0])
        
        return Eachline_KPI
        
    def get_DBS_Goal_Expected(self,lineindex):
        Getfile=Get_file()
        table=Getfile.Get_performance_sheet_Info(self.DBS_Performance_Sheetiname)
        KPIMethod=KPI_method()
        R30=table.row_values(lineindex)[9]
        R7=table.row_values(lineindex)[14]
        Transfers=table.row_values(lineindex)[18]
        AHT=table.row_values(lineindex)[23]
        CloseRate=table.row_values(lineindex)[30]
        VOC=table.row_values(lineindex)[1]
        Achiev=table.row_values(lineindex)[25]
        
        Goal_KPI={'R30':R30,'R7':R7,'Transfers':Transfers,'AHT':AHT,'CloseRate':CloseRate,'VOC':VOC,'Achiev':Achiev}
        for key in Goal_KPI:
            if key=='AHT':
                Decimal_digits='0.00'
                Goal_KPI[key]=str(KPIMethod.Change_Decimal_digits(Goal_KPI[key],Decimal_digits))#If not str, the value of AHT will be Decimal('650.00')
            else:
                Goal_KPI[key]=KPIMethod.Decimal_To_Percentage(Goal_KPI[key])
        return Goal_KPI
        
    
            
    def Get_ManyAgentAchiev_Expected(self,start_lineindex,end_lineindex):
        Agent_Achiev_Dic={}
        for lineindex in range(start_lineindex,end_lineindex+1):
            AllKPI_OneAgent=self.get_DBS_Performance_Data_Expected(lineindex)
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
    
    