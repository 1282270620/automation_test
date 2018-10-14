'''
Created on Apr 5, 2017

@author: symbio
'''
from public_method.Get_file import Get_file
from public_method.KPI_method import KPI_method

class Get_PerformanceData_Expected_PAYPAL():
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.PAYPAL_Performance_Sheetiname="PAYPAL"
        
    def get_PAYPAL_Performance_Data_Expected(self,lineindex): 
        '''
        Can get all data include all KPI of site,tl,agent
        The range of linenumber_Yesterday:TL1~5-16,TL2~21-25
        The range of linenumber_WTD:64-81
        The range of linenumber_MTD:86-103
        The range of linenumber_LASTMONTH:109-126
        The range of linenumber_LASTTWOMONTH:132-137
        '''
        #table=self.Get_sheet_Info(self.PAYPAL_Performance_Sheetiname)
        Getfile=Get_file()
        table=Getfile.Get_performance_sheet_Info(self.PAYPAL_Performance_Sheetiname)
        KPIMethod=KPI_method()
        Name_value=table.row_values(lineindex)[0]
        Name_status=''
        Name=[Name_value,Name_status]
        
        NPS_value=table.row_values(lineindex)[4]
        NPS_status=table.row_values(lineindex)[5]
        NPS=[NPS_value,NPS_status]
        
        AHT_value=table.row_values(lineindex)[8]
        AHT_status=table.row_values(lineindex)[9]
        AHT=[AHT_value,AHT_status]
        
        HP_value=table.row_values(lineindex)[12]
        HP_status=table.row_values(lineindex)[13]
        HP=[HP_value,HP_status]
        
        SGI_value=table.row_values(lineindex)[16]
        SGI_status=table.row_values(lineindex)[17]
        SGI=[SGI_value,SGI_status]
        
        TO_value=table.row_values(lineindex)[20]
        TO_status=table.row_values(lineindex)[21]
        TO=[TO_value,TO_status]
        
        KHR_value=table.row_values(lineindex)[24]
        KHR_status=table.row_values(lineindex)[25]
        KHR=[KHR_value,KHR_status]
        
        VC_value=table.row_values(lineindex)[28]
        VC_status=table.row_values(lineindex)[29]
        VC=[VC_value,VC_status]
        
        KDIPhone_value=table.row_values(lineindex)[30]
        KDIPhone_status=table.row_values(lineindex)[31]
        KDIPhone=[KDIPhone_value,KDIPhone_status]
        
        RCR_value=table.row_values(lineindex)[34]
        RCR_status=table.row_values(lineindex)[35]
        RCR=[RCR_value,RCR_status]
        
        TR_value=table.row_values(lineindex)[38]
        TR_status=table.row_values(lineindex)[39]
        TR=[TR_value,TR_status]
        
        
        Achiev_value=table.row_values(lineindex)[40]
        Achiev_status=table.row_values(lineindex)[41]
        Achiev=[Achiev_value,Achiev_status]

        
        
        Eachline_KPI={"Name":Name,"NPS":NPS,"AHT":AHT,"HP":HP,"SGI":SGI,"TO":TO,"KHR":KHR,"VC":VC,
                  "KDIPhone":KDIPhone,"RCR":RCR,"TR":TR,"Achiev":Achiev}
        for key in Eachline_KPI:
            if key in ["AHT","KDIPhone"]:
                Decimal_digits='0.00'
                Eachline_KPI[key][0]=str(KPIMethod.Change_Decimal_digits(Eachline_KPI[key][0],Decimal_digits))#If not str, the value of AHT will be Decimal('650.00')
            elif key!="Name":
                Eachline_KPI[key][0]=KPIMethod.Decimal_To_Percentage(Eachline_KPI[key][0])
        
        return Eachline_KPI
    
    

    def get_PAYPAL_Goal_Expected(self,lineindex): 
        #table=self.Get_sheet_Info(self.PAYPAL_Performance_Sheetiname)
        Getfile=Get_file()
        table=Getfile.Get_performance_sheet_Info(self.PAYPAL_Performance_Sheetiname)
        KPIMethod=KPI_method()
        NPS=table.row_values(lineindex)[1]
        AHT=table.row_values(lineindex)[6]
        HP=table.row_values(lineindex)[10]
        SGI=table.row_values(lineindex)[14]
        TO=table.row_values(lineindex)[18]
        KHR=table.row_values(lineindex)[22]
        VC=table.row_values(lineindex)[26]
        KDIPhone=table.row_values(lineindex)[30]
        RCR=table.row_values(lineindex)[32]
        TR=table.row_values(lineindex)[36]
        Achiev='N/A'
        Goal_KPI={"NPS":NPS,"AHT":AHT,"HP":HP,"SGI":SGI,"TO":TO,"KHR":KHR,"VC":VC,
                  "KDIPhone":KDIPhone,"RCR":RCR,"TR":TR,"Achiev":Achiev}
        for key in Goal_KPI:
            if key in ["AHT","KDIPhone"]:
                Decimal_digits='0.00'
                Goal_KPI[key]=str(KPIMethod.Change_Decimal_digits(Goal_KPI[key],Decimal_digits))#If not str, the value of AHT will be Decimal('650.00')
            else:
                Goal_KPI[key]=KPIMethod.Decimal_To_Percentage(Goal_KPI[key])
        return Goal_KPI
    
            
    def Get_ManyAgentAchiev_Expected(self,start_lineindex,end_lineindex):
        Agent_Achiev_Dic={}
        for lineindex in range(start_lineindex,end_lineindex+1):
            AllKPI_OneAgent=self.get_PAYPAL_Performance_Data_Expected(lineindex)
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
            Expected_KPIofSITEDic=self.get_PAYPAL_Performance_Data_Expected(135)#For Step2
            Expected_KPIofTl1=self.get_PAYPAL_Performance_Data_Expected(134)#For Step3
            Expected_AgentAchiev=self.Get_ManyAgentAchiev_Expected(131, 133)#For Step4
            Expected_KPIofAgent8="N/A"#For Step5
            Expected_KPIofAgent11=self.get_PAYPAL_Performance_Data_Expected(133)#For Step6
            
        elif Timetab=="LastMonth":
            Expected_KPIofSITEDic=self.get_PAYPAL_Performance_Data_Expected(123)#For Step2
            Expected_KPIofTl1=self.get_PAYPAL_Performance_Data_Expected(117)#For Step3
            Expected_AgentAchiev=self.Get_ManyAgentAchiev_Expected(106, 116)#For Step4
            Expected_KPIofAgent8=self.get_PAYPAL_Performance_Data_Expected(113)#For Step5
            Expected_KPIofAgent11=self.get_PAYPAL_Performance_Data_Expected(116)#For Step6
        elif Timetab=="Yesterday":
            Expected_KPIofSITEDic=self.get_PAYPAL_Performance_Data_Expected(23)#For Step2
            Expected_KPIofTl1=self.get_PAYPAL_Performance_Data_Expected(17)#For Step3
            Expected_AgentAchiev=self.Get_ManyAgentAchiev_Expected(6, 16)#For Step4
            Expected_KPIofAgent8=self.get_PAYPAL_Performance_Data_Expected(13)#For Step5
            Expected_KPIofAgent11=self.get_PAYPAL_Performance_Data_Expected(16)#For Step6
            
        elif Timetab== "Week-to-Date":
            Expected_KPIofSITEDic=self.get_PAYPAL_Performance_Data_Expected(73)#For Step2
            Expected_KPIofTl1=self.get_PAYPAL_Performance_Data_Expected(67)#For Step3
            Expected_AgentAchiev=self.Get_ManyAgentAchiev_Expected(56, 66)#For Step4
            Expected_KPIofAgent8=self.get_PAYPAL_Performance_Data_Expected(63)#For Step5
            Expected_KPIofAgent11=self.get_PAYPAL_Performance_Data_Expected(66)#For Step6
        elif Timetab=="Month-to-Date":
            Expected_KPIofSITEDic=self.get_PAYPAL_Performance_Data_Expected(98)#For Step2
            Expected_KPIofTl1=self.get_PAYPAL_Performance_Data_Expected(92)#For Step3
            Expected_AgentAchiev=self.Get_ManyAgentAchiev_Expected(81, 91)#For Step4
            Expected_KPIofAgent8=self.get_PAYPAL_Performance_Data_Expected(88)#For Step5
            Expected_KPIofAgent11=self.get_PAYPAL_Performance_Data_Expected(91)#For Step6
        AllExpectedValue_Dic={"Expected_KPIofSITEDic":Expected_KPIofSITEDic,"Expected_KPIofTl1":Expected_KPIofTl1,
                              "Expected_AgentAchiev":Expected_AgentAchiev,"Expected_KPIofAgent8":Expected_KPIofAgent8,
                              "Expected_KPIofAgent11":Expected_KPIofAgent11}
        return AllExpectedValue_Dic
