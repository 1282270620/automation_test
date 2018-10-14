'''
Created on Apr 5, 2017

@author: symbio
'''
from public_method.Get_file import Get_file
from public_method.KPI_method import KPI_method

class Get_PerformanceData_Expected_MOVERS():
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.MOVERS_Performance_Sheetiname="MOVERS"
        
    def get_MOVERS_Performance_Data_Expected(self,lineindex): 
        '''
        Can get all data include all KPI of site,tl,agent
        The range of linenumber_Yesterday:TL1~5-16,TL2~21-25
        The range of linenumber_WTD:64-81
        The range of linenumber_MTD:86-103
        The range of linenumber_LASTMONTH:109-126
        The range of linenumber_LASTTWOMONTH:132-137
        '''
        #table=self.Get_sheet_Info(self.MOVERS_Performance_Sheetiname)
        Getfile=Get_file()
        table=Getfile.Get_performance_sheet_Info(self.MOVERS_Performance_Sheetiname)
        KPIMethod=KPI_method()
        Name_value=table.row_values(lineindex)[0]
        Name_status=''
        Name=[Name_value,Name_status]
        
        LoyaltyRate_value=table.row_values(lineindex)[3]
        LoyaltyRate_status=table.row_values(lineindex)[4]
        LoyaltyRate=[LoyaltyRate_value,LoyaltyRate_status]
        
        BroadbandGrossSales1_value=table.row_values(lineindex)[6]
        BroadbandGrossSales2_value=table.row_values(lineindex)[7]
        BroadbandGrossSales_value=[BroadbandGrossSales1_value,BroadbandGrossSales2_value]
        BroadbandGrossSales_status=table.row_values(lineindex)[8]
        BroadbandGrossSales=[BroadbandGrossSales_value,BroadbandGrossSales_status]
        
        DisconnectRate_value=table.row_values(lineindex)[11]
        DisconnectRate_status=table.row_values(lineindex)[12]
        DisconnectRate=[DisconnectRate_value,DisconnectRate_status]
        
        VOC_value=table.row_values(lineindex)[14]
        VOC_status=table.row_values(lineindex)[15]
        VOC=[VOC_value,VOC_status]
        
        MobilityGrossSales1_value=table.row_values(lineindex)[16]
        MobilityGrossSales2_value=table.row_values(lineindex)[17]
        MobilityGrossSales_status=table.row_values(lineindex)[18]
        MobilityGrossSales_value=[MobilityGrossSales1_value,MobilityGrossSales2_value]
        MobilityGrossSales=[MobilityGrossSales_value,MobilityGrossSales_status]
        
        DTVNowActivations1_value=table.row_values(lineindex)[19]
        DTVNowActivations2_value=table.row_values(lineindex)[20]
        DTVNowActivations_value=[DTVNowActivations1_value,DTVNowActivations2_value]
        DTVNowActivations_status=table.row_values(lineindex)[21]
        DTVNowActivations=[DTVNowActivations_value,DTVNowActivations_status]
        
        AHT_value=table.row_values(lineindex)[23]
        AHT_status=table.row_values(lineindex)[24]
        AHT=[AHT_value,AHT_status]
        
        B2P_value=table.row_values(lineindex)[25]
        B2P_status=table.row_values(lineindex)[26]
        B2P=[B2P_value,B2P_status]
        
        ABS_value=table.row_values(lineindex)[29]
        ABS_status=table.row_values(lineindex)[30]
        ABS=[ABS_value,ABS_status]
        
        Achiev_value=table.row_values(lineindex)[31]
        Achiev_status=""
        Achiev=[Achiev_value,Achiev_status]
                
        
        Eachline_KPI={"Name":Name,"LoyaltyRate":LoyaltyRate,"BroadbandGrossSales":BroadbandGrossSales,"DisconnectRate":DisconnectRate,
                      "VOC":VOC,"MobilityGrossSales":MobilityGrossSales,"DTVNowActivations":DTVNowActivations,"AHT":AHT,"B2P":B2P,
                      "ABS":ABS,"Achiev":Achiev}
        
        #print Eachline_KPI
        for key in Eachline_KPI:
            if key in ["BroadbandGrossSales","MobilityGrossSales","DTVNowActivations","AHT"]:
                Decimal_digits='0.00'
                if key=="AHT":
                    Eachline_KPI[key][0]=str(KPIMethod.Change_Decimal_digits(Eachline_KPI[key][0],Decimal_digits))#If not str, the value of AHT will be Decimal('650.00')
                else:
                    Eachline_KPI[key][0][0]=str(KPIMethod.Change_Decimal_digits(Eachline_KPI[key][0][0],Decimal_digits))#If not str, the value of AHT will be Decimal('650.00')
                    Eachline_KPI[key][0][1]=str(KPIMethod.Change_Decimal_digits(Eachline_KPI[key][0][1],Decimal_digits))#If not str, the value of AHT will be Decimal('650.00')
            elif key!="Name":
                Eachline_KPI[key][0]=KPIMethod.Decimal_To_Percentage(Eachline_KPI[key][0])
        
        return Eachline_KPI
    
    

    def get_MOVERS_Goal_Expected(self,lineindex): 
        #table=self.Get_sheet_Info(self.MOVERS_Performance_Sheetiname)
        Getfile=Get_file()
        table=Getfile.Get_performance_sheet_Info(self.MOVERS_Performance_Sheetiname)
        KPIMethod=KPI_method()
        LoyaltyRate=table.row_values(lineindex)[1]
        BroadbandGrossSales1=table.row_values(lineindex)[5]
        BroadbandGrossSales2=table.row_values(lineindex)[6]
        BroadbandGrossSales=[BroadbandGrossSales1,BroadbandGrossSales2]
        DisconnectRate=table.row_values(lineindex)[9]
        VOC=table.row_values(lineindex)[13]
        MobilityGrossSales1=table.row_values(lineindex)[16]
        MobilityGrossSales2=table.row_values(lineindex)[17]
        MobilityGrossSales=[MobilityGrossSales1,MobilityGrossSales2]
        DTVNowActivations1=table.row_values(lineindex)[19]
        DTVNowActivations2=table.row_values(lineindex)[20]
        DTVNowActivations=[DTVNowActivations1,DTVNowActivations2]
        AHT=table.row_values(lineindex)[22]
        B2P=table.row_values(lineindex)[25]
        ABS=table.row_values(lineindex)[27]
        Achiev=table.row_values(lineindex)[31]
        Goal_KPI={"LoyaltyRate":LoyaltyRate,"BroadbandGrossSales":BroadbandGrossSales,"DisconnectRate":DisconnectRate,"VOC":VOC,
                  "MobilityGrossSales":MobilityGrossSales,"DTVNowActivations":DTVNowActivations,"AHT":AHT,"B2P":B2P,"ABS":ABS,
                  "Achiev":Achiev}
        for key in Goal_KPI:
            if key in ["BroadbandGrossSales","MobilityGrossSales","DTVNowActivations","AHT"]:
                Decimal_digits='0.00'
                if key=="AHT":
                    Goal_KPI[key]=str(KPIMethod.Change_Decimal_digits(Goal_KPI[key],Decimal_digits))#If not str, the value of AHT will be Decimal('650.00')
                else:
                    Goal_KPI[key][0]=str(KPIMethod.Change_Decimal_digits(Goal_KPI[key][0],Decimal_digits))#If not str, the value of AHT will be Decimal('650.00')
                    Goal_KPI[key][1]=str(KPIMethod.Change_Decimal_digits(Goal_KPI[key][1],Decimal_digits))#If not str, the value of AHT will be Decimal('650.00')
            elif Goal_KPI[key]!='N/A':
                Goal_KPI[key]=KPIMethod.Decimal_To_Percentage(Goal_KPI[key])
        return Goal_KPI
    
            
    def Get_ManyAgentAchiev_Expected(self,start_lineindex,end_lineindex):
        Agent_Achiev_Dic={}
        for lineindex in range(start_lineindex,end_lineindex+1):
            AllKPI_OneAgent=self.get_MOVERS_Performance_Data_Expected(lineindex)
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
            Expected_KPIofSITEDic=self.get_MOVERS_Performance_Data_Expected(124)#For Step2
            Expected_KPIofTl1=self.get_MOVERS_Performance_Data_Expected(123)#For Step3
            Expected_AgentAchiev=self.Get_ManyAgentAchiev_Expected(120, 122)#For Step4
            Expected_KPIofAgent8="N/A"#For Step5
            Expected_KPIofAgent11=self.get_MOVERS_Performance_Data_Expected(122)#For Step6
            
        elif Timetab=="LastMonth":
            Expected_KPIofSITEDic=self.get_MOVERS_Performance_Data_Expected(114)#For Step2
            Expected_KPIofTl1=self.get_MOVERS_Performance_Data_Expected(108)#For Step3
            Expected_AgentAchiev=self.Get_ManyAgentAchiev_Expected(97, 107)#For Step4
            Expected_KPIofAgent8=self.get_MOVERS_Performance_Data_Expected(104)#For Step5
            Expected_KPIofAgent11=self.get_MOVERS_Performance_Data_Expected(107)#For Step6
        elif Timetab=="Yesterday":
            Expected_KPIofSITEDic=self.get_MOVERS_Performance_Data_Expected(25)#For Step2
            Expected_KPIofTl1=self.get_MOVERS_Performance_Data_Expected(16)#For Step3
            Expected_AgentAchiev=self.Get_ManyAgentAchiev_Expected(5, 15)#For Step4
            Expected_KPIofAgent8=self.get_MOVERS_Performance_Data_Expected(12)#For Step5
            Expected_KPIofAgent11=self.get_MOVERS_Performance_Data_Expected(15)#For Step6
            
        elif Timetab== "Week-to-Date":
            Expected_KPIofSITEDic=self.get_MOVERS_Performance_Data_Expected(68)#For Step2
            Expected_KPIofTl1=self.get_MOVERS_Performance_Data_Expected(62)#For Step3
            Expected_AgentAchiev=self.Get_ManyAgentAchiev_Expected(51, 61)#For Step4
            Expected_KPIofAgent8=self.get_MOVERS_Performance_Data_Expected(58)#For Step5
            Expected_KPIofAgent11=self.get_MOVERS_Performance_Data_Expected(61)#For Step6
        elif Timetab=="Month-to-Date":
            Expected_KPIofSITEDic=self.get_MOVERS_Performance_Data_Expected(91)#For Step2
            Expected_KPIofTl1=self.get_MOVERS_Performance_Data_Expected(85)#For Step3
            Expected_AgentAchiev=self.Get_ManyAgentAchiev_Expected(74, 84)#For Step4
            Expected_KPIofAgent8=self.get_MOVERS_Performance_Data_Expected(81)#For Step5
            Expected_KPIofAgent11=self.get_MOVERS_Performance_Data_Expected(84)#For Step6
        AllExpectedValue_Dic={"Expected_KPIofSITEDic":Expected_KPIofSITEDic,"Expected_KPIofTl1":Expected_KPIofTl1,
                              "Expected_AgentAchiev":Expected_AgentAchiev,"Expected_KPIofAgent8":Expected_KPIofAgent8,
                              "Expected_KPIofAgent11":Expected_KPIofAgent11}
        return AllExpectedValue_Dic
