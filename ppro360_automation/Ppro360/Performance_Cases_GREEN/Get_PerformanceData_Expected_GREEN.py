'''
Created on 2017.10.10

@author: yalan.yin
'''
from public_method.Get_file import Get_file
from public_method.KPI_method import KPI_method
class Get_PerformanceData_Expected_GREEN(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.GREEN_Performance_Sheetiname="GREEN"
        
    def get_GREEN_Performance_Data_Expected(self,lineindex):
        '''
        Can get all data include all KPI of site,tl,agent
        The range of linenumber_Yesterday:TL1~5-16,TL2~21-25
        The range of linenumber_WTD:60-73
        The range of linenumber_MTD:78-91
        '''
        Getfile=Get_file()
        table=Getfile.Get_performance_sheet_Info(self.GREEN_Performance_Sheetiname)
        KPIMethod=KPI_method()
        Name_value=table.row_values(lineindex)[0]
        Name_status=''
        Name=[Name_value,Name_status]
        
        Revenue_value=table.row_values(lineindex)[2]
        Revenue_status=table.row_values(lineindex)[3]
        Revenue=[Revenue_value,Revenue_status]
        
        Video_value=table.row_values(lineindex)[5]
        Video_status=table.row_values(lineindex)[6]
        Video=[Video_value,Video_status]
        
        Broadband_value=table.row_values(lineindex)[8]
        Broadband_status=table.row_values(lineindex)[9]
        Broadband=[Broadband_value,Broadband_status]
        
        Wireless_value=table.row_values(lineindex)[11]
        Wireless_status=table.row_values(lineindex)[12]
        Wireless=[Wireless_value,Wireless_status]
        
        VOIP_value=table.row_values(lineindex)[14]
        VOIP_status=table.row_values(lineindex)[15]
        VOIP=[VOIP_value,VOIP_status]
        
        VOC_value=table.row_values(lineindex)[19]
        VOC_status=table.row_values(lineindex)[20]
        VOC=[VOC_value,VOC_status]
        
        BARAttainment_value=table.row_values(lineindex)[23]
        BARAttainment_status=table.row_values(lineindex)[24]
        BARAttainment=[BARAttainment_value,BARAttainment_status]
        
        AHT_value=table.row_values(lineindex)[30]
        AHT_status=table.row_values(lineindex)[31]
        AHT=[AHT_value,AHT_status]
       
        Achiev_value=table.row_values(lineindex)[32]
        Achieve_status=''
        Achiev=[Achiev_value,Achieve_status]
        
        Eachline_KPI={"Name":Name,'VOIP':VOIP,'Revenue':Revenue,'Video':Video,'Broadband':Broadband,'AHT':AHT,'Wireless':Wireless,'VOC':VOC,'BARAttainment':BARAttainment,'Achiev':Achiev}
        for key in Eachline_KPI:
            if key in ['AHT', 'Revenue','Video','Broadband','Wireless', 'VOIP']:
                Decimal_digits='0.00'
                Eachline_KPI[key][0]=str(KPIMethod.Change_Decimal_digits(Eachline_KPI[key][0],Decimal_digits))#If not str, the value of AHT will be Decimal('650.00')
            elif key!="Name":
                Eachline_KPI[key][0]=KPIMethod.Decimal_To_Percentage(Eachline_KPI[key][0])
        
        return Eachline_KPI
        
    def get_GREEN_Goal_Expected(self,lineindex):
        Getfile=Get_file()
        table=Getfile.Get_performance_sheet_Info(self.GREEN_Performance_Sheetiname)
        KPIMethod=KPI_method()
        Revenue=table.row_values(lineindex)[1]
        Video=table.row_values(lineindex)[4]
        Broadband=table.row_values(lineindex)[7]
        Wireless=table.row_values(lineindex)[10]
        VOIP=table.row_values(lineindex)[13]
        VOC=table.row_values(lineindex)[16]
        BARAttainment=table.row_values(lineindex)[21]
        AHT=table.row_values(lineindex)[25]       
        Achiev=table.row_values(lineindex)[32]
        
        Goal_KPI={'VOIP':VOIP,'Revenue':Revenue,'Video':Video,'Broadband':Broadband,'AHT':AHT,'Wireless':Wireless,'VOC':VOC,'BARAttainment':BARAttainment,'Achiev':Achiev}
        for key in Goal_KPI:
            if key in ['AHT', 'Revenue','Video','Broadband','Wireless', 'VOIP']:
                Decimal_digits='0.00'
                Goal_KPI[key]=str(KPIMethod.Change_Decimal_digits(Goal_KPI[key],Decimal_digits))#If not str, the value of AHT will be Decimal('650.00')
            else:
                Goal_KPI[key]=KPIMethod.Decimal_To_Percentage(Goal_KPI[key])
        return Goal_KPI
        
    
            
    def Get_ManyAgentAchiev_Expected(self,start_lineindex,end_lineindex):
        Agent_Achiev_Dic={}
        for lineindex in range(start_lineindex,end_lineindex+1):
            AllKPI_OneAgent=self.get_GREEN_Performance_Data_Expected(lineindex)
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
    
        