'''
Created on 2017.9.21

@author: yalan.yin
'''
import xlrd
from public_method import Gl
from public_method.Get_file import Get_file
from decimal import Decimal

class Get_PerformanceData_Expected_DTVDS(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.DTVDS_Performance_Sheetiname="DTVDS"
        
    def get_DTVDS_Performance_Data_Expected(self,lineindex):
        '''
        Can get all data include all KPI of site,tl,agent
        The range of linenumber_Yesterday:TL1~5-16,TL2~21-25
        The range of linenumber_WTD:60-73
        The range of linenumber_MTD:78-91
        '''
        table=self.Get_sheet_Info(self.DTVDS_Performance_Sheetiname)
        Name_value=table.row_values(lineindex)[0]
        Name_status=''
        Name=[Name_value,Name_status]
        
        CloseRate_value=table.row_values(lineindex)[3]
        CloseRate_status=table.row_values(lineindex)[4]
        CloseRate=[CloseRate_value,CloseRate_status]
        
        VideoActivations_value=table.row_values(lineindex)[6]
        VideoActivations_status=table.row_values(lineindex)[7]
        VideoActivations=[VideoActivations_value,VideoActivations_status]
        
        IPPBAttachRate_value=table.row_values(lineindex)[10]
        IPPBAttachRate_status=table.row_values(lineindex)[11]
        IPPBAttachRate=[IPPBAttachRate_value,IPPBAttachRate_status]
        
        IPPBGrossSales_value=table.row_values(lineindex)[13]
        IPPBGrossSales_status=table.row_values(lineindex)[14]
        IPPBGrossSales=[IPPBGrossSales_value,IPPBGrossSales_status]
        
        MobilitySales_value=table.row_values(lineindex)[16]
        MobilitySales_status=table.row_values(lineindex)[17]
        MobilitySales=[MobilitySales_value,MobilitySales_status]
        
        OverallCallExp_value=table.row_values(lineindex)[20]
        OverallCallExp_status=table.row_values(lineindex)[21]
        OverallCallExp=[OverallCallExp_value,OverallCallExp_status]
        
        CC_value=table.row_values(lineindex)[24]
        CC_status=table.row_values(lineindex)[25]
        CC=[CC_value,CC_status]
        
        NFCR_value=table.row_values(lineindex)[28]
        NFCR_status=table.row_values(lineindex)[29]
        NFCR=[NFCR_value,NFCR_status]
        
        AHT_value=table.row_values(lineindex)[32]
        AHT_status=table.row_values(lineindex)[33]
        AHT=[AHT_value,AHT_status]
        
        CancelRate_value=''
        CancelRate_status=''
        CancelRate=[CancelRate_value,CancelRate_status]
        
        Achiev_value=table.row_values(lineindex)[34]
        Achieve_status=''
        Achiev=[Achiev_value,Achieve_status]
        
        Eachline_KPI={"Name":Name,'CancelRate':CancelRate,'NFCR':NFCR,'CC':CC,'VideoActivations':VideoActivations,'OverallCallExp':OverallCallExp,'IPPBAttachRate':IPPBAttachRate,'IPPBGrossSales':IPPBGrossSales,'AHT':AHT,'CloseRate':CloseRate,'MobilitySales':MobilitySales,'Achiev':Achiev}
        for key in Eachline_KPI:
            if key in ['AHT','VideoActivations','MobilitySales','IPPBGrossSales']:
                Decimal_digits='0.00'
                Eachline_KPI[key][0]=str(self.Change_Decimal_digits(Eachline_KPI[key][0],Decimal_digits))#If not str, the value of AHT will be Decimal('650.00')
            elif key!="Name":
                Eachline_KPI[key][0]=self.Decimal_To_Percentage(Eachline_KPI[key][0])
        
        return Eachline_KPI
        
    def get_DTVDS_Goal_Expected(self,lineindex):
        table=self.Get_sheet_Info(self.DTVDS_Performance_Sheetiname)
        CloseRate=table.row_values(lineindex)[1]
        VideoActivations=table.row_values(lineindex)[5]
        IPPBAttachRate=table.row_values(lineindex)[8]
        IPPBGrossSales=table.row_values(lineindex)[12]
        MobilitySales=table.row_values(lineindex)[15]
        OverallCallExp=table.row_values(lineindex)[18]
        CC=table.row_values(lineindex)[22]
        NFCR=table.row_values(lineindex)[26]
        AHT=table.row_values(lineindex)[30]
        CancelRate=''
        Achiev=table.row_values(lineindex)[34]
        
        Goal_KPI={'CancelRate':CancelRate,'NFCR':NFCR,'CC':CC,'VideoActivations':VideoActivations,'OverallCallExp':OverallCallExp,'IPPBAttachRate':IPPBAttachRate,'IPPBGrossSales':IPPBGrossSales,'AHT':AHT,'CloseRate':CloseRate,'MobilitySales':MobilitySales,'Achiev':Achiev}
        for key in Goal_KPI:
            if key in ['AHT','VideoActivations','MobilitySales','IPPBGrossSales']:
                Decimal_digits='0.00'
                Goal_KPI[key]=str(self.Change_Decimal_digits(Goal_KPI[key],Decimal_digits))#If not str, the value of AHT will be Decimal('650.00')
            else:
                Goal_KPI[key]=self.Decimal_To_Percentage(Goal_KPI[key])
        return Goal_KPI
        
    def Decimal_To_Percentage(self,KPI_value):
        Decimal_digits='0.0000'
        if KPI_value=='0.0':
            KPI_Percentage='0.00%'
        elif KPI_value=='':
            KPI_Percentage=KPI_value
        elif KPI_value=='N/A':
            KPI_Percentage=KPI_value
        else:
            KPI_new=self.Change_Decimal_digits(KPI_value,Decimal_digits)
            KPI_Percentage='%.2f%%' % (KPI_new * 100)
        return KPI_Percentage
    
    def Change_Decimal_digits(self,KPI_value,Decimal_digits):
        if KPI_value=='N/A':
            KPI=KPI_value
        elif KPI_value=='':
            KPI=KPI_value
        else:
            KPI=Decimal(KPI_value).quantize(Decimal(Decimal_digits))#2:'0.00',4:'0.0000'
        return KPI
            
    def Get_ManyAgentAchiev_Expected(self,start_lineindex,end_lineindex):
        Agent_Achiev_Dic={}
        for lineindex in range(start_lineindex,end_lineindex+1):
            AllKPI_OneAgent=self.get_DTVDS_Performance_Data_Expected(lineindex)
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
    
    def Get_sheet_Info(self,sheetname): 
        G=Get_file()
        PerformanceData=G.Get_fileaddress(Gl.PerformanceDatafilename)
    
        Performancedata=xlrd.open_workbook(PerformanceData)
        table = Performancedata.sheet_by_name(sheetname)
        return table
        