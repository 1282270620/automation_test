'''
Created on Jun 7, 2018

@author: symbio
'''
from Tablet_pages import BasePage
from Tablet_pages.TabletHomepage import TabletHomepage
from Tablet_pages.LeadershipAcademyCoachingScoresPage import LeadershipAcademyCoachingScoresPage
from Tablet_pages.LeaderAcademyCoachingLeaderScorespage import LeaderAcademyCoachingLeaderScorespage
class Check_Tablet(BasePage.Action):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.NoLACSandLACLS_loblist=['AOL','paypal','CENTURYLINK','COMCAST NED BILLING','UBER TRANSPORT VOICE','CENTURYLINK RETENTION','EBAY']
    def Check_TabletHomepageCircle_ByRole(self,lobname,role):
        Tablet=TabletHomepage()
        AllModules_list=Tablet.get_AllTabletCircleName()
        OM_Modules_list=["Performance","Coaching","Triad Coaching","My Team Info","Coaching Export","Leadership Academy Coaching Scores","Leaders Academy Coaching Leader Scores","Satisfaction","Coach Due Reports","My Info","Redemption Report"]
        OM_Modules_list_NoLACS=["Performance","Coaching","Triad Coaching","My Team Info","Coaching Export","Satisfaction","Coach Due Reports","My Info","Redemption Report"]
        SVP_Modules_list=["Performance","Coaching","Triad Coaching","Coaching Export","Leadership Academy Coaching Scores","Leaders Academy Coaching Leader Scores","My Info"]
        SVP_Modules_list_NoLACS=["Performance","Coaching","Triad Coaching","Coaching Export","My Info"]
        L1_Modules_list=["Performance","Outlier","Coaching","Triad Coaching","My Team Info","Coaching Export","Leadership Academy Coaching Scores","Satisfaction","Coach Due Reports","My Info","Redemption Report"]
        L1_Modules_list_NoLACS=["Performance","Outlier","Coaching","Triad Coaching","My Team Info","Coaching Export","Satisfaction","Coach Due Reports","My Info","Redemption Report"]
        Agent_Modules_list=["Performance","My Achievement","Coaching","Leadership Academy Coaching Scores","My Info"]
        Agent_Modules_list_NoLACS=["Performance","My Achievement","Coaching","My Info"]
        LC_Modules_list=["Performance","Coaching","Triad Coaching","Coaching Export","Leadership Academy Coaching Scores","Leaders Academy Coaching Leader Scores","Satisfaction","Coach Due Reports","My Info","Redemption Report"]
        LC_Modules_list_NoLACS=["Performance","Coaching","Triad Coaching","Coaching Export","Satisfaction","Coach Due Reports","My Info","Redemption Report"]
        
        print AllModules_list
        if lobname not in self.NoLACSandLACLS_loblist:
            if role=="L3" or role=="L2":
                ExpectedModules_list=OM_Modules_list
            elif role=="LC":
                ExpectedModules_list=LC_Modules_list
            elif role=="SVP":
                ExpectedModules_list=SVP_Modules_list
            elif role=="L1":
                ExpectedModules_list=L1_Modules_list
            elif role=="Agent":
                ExpectedModules_list=Agent_Modules_list
                
        else:
            if role=="L3" or role=="L2":
                ExpectedModules_list=OM_Modules_list_NoLACS
            elif role=="LC":
                ExpectedModules_list=LC_Modules_list_NoLACS
            elif role=="SVP":
                ExpectedModules_list=SVP_Modules_list_NoLACS
            elif role=="L1":
                ExpectedModules_list=L1_Modules_list_NoLACS
            elif role=="Agent":
                ExpectedModules_list=Agent_Modules_list_NoLACS
                
                
        print ExpectedModules_list
        assert len(AllModules_list)==len(ExpectedModules_list)
        for key in range(0,len(AllModules_list)) :
            print AllModules_list[key],ExpectedModules_list[key]
            assert AllModules_list[key]==ExpectedModules_list[key]
    
    
    
    
    def Check_TabletHomepageCircle_OM(self,lobname):
        Tablet=TabletHomepage()
        AllModules_list=Tablet.get_AllTabletCircleName()
        list1=["Performance","Coaching","Triad Coaching","My Team Info","Coaching Export","Leadership Academy Coaching Scores","Leaders Academy Coaching Leader Scores","Satisfaction","Coach Due Reports","My Info","Redemption Report"]
        list2_NoLACS=["Performance","Coaching","Triad Coaching","My Team Info","Coaching Export","Satisfaction","Coach Due Reports","My Info","Redemption Report"]
        
        print AllModules_list
        if lobname not in self.NoLACSandLACLS_loblist:
            ExpectedModules_list=list1
        else:
            ExpectedModules_list=list2_NoLACS
        print ExpectedModules_list
        assert len(AllModules_list)==len(ExpectedModules_list)
        for key in range(0,len(AllModules_list)) :
            print AllModules_list[key],ExpectedModules_list[key]
            assert AllModules_list[key]==ExpectedModules_list[key]
        
    def Check_TabletHomepageCircle_TL(self,lobname):
        Tablet=TabletHomepage()
        #Check performance circle
        assert Tablet.get_performancename() == "Performance" #Verify performance displayed
        #Check outlier circle
        assert Tablet.get_TL_outliername() =='Outlier'  #Verify Coaching displayed
        #Check coaching circle
        assert Tablet.get_TL_coachingname() == "Coaching" #Verify Coaching displayed
        #Check triad coaching circle
        assert Tablet.get_TL_triadcoachingname()=="Triad Coaching" #Verify Triad Coaching displayed
        
        #Check My Team Info circle
        assert Tablet.get_TL_myteaminfoname()=="My Team Info" #Verify My Team Info displayed
        #Check Coaching Export
        assert  Tablet.get_CoachingExportname_TL()=="Coaching Export"
        #if lobname != "AOL":
        if lobname not in self.NoLACSandLACLS_loblist:
            #check Leadership Academy Coaching Scores
            print Tablet.get_LeadershipAcademyCoachingScoresname_TL_OMLeaderScoresname()
            assert Tablet.get_LeadershipAcademyCoachingScoresname_TL_OMLeaderScoresname()=='Leadership Academy Coaching Scores'
    def Check_MyTeamInfo_Header(self,Header_excel):
        Header_onpage=['Name','HR ID','Title','Points','Activated Date']
        assert Header_onpage==Header_excel
        

    def Check_TabletHomepageCircle_VPSVP(self,lobname):
        Tablet=TabletHomepage()
        #Check performance circle
        assert Tablet.get_performancename() == "Performance"#Verify performance displayed
        #Check coaching circle
        assert Tablet.get_coachingname() == "Coaching"#Verify Coaching displayed
        #Check triad coaching circle
        assert Tablet.get_triadcoachingname()=="Triad Coaching"#Verify Triad Coaching displayed
        #Check Coaching Export
        assert  Tablet.get_CoachingExportname_LCVPSVP()=="Coaching Export"
        if lobname not in self.NoLACSandLACLS_loblist:
            #check Leadership Academy Coaching Scores
            assert Tablet.get_TL_myteaminfoname()=='Leadership Academy Coaching Scores'
            assert Tablet.get_LeadershipAcademyCoachingScoresname_OM()=='Leaders Academy Coaching Leader Scores'    
        
    def Check_TabletHomepageCircle_Agent(self,lobname):    
        Tablet=TabletHomepage()
        #Check performance circle
        assert Tablet.get_performancename() == "Performance"#Verify performance displayed
        assert Tablet.get_MyAchievementname()=='My Achievement' #verify My achievement displayed
        assert Tablet.get_Agent_coachingname()=='Coaching' #verify Coaching displayed
        if lobname not in self.NoLACSandLACLS_loblist:
                #Leadership Academy Coaching Scores
                assert Tablet.get_myteaminfoname()=='Leadership Academy Coaching Scores'  


    ####Check LeaderShipAcademyCoachingScores###
    def Check_DefaultValuesOfQueryConditions_LeaderShipAcademyCoachingScores(self):
        LSACoachingScores=LeadershipAcademyCoachingScoresPage()
        CreatedDate_1=LSACoachingScores.get_datevalu(1,1,1)
        CreatedDate_2=LSACoachingScores.get_datevalu(1,1,2)
        CompletedDate_1=LSACoachingScores.get_datevalu(1,2,1)
        CompletedDate_2=LSACoachingScores.get_datevalu(1,2,1)
        AcknowledgeDate_1=LSACoachingScores.get_datevalu(2,1,1)
        AcknowledgeDate_2=LSACoachingScores.get_datevalu(2,1,2)
        Status_DefaultValue=LSACoachingScores.get_statusvalue()
        Status_DropDownList=LSACoachingScores.get_StatusDropDownList()
        assert CreatedDate_1==""
        assert CreatedDate_2==""
        assert CompletedDate_1==""
        assert CompletedDate_2==""
        assert AcknowledgeDate_1==""
        assert AcknowledgeDate_2==""
        assert Status_DefaultValue=="Acknowledged"
        assert Status_DropDownList==["Completed","Acknowledged","Completed and Acknowledged"]

        
    ####Check LeaderShipAcademyCoachingScores###
        
     #def CheckData_LeaderShipAcademyCoachingScores(self,DataLSACS_DataBase,DataLSACS_FromPage):
    def CheckData_DataBaseAndPage(self,Data_DataBase,Data_FromPage):  
        print len(Data_DataBase),len(Data_FromPage)
        assert len(Data_DataBase)==len(Data_FromPage)
        for i in range(0,len(Data_DataBase)):
            if Data_DataBase[i]==None or Data_DataBase[i]=='None':
                Data_DataBase[i]='N/A'
            index=Data_DataBase[i].find(".")
            if index!="":
                if len(Data_DataBase[i][index+1:])==1:
                    Data_DataBase[i]=str(Data_DataBase[i])+'0'
                    print Data_DataBase[i]
            print Data_DataBase[i],Data_FromPage[i]
            assert Data_DataBase[i]==Data_FromPage[i]        
            
       
    
    ####Check LeadersAcademyCoachingLeaderScores###    
    
    def Check_DefaltDateValue_LeadersAcademyCoachingLeaderScores(self):
        LACLS=LeaderAcademyCoachingLeaderScorespage()
        CreatedDate_Start=LACLS.get_datevalu(1, 1)
        CreatedDate_End=LACLS.get_datevalu(1, 2)
        Acknowledge_Start=LACLS.get_datevalu(2, 1)
        Acknowledge_End=LACLS.get_datevalu(2, 2)
        assert CreatedDate_Start==""
        assert CreatedDate_End==""
        assert Acknowledge_Start==""
        assert Acknowledge_End==""
        
        
    def Check_WarningMessageOfMoreThanSixMonth_LeadersAcademyCoachingLeaderScores(self,DateType,Actual_Message): #DateType:Created_Date or Acknowledge_Date 
        Expected_Message_created="The time span between start date and end date of Created Date should not be longer than 6 months."
        Expected_Message_acknowledge="The time span between start date and end date of Acknowledge Date should not be longer than 6 months."
        if DateType=="Created_Date":
            assert Actual_Message==Expected_Message_created
        elif DateType=="Acknowledge_Date":
            assert Actual_Message==Expected_Message_acknowledge
        
    def Check_WarningMessageOfNoStartDate_LeadersAcademyCoachingLeaderScores(self,DateType,Actual_Message): #DateType:Created_Date or Acknowledge_Date  
        Expected_Message_created="Please select start date of Created Date"
        Expected_Message_acknowledge="Please select start date of Acknowledge Date"
        if DateType=="Created_Date":
            assert Actual_Message==Expected_Message_created
        elif DateType=="Acknowledge_Date":
            assert Actual_Message==Expected_Message_acknowledge
        
    def Check_WarningMessageNoEndDate_LeadersAcademyCoachingLeaderScores(self,DateType,Actual_Message): #DateType:Created_Date or Acknowledge_Date  
        Expected_Message_created="Please select end date of Created Date"
        Expected_Message_acknowledge="Please select end date of Acknowledge Date"
        if DateType=="Created_Date":
            assert Actual_Message==Expected_Message_created
        elif DateType=="Acknowledge_Date":
            assert Actual_Message==Expected_Message_acknowledge
        
    def Check_DateDisabled_LeadersAcademyCoachingLeaderScores(self,Actual_classvalue):
        Expected_classvalue="day disabled"
        assert Actual_classvalue==Expected_classvalue
            
            

