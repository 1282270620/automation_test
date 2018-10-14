'''
Created on Apr 5, 2017

@author: symbio
'''
from public_method.Get_file import Get_file
from public_method.KPI_method import KPI_method

class Get_PerformanceData_Expected_SPANISH():
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.SPANISH_Performance_Sheetiname="SPANISH"
        
    def get_SPANISH_Performance_Data_Expected(self,lineindex): 
        '''
        Can get all data include all KPI of site,tl,agent
        The range of linenumber_Yesterday:TL1~5-16,TL2~21-25
        The range of linenumber_WTD:60-73
        The range of linenumber_MTD:78-91
        '''
        #table=self.Get_sheet_Info(self.SPANISH_Performance_Sheetiname)
        Getfile=Get_file()
        table=Getfile.Get_performance_sheet_Info(self.SPANISH_Performance_Sheetiname)
        KPIMethod=KPI_method()
        Name_value=table.row_values(lineindex)[0]
        Name_status=''
        Name=[Name_value,Name_status]
        
        NetRevenue_Actual_value=[table.row_values(lineindex)[2],table.row_values(lineindex+1)[2]]
        NetRevenue_Actual_status=table.row_values(lineindex+1)[3]
        NetRevenue_Actual=[NetRevenue_Actual_value,NetRevenue_Actual_status]
        
        NetRevenue_Attain_value=table.row_values(lineindex)[5]
        NetRevenue_Attain_status=table.row_values(lineindex)[6]
        NetRevenue_Attain=[NetRevenue_Attain_value,NetRevenue_Attain_status]
        
        HSIAIPDSL_Actual_value=[table.row_values(lineindex)[8],table.row_values(lineindex+1)[8]]
        HSIAIPDSL_Actual_status=table.row_values(lineindex+1)[9]
        HSIAIPDSL_Actual=[HSIAIPDSL_Actual_value,HSIAIPDSL_Actual_status]
        
        HSIAIPDSL_Attain_value=table.row_values(lineindex)[11]
        HSIAIPDSL_Attain_status=table.row_values(lineindex)[12]
        HSIAIPDSL_Attain=[HSIAIPDSL_Attain_value,HSIAIPDSL_Attain_status]
        
        CRFT_Actual_value=table.row_values(lineindex)[14]
        CRFT_Actual_status=table.row_values(lineindex)[15]
        CRFT_Actual=[CRFT_Actual_value,CRFT_Actual_status]
        
        CRFT_Attain_value=table.row_values(lineindex)[17]
        CRFT_Attain_status=table.row_values(lineindex)[18]
        CRFT_Attain=[CRFT_Attain_value,CRFT_Attain_status]
        
        OpsAht_value=table.row_values(lineindex)[20]
        OpsAht_status=table.row_values(lineindex)[21]
        OpsAht=[OpsAht_value,OpsAht_status]
        
        VOIP_Actual_value=[table.row_values(lineindex)[23],table.row_values(lineindex+1)[23]]
        VOIP_Actual_status=table.row_values(lineindex+1)[24]
        VOIP_Actual=[VOIP_Actual_value,VOIP_Actual_status]
        
        VOIP_Attain_value=table.row_values(lineindex)[26]
        VOIP_Attain_status=table.row_values(lineindex)[27]
        VOIP_Attain=[VOIP_Attain_value,VOIP_Attain_status]
        
        WLS_Actual_value=[table.row_values(lineindex)[29],table.row_values(lineindex+1)[29]]
        WLS_Actual_status=table.row_values(lineindex+1)[30]
        WLS_Actual=[WLS_Actual_value,WLS_Actual_status]
        
        WLS_Attain_value=table.row_values(lineindex)[32]
        WLS_Attain_status=table.row_values(lineindex)[33]
        WLS_Attain=[WLS_Attain_value,WLS_Attain_status]
        
        Achiev_value=table.row_values(lineindex)[34]
        Achiev_status=""
        Achiev=[Achiev_value,Achiev_status]
        
        
        Eachline_KPI={"Name":Name,"NetRevenue_Actual":NetRevenue_Actual,"NetRevenue_Attain":NetRevenue_Attain,"HSIAIPDSL_Actual":HSIAIPDSL_Actual,
                  "HSIAIPDSL_Attain":HSIAIPDSL_Attain,"CRFT_Actual":CRFT_Actual,"CRFT_Attain":CRFT_Attain,
                  "OpsAht":OpsAht,"VOIP_Actual":VOIP_Actual,"VOIP_Attain":VOIP_Attain,"WLS_Actual":WLS_Actual,"WLS_Attain":WLS_Attain,
                  "Achiev":Achiev}
        for key in Eachline_KPI:
            if type(Eachline_KPI[key][0])==list:
                if Eachline_KPI[key][0][0]=='N/A' and Eachline_KPI[key][0][1]=='':
                    Eachline_KPI[key][0]='N/A'
                elif Eachline_KPI[key][0][0]=='N/A' and Eachline_KPI[key][0][1]=='N/A':
                    Eachline_KPI[key][0]='N/A'
       
        for key in Eachline_KPI:
            if key in ["NetRevenue_Attain","HSIAIPDSL_Attain","CRFT_Actual","CRFT_Attain","VOIP_Attain","WLS_Attain"]:
                Eachline_KPI[key][0]=KPIMethod.Decimal_To_Percentage(Eachline_KPI[key][0])
            elif key in ["NetRevenue_Actual","HSIAIPDSL_Actual","OpsAht","VOIP_Actual","WLS_Actual"]:
                b=[]
                if type(Eachline_KPI[key][0])==list:
                    for item in Eachline_KPI[key][0]:
                        if key=="NetRevenue_Actual":
                            Decimal_digits='0.000'
                            item=str(KPIMethod.Change_Decimal_digits(item,Decimal_digits))#If not str, the value of AHT will be Decimal('650.00')
                        
                            l=len(item)
                            for i in range(1,4):
                                if item[l-i]=="0": 
                                    item=item[0:l-i]
                                    if i==3 and item[l-i-1]==".":
                                        item=item[0:l-i-1]
                                else:
                                    break
                        else:
                            Decimal_digits='0.00'
                            item=str(KPIMethod.Change_Decimal_digits(item,Decimal_digits))#If not str, the value of AHT will be Decimal('650.00')
                        
                   
                        #if item[len(item)-1]=='0':
                            #item=item[0:len(item)-1]
                        b.append(item)
                    Eachline_KPI[key][0]=b
                elif Eachline_KPI[key][0] !='N/A':
                    Decimal_digits='0.00'
                    Eachline_KPI[key][0]=str(KPIMethod.Change_Decimal_digits(Eachline_KPI[key][0],Decimal_digits))#If not str, the value of AHT will be Decimal('650.00')
                    
        return Eachline_KPI
    
    

    def get_SPANISH_Goal_Expected(self,lineindex): 
        #table=self.Get_sheet_Info(self.SPANISH_Performance_Sheetiname)
        Getfile=Get_file()
        table=Getfile.Get_performance_sheet_Info(self.SPANISH_Performance_Sheetiname)
        NetRevenue_Actual=[table.row_values(lineindex)[1],table.row_values(lineindex+1)[1]]
        NetRevenue_Attain=table.row_values(lineindex)[4]
        HSIAIPDSL_Actual=[table.row_values(lineindex)[7],table.row_values(lineindex+1)[7]]
        HSIAIPDSL_Attain=table.row_values(lineindex)[10]
        CRFT_Actual=table.row_values(lineindex)[13]
        CRFT_Attain=table.row_values(lineindex)[16]
        OpsAht=table.row_values(lineindex)[19]
        VOIP_Actual=[table.row_values(lineindex)[22],table.row_values(lineindex+1)[22]]
        VOIP_Attain=table.row_values(lineindex)[25]
        WLS_Actual=[table.row_values(lineindex)[28],table.row_values(lineindex+1)[28]]
        WLS_Attain=table.row_values(lineindex)[31]
        Achiev='N/A'
        
        Goal_KPI={"NetRevenue_Actual":NetRevenue_Actual,"NetRevenue_Attain":NetRevenue_Attain,"HSIAIPDSL_Actual":HSIAIPDSL_Actual,
                  "HSIAIPDSL_Attain":HSIAIPDSL_Attain,"CRFT_Actual":CRFT_Actual,"CRFT_Attain":CRFT_Attain,
                  "OpsAht":OpsAht,"VOIP_Actual":VOIP_Actual,"VOIP_Attain":VOIP_Attain,"WLS_Actual":WLS_Actual,"WLS_Attain":WLS_Attain,
                  "Achiev":Achiev}
        Goal_KPI=self.handle_kpidata(Goal_KPI)
        return Goal_KPI
    
     
    def handle_kpidata(self,Goal_KPI):  
        KPIMethod=KPI_method()  
        for key in Goal_KPI:
            if type(Goal_KPI[key])==list:
                Decimal_digits='0.00'
                for i in range(0,len(Goal_KPI[key])):
                    Goal_KPI[key][i]=str(KPIMethod.Change_Decimal_digits(Goal_KPI[key][i],Decimal_digits))
            elif key=="Broadband_Chargeback":
                Goal_KPI[key]=str(KPIMethod.Change_Decimal_digits(Goal_KPI[key],Decimal_digits))
            else:
                Goal_KPI[key]=KPIMethod.Decimal_To_Percentage(Goal_KPI[key])
        for key in Goal_KPI:
            if type(Goal_KPI[key])==list:
                if Goal_KPI[key][0]=='' and Goal_KPI[key][1]=='':
                    Goal_KPI[key]='N/A'
                elif Goal_KPI[key][0]=='' and Goal_KPI[key][1]!='':
                    Goal_KPI[key][0]='N/A'
                elif Goal_KPI[key][1]=='' and Goal_KPI[key][0]!='':
                    Goal_KPI[key][1]='N/A'
                elif  Goal_KPI[key][0]=='N/A' and Goal_KPI[key][1]=='N/A':
                    Goal_KPI[key]='N/A'
                    print Goal_KPI[key]
            elif Goal_KPI[key]=='':
                Goal_KPI[key]='N/A'
        return Goal_KPI
    
            
    def Get_ManyAgentAchiev_Expected(self,start_lineindex,end_lineindex):
        Agent_Achiev_Dic={}
        for lineindex in range(start_lineindex,end_lineindex+1,2):
            AllKPI_OneAgent=self.get_SPANISH_Performance_Data_Expected(lineindex)
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
    
    
