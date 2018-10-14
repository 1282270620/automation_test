'''
Created on Apr 5, 2017

@author: symbio
'''
from public_method.Get_file import Get_file
from public_method.KPI_method import KPI_method

class Get_PerformanceData_Expected_UBIZICM():
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.UBIZICM_Performance_Sheetiname="UBIZICM"
        
    def get_UBIZICM_Performance_Data_Expected(self,lineindex): 
        '''
        Can get all data include all KPI of site,tl,agent
        The range of linenumber_Yesterday:TL1~5-16,TL2~21-25
        The range of linenumber_WTD:64-81
        The range of linenumber_MTD:86-103
        The range of linenumber_LASTMONTH:109-126
        The range of linenumber_LASTTWOMONTH:132-137
        '''
        #table=self.Get_sheet_Info(self.UBIZICM_Performance_Sheetiname)
        Getfile=Get_file()
        table=Getfile.Get_performance_sheet_Info(self.UBIZICM_Performance_Sheetiname)
        KPIMethod=KPI_method()
        Name_value=table.row_values(lineindex)[0]
        Name_status=''
        Name=[Name_value,Name_status]
        
        AvgHoldTime_value=table.row_values(lineindex)[2]
        AvgHoldTime_status=table.row_values(lineindex)[3]
        AvgHoldTime=[AvgHoldTime_value,AvgHoldTime_status]
        
        IBAHT_value=table.row_values(lineindex)[5]
        IBAHT_status=table.row_values(lineindex)[6]
        IBAHT=[IBAHT_value,IBAHT_status]
        
        CaseTocall_value=table.row_values(lineindex)[9]
        CaseTocall_status=table.row_values(lineindex)[10]
        CaseTocall=[CaseTocall_value,CaseTocall_status]
        
        Misdirects_value=table.row_values(lineindex)[13]
        Misdirects_status=table.row_values(lineindex)[14]
        Misdirects=[Misdirects_value,Misdirects_status]
        
        Ghosts_value=table.row_values(lineindex)[17]
        Ghosts_status=table.row_values(lineindex)[18]
        Ghosts=[Ghosts_value,Ghosts_status]
        
        SwitchTransfer_value=table.row_values(lineindex)[21]
        SwitchTransfer_status=table.row_values(lineindex)[22]
        SwitchTransfer=[SwitchTransfer_value,SwitchTransfer_status]
        
        DailyRepeatRate_value=table.row_values(lineindex)[25]
        DailyRepeatRate_status=table.row_values(lineindex)[26]
        DailyRepeatRate=[DailyRepeatRate_value,DailyRepeatRate_status]
        
        DispatchRateByCTV_value=table.row_values(lineindex)[29]
        DispatchRateByCTV_status=table.row_values(lineindex)[30]
        DispatchRateByCTV=[DispatchRateByCTV_value,DispatchRateByCTV_status]
        
        WFEComplianceRate_value=table.row_values(lineindex)[33]
        WFEComplianceRate_status=table.row_values(lineindex)[34]
        WFEComplianceRate=[WFEComplianceRate_value,WFEComplianceRate_status]
        
        R3AllIn_value=table.row_values(lineindex)[37]
        R3AllIn_status=table.row_values(lineindex)[38]
        R3AllIn=[R3AllIn_value,R3AllIn_status]
        
        R30AllIn_value=table.row_values(lineindex)[41]
        R30AllIn_status=table.row_values(lineindex)[42]
        R30AllIn=[R30AllIn_value,R30AllIn_status]
        
        R7AllIn_value=table.row_values(lineindex)[45]
        R7AllIn_status=table.row_values(lineindex)[46]
        R7AllIn=[R7AllIn_value,R7AllIn_status]
        
        Achiev_value=table.row_values(lineindex)[47]
        Achiev_status=table.row_values(lineindex)[48]
        Achiev=[Achiev_value,Achiev_status]

        
        
        Eachline_KPI={"Name":Name,"AvgHoldTime":AvgHoldTime,"IBAHT":IBAHT,"CaseTocall":CaseTocall,"Misdirects":Misdirects,"Ghosts":Ghosts,
                  "SwitchTransfer":SwitchTransfer,"DailyRepeatRate":DailyRepeatRate,"DispatchRateByCTV":DispatchRateByCTV,
                  "WFEComplianceRate":WFEComplianceRate,"R3AllIn":R3AllIn,"R30AllIn":R30AllIn,"R7AllIn":R7AllIn,"Achiev":Achiev}
        for key in Eachline_KPI:
            if key in ["AvgHoldTime","IBAHT"]:
                Decimal_digits='0.00'
                Eachline_KPI[key][0]=str(KPIMethod.Change_Decimal_digits(Eachline_KPI[key][0],Decimal_digits))#If not str, the value of AHT will be Decimal('650.00')
            elif key!="Name":
                Eachline_KPI[key][0]=KPIMethod.Decimal_To_Percentage(Eachline_KPI[key][0])
        
        return Eachline_KPI
    
    

    def get_UBIZICM_Goal_Expected(self,lineindex): 
        #table=self.Get_sheet_Info(self.UBIZICM_Performance_Sheetiname)
        Getfile=Get_file()
        table=Getfile.Get_performance_sheet_Info(self.UBIZICM_Performance_Sheetiname)
        KPIMethod=KPI_method()
        AvgHoldTime=table.row_values(lineindex)[1]
        IBAHT=table.row_values(lineindex)[4]
        CaseTocall=table.row_values(lineindex)[7]
        Misdirects=table.row_values(lineindex)[11]
        Ghosts=table.row_values(lineindex)[15]
        SwitchTransfer=table.row_values(lineindex)[19]
        DailyRepeatRate=table.row_values(lineindex)[23]
        DispatchRateByCTV=table.row_values(lineindex)[27]
        WFEComplianceRate=table.row_values(lineindex)[31]
        R3AllIn=table.row_values(lineindex)[35]
        R30AllIn=table.row_values(lineindex)[39]
        R7AllIn=table.row_values(lineindex)[43]
        Achiev='N/A'
        Goal_KPI={"AvgHoldTime":AvgHoldTime,"IBAHT":IBAHT,"CaseTocall":CaseTocall,"Misdirects":Misdirects,"Ghosts":Ghosts,
                  "SwitchTransfer":SwitchTransfer,"DailyRepeatRate":DailyRepeatRate,"DispatchRateByCTV":DispatchRateByCTV,
                  "WFEComplianceRate":WFEComplianceRate,"R3AllIn":R3AllIn,"R30AllIn":R30AllIn,"R7AllIn":R7AllIn,"Achiev":Achiev}
        for key in Goal_KPI:
            if key in ["AvgHoldTime","IBAHT"]:
                Decimal_digits='0.00'
                Goal_KPI[key]=str(KPIMethod.Change_Decimal_digits(Goal_KPI[key],Decimal_digits))#If not str, the value of AHT will be Decimal('650.00')
            else:
                Goal_KPI[key]=KPIMethod.Decimal_To_Percentage(Goal_KPI[key])
        return Goal_KPI
    
            
    def Get_ManyAgentAchiev_Expected(self,start_lineindex,end_lineindex):
        Agent_Achiev_Dic={}
        for lineindex in range(start_lineindex,end_lineindex+1):
            AllKPI_OneAgent=self.get_UBIZICM_Performance_Data_Expected(lineindex)
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
    
    
