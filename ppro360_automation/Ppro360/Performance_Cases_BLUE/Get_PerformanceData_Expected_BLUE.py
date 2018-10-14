'''
Created on Apr 5, 2017

@author: symbio
'''
from public_method.Get_file import Get_file
from public_method.KPI_method import KPI_method

class Get_PerformanceData_Expected_BLUE():
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.BLUE_Performance_Sheetiname="BLUE"
        
    def get_BLUE_Performance_Data_Expected(self,lineindex): 
        '''
        Can get all data include all KPI of site,tl,agent
        The range of linenumber_Yesterday:TL1~5-16,TL2~21-25
        The range of linenumber_WTD:60-73
        The range of linenumber_MTD:78-91
        '''
        #table=self.Get_sheet_Info(self.BLUE_Performance_Sheetiname)
        Getfile=Get_file()
        table=Getfile.Get_performance_sheet_Info(self.BLUE_Performance_Sheetiname)
        KPIMethod=KPI_method()
        Name_value=table.row_values(lineindex)[0]
        Name_status=''
        Name=[Name_value,Name_status]
        
        CRFT_value=table.row_values(lineindex)[2]
        CRFT_status=table.row_values(lineindex)[3]
        CRFT=[CRFT_value,CRFT_status]
        
        SevenDayRepeats_value=table.row_values(lineindex)[5]
        SevenDayRepeats_status=table.row_values(lineindex)[6]
        SevenDayRepeats=[SevenDayRepeats_value,SevenDayRepeats_status]
        
        NetRevenue_Chargeback_value=table.row_values(lineindex)[8]
        NetRevenue_Chargeback_status=table.row_values(lineindex)[9]
        NetRevenue_Chargeback=[NetRevenue_Chargeback_value,NetRevenue_Chargeback_status]
        
        NetRevenue_Net_value=table.row_values(lineindex)[11]
        NetRevenue_Net_status=table.row_values(lineindex+1)[12]
        NetRevenue_Net=[NetRevenue_Net_value,NetRevenue_Net_status]
        
        Broadband_Chargeback_value=table.row_values(lineindex)[14]
        Broadband_Chargeback_status=table.row_values(lineindex)[15]
        Broadband_Chargeback=[Broadband_Chargeback_value,Broadband_Chargeback_status]
        
        Broadband_Net_value=[table.row_values(lineindex)[17],table.row_values(lineindex+1)[17]]
        Broadband_Net_status=table.row_values(lineindex+1)[18]
        Broadband_Net=[Broadband_Net_value,Broadband_Net_status]
        
        DTV_Chargeback_value=table.row_values(lineindex)[20]
        DTV_Chargeback_status=table.row_values(lineindex+1)[21]
        DTV_Chargeback=[DTV_Chargeback_value,DTV_Chargeback_status]
        
        DTV_Net_value=[table.row_values(lineindex)[23],table.row_values(lineindex+1)[23]]
        DTV_Net_status=table.row_values(lineindex+1)[24]
        DTV_Net=[DTV_Net_value,DTV_Net_status]
        
        IPTV_value=[table.row_values(lineindex)[26],table.row_values(lineindex+1)[26]]
        IPTV_status=table.row_values(lineindex+1)[27]
        IPTV=[IPTV_value,IPTV_status]
        
        VOIP_value=[table.row_values(lineindex)[29],table.row_values(lineindex+1)[29]]
        VOIP_status=table.row_values(lineindex+1)[30]
        VOIP=[VOIP_value,VOIP_status]
        
        Wireless_value=[table.row_values(lineindex)[32],table.row_values(lineindex+1)[32]]
        Wireless_status=table.row_values(lineindex+1)[33]
        Wireless=[Wireless_value,Wireless_status]
        
        IPTV_VOIP_Wireless_value=[table.row_values(lineindex)[34],table.row_values(lineindex+1)[34]]
        IPTV_VOIP_Wireless_status=table.row_values(lineindex+1)[35]
        IPTV_VOIP_Wireless=[IPTV_VOIP_Wireless_value,IPTV_VOIP_Wireless_status]
        
        Achiev_value=table.row_values(lineindex)[36]
        Achiev_status=''
        Achiev=[Achiev_value,Achiev_status]


        
        Eachline_KPI={"Name":Name,"CRFT":CRFT,"SevenDayRepeats":SevenDayRepeats,"NetRevenue_Chargeback":NetRevenue_Chargeback,
                  "NetRevenue_Net":NetRevenue_Net,"Broadband_Chargeback":Broadband_Chargeback,"Broadband_Net":Broadband_Net,
                  "DTV_Chargeback":DTV_Chargeback,"DTV_Net":DTV_Net,"IPTV":IPTV,"VOIP":VOIP,"Wireless":Wireless,
                  "IPTV_VOIP_Wireless":IPTV_VOIP_Wireless,"Achiev":Achiev}
        for key in Eachline_KPI:
            if type(Eachline_KPI[key][0])==list:
                if Eachline_KPI[key][0][0]=='N/A' and Eachline_KPI[key][0][1]=='':
                    Eachline_KPI[key][0]='N/A'
       
        for key in Eachline_KPI:
            if key in ["CRFT","SevenDayRepeats"]:
                Eachline_KPI[key][0]=KPIMethod.Decimal_To_Percentage(Eachline_KPI[key][0])
            elif key not in ["Name","NetRevenue_Chargeback","NetRevenue_Net"]:
                if type(Eachline_KPI[key][0])==list:
                    for item in Eachline_KPI[key][0]:
                        Decimal_digits='0.00'
                        item=str(KPIMethod.Change_Decimal_digits(item,Decimal_digits))#If not str, the value of AHT will be Decimal('650.00')
                elif Eachline_KPI[key][0] !='N/A':
                    Decimal_digits='0.00'
                    Eachline_KPI[key][0]=str(KPIMethod.Change_Decimal_digits(Eachline_KPI[key][0],Decimal_digits))#If not str, the value of AHT will be Decimal('650.00')
        
        return Eachline_KPI
    
    

    def get_BLUE_Goal_Expected(self,lineindex): 
        #table=self.Get_sheet_Info(self.BLUE_Performance_Sheetiname)
        Getfile=Get_file()
        table=Getfile.Get_performance_sheet_Info(self.BLUE_Performance_Sheetiname)
        
        CRFT=table.row_values(lineindex)[1]
        SevenDayRepeats=table.row_values(lineindex)[4]
        #NetRevenue_Chargeback=[table.row_values(lineindex)[7],table.row_values(lineindex+1)[7]]
        NetRevenue_Chargeback=table.row_values(lineindex)[7]
        NetRevenue_Net=[table.row_values(lineindex)[10],table.row_values(lineindex+1)[10]]
        Broadband_Chargeback=table.row_values(lineindex)[13]
        Broadband_Net=[table.row_values(lineindex)[16],table.row_values(lineindex+1)[16]]
        DTV_Chargeback=table.row_values(lineindex)[19]
        
        DTV_Net=[table.row_values(lineindex)[22],table.row_values(lineindex+1)[22]]
        IPTV=[table.row_values(lineindex)[25],table.row_values(lineindex+1)[25]]
        VOIP=[table.row_values(lineindex)[28],table.row_values(lineindex+1)[28]]
        Wireless=[table.row_values(lineindex)[31],table.row_values(lineindex+1)[31]]
        IPTV_VOIP_Wireless=[table.row_values(lineindex)[34],table.row_values(lineindex+1)[34]]
        
        #Achiev=table.row_values(lineindex)[36]
        Achiev='N/A'
        Goal_KPI={"CRFT":CRFT,"SevenDayRepeats":SevenDayRepeats,"NetRevenue_Chargeback":NetRevenue_Chargeback,
                  "NetRevenue_Net":NetRevenue_Net,"Broadband_Chargeback":Broadband_Chargeback,"Broadband_Net":Broadband_Net,
                  "DTV_Chargeback":DTV_Chargeback,"DTV_Net":DTV_Net,"IPTV":IPTV,"VOIP":VOIP,"Wireless":Wireless,
                  "IPTV_VOIP_Wireless":IPTV_VOIP_Wireless,"Achiev":Achiev}
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
        for lineindex in range(start_lineindex,end_lineindex+1):
            AllKPI_OneAgent=self.get_BLUE_Performance_Data_Expected(lineindex)
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
    
    
