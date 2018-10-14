'''
Created on Apr 5, 2017

@author: symbio
'''
from public_method.Get_file import Get_file
from public_method.KPI_method import KPI_method

class Get_PerformanceData_Expected_VXIIP():
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.VXIIP_Performance_Sheetiname="VXIIP"
        
    def get_VXIIP_Performance_Data_Expected(self,lineindex): 
        '''
        Can get all data include all KPI of site,tl,agent
        The range of linenumber_Yesterday:TL1~5-16,TL2~21-25
        The range of linenumber_WTD:64-81
        The range of linenumber_MTD:86-103
        The range of linenumber_LASTMONTH:109-126
        The range of linenumber_LASTTWOMONTH:132-137
        '''
        #table=self.Get_sheet_Info(self.VXIIP_Performance_Sheetiname)
        Getfile=Get_file()
        table=Getfile.Get_performance_sheet_Info(self.VXIIP_Performance_Sheetiname)
        KPIMethod=KPI_method()
        Name_value=table.row_values(lineindex)[0]
        Name_status=''
        Name=[Name_value,Name_status]
        
        VOC_Number_value=table.row_values(lineindex)[2]
        VOC_Number_status=table.row_values(lineindex)[3]
        VOC_Number=[VOC_Number_value,VOC_Number_status]
        
        VOC_OverallScore_value=table.row_values(lineindex)[5]
        VOC_OverallScore_status=table.row_values(lineindex)[6]
        VOC_OverallScore=[VOC_OverallScore_value,VOC_OverallScore_status]
        
        SevenDayRepeats_Repeats_value=table.row_values(lineindex)[9]
        SevenDayRepeats_Repeats_status=table.row_values(lineindex)[10]
        SevenDayRepeats_Repeats=[SevenDayRepeats_Repeats_value,SevenDayRepeats_Repeats_status]
        
        SevenDayRepeats_ManagedCalls_value=table.row_values(lineindex)[12]
        SevenDayRepeats_ManagedCalls_status=table.row_values(lineindex)[13]
        SevenDayRepeats_ManagedCalls=[SevenDayRepeats_ManagedCalls_value,SevenDayRepeats_ManagedCalls_status]
        
        SevenDayRepeats_RepeatRate_value=table.row_values(lineindex)[14]
        SevenDayRepeats_RepeatRate_status=table.row_values(lineindex)[15]
        SevenDayRepeats_RepeatRate=[SevenDayRepeats_RepeatRate_value,SevenDayRepeats_RepeatRate_status]
        
        Productivity_AHT_value=table.row_values(lineindex)[20]
        Productivity_AHT_status=table.row_values(lineindex)[21]
        Productivity_AHT=[Productivity_AHT_value,Productivity_AHT_status]
        
        Transfers_value=table.row_values(lineindex)[27]
        Transfers_status=table.row_values(lineindex)[28]
        Transfers=[Transfers_value,Transfers_status]
        
        Adjustment_value=table.row_values(lineindex)[30]
        Adjustment_status=table.row_values(lineindex)[31]
        Adjustment=[Adjustment_value,Adjustment_status]
        
        AdjustmentPerCall_value=table.row_values(lineindex)[32]
        AdjustmentPerCall_status=table.row_values(lineindex)[33]
        AdjustmentPerCall=[AdjustmentPerCall_value,AdjustmentPerCall_status]
        
        Wireless_value=table.row_values(lineindex)[35]
        Wireless_status=table.row_values(lineindex)[36]
        Wireless=[Wireless_value,Wireless_status]
        
        Broadband_value=table.row_values(lineindex)[38]
        Broadband_status=table.row_values(lineindex)[39]
        Broadband=[Broadband_value,Broadband_status]
        
        DTV_value=table.row_values(lineindex)[41]
        DTV_status=table.row_values(lineindex)[42]
        DTV=[DTV_value,DTV_status]
        
        DTV_BB_VOIP_IPTV_value=table.row_values(lineindex)[43]
        DTV_BB_VOIP_IPTV_status=""
        DTV_BB_VOIP_IPTV=[DTV_BB_VOIP_IPTV_value,DTV_BB_VOIP_IPTV_status]
        
        Achiev_value=table.row_values(lineindex)[44]
        Achiev_status=""
        Achiev=[Achiev_value,Achiev_status]

        
        
        Eachline_KPI={"Name":Name,"VOC_Number":VOC_Number,"VOC_OverallScore":VOC_OverallScore,"SevenDayRepeats_Repeats":SevenDayRepeats_Repeats,
                  "SevenDayRepeats_ManagedCalls":SevenDayRepeats_ManagedCalls,"SevenDayRepeats_RepeatRate":SevenDayRepeats_RepeatRate,
                  "Productivity_AHT":Productivity_AHT,"Transfers":Transfers,"Adjustment":Adjustment,"AdjustmentPerCall":AdjustmentPerCall,
                  "Wireless":Wireless,"Broadband":Broadband,"DTV":DTV,"DTV_BB_VOIP_IPTV":DTV_BB_VOIP_IPTV,"Achiev":Achiev}
        for key in Eachline_KPI:
            if key not in ["Name","VOC_OverallScore","Transfers","SevenDayRepeats_RepeatRate"]:
                Decimal_digits='0.00'
                Eachline_KPI[key][0]=str(KPIMethod.Change_Decimal_digits(Eachline_KPI[key][0],Decimal_digits))#If not str, the value of AHT will be Decimal('650.00')
            elif key!="Name":
                Eachline_KPI[key][0]=KPIMethod.Decimal_To_Percentage(Eachline_KPI[key][0])
        
        return Eachline_KPI
    
    

    def get_VXIIP_Goal_Expected(self,lineindex): 
        #table=self.Get_sheet_Info(self.VXIIP_Performance_Sheetiname)
        Getfile=Get_file()
        table=Getfile.Get_performance_sheet_Info(self.VXIIP_Performance_Sheetiname)
        KPIMethod=KPI_method()
        VOC_Number=table.row_values(lineindex)[1]
        VOC_OverallScore=table.row_values(lineindex)[4]
        SevenDayRepeats_Repeats=table.row_values(lineindex)[8]
        SevenDayRepeats_ManagedCalls =table.row_values(lineindex)[11]
        SevenDayRepeats_RepeatRate=table.row_values(lineindex)[14]
        Productivity_AHT=table.row_values(lineindex)[17]
        Transfers=table.row_values(lineindex)[24]
        Adjustment=table.row_values(lineindex)[29]
        AdjustmentPerCall=table.row_values(lineindex)[32]
        Wireless=table.row_values(lineindex)[34]
        Broadband=table.row_values(lineindex)[37]
        DTV=table.row_values(lineindex)[40]
        DTV_BB_VOIP_IPTV=table.row_values(lineindex)[43]
        Achiev='N/A'
        Goal_KPI={"VOC_Number":VOC_Number,"VOC_OverallScore":VOC_OverallScore,"SevenDayRepeats_Repeats":SevenDayRepeats_Repeats,
                  "SevenDayRepeats_ManagedCalls":SevenDayRepeats_ManagedCalls,"SevenDayRepeats_RepeatRate":SevenDayRepeats_RepeatRate,
                  "Productivity_AHT":Productivity_AHT,"Transfers":Transfers,"Adjustment":Adjustment,"AdjustmentPerCall":AdjustmentPerCall,
                  "Wireless":Wireless,"Broadband":Broadband,"DTV":DTV,"DTV_BB_VOIP_IPTV":DTV_BB_VOIP_IPTV,"Achiev":Achiev}
        for key in Goal_KPI:
            if key not in ["VOC_OverallScore","Transfers","SevenDayRepeats_RepeatRate"]:
                Decimal_digits='0.00'
                Goal_KPI[key]=str(KPIMethod.Change_Decimal_digits(Goal_KPI[key],Decimal_digits))#If not str, the value of AHT will be Decimal('650.00')
            else:
                Goal_KPI[key]=KPIMethod.Decimal_To_Percentage(Goal_KPI[key])
        return Goal_KPI
    
            
    def Get_ManyAgentAchiev_Expected(self,start_lineindex,end_lineindex):
        Agent_Achiev_Dic={}
        for lineindex in range(start_lineindex,end_lineindex+1):
            AllKPI_OneAgent=self.get_VXIIP_Performance_Data_Expected(lineindex)
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
    
    def Get_AllDic_Expected(self,Timetab):   
        '''Prepare Data for the following test '''
        if Timetab=="LastTwoMonth":
            Expected_KPIofSITEDic=self.get_VXIIP_Performance_Data_Expected(133)#For Step2
            Expected_KPIofTl1=self.get_VXIIP_Performance_Data_Expected(132)#For Step3
            Expected_AgentAchiev=self.Get_ManyAgentAchiev_Expected(129, 131)#For Step4
            Expected_KPIofAgent8="N/A"#For Step5
            Expected_KPIofAgent11=self.get_VXIIP_Performance_Data_Expected(131)#For Step6
            
        elif Timetab=="LastMonth":
            Expected_KPIofSITEDic=self.get_VXIIP_Performance_Data_Expected(121)#For Step2
            Expected_KPIofTl1=self.get_VXIIP_Performance_Data_Expected(115)#For Step3
            Expected_AgentAchiev=self.Get_ManyAgentAchiev_Expected(104, 114)#For Step4
            Expected_KPIofAgent8=self.get_VXIIP_Performance_Data_Expected(111)#For Step5
            Expected_KPIofAgent11=self.get_VXIIP_Performance_Data_Expected(114)#For Step6
        elif Timetab=="Yesterday":
            Expected_KPIofSITEDic=self.get_VXIIP_Performance_Data_Expected(26)#For Step2
            Expected_KPIofTl1=self.get_VXIIP_Performance_Data_Expected(16)#For Step3
            Expected_AgentAchiev=self.Get_ManyAgentAchiev_Expected(5, 15)#For Step4
            Expected_KPIofAgent8=self.get_VXIIP_Performance_Data_Expected(12)#For Step5
            Expected_KPIofAgent11=self.get_VXIIP_Performance_Data_Expected(15)#For Step6
            
        elif Timetab== "Week-to-Date":
            Expected_KPIofSITEDic=self.get_VXIIP_Performance_Data_Expected(72)#For Step2
            Expected_KPIofTl1=self.get_VXIIP_Performance_Data_Expected(66)#For Step3
            Expected_AgentAchiev=self.Get_ManyAgentAchiev_Expected(55, 65)#For Step4
            Expected_KPIofAgent8=self.get_VXIIP_Performance_Data_Expected(62)#For Step5
            Expected_KPIofAgent11=self.get_VXIIP_Performance_Data_Expected(65)#For Step6
        elif Timetab=="Month-to-Date":
            Expected_KPIofSITEDic=self.get_VXIIP_Performance_Data_Expected(97)#For Step2
            Expected_KPIofTl1=self.get_VXIIP_Performance_Data_Expected(91)#For Step3
            Expected_AgentAchiev=self.Get_ManyAgentAchiev_Expected(80, 90)#For Step4
            Expected_KPIofAgent8=self.get_VXIIP_Performance_Data_Expected(87)#For Step5
            Expected_KPIofAgent11=self.get_VXIIP_Performance_Data_Expected(90)#For Step6
        AllExpectedValue_Dic={"Expected_KPIofSITEDic":Expected_KPIofSITEDic,"Expected_KPIofTl1":Expected_KPIofTl1,
                              "Expected_AgentAchiev":Expected_AgentAchiev,"Expected_KPIofAgent8":Expected_KPIofAgent8,
                              "Expected_KPIofAgent11":Expected_KPIofAgent11}
        return AllExpectedValue_Dic
