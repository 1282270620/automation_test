'''
Created on 20170918

@author: luming.zhao
'''
from public_method.Get_file import Get_file
from public_method.KPI_method import KPI_method

class Get_PerformanceData_Expected_DTVSS(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.DTVSS_Performance_Sheetiname="DTVSS"
        
    def get_DTVSS_Performance_Data_Expected(self,lineindex): 
        '''
        Can get all data include all KPI of site,tl,agent
        The range of linenumber_Yesterday:TL1~5-17,TL2~23-27
        The range of linenumber_WTD:57-69
        The range of linenumber_MTD:77-89
        '''
        Getfile=Get_file()
        table=Getfile.Get_performance_sheet_Info(self.DTVSS_Performance_Sheetiname)
        KPIMethod=KPI_method()
        Name_value=table.row_values(lineindex)[0]
        Name_status=''
        Name=[Name_value,Name_status]
        
        ActivationRateModify_value=table.row_values(lineindex)[3]
        ActivationRateModify_status=table.row_values(lineindex)[4]
        ActivationRateModify=[ActivationRateModify_value,ActivationRateModify_status]
        
        CancelTransfer_value=table.row_values(lineindex)[7]
        CancelTransferHoldTime_status=table.row_values(lineindex)[8]
        CancelTransfer=[CancelTransfer_value,CancelTransferHoldTime_status]
        
        CancelIVR_value=table.row_values(lineindex)[11]
        CancelIVR_status=table.row_values(lineindex)[12]
        CancelIVR=[CancelIVR_value,CancelIVR_status]
        
        IPBBNet_value=table.row_values(lineindex)[14]
        IPBBNet_status=table.row_values(lineindex)[15]
        IPBBNet=[IPBBNet_value,IPBBNet_status]
        
        MobilityGrossSales_value=table.row_values(lineindex)[17]
        MobilityGrossSales_status=table.row_values(lineindex)[18]
        MobilityGrossSales=[MobilityGrossSales_value,MobilityGrossSales_status]
        
        AgentSatisfaction_value=table.row_values(lineindex)[20]
        AgentSatisfaction=[AgentSatisfaction_value]
        
        
        Achiev_value=table.row_values(lineindex)[21]
        Achieve_status=table.row_values(lineindex)[22]
        Achiev=[Achiev_value,Achieve_status]
        
        Eachline_KPI={"Name":Name,"ActivationRateModify":ActivationRateModify,"CancelTransfer":CancelTransfer,"CancelIVR":CancelIVR,"IPBBNet":IPBBNet,"MobilityGrossSales":MobilityGrossSales,"AgentSatisfaction":AgentSatisfaction,"Achiev":Achiev}
        for key in Eachline_KPI:
            if key in {'IPBBNet', 'MobilityGrossSales'}:
                Decimal_digits='0.00'
                Eachline_KPI[key][0]=str(KPIMethod.Change_Decimal_digits(Eachline_KPI[key][0],Decimal_digits))
            elif key!="Name":
                Eachline_KPI[key][0]=KPIMethod.Decimal_To_Percentage(Eachline_KPI[key][0])
        
        return Eachline_KPI
    

    def get_DTVSS_Goal_Expected(self,lineindex): 
        Getfile=Get_file()
        table=Getfile.Get_performance_sheet_Info(self.DTVSS_Performance_Sheetiname)
        KPIMethod=KPI_method()
        ActivationRateModify=table.row_values(lineindex)[1]
        CancelTransfer=table.row_values(lineindex)[5]
        CancelIVR=table.row_values(lineindex)[9]
        IPBBNet=table.row_values(lineindex)[13]
        MobilityGrossSales=table.row_values(lineindex)[16]
        AgentSatisfaction=table.row_values(lineindex)[19]
        Achiev=table.row_values(lineindex)[20]
        #Achiev='N/A'
        Goal_KPI={'ActivationRateModify':ActivationRateModify,'CancelTransfer':CancelTransfer,'CancelIVR':CancelIVR,'IPBBNet':IPBBNet,'MobilityGrossSales':MobilityGrossSales,'AgentSatisfaction':AgentSatisfaction,'Achiev':Achiev}
        for key in Goal_KPI:
            if key in {'IPBBNet', 'MobilityGrossSales'}:
                Decimal_digits='0.00'
                Goal_KPI[key]=str(KPIMethod.Change_Decimal_digits(Goal_KPI[key],Decimal_digits))
            else:
                Goal_KPI[key]=KPIMethod.Decimal_To_Percentage(Goal_KPI[key])
        return Goal_KPI

            
    def Get_ManyAgentAchiev_Expected(self,start_lineindex,end_lineindex):
        Agent_Achiev_Dic={}
        for lineindex in range(start_lineindex,end_lineindex+1):
            AllKPI_OneAgent=self.get_DTVSS_Performance_Data_Expected(lineindex)
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
    
    

    
    
    
    

    
