'''
Created on Jun 14, 2017

@author: symbio
'''
import unittest
import time
from public_method import Gl
from public_method.Get_configration_data import Get_configration_data
from public_method.Coach_Triad_General import Coach_Triad_General
from Tablet_pages.PerformancPage import PerformancePage
from public_method.Login import Login
from Tablet_pages.TabletHomepage import TabletHomepage
from Tablet_pages.Coachinghomepage import Coachinghomepage
from CoachingAndTriadCoaching_Pages.BasicInfoforCoaching import BasicInfoforCoaching
import MySQLdb
from CoachingAndTriadCoaching_Pages.SalesWeeklyPerformanceReviewForm import SalesWeeklyPerformanceReviewForm
from public_method.Coaching_PublicFunction import Coaching_PublicFunction
from Tablet_pages.HeaderPage import HeaderPage
from public_method.Get_AllRoleAccountForTest import Get_AllRoleAccountForTest
from public_method.KPI_method import KPI_method
from public_method.HandleMySQL import HandleMySQL

class SalesWeeklyPerformanceReviewForm_PlanedToAcknowledged_TL(unittest.TestCase):


    def setUp(self):
        #Case ID
        self.caseID="SalesWeeklyPerformanceReviewForm_PlanedToAcknowledged_TL"
        
        GetData=Get_configration_data()
        #Get URL 
        self.tableturl=GetData.get_TabletUrl()
        #Get OM account
        OMaccount=GetData.get_OMaccount()
        self.OMuserid=OMaccount["OMuserid"]
        self.OMpassword=OMaccount["OMpassword"]
        #Get all lobs from CSV
        self.testLOBSITE_list=GetData.get_LOBSITEtoTest(self.caseID)
        #Database info
        self.host=GetData.get_StageDatabaseHost()
        self.hostindex=92
        self.dbuser=GetData.get_StageDatabaseUser()
        self.dbpassword=GetData.get_StageDatabasePassword()
        #Get coachpopuptittle
        self.title=GetData.get_AddCoachingFormTitle()
        
        #Get FormCommonParameter
        FormCommonParameter_Dic=GetData.get_FormCommonParameter()
        self.CallRecordingNumber1=FormCommonParameter_Dic["CallRecordingNumber1"]
        self.CallRecordingNumber2=FormCommonParameter_Dic["CallRecordingNumber2"]
        self.Shorttextboxesprefix1=FormCommonParameter_Dic["Shorttextboxesprefix1"]
        self.Shorttextboxesprefix2=FormCommonParameter_Dic["Shorttextboxesprefix2"]
        self.Longtextboxesprefix1=FormCommonParameter_Dic["Longtextboxesprefix1"]
        self.Longtextboxesprefix2=FormCommonParameter_Dic["Longtextboxesprefix2"]
        
        #coaching or Triad coaching
        self.coachtype="coaching"  
        #Coachformname
        self.coachformname="Sales Weekly Performance Review Form" 
        self.coachpagetitle="Coaching - "+self.coachformname
        #KPI box title in coaching detail page
        self.KPIbox_title="Coaching KPIs(Month-To-Date):"
        
        
        
        #CheckBox Status
        self.CheckBox_CheckedStatus="fa fa-check-square"
        self.CheckBox_UnCheckedStatus="fa fa-uncheck"
        #User's role
        self.UserRole="TL"
        
      


    def tearDown(self):
        #Gl.driver.quit()
        pass


    def test_SalesWeeklyPerformanceReviewForm_PlanedToAcknowledged_TL(self):
        GetConfig=Get_configration_data()
        Tablet=TabletHomepage()
        Ppage=PerformancePage()
        TCoach=Coach_Triad_General()
        CoachHome=Coachinghomepage()
        BasicInfo=BasicInfoforCoaching()
        CoachPublic=Coaching_PublicFunction()
        Header=HeaderPage()
        SalesWPRF=SalesWeeklyPerformanceReviewForm()
        Getaccount=Get_AllRoleAccountForTest()
        KPIMethod=KPI_method()
        HMysql=HandleMySQL()
        #Commendation=Commendation()
        for i in range(0,len(self.testLOBSITE_list)):
            Flag=GetConfig.get_LOBSITE_STATUS(self.testLOBSITE_list[i])
            if Flag==True:
                each_LOBSITE=self.testLOBSITE_list[i].split(":")
                lobname=each_LOBSITE[0]
                #Get Site to test
                site_list=each_LOBSITE[1].split("*")
                for n in range(0,len(site_list)):
                    sitename=site_list[n]
                    GetConfig.print_StartTest_message(lobname, sitename)
                    
                        #Get coach information from database
                    
                    #Step1:Login tablet,and Get AgentInfo using for testing
                    TLInfo=Getaccount.get_TLInfoandAgentHridFromPerformance(self.tableturl, lobname, sitename, self.OMuserid, self.OMpassword,"Month-To-Date")
                    TLHrid=TLInfo["TLHrid"]
                    TLPassword=TLInfo["TLPassword"]
                    
                    AgentInfo_Dic=Getaccount.get_AgentInfoFromTablet(self.tableturl, lobname, sitename, self.OMuserid, self.OMpassword,"Month-To-Date")
                    Agent_name=AgentInfo_Dic["AgentName"]
                    Agent_hrid=AgentInfo_Dic["AgentHrid"]
                    Agent_password=AgentInfo_Dic["AgentPassword"]
                    
                    Agent_Sign_Date_list=[]
                    TL_Sign_Date_list=[]
                    L=Login()
                    L.Login_tablet(self.tableturl,lobname,sitename,TLHrid,TLPassword)
                    time.sleep(Gl.waittime)
                    #Step2:Enter performance
                    Tablet.click_performancecircle()
                   
                    #Step3:Select one Agent to add coaching to follow Planed to Acknowledged
                    print "Start=====Monthly-To-Day is in testing",
                    #Ppage.select_Agentkpi()#select the first Agent's kpi of the first TL
                    #Ppage.select_AgentofTLkpi()
                    #Ppage.unselect_AgentofTLkpi()
                    #Ppage.select_Agentkpi()
                    #Ppage.unselect_Agentkpi()
                    #KPInumber=Ppage.get_KPInumber()
                    if lobname in Gl.DoubleKPIname_lob:
                        KPInumber=Ppage.get_KPInumber_All()
                        KPIname_FromPerformancePage_list=Ppage.get_KPIname_list_Double()
                        
                    else:
                        KPInumber=Ppage.get_KPInumber()
                        KPIname_FromPerformancePage_list=Ppage.get_KPIname_list(KPInumber)
                        
                    for i in range(0,len(KPIname_FromPerformancePage_list)):
                        if len(KPIname_FromPerformancePage_list[i])>12:
                            if KPIname_FromPerformancePage_list[i][-12]=="(" and KPIname_FromPerformancePage_list[i][-1]==")":
                                KPIname_FromPerformancePage_list[i]=KPIname_FromPerformancePage_list[i].replace(KPIname_FromPerformancePage_list[i][-13:],"")    
                    
                    KPIofGoal_FromPerformancePage_list=Ppage.get_AllKPIsofGoal_list(KPInumber)
                    KPIofSite_FromPerformancePage_list=Ppage.get_AllKPIsofSite_list(KPInumber)
                    KPIofTeam_FromPerformancePage_list=Ppage.get_AllKPIsofTeam_list(KPInumber)
                    KPIofAgent_FromPerformancePage_list=Ppage.get_AllKPIsofAgent_TL_list(KPInumber, 1)
                    #KPIofAgentOrTL_FromPerformancePage_list=Ppage.get_AllKPIsofAgentForOM_list(KPInumber)
                    if lobname in Gl.performancefor_MultiTimeTab_lob:
                        Ppage.click_timetab_performance(5)#Ppage.click_mtd()
                    else:    
                        Ppage.click_timetab_performance(3)#Ppage.click_mtd()
                    #Ppage.select_AnyKpiOfAgent_OM(4)#Select three KPI
                    Ppage.select_AnyKpiOfAgent_TL(4,4)#Select three KPI
                    
                    
                    #Step3.1:1.Login with an OM/TL1/LC account;
                            #2.Enter performance module->Select an AGENT->select first three KPs to add this  form 
                            #3.Enter Coaching list page.
                            #4. Click the  form in coaching list.
                    #Get KPI for Goal,Site,and Agent of the first one of the first TL
                    
                    
                    Ppage.click_addcoachbutton()
                    TCoach.Add_AnyCoachOrTriad(self.coachformname)
                    
                    
                    '''
                    message=Ppage.get_messageOfaddCoachOrtriad()
                    
                    '''
                    Ppage.click_backbutton()
                    Tablet.click_TL_coachingcircle()
                     
                    #The following:Get basic info of coaching from the first one of coaching home page
                    #Anyinfo_Firstcoaching_path="//*[@id='container']/div/section/div/div[2]/table/tbody/tr[1]/td[%d]"
                    #SN_path=Anyinfo_Firstcoaching_path % 1
                    #typename_path=Anyinfo_Firstcoaching_path % 5
                    #createdtime_path=Anyinfo_Firstcoaching_path % 7
                    SN_coachhomepage=CoachHome.get_anyCoach_attribute(1, 1)
                    #SN_coachhomepage=CoachHome.get_eachtextOfanycoachline(SN_path)
                    typename_Actual=CoachHome.get_anyCoach_attribute(1, 5)#Coaching form name
                    createdtime_Actual=CoachHome.get_anyCoach_attribute(1, 7)
                    Created_Date_FromServer=GetConfig.get_ServerCurrentDate().replace("-","/")
                    
                    '''Check1:1.After added, shown message 'Coaching Added' at page bottom.
                              2.The newly added record should be automatically shown in search result list page.'''
                    
                    #print message
                    #assert message=="Coaching Added"
                    assert self.coachformname==typename_Actual
                    assert Created_Date_FromServer==createdtime_Actual
                    
                    #Step3.2:Enter to the detail page and Get all basic info of coaching from coaching detail page
                    #CoachHome.click_eachcoach(typename_path)
                    CoachHome.click_eachcoach(1)
                    SN_Actual=BasicInfo.get_SN()
                    employee_name_Actual=BasicInfo.get_employeename()
                    employee_hrid_Actual=BasicInfo.get_employeeHrid()
                    coach_name_Actual=BasicInfo.get_coachname()
                    created_time_Actual=BasicInfo.get_createdate()
                    status_Actual=BasicInfo.get_status()
                    completed_time_Actual=BasicInfo.get_completeddate()
                    acknowledge_time_Actual=BasicInfo.get_acknowledgedDate()
                    call_recording_number_Actual=BasicInfo.get_callrecordingnumber()
                    '''Check2:1.Page title :'Coaching - Sales Weekly Performance Review Meeting'.
                              2.Shown logged-in User info as below: 1)Antonette Corpus (OM/TL);2)BLUE, HPI-PHIL-01'''
                    assert Header.get_HeaderTittle()==self.coachpagetitle
                    assert Header.get_loginLob()==lobname
                    assert Header.get_loginSite()==sitename
                    assert Header.get_loginName()==coach_name_Actual
                    assert Header.get_loginRole()==self.UserRole
                    
                    #Step3.3:Get Basic information section from database:[SN, Employee Name,Employee ID, Status, Coaching Name, Call Recording Number,Create Date, Completed Date, Acknowledged Date]
                    sql_employeename_all="select c.created_time,c.completed_time,c.cancel_time,c.acknowledge_time,c.call_recording_number,c.status, a.firstname,a.lastname,c.hr_id from coach c join account a on c.hr_id=a.hr_id where c.sn="+"'"+SN_coachhomepage+"'"+";"
                    sql_coachname="select a.firstname,a.lastname from coach c join account a on c.assign_to_id=a.hr_id where sn="+"'"+SN_coachhomepage+"'"+";"
                    
                    #database_name=lobname.lower()+'_'+sitename.lower().replace("-","").replace(" ","")    
                    #conn=MySQLdb.connect(self.host,self.dbuser,self.dbpassword,database_name)
                    #cursor=conn.cursor()
                    #conn.autocommit(True)
                    #cursor.execute(sql_employeename_all)#Get all info of Coaching except coach_name
                    Datalist1=HMysql.Get_datafromDB(self.hostindex, lobname, sitename, self.dbuser, self.dbpassword, sql_employeename_all)
                    DataFromDB_content1=Datalist1[1]
                    for row in DataFromDB_content1:
                    #for row in cursor:
                        created_time_database=str(row[0])[0:10].replace("-","/")
                        completed_time_database=str(row[1])[0:10].replace("-","/")
                        cancel_time_database=str(row[2])[0:10].replace("-","/")
                        acknowledge_time_database=str(row[3])[0:10].replace("-","/")
                        call_recording_number_database=row[4]
                        status_database=row[5]
                        employee_name_database=row[6]+" "+row[7]
                        employee_hrid_database=row[8]
                    #cursor.execute(sql_coachname)#Get coach name
                    Datalist2=HMysql.Get_datafromDB(self.hostindex, lobname, sitename, self.dbuser, self.dbpassword, sql_coachname)
                    DataFromDB_content2=Datalist2[1]
                    for row in DataFromDB_content2:
                    #for row in cursor:
                        coach_name_database=row[0]+" "+row[1]   
                    if status_database==0:
                        status_database='Planned'
                    else:
                        print "status_database=",
                        print status_database    
                    if completed_time_database=="None":
                        completed_time_database=""
                    if cancel_time_database=="None":
                        cancel_time_database=""
                    if acknowledge_time_database=="None":
                        acknowledge_time_database=""
                    if call_recording_number_database==None:
                        call_recording_number_database=""
                    '''Check3:1.The data of SN, Employee Name,EmployeeID, Coaching Name, Create Date are correct;
                              2.Status is "Planned";
                              3.Completed Date and Acknowledged Date are blank
                              4.CallRecordingNumber is blank.'''
                    assert SN_Actual==SN_coachhomepage                    
                    assert employee_name_Actual==employee_name_database==Agent_name
                    assert coach_name_Actual==coach_name_database
                    assert created_time_Actual==created_time_database==Created_Date_FromServer
                    assert status_Actual==status_database=="Planned"
                    assert completed_time_Actual==completed_time_database==""
                    assert acknowledge_time_Actual==acknowledge_time_database==""
                    assert call_recording_number_Actual==call_recording_number_database==""
                    assert employee_hrid_Actual==employee_hrid_database
                    
                    #Step3.4:Get and Check Coaching KPIs (Month to Date) section:[Coaching forms added at Performance page with Month-to-Date table selected]
                    
                    if lobname in Gl.DoubleKPIname_lob:
                        KPInumber=BasicInfo.get_KPInumber_All()
                        KPIname_FromDetailPage_list=BasicInfo.get_KPIname_list_Double()
                    else:
                        KPInumber=BasicInfo.get_KPInumber()
                        KPIname_FromDetailPage_list=BasicInfo.get_KPIname_list( KPInumber)
                    
                    KPIofGoal_FromDetailPage_list=BasicInfo.get_KPIofGoal_list(KPInumber)
                    KPIofSite_FromDetailPage_list=BasicInfo.get_KPIofSite_list(KPInumber)
                    KPIofTeam_FromDetailPage_list=BasicInfo.get_KPIofTeam_list(KPInumber)
                    KPIofAgent_FromDetailPage_list=BasicInfo.get_KPIofAgentOfTL_list(KPInumber)
                    CheckBoxStatus_FromDetailPage_list=BasicInfo.get_CheckBoxStatus_Agent_list(KPInumber)
                    KPIboxTitle=BasicInfo.get_KPIboxTitle()
                    '''Check4: 1.Show header name 'Coaching KPIs(Month-To-Date)';
                               2.All KPI data of Goal, Site,Team,Agent should be the same as those on the corresponding performance page;
                               3.The first three KPIs are checked by default.'''
                    assert KPIboxTitle=="Coaching KPIs(Month-To-Date):"
                    assert KPIname_FromPerformancePage_list==KPIname_FromDetailPage_list
                    
                    
                    if lobname in Gl.DoubleKPIname_lob:
                            Goal_index_Dic=KPIMethod.get_IndexOfTwovalue_list(KPIofGoal_FromPerformancePage_list)
                            Goal_SingleValue_index_list=Goal_index_Dic["SingleValue_index_list"]
                            Goal_TwoValue_index_list=Goal_index_Dic["TwoValue_index_list"]
                            for a1 in range(0,len(Goal_SingleValue_index_list)):
                                i=Goal_SingleValue_index_list[a1]
                                assert KPIofGoal_FromPerformancePage_list[i]==KPIofGoal_FromDetailPage_list[i]
                            for a2 in range(0,len(Goal_TwoValue_index_list)):
                                i=Goal_TwoValue_index_list[a2]
                                assert (KPIofGoal_FromPerformancePage_list[i].split("\n"))[1]==(KPIofGoal_FromDetailPage_list[i].split("\n"))[0]==(KPIofGoal_FromDetailPage_list[i].split("\n"))[1]
                    else:
                            assert KPIofGoal_FromPerformancePage_list==KPIofGoal_FromDetailPage_list
                    assert KPIofSite_FromPerformancePage_list==KPIofSite_FromDetailPage_list
                    assert KPIofTeam_FromPerformancePage_list==KPIofTeam_FromDetailPage_list
                    assert KPIofAgent_FromPerformancePage_list==KPIofAgent_FromDetailPage_list
                    assert CheckBoxStatus_FromDetailPage_list[0]==self.CheckBox_CheckedStatus
                    assert CheckBoxStatus_FromDetailPage_list[1]==self.CheckBox_CheckedStatus
                    assert CheckBoxStatus_FromDetailPage_list[2]==self.CheckBox_CheckedStatus
                    
                    #Step3.5: 1. All content should be shown the same as UI design.
                                    #'Week1' section: is editable.
                                    #'WEEK ENDING 1' section: 
                                            #is editable
                                            #Two buttons 'Save','TL Sign'  
                            #2.Following sectinos are uneditable:
                                    #WEEK2-WEEK5, MONTHLY PERFORMANCE RESULTS.
                                    #WEEK ENDING2- WEEK ENDING 5
                                    #Under each section of WEEK ENDING2- WEEK ENDING 5:
                                            #Show two buttons 'Save', 'TL Sign' , but disabled.    
                            #3.Check other sections: other buttons
                    '''Check5.1:1)Week1' section: is editable.
                                2)'WEEK ENDING 1' section: is editable.'''
                    for nameindex in range(11,14):
                        assert SalesWPRF.anyOtherMETRICname_disabled(nameindex)!="true"
                    for METRICindex in range(1,14):
                        assert SalesWPRF.anyMETRICOfanyWeekOrmonthly_disabled(METRICindex, 2)!="true"
                    for QuestionNumber in range(1,6):
                        assert SalesWPRF.AnyQuestionsOfAnyWeekEnding_disabled(QuestionNumber, 1)!="true"
                    assert SalesWPRF.anyButtonOfAnyWeekEnding_disabled(1, 1)!="true"
                    assert SalesWPRF.anyButtonOfAnyWeekEnding_disabled(1, 2)!="true"
                    
                    '''Check5.2:1)WEEK2-WEEK5, MONTHLY PERFORMANCE RESULTS can not be editable
                                2)Questions of WEEK ENDING2- WEEK ENDING 5 can not be editable, and Show two buttons 'Save', 'TL Sign' , but disabled'''
                    for METRICindex in range(1,14):
                        assert SalesWPRF.anyMETRICOfanyWeekOrmonthly_disabled(METRICindex, 3)=="true"
                        assert SalesWPRF.anyMETRICOfanyWeekOrmonthly_disabled(METRICindex, 4)=="true"
                        assert SalesWPRF.anyMETRICOfanyWeekOrmonthly_disabled(METRICindex, 5)=="true"
                        assert SalesWPRF.anyMETRICOfanyWeekOrmonthly_disabled(METRICindex, 6)=="true"
                        assert SalesWPRF.anyMETRICOfanyWeekOrmonthly_disabled(METRICindex, 7)=="true"
                    for QuestionNumber in range(1,6):
                        assert SalesWPRF.AnyQuestionsOfAnyWeekEnding_disabled(QuestionNumber, 2)=="true"
                        assert SalesWPRF.AnyQuestionsOfAnyWeekEnding_disabled(QuestionNumber, 3)=="true"
                        assert SalesWPRF.AnyQuestionsOfAnyWeekEnding_disabled(QuestionNumber, 4)=="true"
                        assert SalesWPRF.AnyQuestionsOfAnyWeekEnding_disabled(QuestionNumber, 5)=="true"
                        
                    for WeekEndingIndex in range(2,6):
                        assert SalesWPRF.anyButtonOfAnyWeekEnding_disabled(WeekEndingIndex, 1)=="true"
                        assert SalesWPRF.anyButtonOfAnyWeekEnding_disabled(WeekEndingIndex, 2)=="true"
                    
                    '''Check5.3:Check all buttons are displayed'''
                    assert BasicInfo.get_ButtonName(1)=="Print"
                    assert BasicInfo.get_ButtonName(2)=="Save and Continue Later"
                    assert BasicInfo.get_ButtonName(3)=="Complete Coaching"
                    assert BasicInfo.Button_disabled(3)=="true"
                    assert BasicInfo.get_ButtonName(4)=="Cancel Coaching"
                    assert BasicInfo.get_ButtonName(5)=="Quit Without Save"
                    
                    #Step3.6:1.Click 'Quit without Save'
                            #2.Get all coaching number & status
                    BasicInfo.Click_Button(5)#Click Quit without Save button
                    assign_to_id=TLHrid
                    total_PageandCoachnumber_tablet_Dic6=CoachPublic.get_Total_PageandCoachnumber()
                    Total_coachnumber_tablet6=total_PageandCoachnumber_tablet_Dic6['Total_coachnumber_tablet']
                    Status_Coach=CoachHome.get_anyCoach_attribute(1, 6)
                    sql_coach="select * from coach  where  assign_to_id="+assign_to_id+"  and classification=0 and status in (0,3) order by id desc"
                    Datalist6=HMysql.Get_datafromDB(self.hostindex, lobname, sitename, self.dbuser, self.dbpassword, sql_coach)
                    Total_coachnumber_database6=Datalist6[0]
                    
                    #Total_coachnumber_database6=cursor.execute(sql_coach)
                    '''Check6:Return to Coaching list page,On search fields section,show:
                              1.CoachingName=TL(logged-in)
                              2.EmployeeName=All
                              3.Status=Incompleted.
                              4.Type=All
                              5.All incompleted coaching records of logged-in user is listed.
                              6.This coach record is shown by default  with  status 'Planned'.'''
                    assert CoachHome.get_CoachName()==Header.get_loginName()
                    assert CoachHome.get_EmployeeName()=="All"
                    assert CoachHome.get_typename_selected()=="All"
                    assert CoachHome.get_status_selected()=="Incompleted"
                    print "Total_coachnumber_tablet6==Total_coachnumber_database6:",Total_coachnumber_tablet6,Total_coachnumber_database6
                    assert Total_coachnumber_tablet6==Total_coachnumber_database6#Check total number of coachings in tablet is the same with it in database
                    assert Status_Coach=="Planned"
                        
                    #Step3.7:Select this record to enter the  form again. 
                    #CoachHome.click_eachcoach(typename_path)
                    CoachHome.click_eachcoach(1)
                    '''Check7:Enter the  form detail page with title 'Coaching - Sales Weekly Performance Review Form'''
                    assert Header.get_HeaderTittle()==self.coachpagetitle 
                    
                    #Step3.8:Input content in following editable fields:
                            #1.Uncheck the third KPI;
                            #2.Check the fouth KPI.;
                    BasicInfo.click_anyKPIstatusofCheckBox_Agent(4)
                    BasicInfo.click_anyKPIstatusofCheckBox_Agent(5)
                    '''Check8:1.The third KPI is in unchecked status.
                              2.The fourth KPI is in checked status.'''
                    assert BasicInfo.get_anyCheckBoxStatus_Agent(4)==self.CheckBox_UnCheckedStatus
                    assert BasicInfo.get_anyCheckBoxStatus_Agent(5)==self.CheckBox_CheckedStatus
                    
                    #Step3.9:1. input call Recording Number
                            #2.Week1 section:(same in triad coching value input)
                                                            #Week1
                            #CR                            keep empty      
                            #%CC                           N/A
                            #NFCR                          2000.09
                            #.COM                          300
                            #VOC                           0
                            #PP                            99.99%
                            #FCR                           99.99%
                            #ATT3                          99.99%
                            #BAR                           99.99%
                            #MOB Units                     100.00%
                            #3.input Week ENDING1 section:
                            #Firstly input content in test boxes to test-WEEK ENDING1 section.
                    
                    
                    call_Recording_Number=self.CallRecordingNumber1
                    if lobname != "AOL":
                        BasicInfo.input_callrecordingnumber(call_Recording_Number)
                        
                    text_list1=["","N/A","2000.09","300","0","99.99%","99.99%","99.99%","99.99%","100.00%"]
                    for i in range(0,len(text_list1)):
                        METRICindex=i+1
                        SalesWPRF.input_anyMETRICOfanyWeekOrmonthly(METRICindex, 2, text_list1[i]) 
                    
                    for QuestionNumber in range(1,6):
                        question_title=SalesWPRF.get_AnyQuestionsOfAnyWeekEnding_title(QuestionNumber, 1) 
                        text=self.Longtextboxesprefix1+question_title
                        SalesWPRF.input_AnyQuestionsOfAnyWeekEnding(QuestionNumber, 1, text)
                    #Step3.10:Click TL Sign button;
                    SalesWPRF.click_SaveOrSignButtonOfAnyWeekEnding(1, 2)
                    TL_Sign_Date_1=GetConfig.get_ServerCurrentDate().replace("-","/")
                    TL_Sign_Date_list.append(TL_Sign_Date_1)
                    
                    '''Check10:1. 1) Shown message:Team leader signed.
                                 2)  Status is changed to Ongoing
                                 3) Under section 'WEEK ENDING 1' :
                                    --Buttons: Save and TL Sign disappeared.
                                    ---Button 'Agent Sign' shown with disabled status.
                                    -- "TL Signed Date: yyyy/mm/dd" showing on left side.
                                 4)  WEEK 2 section and WEEK ENDING 2 section become editable;
                                 5). Following sectinos are uneditable:
                                     --WEEK1,WEEK3-WEEK5, MONTHLY PERFORMANCE RESULTS.
                                     -- WEEK ENDING1,WEEK ENDING3- WEEK ENDING 5
                                     -- Under each section of WEEK ENDING3- WEEK ENDING 5:
                                            Show two buttons 'Save', 'TL Sign' , but disabled.'''
                    assert SalesWPRF.Get_AnyQuestion_RoleSign_text(1,1)=="TL Signed Date:"
                    assert SalesWPRF.Get_AnyQuestion_RoleSign_date(1,1)==TL_Sign_Date_1
                    assert BasicInfo.get_status()=="Ongoing"
                    print "SalesWPRF.Get_SaveOrSignButtonOfAnyWeekEnding_text(1, 1):",SalesWPRF.Get_SaveOrSignButtonOfAnyWeekEnding_text(1, 1)
                    print "SalesWPRF.Get_SaveOrSignButtonOfAnyWeekEnding_text(1, 2):",SalesWPRF.Get_SaveOrSignButtonOfAnyWeekEnding_text(1, 1)
                    assert SalesWPRF.Get_SaveOrSignButtonOfAnyWeekEnding_text(1, 1)=="Agent Sign"#Button is not Save button
                    assert SalesWPRF.anyButtonOfAnyWeekEnding_disabled(1, 1)=="true"
                    assert SalesWPRF.SaveOrSignButtonOfAnyWeekEnding_exist(1, 2)==False#TL Sign disappear
                    
                    for METRICindex in range(1,14):
                        assert SalesWPRF.anyMETRICOfanyWeekOrmonthly_disabled(METRICindex, 3)!="true"
                        assert SalesWPRF.anyMETRICOfanyWeekOrmonthly_disabled(METRICindex, 4)=="true"
                        assert SalesWPRF.anyMETRICOfanyWeekOrmonthly_disabled(METRICindex, 5)=="true"
                        assert SalesWPRF.anyMETRICOfanyWeekOrmonthly_disabled(METRICindex, 6)=="true"
                        assert SalesWPRF.anyMETRICOfanyWeekOrmonthly_disabled(METRICindex, 7)=="true"
                    for QuestionNumber in range(1,6):
                        assert SalesWPRF.AnyQuestionsOfAnyWeekEnding_disabled(QuestionNumber, 2)!="true"
                        assert SalesWPRF.AnyQuestionsOfAnyWeekEnding_disabled(QuestionNumber, 3)=="true"
                        assert SalesWPRF.AnyQuestionsOfAnyWeekEnding_disabled(QuestionNumber, 4)=="true"
                        assert SalesWPRF.AnyQuestionsOfAnyWeekEnding_disabled(QuestionNumber, 5)=="true"
                        
                    for WeekEndingIndex in range(3,6):
                        assert SalesWPRF.anyButtonOfAnyWeekEnding_disabled(WeekEndingIndex, 1)=="true"
                        assert SalesWPRF.anyButtonOfAnyWeekEnding_disabled(WeekEndingIndex, 2)=="true"
                    
                    #Step11:a.Click "Save and Continue Later";
                            #b Open this record SWPR form again.
                    
                    BasicInfo.Click_Button(2)
                    '''Check11: 1)Return to Coaching list page with status of the form is 'Ongoing' 
                                2)Following KPIs in checked status: 
                                   the first two KPIs, the fourth KPIs
                                   Other KPI shown unchecked status.
                                3)All my inputted info  are saved,including WEEK1 and WEEK ENDING1.
                                4)At page bottom, button 'Complete coaching' is still disabled'''
                    assert CoachHome.get_anyCoach_attribute(1, 6)=="Ongoing"
                    CoachHome.click_eachcoach(1)
                    assert CheckBoxStatus_FromDetailPage_list[0]==self.CheckBox_CheckedStatus
                    assert CheckBoxStatus_FromDetailPage_list[1]==self.CheckBox_CheckedStatus
                    assert CheckBoxStatus_FromDetailPage_list[2]==self.CheckBox_CheckedStatus
                    assert BasicInfo.get_anyCheckBoxStatus_Agent(4)==self.CheckBox_UnCheckedStatus
                    assert BasicInfo.get_anyCheckBoxStatus_Agent(5)==self.CheckBox_CheckedStatus
                    for index in range(6,KPInumber+1):
                        assert BasicInfo.get_anyCheckBoxStatus_Agent(index)==self.CheckBox_UnCheckedStatus
                        
                
                    for i in range(1,len(text_list1)):
                        METRICindex=i+1
                        assert SalesWPRF.Get_anyMETRICOfanyWeekOrmonthly(METRICindex, 2)==text_list1[i]  
                        
                    for QuestionNumber in range(1,6):
                        question_title=SalesWPRF.get_AnyQuestionsOfAnyWeekEnding_title(QuestionNumber, 1) 
                        text=self.Longtextboxesprefix1+question_title
                        assert SalesWPRF.get_AnyQuestionsOfAnyWeekEnding_text(QuestionNumber, 1)==text
                          
                    assert BasicInfo.get_ButtonName(3)=="Complete Coaching"
                    assert BasicInfo.Button_disabled(3)=="true"
                    
                    #Step12:a.Logout->login with the Agent.
                            #b.Enter coaching module.
                            #c.Directly select this record to enter form detail page.
                            #d.Click button 'Agent Sign'
                            
                    L.logout_tablet()
                    L.Login_tablet(self.tableturl, lobname, sitename, Agent_hrid, Agent_password)
                    Tablet.click_Agent_coachingcircle()
                    CoachHome.click_eachcoach(1)
                    coach_title=Header.get_HeaderTittle()
                    #SalesWPRF.click_SaveOrSignButtonOfAnyWeekEnding(1, 1)#Click button 'Agent Sign'
                    
                    '''Check12.1: 1)Enter this form detail page with title 'Coaching - Sales Weekly Performance Review Form'
                                2) Under section  'WEEK ENDING1' :
                                     --show button 'Agent Sign'
                                     --'TL Signed Date: yyyy/mm/dd' shown on left side.                                
                                3) Under other 'WEEK ENDING' sections:
                                    shown buttons 'save','TL Sign',but disabled.
                                4) At page bottom, only shown one button:BACK.'''
                    assert coach_title==self.coachpagetitle
                    print "SalesWPRF.Get_SaveOrSignButtonOfAnyWeekEnding_text(1, 1):",SalesWPRF.Get_SaveOrSignButtonOfAnyWeekEnding_text(1, 1)
                    print "SalesWPRF.Get_SaveOrSignButtonOfAnyWeekEnding_text(1, 2):",SalesWPRF.Get_SaveOrSignButtonOfAnyWeekEnding_text(1, 1)
                    assert SalesWPRF.Get_SaveOrSignButtonOfAnyWeekEnding_text(1, 1)=="Agent Sign"
                    assert SalesWPRF.Get_AnyQuestion_RoleSign_text(1,1)=="TL Signed Date:"
                    assert SalesWPRF.Get_AnyQuestion_RoleSign_date(1,1)==TL_Sign_Date_1
                    for WeekEndingIndex in range(2,6):
                        assert SalesWPRF.Get_SaveOrSignButtonOfAnyWeekEnding_text(WeekEndingIndex, 1)=="Save"
                        assert SalesWPRF.anyButtonOfAnyWeekEnding_disabled(WeekEndingIndex, 1)=="true"
                        assert SalesWPRF.Get_SaveOrSignButtonOfAnyWeekEnding_text(WeekEndingIndex, 2)=="TL Sign"
                        assert SalesWPRF.anyButtonOfAnyWeekEnding_disabled(WeekEndingIndex, 2)=="true"
                        
                    assert BasicInfo.get_ButtonName(1)=="Back"
                    assert BasicInfo.Button_Displayed(2)==False
                    
                    SalesWPRF.click_SaveOrSignButtonOfAnyWeekEnding(1, 1)#d.Click button 'Agent Sign'
                    Agent_Sign_Date_1=GetConfig.get_ServerCurrentDate().replace("-","/")
                    Agent_Sign_Date_list.append(Agent_Sign_Date_1)
                    '''Check12.2:1)  Shown message at page bottom:Agent Signed(No script)
                                 2) 'Agent Sign' button dissapears,and "Agent Signed Date: yyyy/mm/dd" showing at the corresponding right side.'''
                    assert SalesWPRF.Get_AnyQuestion_RoleSign_text(1, 2)=="Agent Signed Date:"
                    assert SalesWPRF.Get_AnyQuestion_RoleSign_date(1, 2)==Agent_Sign_Date_1
                    
                    #Step13:a.logout,login with creater TL.
                            #b.Enter coaching module->directly select this record to enter form detail page.
                            #c. Under WEEK ENDING2 section:
                                #1)  Directly click 'TL Sign' button.
                                #2) Click 'Save' button.
                    L.logout_tablet()
                    
                    L.Login_tablet(self.tableturl, lobname, sitename,TLHrid,TLPassword)
                    Tablet.click_TL_coachingcircle()
                    CoachHome.click_eachcoach(1)
                    SalesWPRF.click_SaveOrSignButtonOfAnyWeekEnding(2, 2)#click TL Sign
                    #alert_message=BasicInfo.get_AlertMessage()
                    time.sleep(5*Gl.waittime)
                    SalesWPRF.click_SaveOrSignButtonOfAnyWeekEnding(2, 1)#Click Save
                    #time.sleep(Gl.waittime)
                    #save_message=BasicInfo.get_AlertMessage()
                    
                    
                    '''Check13:b.Under section 'WEEK EDNING1':
                                "TL Signed Date:  yyyy/mm/dd" showing at the correspondg left side.
                                "Agent Signed Date: yyyy/mm/dd" showing at the corresponding right side.
                               c.1) Cannot sign;
                                    Pop up a message: Please add some comments to 1-5.
                                 2) Pop up a message: Coaching Saved
                                    Stay at current page;
                                    Status: Ongoing'''
                    assert SalesWPRF.Get_AnyQuestion_RoleSign_text(1, 1)=="TL Signed Date:"
                    assert SalesWPRF.Get_AnyQuestion_RoleSign_date(1, 1)==TL_Sign_Date_1
                    assert SalesWPRF.Get_AnyQuestion_RoleSign_text(1, 2)=="Agent Signed Date:"
                    assert SalesWPRF.Get_AnyQuestion_RoleSign_date(1, 2)==Agent_Sign_Date_1
                    #assert alert_message=="Please add some comments for 1 - 5"
                    #assert save_message=="Coaching Saved"
                    assert Header.get_HeaderTittle()==self.coachpagetitle
                    assert BasicInfo.get_status()=="Ongoing"
                    
                    #Step14:11.Under WEEK ENDING2 section:
                                #a. Input following content:
                                    #Firstly input content in test boxes to test-WEEK ENDING 2 section.
                                #b.Click button ' TL Sign'.
                    for QuestionNumber in range(1,6):
                        question_title=SalesWPRF.get_AnyQuestionsOfAnyWeekEnding_title(QuestionNumber, 2) 
                        text=self.Longtextboxesprefix1+question_title
                        SalesWPRF.input_AnyQuestionsOfAnyWeekEnding(QuestionNumber, 2, text)
                        
                    SalesWPRF.click_SaveOrSignButtonOfAnyWeekEnding(2, 2)
                    TL_Sign_Date_2=GetConfig.get_ServerCurrentDate().replace("-","/")
                    TL_Sign_Date_list.append(TL_Sign_Date_2)
                    
                    '''Check14:1)  Shown message:Team leader signed.(No Script)
                               2)  Under section 'WEEK ENDING 2' :
                                        --Buttons: Save and TL Sign disappeared.
                                        ---Button 'Agent Sign' shown with disabled status.
                                        -- "TL Signed Date: yyyy/mm/dd" showing on left side.
                               3)  WEEK 3 section and WEEK ENDING 3 section become editable;
                               4)  WEEK 2 section and WEEK ENDING 2 section become disabled.'''
                    #assert BasicInfo.get_AlertMessage()=="Team Leader Signed"  
                    print "SalesWPRF.Get_SaveOrSignButtonOfAnyWeekEnding_text(2, 1):",SalesWPRF.Get_SaveOrSignButtonOfAnyWeekEnding_text(2, 1)
                    #print "SalesWPRF.Get_SaveOrSignButtonOfAnyWeekEnding_text(2, 2):",SalesWPRF.Get_SaveOrSignButtonOfAnyWeekEnding_text(2, 2)
                    assert SalesWPRF.Get_SaveOrSignButtonOfAnyWeekEnding_text(2, 1)=="Agent Sign"  
                    assert SalesWPRF.SaveOrSignButtonOfAnyWeekEnding_exist(2, 2)==False
                    assert SalesWPRF.anyButtonOfAnyWeekEnding_disabled(2, 1)=="true"
                    assert SalesWPRF.Get_AnyQuestion_RoleSign_text(2, 1)=="TL Signed Date:"
                    assert SalesWPRF.Get_AnyQuestion_RoleSign_date(2, 1)==TL_Sign_Date_2
                    for QuestionNumber in range(1,6):
                        assert SalesWPRF.AnyQuestionsOfAnyWeekEnding_disabled(QuestionNumber, 3)!="true"
                    for QuestionNumber in range(1,6):
                        assert SalesWPRF.AnyQuestionsOfAnyWeekEnding_disabled(QuestionNumber, 2)=="true"    
                                          
                    #Step15:12.Under WEEK ENDING3 section:
                                #a. Input following content:
                                    #Firstly input content in test boxes to test-WEEK ENDING 3 section.
                                #b.Click button ' TL Sign'.                                   
                                                       
                    for QuestionNumber in range(1,6):
                        question_title=SalesWPRF.get_AnyQuestionsOfAnyWeekEnding_title(QuestionNumber, 3) 
                        text=self.Longtextboxesprefix1+question_title
                        SalesWPRF.input_AnyQuestionsOfAnyWeekEnding(QuestionNumber, 3, text)                                   
                                                       
                    SalesWPRF.click_SaveOrSignButtonOfAnyWeekEnding(3, 2)
                    TL_Sign_Date_3=GetConfig.get_ServerCurrentDate().replace("-","/")
                    TL_Sign_Date_list.append(TL_Sign_Date_3)
                    '''Check15:Shown message:Team leader signed.(No Script)'''
                    #assert BasicInfo.get_AlertMessage()=="Team Leader Signed"  
                    
                    #Step16:13.Under WEEK ENDING4 section:
                            #a. Input following content:
                                #Firstly input content in test boxes to test-WEEK ENDING 4 section.
                            #b.Click button ' TL Sign'.
                    for QuestionNumber in range(1,6):
                        question_title=SalesWPRF.get_AnyQuestionsOfAnyWeekEnding_title(QuestionNumber, 4) 
                        text=self.Longtextboxesprefix1+question_title
                        SalesWPRF.input_AnyQuestionsOfAnyWeekEnding(QuestionNumber, 4, text)                                   
                                                       
                    SalesWPRF.click_SaveOrSignButtonOfAnyWeekEnding(4, 2)
                    TL_Sign_Date_4=GetConfig.get_ServerCurrentDate().replace("-","/")
                    TL_Sign_Date_list.append(TL_Sign_Date_4)
                    '''Check16:Shown message:Team leader signed.(No Script)'''
                    #assert BasicInfo.get_AlertMessage()=="Team Leader Signed"  
                    
                    #Step17:a.
                                                        #Week5      MONTHLY PERFORMANCE RESULTS
                                #...                        keep blank           keep blank
                                #...                       keep blank          keep blank
                                #...                       keep blank            keep blank
                                #MOB Units      56.98                      better than 56.98
                            
                            #KPIs new column1  keep blank  content the same as weekending5  
                            #b. Under WEEK ENDING5 section:
                                #Input following content:
                            #Firstly input content in test boxes to test-WEEK ENDING 5 section.
                            #c.Click button ' TL Sign'.
                    
                    
                    SalesWPRF.input_anyMETRICOfanyWeekOrmonthly(10, 6, "56.98")
                    SalesWPRF.input_anyMETRICOfanyWeekOrmonthly(10, 7, "better than 56.98")
                    
                    for QuestionNumber in range(1,6):
                        question_title=SalesWPRF.get_AnyQuestionsOfAnyWeekEnding_title(QuestionNumber, 5) 
                        text=self.Longtextboxesprefix1+question_title
                        SalesWPRF.input_AnyQuestionsOfAnyWeekEnding(QuestionNumber, 5, text)   
                        
                    SalesWPRF.click_SaveOrSignButtonOfAnyWeekEnding(5, 2)
                    TL_Sign_Date_5=GetConfig.get_ServerCurrentDate().replace("-","/")
                    TL_Sign_Date_list.append(TL_Sign_Date_5)
                    
                    '''Check17:c.1)  Shown message:Team leader signed.(No Script)
                                 2)  WEEK 5 section and WEEK ENDING 5,
                                     MONTHLY PERFORMANCE RESULTS  section become disabled.
                                 3) Button 'Completed coaching' is still disabled.'''
                    
                    #assert BasicInfo.get_AlertMessage()=="Team Leader Signed"
                    for METRICindex in range(1,14):
                        assert SalesWPRF.anyMETRICOfanyWeekOrmonthly_disabled(METRICindex, 6)=="true"
                    for METRICindex in range(1,14):
                        assert SalesWPRF.anyMETRICOfanyWeekOrmonthly_disabled(METRICindex, 7)=="true"
                    for QuestionNumber in range(1,6):
                        assert SalesWPRF.AnyQuestionsOfAnyWeekEnding_disabled(QuestionNumber, 5)=="true"
                        
                    #Step18:15.a. Input content in other text boxes:(item6-item12)
                                    #Performance pro test team to input content in text boxes ,alice_shu0823~!@#$%^&*();:'"?/\[]{},sabrina's@symbio.com.
                                #b. Unchecked the first two KPIs
                                    #Check the third KPI
                                #c. Change call Recording Number
                                #d.Click button 'Save and Continue Later'.
                                #e.Directly select this record to open form detail page.
                    for QuestionNumber in range(4,9):
                        text=self.Longtextboxesprefix1+SalesWPRF.get_OtherQuestion_title(QuestionNumber, 1)
                        SalesWPRF.input_OtherQuestion(QuestionNumber, text)
                    for SubQuestionNumber in range(2,7):   
                        text=self.Longtextboxesprefix1+SalesWPRF.get_SubQuestion_title(1, SubQuestionNumber)
                        SalesWPRF.input_SubQuestion(1, SubQuestionNumber,text)
                    for SubQuestionNumber in range(2,4):   
                        text=self.Longtextboxesprefix1+SalesWPRF.get_SubQuestion_title(2, SubQuestionNumber)
                        SalesWPRF.input_SubQuestion(2, SubQuestionNumber,text)
                    BasicInfo.click_anyKPIstatusofCheckBox_Agent(2)
                    BasicInfo.click_anyKPIstatusofCheckBox_Agent(3)
                    BasicInfo.click_anyKPIstatusofCheckBox_Agent(4)
                    if lobname != "AOL":
                        BasicInfo.input_callrecordingnumber(self.CallRecordingNumber2) 
                        
                    BasicInfo.Click_Button(2)
                    
                    '''Check19:d.Directly back to coaching search main page.
                               e.On detail page:
                                 1) Following KPIs in checked status: 
                                                The third and the fourth KPIs.
                                 Other KPI shown unchecked status.
                                 2) Following field shown correct:
                                  ---Call recording number
                                  -- Value in Week5 ,  MONTHLY PERFORMANCE RESULTS
                                  --content in item6-item12.'''
                    CoachHome.click_eachcoach(1)
                    assert BasicInfo.get_anyCheckBoxStatus_Agent(2)==self.CheckBox_UnCheckedStatus
                    assert BasicInfo.get_anyCheckBoxStatus_Agent(3)==self.CheckBox_UnCheckedStatus
                    assert BasicInfo.get_anyCheckBoxStatus_Agent(4)==self.CheckBox_CheckedStatus
                    assert BasicInfo.get_anyCheckBoxStatus_Agent(5)==self.CheckBox_CheckedStatus
                    for index in range(6,KPInumber+1):
                        assert BasicInfo.get_anyCheckBoxStatus_Agent(index)==self.CheckBox_UnCheckedStatus
                    assert BasicInfo.get_callrecordingnumber()==self.CallRecordingNumber2
                    for METRICindex in range(1,14):
                        if METRICindex ==10:
                            assert SalesWPRF.Get_anyMETRICOfanyWeekOrmonthly(METRICindex, 6)=="56.98"
                            assert SalesWPRF.Get_anyMETRICOfanyWeekOrmonthly(METRICindex, 7)=="better than 56.98"
                        else:
                            assert SalesWPRF.Get_anyMETRICOfanyWeekOrmonthly(METRICindex, 6)==""
                            assert SalesWPRF.Get_anyMETRICOfanyWeekOrmonthly(METRICindex, 7)==""
                    for QuestionNumber in range(4,9):
                        text=self.Longtextboxesprefix1+SalesWPRF.get_OtherQuestion_title(QuestionNumber, 1)
                        assert SalesWPRF.get_OtherQuestion_content(QuestionNumber)==text
                    for SubQuestionNumber in range(2,7):   
                        text=self.Longtextboxesprefix1+SalesWPRF.get_SubQuestion_title(1, SubQuestionNumber)
                        assert SalesWPRF.get_SubQuestion_content(1, SubQuestionNumber)==text
                    for SubQuestionNumber in range(2,4):   
                        text=self.Longtextboxesprefix1+SalesWPRF.get_SubQuestion_title(2, SubQuestionNumber)
                        assert SalesWPRF.get_SubQuestion_content(2, SubQuestionNumber)==text
                    
                                                    
                    #Step20:16.
                        #a) Logout and login the Agent who is coached in the form;
                        #b) Go to Coaching module and open the form;
                        #c) Click Agent Sign buttons in sequence.
                    L.logout_tablet()
                    L.Login_tablet(self.tableturl, lobname, sitename, Agent_hrid, Agent_password)
                    Tablet.click_Agent_coachingcircle()
                    CoachHome.click_eachcoach(1)
                    '''Check21:c) 
                                 Agent signed successfully;
                                "Agent Signed Date: yyyy/mm/dd" showing at the corresponding right positions.'''
                    for WeekEndingIndex in range(2,6):
                        SalesWPRF.click_SaveOrSignButtonOfAnyWeekEnding(WeekEndingIndex, 1)
                        Agent_Sign_Date_left=GetConfig.get_ServerCurrentDate().replace("-","/")
                        Agent_Sign_Date_list.append(Agent_Sign_Date_left)
                        #assert BasicInfo.get_AlertMessage()=="Agent Signed"
                        assert SalesWPRF.Get_AnyQuestion_RoleSign_text(WeekEndingIndex, 2)=="Agent Signed Date:"
                        assert SalesWPRF.Get_AnyQuestion_RoleSign_date(WeekEndingIndex, 2)==Agent_Sign_Date_left
                    
                    #Step21:17.
                            #a) Logout and login the TL who added the form;
                            #b) Go to Coaching module and open the form
                            #c) Click button: Complete Coaching ;
                    L.logout_tablet()
                    L.Login_tablet(self.tableturl, lobname, sitename, TLHrid, TLPassword)
                    Tablet.click_TL_coachingcircle()
                    CoachHome.click_eachcoach(1)
                    
                    
                    '''Check21:b)
                                .Under each sections from WEEK EDNING1' to WEEK EDNING5:
                                "TL Signed Date:  yyyy/mm/dd" showing at the correspondg left side.
                                "Agent Signed Date: yyyy/mm/dd" showing at the corresponding right side.
                                
                               c)  Back to coaching list page.'''
                    for WeekEndingIndex in range(2,6):
                        i=WeekEndingIndex-1
                        assert SalesWPRF.Get_AnyQuestion_RoleSign_text(WeekEndingIndex, 1)=="TL Signed Date:"
                        assert SalesWPRF.Get_AnyQuestion_RoleSign_date(WeekEndingIndex, 1)==TL_Sign_Date_list[i]
                        assert SalesWPRF.Get_AnyQuestion_RoleSign_text(WeekEndingIndex, 2)=="Agent Signed Date:"
                        assert SalesWPRF.Get_AnyQuestion_RoleSign_date(WeekEndingIndex, 2)==Agent_Sign_Date_list[i]
                    
                    BasicInfo.Click_Button(3)
                    completed_Date=GetConfig.get_ServerCurrentDate().replace("-","/")
                    assert Header.get_HeaderTittle()=="Coaching"
                    #Step22:d). From status drop-down, select Status ='Completed'->Click Filter;
                            #e) Open the form again;
                    CoachHome.select_status("Completed")
                    CoachHome.click_filterbutton()
                    CoachHome.click_eachcoach(1)
                    '''Check22:e. On form detail page:
                                  Status: Completed;
                                 .Complete Date: the date when the form is completed'''
                    assert BasicInfo.get_status()=="Completed"
                    assert BasicInfo.get_completeddate()==completed_Date
                    #Step23:18.
                            #a. Logout and login the Agent who is coached in the form;
                            #b. Go to coaching module.
                            #c.Status drop-down:Select Completed;
                            #d. Click Filter;
                            #e. Open the SWPRM form
                    L.logout_tablet()
                    L.Login_tablet(self.tableturl, lobname, sitename, Agent_hrid, Agent_password)
                    Tablet.click_Agent_coachingcircle()
                    CoachHome.select_status("Completed")
                    CoachHome.click_filterbutton()
                    CoachHome.click_eachcoach(1)
                    '''Check23:e. At page bottom showing two buttons: 
                                Acknowledge Coaching
                                Back;'''
                    assert BasicInfo.get_ButtonName(1)=="Acknowledge Coaching"
                    assert BasicInfo.get_ButtonName(2)=="Back"
                    #Step24:19.a.Click button:  Acknowledge Coaching;
                    BasicInfo.Click_Button(1)
                    acknowledge_Date=GetConfig.get_ServerCurrentDate().replace("-","/")
                    
                    '''Check24:a. Acknowledge coaching successfully.
                                  Back to coachig search list page.'''
                    #assert BasicInfo.get_AlertMessage()=="Coaching Acknowledged"
                    assert Header.get_HeaderTittle()=="Coaching"
                    
                    #Step25:b. Status Drop-down:Select Status = Acknowledged;
                            #c. Click Filter
                            #d. Open this form again.
                            #e. Try to edit this form.
                    CoachHome.select_status("Acknowledged")
                    CoachHome.click_filterbutton()
                    CoachHome.click_eachcoach(1)
                    '''Check25:d.
                                On this form:
                                1)  Status = Acknowledged;
                                2)  Completed Date = The date when the form is completed;
                                3)  Acknowledged Date = The date when the form is acknowledged.
                                e. Agent cannot edit the form.(each of fields in uneditable status)(Only check one weekending's question)'''
                    assert BasicInfo.get_status()=="Acknowledged"
                    assert BasicInfo.get_completeddate()==completed_Date
                    assert BasicInfo.get_acknowledgedDate()==acknowledge_Date
                    for QuestionNumber in range(1,6):
                        assert SalesWPRF.AnyQuestionsOfAnyWeekEnding_disabled(QuestionNumber, 2)=="true" 
                        
                    #Step26:20.
                            #a. Logout and Login tablet with TL account that added this form;
                            #b. Click Coaching icon;
                            #c. Select Status = Acknowledged;
                            #d. Click Filter;
                            #e. Open this form.
                            #f. Try to edit this form.
                    L.logout_tablet()
                    L.Login_tablet(self.tableturl, lobname, sitename, TLHrid, TLPassword)
                    Tablet.click_TL_coachingcircle()
                    CoachHome.select_status("Acknowledged")
                    CoachHome.click_filterbutton()
                    CoachHome.click_eachcoach(1)
                    '''Check26:Status of the form: Acknowledged '''
                    assert BasicInfo.get_status()=="Acknowledged"
                    L.logout_tablet()
                   
                    
                GetConfig.print_EndTest_message(lobname, sitename)    
                    

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()