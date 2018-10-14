'''
Created on Apr 5, 2017

@author: symbio
'''
from public_method.Get_file import Get_file
from public_method.KPI_method import KPI_method

class Get_PerformanceData_Expected_CENTURYLINK():
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.CENTURYLINK_Performance_Sheetiname="CENTURYLINK"
        
    def get_CENTURYLINK_Performance_Data_Expected(self,lineindex): 
        '''
        Can get all data include all KPI of site,tl,agent
        The range of linenumber_Yesterday:TL1~5-16,TL2~21-25
        The range of linenumber_WTD:64-81
        The range of linenumber_MTD:86-103
        The range of linenumber_LASTMONTH:109-126
        The range of linenumber_LASTTWOMONTH:132-137
        '''
        #table=self.Get_sheet_Info(self.CENTURYLINK_Performance_Sheetiname)
        Getfile=Get_file()
        table=Getfile.Get_performance_sheet_Info(self.CENTURYLINK_Performance_Sheetiname)
        KPIMethod=KPI_method()
        Name_value=table.row_values(lineindex)[0]
        Name_status=''
        Name=[Name_value,Name_status]
        
        AttainmenttoGoal_HSI_value=table.row_values(lineindex)[3]
        AttainmenttoGoal_HSI_status=table.row_values(lineindex)[4]
        AttainmenttoGoal_HSI=[AttainmenttoGoal_HSI_value,AttainmenttoGoal_HSI_status]
        
        B2P_value=table.row_values(lineindex)[7]
        B2P_status=table.row_values(lineindex)[8]
        B2P=[B2P_value,B2P_status]
        
        AHT_value=table.row_values(lineindex)[13]
        AHT_status=table.row_values(lineindex)[14]
        AHT=[AHT_value,AHT_status]
        
        Hold_value=table.row_values(lineindex)[16]
        Hold_status=table.row_values(lineindex)[17]
        Hold=[Hold_value,Hold_status]
        
        AbsAbsenteeism_value=table.row_values(lineindex)[20]
        AbsAbsenteeism_status=table.row_values(lineindex)[21]
        AbsAbsenteeism=[AbsAbsenteeism_value,AbsAbsenteeism_status]
        
        AvgQAScore_value=table.row_values(lineindex)[24]
        AvgQAScore_status=table.row_values(lineindex)[25]
        AvgQAScore=[AvgQAScore_value,AvgQAScore_status]
        
        QACalls_value=table.row_values(lineindex)[27]
        QACalls_status=table.row_values(lineindex)[28]
        QACalls=[QACalls_value,QACalls_status]
        
        ofAutoFails_value=table.row_values(lineindex)[30]
        ofAutoFails_status=table.row_values(lineindex)[31]
        ofAutoFails=[ofAutoFails_value,ofAutoFails_status]
        
        MixClose_HSI_value=table.row_values(lineindex)[32]
        MixClose_HSI_status=table.row_values(lineindex)[33]
        MixClose_HSI=[MixClose_HSI_value,MixClose_HSI_status]
        
        AttainmenttoGoal_HSI_1_value=table.row_values(lineindex)[34]
        AttainmenttoGoal_HSI_1_status=table.row_values(lineindex)[35]
        AttainmenttoGoal_HSI_1=[AttainmenttoGoal_HSI_1_value,AttainmenttoGoal_HSI_1_status]
        
        MixClose_TV_value=table.row_values(lineindex)[38]
        MixClose_TV_status=table.row_values(lineindex)[39]
        MixClose_TV=[MixClose_TV_value,MixClose_TV_status]
        
        AttainmenttoGoal_TV_value=table.row_values(lineindex)[41]
        AttainmenttoGoal_TV_status=table.row_values(lineindex)[42]
        AttainmenttoGoal_TV=[AttainmenttoGoal_TV_value,AttainmenttoGoal_TV_status]
        
        AttachRate_DTV_value=table.row_values(lineindex)[43]
        AttachRate_DTV_status=table.row_values(lineindex)[44]
        AttachRate_DTV=[AttachRate_DTV_value,AttachRate_DTV_status]
        
        MixClose_PhoneLines_value=table.row_values(lineindex)[46]
        MixClose_PhoneLines_status=table.row_values(lineindex)[47]
        MixClose_PhoneLines=[MixClose_PhoneLines_value,MixClose_PhoneLines_status]
        
        MixClose_Ease_value=table.row_values(lineindex)[49]
        MixClose_Ease_status=table.row_values(lineindex)[50]
        MixClose_Ease=[MixClose_Ease_value,MixClose_Ease_status]
        
        ACDCalls_value=table.row_values(lineindex)[52]
        ACDCalls_status=table.row_values(lineindex)[53]
        ACDCalls=[ACDCalls_value,ACDCalls_status]
        
        AHTIneligible_value=table.row_values(lineindex)[56]
        AHTIneligible_status=table.row_values(lineindex)[57]
        AHTIneligible=[AHTIneligible_value,AHTIneligible_status]
        
        QualifiedCloseRate_value=table.row_values(lineindex)[58]
        QualifiedCloseRate_status=table.row_values(lineindex)[59]
        QualifiedCloseRate=[QualifiedCloseRate_value,QualifiedCloseRate_status]
        
        
        Achiev_value=table.row_values(lineindex)[60]
        Achiev_status=table.row_values(lineindex)[61]
        Achiev=[Achiev_value,Achiev_status]

        
        
        Eachline_KPI={"Name":Name,"AttainmenttoGoal_HSI":AttainmenttoGoal_HSI,"B2P":B2P,"AHT":AHT,"Hold":Hold,"AbsAbsenteeism":AbsAbsenteeism,
                  "AvgQAScore":AvgQAScore,"QACalls":QACalls,"ofAutoFails":ofAutoFails,"MixClose_HSI":MixClose_HSI,
                  "AttainmenttoGoal_HSI_1":AttainmenttoGoal_HSI_1,"MixClose_TV":MixClose_TV,"AttainmenttoGoal_TV":AttainmenttoGoal_TV,
                  "AttachRate_DTV":AttachRate_DTV,"MixClose_PhoneLines":MixClose_PhoneLines,"MixClose_Ease":MixClose_Ease,"ACDCalls":ACDCalls,
                  "AHTIneligible":AHTIneligible,"QualifiedCloseRate":QualifiedCloseRate,"Achiev":Achiev}
        
        for key in Eachline_KPI:
            if key!="Name":
                if key not in ["AHT","Hold","AvgQAScore","QACalls","ofAutoFails","ACDCalls","AHTIneligible"] and Eachline_KPI[key][0]!='N/A':
                    Eachline_KPI[key][0]=(Eachline_KPI[key][0])*100
        for key in Eachline_KPI:
            if key!="Name":
                Decimal_digits='0.00'
                Eachline_KPI[key][0]=str(KPIMethod.Change_Decimal_digits(Eachline_KPI[key][0],Decimal_digits))#If not str, the value of AHT will be Decimal('650.00')
    
        return Eachline_KPI
    
    

    def get_CENTURYLINK_Goal_Expected(self,lineindex): 
        #table=self.Get_sheet_Info(self.CENTURYLINK_Performance_Sheetiname)
        Getfile=Get_file()
        table=Getfile.Get_performance_sheet_Info(self.CENTURYLINK_Performance_Sheetiname)
        KPIMethod=KPI_method()
        AttainmenttoGoal_HSI=table.row_values(lineindex)[1]
        B2P=table.row_values(lineindex)[5]
        AHT=table.row_values(lineindex)[9]
        Hold=table.row_values(lineindex)[15]
        AbsAbsenteeism=table.row_values(lineindex)[18]
        AvgQAScore=table.row_values(lineindex)[22]
        QACalls=table.row_values(lineindex)[26]
        ofAutoFails=table.row_values(lineindex)[29]
        MixClose_HSI=table.row_values(lineindex)[32]
        AttainmenttoGoal_HSI_1=table.row_values(lineindex)[34]
        MixClose_TV=table.row_values(lineindex)[36]
        AttainmenttoGoal_TV=table.row_values(lineindex)[40]
        AttachRate_DTV=table.row_values(lineindex)[43]
        MixClose_PhoneLines=table.row_values(lineindex)[45]
        MixClose_Ease=table.row_values(lineindex)[48]
        ACDCalls=table.row_values(lineindex)[51]
        AHTIneligible=table.row_values(lineindex)[54]
        QualifiedCloseRate=table.row_values(lineindex)[58]
        Achiev='N/A'
        Goal_KPI={"AttainmenttoGoal_HSI":AttainmenttoGoal_HSI,"B2P":B2P,"AHT":AHT,"Hold":Hold,"AbsAbsenteeism":AbsAbsenteeism,
                  "AvgQAScore":AvgQAScore,"QACalls":QACalls,"ofAutoFails":ofAutoFails,"MixClose_HSI":MixClose_HSI,
                  "AttainmenttoGoal_HSI_1":AttainmenttoGoal_HSI_1,"MixClose_TV":MixClose_TV,"AttainmenttoGoal_TV":AttainmenttoGoal_TV,
                  "AttachRate_DTV":AttachRate_DTV,"MixClose_PhoneLines":MixClose_PhoneLines,"MixClose_Ease":MixClose_Ease,"ACDCalls":ACDCalls,
                  "AHTIneligible":AHTIneligible,"QualifiedCloseRate":QualifiedCloseRate,"Achiev":Achiev}
        for key in Goal_KPI:
            if Goal_KPI[key]!='N/A':
                Decimal_digits='0.00'
                Goal_KPI[key]=str(KPIMethod.Change_Decimal_digits(Goal_KPI[key],Decimal_digits))#If not str, the value of AHT will be Decimal('650.00')

        return Goal_KPI
    
            
    def Get_ManyAgentAchiev_Expected(self,start_lineindex,end_lineindex):
        Agent_Achiev_Dic={}
        for lineindex in range(start_lineindex,end_lineindex+1):
            AllKPI_OneAgent=self.get_CENTURYLINK_Performance_Data_Expected(lineindex)
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
            Expected_KPIofSITEDic=self.get_CENTURYLINK_Performance_Data_Expected(135)#For Step2
            Expected_KPIofTl1=self.get_CENTURYLINK_Performance_Data_Expected(134)#For Step3
            Expected_AgentAchiev=self.Get_ManyAgentAchiev_Expected(131, 133)#For Step4
            Expected_KPIofAgent8="N/A"#For Step5
            Expected_KPIofAgent11=self.get_CENTURYLINK_Performance_Data_Expected(133)#For Step6
            
        elif Timetab=="LastMonth":
            Expected_KPIofSITEDic=self.get_CENTURYLINK_Performance_Data_Expected(123)#For Step2
            Expected_KPIofTl1=self.get_CENTURYLINK_Performance_Data_Expected(117)#For Step3
            Expected_AgentAchiev=self.Get_ManyAgentAchiev_Expected(106, 116)#For Step4
            Expected_KPIofAgent8=self.get_CENTURYLINK_Performance_Data_Expected(113)#For Step5
            Expected_KPIofAgent11=self.get_CENTURYLINK_Performance_Data_Expected(116)#For Step6
        elif Timetab=="Yesterday":
            Expected_KPIofSITEDic=self.get_CENTURYLINK_Performance_Data_Expected(23)#For Step2
            Expected_KPIofTl1=self.get_CENTURYLINK_Performance_Data_Expected(16)#For Step3
            Expected_AgentAchiev=self.Get_ManyAgentAchiev_Expected(5, 15)#For Step4
            Expected_KPIofAgent8=self.get_CENTURYLINK_Performance_Data_Expected(12)#For Step5
            Expected_KPIofAgent11=self.get_CENTURYLINK_Performance_Data_Expected(15)#For Step6
            
        elif Timetab== "Week-to-Date":
            Expected_KPIofSITEDic=self.get_CENTURYLINK_Performance_Data_Expected(73)#For Step2
            Expected_KPIofTl1=self.get_CENTURYLINK_Performance_Data_Expected(67)#For Step3
            Expected_AgentAchiev=self.Get_ManyAgentAchiev_Expected(56, 66)#For Step4
            Expected_KPIofAgent8=self.get_CENTURYLINK_Performance_Data_Expected(63)#For Step5
            Expected_KPIofAgent11=self.get_CENTURYLINK_Performance_Data_Expected(66)#For Step6
        elif Timetab=="Month-to-Date":
            Expected_KPIofSITEDic=self.get_CENTURYLINK_Performance_Data_Expected(98)#For Step2
            Expected_KPIofTl1=self.get_CENTURYLINK_Performance_Data_Expected(92)#For Step3
            Expected_AgentAchiev=self.Get_ManyAgentAchiev_Expected(81, 91)#For Step4
            Expected_KPIofAgent8=self.get_CENTURYLINK_Performance_Data_Expected(88)#For Step5
            Expected_KPIofAgent11=self.get_CENTURYLINK_Performance_Data_Expected(91)#For Step6
        AllExpectedValue_Dic={"Expected_KPIofSITEDic":Expected_KPIofSITEDic,"Expected_KPIofTl1":Expected_KPIofTl1,
                              "Expected_AgentAchiev":Expected_AgentAchiev,"Expected_KPIofAgent8":Expected_KPIofAgent8,
                              "Expected_KPIofAgent11":Expected_KPIofAgent11}
        return AllExpectedValue_Dic
