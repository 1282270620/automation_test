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
                   
                    
                    #Step3.7:Select this record to enter the  form again. 
                    #CoachHome.click_eachcoach(typename_path)
                    CoachHome.click_eachcoach(1)
                    
                    #Step14:11.Under WEEK ENDING2 section:
                                #a. Input following content:
                                    #Firstly input content in test boxes to test-WEEK ENDING 2 section.
                                #b.Click button ' TL Sign'.
                    for QuestionNumber in range(1,6):
                        question_title=SalesWPRF.get_AnyQuestionsOfAnyWeekEnding_title(QuestionNumber, 2) 
                        text=self.Longtextboxesprefix1+question_title
                        SalesWPRF.input_AnyQuestionsOfAnyWeekEnding(QuestionNumber, 2, text)
                        
                   
                    for QuestionNumber in range(1,6):
                        question_title=SalesWPRF.get_AnyQuestionsOfAnyWeekEnding_title(QuestionNumber, 3) 
                        text=self.Longtextboxesprefix1+question_title
                        SalesWPRF.input_AnyQuestionsOfAnyWeekEnding(QuestionNumber, 3, text)                                   
                    
                    #assert BasicInfo.get_AlertMessage()=="Team Leader Signed"  
                    
                    #Step16:13.Under WEEK ENDING4 section:
                            #a. Input following content:
                                #Firstly input content in test boxes to test-WEEK ENDING 4 section.
                            #b.Click button ' TL Sign'.
                    for QuestionNumber in range(1,6):
                        question_title=SalesWPRF.get_AnyQuestionsOfAnyWeekEnding_title(QuestionNumber, 4) 
                        text=self.Longtextboxesprefix1+question_title
                        SalesWPRF.input_AnyQuestionsOfAnyWeekEnding(QuestionNumber, 4, text)                                   
                                                       
                  
                    
                    for QuestionNumber in range(1,6):
                        question_title=SalesWPRF.get_AnyQuestionsOfAnyWeekEnding_title(QuestionNumber, 5) 
                        text=self.Longtextboxesprefix1+question_title
                        SalesWPRF.input_AnyQuestionsOfAnyWeekEnding(QuestionNumber, 5, text)   
                        
                  
                        
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
                        SalesWPRF.input_SubQuestion(1, SubQuestionNumber,text)
                   
                    BasicInfo.Click_Button(2)
                    
                   
                    for QuestionNumber in range(4,9):
                        text=self.Longtextboxesprefix1+SalesWPRF.get_OtherQuestion_title(QuestionNumber, 1)
                        assert SalesWPRF.get_OtherQuestion_content(QuestionNumber)==text
                    print "SubQuestion"
                    for SubQuestionNumber in range(2,7):   
                        text=self.Longtextboxesprefix1+SalesWPRF.get_SubQuestion_title(1, SubQuestionNumber)
                        print SubQuestionNumber
                        print SalesWPRF.get_SubQuestion_content(1, SubQuestionNumber) 
                        print text
                        
                        assert SalesWPRF.get_SubQuestion_content(1, SubQuestionNumber)==text
                        
                    print "SubQuestionNumber"
                    for SubQuestionNumber in range(2,4):   
                        text=self.Longtextboxesprefix1+SalesWPRF.get_SubQuestion_title(2, SubQuestionNumber)
                        print SalesWPRF.get_SubQuestion_content(2, SubQuestionNumber) 
                        print text
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
                        assert BasicInfo.get_AlertMessage()=="Agent Signed"
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
                    assert BasicInfo.get_AlertMessage()=="Coaching Acknowledged"
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