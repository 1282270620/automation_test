'''
Created on 20170906

@author: luming.zhao
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
from CoachingAndTriadCoaching_Pages.DirectSalesQACoachingForm import DirectSalesQACoachingForm
from public_method.Coaching_PublicFunction import Coaching_PublicFunction
from Tablet_pages.HeaderPage import HeaderPage
from public_method.Get_AllRoleAccountForTest import Get_AllRoleAccountForTest
from public_method.KPI_method import KPI_method
from public_method.HandleMySQL import HandleMySQL

class DirectSalesQACoachingForm_PlanedToAcknowledged(unittest.TestCase):


    def setUp(self):
        #Case ID
        self.caseID="DirectSalesQACoachingForm_PlanedToAcknowledged"
        
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
        #coaching or Triad coaching
        self.coachtype="coaching"  
        #Coachformname
        self.coachformname="Direct Sales QA/Coaching Form" 
        self.coachpagetitle="Coaching - "+self.coachformname
        #KPI box title in coaching detail page
        self.KPIbox_title="Coaching KPIs(Month-To-Date):"
        
        #CheckBox Status
        self.CheckBox_CheckedStatus="fa fa-check-square"
        self.CheckBox_UnCheckedStatus="fa fa-uncheck"
        #User's role
        self.UserRole="OM"


    def tearDown(self):
        Gl.driver.quit()


    def test_DirectSalesQACoachingForm_PlanedToAcknowledged(self):
        GetConfig=Get_configration_data()
        Tablet=TabletHomepage()
        Ppage=PerformancePage()
        TCoach=Coach_Triad_General()
        CoachHome=Coachinghomepage()
        BasicInfo=BasicInfoforCoaching()
        CoachPublic=Coaching_PublicFunction()
        Header=HeaderPage()
        DirectSalesQACoachingForm1=DirectSalesQACoachingForm()
        Getaccount=Get_AllRoleAccountForTest()
        KPIMethod=KPI_method()
        HMysql=HandleMySQL()
        
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
                    AgentInfo_Dic=Getaccount.get_AgentInfoFromTablet(self.tableturl, lobname, sitename, self.OMuserid, self.OMpassword,"Month-To-Date")
                    Agent_name=AgentInfo_Dic["AgentName"]
                    Agent_hrid=AgentInfo_Dic["AgentHrid"]
                    Agent_password=AgentInfo_Dic["AgentPassword"]
                    L=Login()
                    L.Login_tablet(self.tableturl,lobname,sitename,self.OMuserid,self.OMpassword)
                    time.sleep(Gl.waittime)
                    #Step2:Enter performance
                    Tablet.click_performancecircle()
                   
                    #Step3:Select one Agent to add coaching to follow Planed to Acknowledged
                    print "Start=====Monthly-To-Day is in testing",
                    #Ppage.select_Agentkpi()#select the first Agent's kpi of the first TL
                    Ppage.select_Agentkpi()
                    Ppage.unselect_Agentkpi()
                    #KPInumber=Ppage.get_KPInumber()
                    if lobname in Gl.DoubleKPIname_lob:
                        KPInumber=Ppage.get_KPInumber_All()
                        KPIname_FromPerformancePage_list=Ppage.get_KPIname_list_Double()
                        for index in range(0,len(KPIname_FromPerformancePage_list)):
                            if KPIname_FromPerformancePage_list[-12]=="(" and KPIname_FromPerformancePage_list[-1]==")":
                                KPIname_FromPerformancePage_list[-12:]
                    else:
                        KPInumber=Ppage.get_KPInumber()
                        KPIname_FromPerformancePage_list=Ppage.get_KPIname_list(KPInumber)
                        
                    KPIofGoal_FromPerformancePage_list=Ppage.get_AllKPIsofGoal_list(KPInumber)
                    KPIofSite_FromPerformancePage_list=Ppage.get_AllKPIsofSite_list(KPInumber)
                    KPIofAgentOrTL_FromPerformancePage_list=Ppage.get_AllKPIsofAgentForOM_list(KPInumber)
                    if lobname in Gl.performancefor_MultiTimeTab_lob:
                        Ppage.click_timetab_performance(5)#Ppage.click_mtd()
                    else:    
                        Ppage.click_timetab_performance(3)#Ppage.click_mtd()
                    Ppage.select_AnyKpiOfAgent_OM(4)#Select three KPI
                    
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
                    Tablet.click_coachingcircle() 
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
                    '''Check2:1.Page title :'Coaching - Accountability Conversation'.
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
                    KPIofAgentOrTL_FromDetailPage_list=BasicInfo.get_AllKPIsofAgentOrTL_list(KPInumber)
                    CheckBoxStatus_FromDetailPage_list=BasicInfo.get_CheckBoxStatus_list(KPInumber)
                    KPIboxTitle=BasicInfo.get_KPIboxTitle()
                    '''Check4: 1.Show header name 'Coaching KPIs(Month-To-Date)';
                               2.All KPI data of Goal, Site,Team,Agent should be the same as those on the corresponding performance page;
                               3.The first three KPIs are checked by default.'''
                    assert KPIboxTitle=="Coaching KPIs(Month-To-Date):"
                    #assert KPIname_FromPerformancePage_list==KPIname_FromDetailPage_list
                    assert KPIofGoal_FromPerformancePage_list==KPIofGoal_FromDetailPage_list
                    assert KPIofSite_FromPerformancePage_list==KPIofSite_FromDetailPage_list
                    assert KPIofAgentOrTL_FromPerformancePage_list==KPIofAgentOrTL_FromDetailPage_list
                    assert CheckBoxStatus_FromDetailPage_list[0]==self.CheckBox_CheckedStatus
                    assert CheckBoxStatus_FromDetailPage_list[1]==self.CheckBox_CheckedStatus
                    assert CheckBoxStatus_FromDetailPage_list[2]==self.CheckBox_CheckedStatus
                    
                    #Step3.5: Check other sections: other buttons
                    '''Check5:Check all buttons are displayed'''
                    assert BasicInfo.get_ButtonName(1)=="Print"
                    assert BasicInfo.get_ButtonName(2)=="Save and Continue Later"
                    assert BasicInfo.get_ButtonName(3)=="Complete Coaching"
                    assert BasicInfo.get_ButtonName(4)=="Cancel Coaching"
                    assert BasicInfo.get_ButtonName(5)=="Quit Without Save"
                    
                    #Step3.6:1.Click 'Quit without Save'
                            #2.Get all coaching number & status
                    BasicInfo.Click_Button(5)#Click Quit without Save button
                    assign_to_id=self.OMuserid
                    total_PageandCoachnumber_tablet_Dic6=CoachPublic.get_Total_PageandCoachnumber()
                    Total_coachnumber_tablet6=total_PageandCoachnumber_tablet_Dic6['Total_coachnumber_tablet']
                    Status_Coach=CoachHome.get_anyCoach_attribute(1, 6)
                    sql_coach="select * from coach  where  assign_to_id="+assign_to_id+"  and classification=0 and status in (0,3) order by id desc"
                    Datalist6=HMysql.Get_datafromDB(self.hostindex, lobname, sitename, self.dbuser, self.dbpassword, sql_coach)
                    Total_coachnumber_database6=Datalist6[0]
                    '''Check6:Return to Coaching list page,On search fields section,show:
                              1.CoachingName=OM(logged-in)
                              2.EmployeeName=All
                              3.Status=Incompleted.
                              4.Type=All
                              5.All incompleted coaching records of logged-in user is listed.
                              6.This coach record is shown by default  with  status 'Planned'.'''
                    assert CoachHome.get_CoachName()==Header.get_loginName()
                    assert CoachHome.get_EmployeeName()=="All"
                    assert CoachHome.get_typename_selected()=="All"
                    assert CoachHome.get_status_selected()=="Incompleted"
                    assert Total_coachnumber_tablet6==Total_coachnumber_database6#Check total number of coachings in tablet is the same with it in database
                    assert Status_Coach=="Planned"
                        
                    #Step3.7:Select this record to enter the  form again. 
                    #CoachHome.click_eachcoach(typename_path)
                    CoachHome.click_eachcoach(1)
                    '''Check7:Enter the  form detail page with title 'Coaching - Accountability Conversation'''
                    assert Header.get_HeaderTittle()==self.coachpagetitle 
                    
                    #Step3.8:Input content in following editable fields:
                            #1.Uncheck the third KPI;
                            #2.Check the fouth KPI.;
                    BasicInfo.click_anyKPIstatusofCheckBox(4)
                    BasicInfo.click_anyKPIstatusofCheckBox(5)
                    '''Check8:1.The third KPI is in unchecked status.
                              2.The fourth KPI is in checked status.'''
                    assert BasicInfo.get_anyCheckBoxStatus(4)==self.CheckBox_UnCheckedStatus
                    assert BasicInfo.get_anyCheckBoxStatus(5)==self.CheckBox_CheckedStatus
                    
                    #Step3.8:#3.input call Recording Number

                    call_Recording_Number='Test_callrecordingnumber123!@#'
                    if lobname != "AOL":
                        BasicInfo.input_callrecordingnumber(call_Recording_Number)
                    
                    #Step3.9:Click Save and continue later button
                    BasicInfo.Click_Button(2)#Click Save and Continue Later button
                    total_PageandCoachnumber_tablet_Dic10=CoachPublic.get_Total_PageandCoachnumber()
                    Total_coachnumber_tablet10=total_PageandCoachnumber_tablet_Dic10['Total_coachnumber_tablet']
                    Status_Coach=CoachHome.get_anyCoach_attribute(1, 6)
                    assign_to_id=self.OMuserid
                    sql_coach="select * from coach  where  assign_to_id="+assign_to_id+"  and classification=0 and status in (0,3) order by id desc"
                    Datalist10=HMysql.Get_datafromDB(self.hostindex, lobname, sitename, self.dbuser, self.dbpassword, sql_coach)
                    Total_coachnumber_database10=Datalist10[0]
                    '''Check9:1.Check total number of coachings in tablet is the same with it in database
                               2.Check Status of all coachings in tablet is changed to Ongoing'''
                    assert Total_coachnumber_tablet10==Total_coachnumber_database10                    
                    assert Status_Coach=="Ongoing"
                    
                    #Step3.10:Select this record to open form detail page again.
                    #CoachHome.click_eachcoach(typename_path)
                    CoachHome.click_eachcoach(1)
                    '''Check10:1.Check the title of the detail page
                               2.Check the status of this coaching in detail page is Ongoing
                               3.Check the first two and fourth KPIs is in checked status
                               4.Check  Other KPI is shown unchecked status'''
                    assert Header.get_HeaderTittle()==self.coachpagetitle
                    assert BasicInfo.get_status()=="Ongoing"

                    if lobname != "AOL":
                        assert BasicInfo.get_callrecordingnumber()==call_Recording_Number
                    assert BasicInfo.get_anyCheckBoxStatus(2)==self.CheckBox_CheckedStatus
                    assert BasicInfo.get_anyCheckBoxStatus(3)==self.CheckBox_CheckedStatus
                    assert BasicInfo.get_anyCheckBoxStatus(4)==self.CheckBox_UnCheckedStatus
                    assert BasicInfo.get_anyCheckBoxStatus(5)==self.CheckBox_CheckedStatus
                    for index in range(6,KPInumber+1):
                        assert BasicInfo.get_anyCheckBoxStatus(index)==self.CheckBox_UnCheckedStatus
                        
                    #Step3.11:In all  other text boxes with following content:Firstly input content in test boxes to test.
                    
                    Content_InTextBox="Performance pro test team to input content in text boxes ,alice_shu0823~!@#$%^&*();:'?/\[]{},sabrina's@symbio.com."
                    Maxline1index=DirectSalesQACoachingForm1.select_Discover
                    DirectSalesQACoachingForm1.select_Discover(1, Maxline1index)
                    DirectSalesQACoachingForm1.select_Transition(2, 2)
                    DirectSalesQACoachingForm1.select_Pitch(4, 2)
                    DirectSalesQACoachingForm1.select_Overcome(3)
                    DirectSalesQACoachingForm1.select_Close(3, 1)
                    DirectSalesQACoachingForm1.input_strengths(Content_InTextBox)
                    DirectSalesQACoachingForm1.input_opportunities1(Content_InTextBox)
                    DirectSalesQACoachingForm1.input_opportunities2(Content_InTextBox)
                    DirectSalesQACoachingForm1.input_plan1(Content_InTextBox)
                    DirectSalesQACoachingForm1.input_plan2(Content_InTextBox)
                    
                    
                    #Step3.12:click "Save and Continue Later"
                    BasicInfo.Click_Button(2)
                    Status_Coach=CoachHome.get_anyCoach_attribute(1, 6)
                    '''Check12:Check the status of this coaching in detail page is Ongoing'''
                    assert Status_Coach=="Ongoing"
                    
                    #Step3.13:Open this record  form again.
                    #CoachHome.click_eachcoach(typename_path)
                    CoachHome.click_eachcoach(1)
                    '''Check13:1.Check the title of the detail page
                               2.Check the status of this coaching in detail page is Ongoing
                               3.Check the first two and fourth KPIs is in checked status
                               4.Check  Other KPI is shown unchecked status
                               5.Check the content shown in text box is the same as that input'''
                    assert Header.get_HeaderTittle()==self.coachpagetitle
                    assert BasicInfo.get_status()=="Ongoing"

                    if lobname != "AOL":
                        assert BasicInfo.get_callrecordingnumber()==call_Recording_Number
                    assert BasicInfo.get_anyCheckBoxStatus(2)==self.CheckBox_CheckedStatus
                    assert BasicInfo.get_anyCheckBoxStatus(3)==self.CheckBox_CheckedStatus
                    assert BasicInfo.get_anyCheckBoxStatus(4)==self.CheckBox_UnCheckedStatus
                    assert BasicInfo.get_anyCheckBoxStatus(5)==self.CheckBox_CheckedStatus
                    for index in range(6,KPInumber+1):
                        assert BasicInfo.get_anyCheckBoxStatus(index)==self.CheckBox_UnCheckedStatus
                    
                    assert DirectSalesQACoachingForm1.select_Discover()=="no"
                    assert DirectSalesQACoachingForm1.select_Transition()=="no"
                    assert DirectSalesQACoachingForm1.select_Pitch()=="no"
                    assert DirectSalesQACoachingForm1.select_Overcome()=="na"
                    assert DirectSalesQACoachingForm1.select_Close()=="yes"
                    assert DirectSalesQACoachingForm1.input_strengths()==Content_InTextBox
                    assert DirectSalesQACoachingForm1.input_opportunities1()==Content_InTextBox
                    assert DirectSalesQACoachingForm1.input_opportunities2()==Content_InTextBox
                    assert DirectSalesQACoachingForm1.input_plan1()==Content_InTextBox
                    assert DirectSalesQACoachingForm1.input_plan2()==Content_InTextBox

                    
                    #Step3.14:1.Change content in all editable fields to new one:
                            #1)Unchecked the first two KPIs,Check the third KPI
                            #2)Input Call Recording ID ='callRecordingID_003&004'
                            #3)select ' Date and Time of Call'=select the second date in date picker
                            #4)input call Recording Number
                            #5)in all other text boxes:Edit content, performance pro test team to input content in text boxes ,alice_shu0823~!@#$%^&*();:'"?/\[]{},sabrina's@symbio.com.

                    call_Recording_Number_new='edit test_number123!~@#$%^&*()'
                    Content_InTextBox_new="Edit content, performance pro test team to input content in text boxes ,alice_shu0823~!@#$%^&*();:'""?/\[]{},sabrina's@symbio.com."
                    BasicInfo.click_anyKPIstatusofCheckBox(2)#)Unchecked the first two KPIs
                    BasicInfo.click_anyKPIstatusofCheckBox(3)#Unchecked the first two KPIs
                    BasicInfo.click_anyKPIstatusofCheckBox(4)#Check the third KPI

                    if lobname != "AOL":
                        BasicInfo.input_callrecordingnumber(call_Recording_Number_new)

                    DirectSalesQACoachingForm1.select_Discover(1, 2)
                    DirectSalesQACoachingForm1.select_Transition(2, 2)
                    DirectSalesQACoachingForm1.select_Pitch(4, 2)
                    DirectSalesQACoachingForm1.select_Overcome(3)
                    DirectSalesQACoachingForm1.select_Close(3, 1)
                    DirectSalesQACoachingForm1.input_strengths(Content_InTextBox_new)
                    DirectSalesQACoachingForm1.input_opportunities1(Content_InTextBox_new)
                    DirectSalesQACoachingForm1.input_opportunities2(Content_InTextBox_new)
                    DirectSalesQACoachingForm1.input_plan1(Content_InTextBox_new)
                    DirectSalesQACoachingForm1.input_plan2(Content_InTextBox_new)

                    '''Check14:1.The first two KPIs are in unchecked status.
                               2.The third and the fourth KPIs are in checked status.'''
                    assert BasicInfo.get_anyCheckBoxStatus(2)==self.CheckBox_UnCheckedStatus
                    assert BasicInfo.get_anyCheckBoxStatus(3)==self.CheckBox_UnCheckedStatus
                    assert BasicInfo.get_anyCheckBoxStatus(4)==self.CheckBox_CheckedStatus
                    assert BasicInfo.get_anyCheckBoxStatus(5)==self.CheckBox_CheckedStatus

                    #Step3.14:2.Click  button "Complete Coaching";
                    BasicInfo.Click_Button(3)#Click Complete coaching
                    Completed_Date_FromServer=GetConfig.get_ServerCurrentDate().replace("-","/")
                    SN_ThefirstCoachInlist_old=SN_coachhomepage
                    SN_ThefirstCoachInlist_new=CoachHome.get_anyCoach_attribute(1, 1)
                    total_PageandCoachnumber_tablet_Dic13=CoachPublic.get_Total_PageandCoachnumber()
                    Total_coachnumber_tablet13=total_PageandCoachnumber_tablet_Dic13['Total_coachnumber_tablet']
                    ##cursor=conn.cursor()
                    assign_to_id=self.OMuserid
                    sql_coach="select * from coach  where  assign_to_id="+assign_to_id+"   and status in (0,3) and classification=0 order by id desc"
                    #time.sleep(30*Gl.waittime)
                    Datalist13=HMysql.Get_datafromDB(self.hostindex, lobname, sitename, self.dbuser, self.dbpassword, sql_coach)
                    Total_coachnumber_database13=Datalist13[0]  
                    '''Check14:3.Return to Coaching list page,Status Drop-down: shown'Incompleted' by default
                               4.This coaching record is not shown by default.
                               5.The current coaching list is the incompleted coaching list.'''
                    assert CoachHome.get_status_selected()=="Incompleted"
                    assert SN_ThefirstCoachInlist_new!=SN_ThefirstCoachInlist_old
                    print "Total_coachnumber_tablet13==Total_coachnumber_database13 :",Total_coachnumber_tablet13,Total_coachnumber_database13 
                    assert Total_coachnumber_tablet13==Total_coachnumber_database13 #There some error while get Total_coachnumber_database 
                    
                    #Step3.15: From status drop-down, select Status ='Completed'->Click Filter;
                    CoachHome.select_status("Completed")
                    CoachHome.click_filterbutton()
                    SN_ThefirstCoachInCompletedlist=CoachHome.get_anyCoach_attribute(1,1)
                    Status_ThefirstCoachInCompletedlist=CoachHome.get_anyCoach_attribute(1, 6)
                    '''Check15:1.Check this coach is in completed coach list
                               2.Check the status of this coach is Completed'''
                    assert SN_ThefirstCoachInCompletedlist==SN_coachhomepage
                    assert Status_ThefirstCoachInCompletedlist=="Completed"
                    
                    #Step3.16:Select this record enter  form detail page again.
                    #CoachHome.click_eachcoach(typename_path)
                    CoachHome.click_eachcoach(1)
                    '''Check16:1.Check the title of the detail page
                               2.Check the status of this coaching in detail page is Completed
                               3.Check Completed Date =The date when the form is completed
                               4.Check Acknowledged Date is blank.
                               5.Check The third and the fourth KPIs are in checked status.
                               6.Check The other KPIs are in unchecked status.
                               7.Check SN, Employee Name,EmployeeID, Coaching Name, Create Date,each of text boxes,dates and Call Recording Number are shown correct
                               8.Check There are only two buttons: Print and Back at page bottom: '''
                    assert Header.get_HeaderTittle()==self.coachpagetitle
                    assert BasicInfo.get_status()=="Completed"
                    assert BasicInfo.get_completeddate()==Completed_Date_FromServer
                    assert BasicInfo.get_acknowledgedDate()==""
                    assert BasicInfo.get_anyCheckBoxStatus(2)==self.CheckBox_UnCheckedStatus
                    assert BasicInfo.get_anyCheckBoxStatus(3)==self.CheckBox_UnCheckedStatus
                    assert BasicInfo.get_anyCheckBoxStatus(4)==self.CheckBox_CheckedStatus
                    assert BasicInfo.get_anyCheckBoxStatus(5)==self.CheckBox_CheckedStatus
                    for index in range(6,KPInumber+1):
                        assert BasicInfo.get_anyCheckBoxStatus(index)==self.CheckBox_UnCheckedStatus
                    assert BasicInfo.get_SN()==SN_coachhomepage
                    assert BasicInfo.get_employeename()==Agent_name
                    assert BasicInfo.get_employeeHrid()==employee_hrid_database
                    assert BasicInfo.get_coachname()==Header.get_loginName()
                    assert BasicInfo.get_createdate()==Created_Date_FromServer
                    if lobname != "AOL":
                        assert BasicInfo.get_callrecordingnumber()==call_Recording_Number_new
                    assert DirectSalesQACoachingForm1.select_Discover()=="no"
                    assert DirectSalesQACoachingForm1.select_Transition()=="no"
                    assert DirectSalesQACoachingForm1.select_Pitch()=="no"
                    assert DirectSalesQACoachingForm1.select_Overcome()=="na"
                    assert DirectSalesQACoachingForm1.select_Close()=="yes"
                    assert DirectSalesQACoachingForm1.input_strengths()==Content_InTextBox_new
                    assert DirectSalesQACoachingForm1.input_opportunities1()==Content_InTextBox_new
                    assert DirectSalesQACoachingForm1.input_opportunities2()==Content_InTextBox_new
                    assert DirectSalesQACoachingForm1.input_plan1()==Content_InTextBox_new
                    assert DirectSalesQACoachingForm1.input_plan2()==Content_InTextBox_new

                    assert BasicInfo.get_ButtonName(1)=="Print"
                    assert BasicInfo.get_ButtonName(2)=="Back"
                    for index in range(3,6):
                        assert BasicInfo.Button_Displayed(index)==False
                    
                    #Step3.16:Try to edit the  form again
                    '''Check16:The form cannot be edited now.( each field is in uneditable status)
                               1.All KPIs can not be checked or unchecked
                               2.Input box is disabled
                    '''
                    for index in range(2,KPInumber):
                        BasicInfo.click_anyKPIstatusofCheckBox(index)
                    assert BasicInfo.get_anyCheckBoxStatus(2)==self.CheckBox_UnCheckedStatus
                    assert BasicInfo.get_anyCheckBoxStatus(3)==self.CheckBox_UnCheckedStatus
                    assert BasicInfo.get_anyCheckBoxStatus(4)==self.CheckBox_CheckedStatus
                    assert BasicInfo.get_anyCheckBoxStatus(5)==self.CheckBox_CheckedStatus
                    for index in range(6,KPInumber+1):
                        assert BasicInfo.get_anyCheckBoxStatus(index)==self.CheckBox_UnCheckedStatus
                    
                    
                    assert DirectSalesQACoachingForm1.strengths__disabled()=="true"
                    assert DirectSalesQACoachingForm1.opportunities1__disabled()=="true"
                    assert DirectSalesQACoachingForm1.opportunities2__disabled()=="true"
                    assert DirectSalesQACoachingForm1.plan1__disabled()=="true"
                    assert DirectSalesQACoachingForm1.plan2__disabled()=="true"

                    
                    #Step3.16:Click BACK button form top left page.
                    Header.click_backbutton()
                    '''Check16:1.Back to search main page with status option 'Completed' is selected by default.
                               2.This coaching record is shown by default with status 'Completed'.
                               3.All completed coaching records listed.'''
                    assert CoachHome.get_status_selected()=="Completed"
                    assert CoachHome.get_anyCoach_attribute(1, 6)=="Completed"
                    total_PageandCoachnumber_tablet_Dic17=CoachPublic.get_Total_PageandCoachnumber()
                    Total_coachnumber_tablet17=total_PageandCoachnumber_tablet_Dic17['Total_coachnumber_tablet']
                    assign_to_id=self.OMuserid
                    sql_coach="select * from coach  where  assign_to_id="+assign_to_id+"  and classification=0 and status=1 order by id desc"
                    Datalist17=HMysql.Get_datafromDB(self.hostindex, lobname, sitename, self.dbuser, self.dbpassword, sql_coach)
                    Total_coachnumber_database17=Datalist17[0]
                    print "Total_coachnumber_tablet17==Total_coachnumber_database17:",Total_coachnumber_tablet17,Total_coachnumber_database17 
                    #There some error in for Total_coachnumber_database  
                    assert Total_coachnumber_tablet17==Total_coachnumber_database17 
                    
                    #Step3.17:a.Logout and Login tablet with the Agent account that is coached by the  form(TL1/OM1/LC);
                            # b. Click Coaching icon in home page;
                            # c. Status drop-down:Select Completed;
                            # d. Click Filter;
                            # e. Open the  form
                            # F. Try to edit the form. 
                    L.logout_tablet()
                    L.Login_tablet(self.tableturl, lobname, sitename, Agent_hrid, Agent_password)
                    Tablet.click_Agent_coachingcircle()
                    CoachHome.select_status("Completed")
                    CoachHome.click_filterbutton()
                    SN_inAgentCoachHomepage=CoachHome.get_anyCoach_attribute(1, 1)
                    #CoachHome.click_eachcoach(SN_path)
                    CoachHome.click_eachcoach(1)
                    '''Check17:1.This  form record should be in the list
                               2. Enter the  form detail page with title 'Coaching - Accountability Conversation' On this form:1)Status = Completed; 2)Completed Date = The date when the form is completed;3)Acknowledged Date=blank
                               3. 1).The third and the fourth KPIs in checked status.2) Other KPI shown unchecked status.
                               4. Each of other fields content shown correct:SN, Employee Name,EmployeeID, Coaching Name, Create Date,each of text boxes,Date and Time of Call
                               5. There are two buttons: [Acknowledge Coaching] and [Back];
                               6. Agent should not edit the form.(each of field in uneditable status)'''
                    assert SN_inAgentCoachHomepage==SN_Actual
                    assert Header.get_HeaderTittle()==self.coachpagetitle
                    assert BasicInfo.get_status()=="Completed"
                    assert BasicInfo.get_completeddate()==created_time_Actual
                    assert BasicInfo.get_acknowledgedDate()==""
                    assert BasicInfo.get_anyCheckBoxStatus_Agent(2)==self.CheckBox_UnCheckedStatus
                    assert BasicInfo.get_anyCheckBoxStatus_Agent(3)==self.CheckBox_UnCheckedStatus
                    assert BasicInfo.get_anyCheckBoxStatus_Agent(4)==self.CheckBox_CheckedStatus
                    assert BasicInfo.get_anyCheckBoxStatus_Agent(5)==self.CheckBox_CheckedStatus
                    for index in range(6,KPInumber+1):
                        assert BasicInfo.get_anyCheckBoxStatus_Agent(index)==self.CheckBox_UnCheckedStatus
                    assert BasicInfo.get_SN()==SN_coachhomepage
                    assert BasicInfo.get_employeename()==Agent_name
                    assert BasicInfo.get_employeeHrid()==employee_hrid_database
                    assert BasicInfo.get_coachname()==coach_name_Actual
                    assert BasicInfo.get_createdate()==Created_Date_FromServer
                    if lobname != "AOL":
                        assert BasicInfo.get_callrecordingnumber()==call_Recording_Number_new
                    assert DirectSalesQACoachingForm1.select_Discover()=="no"
                    assert DirectSalesQACoachingForm1.select_Transition()=="no"
                    assert DirectSalesQACoachingForm1.select_Pitch()=="no"
                    assert DirectSalesQACoachingForm1.select_Overcome()=="na"
                    assert DirectSalesQACoachingForm1.select_Close()=="yes"
                    assert DirectSalesQACoachingForm1.input_strengths()==Content_InTextBox_new
                    assert DirectSalesQACoachingForm1.input_opportunities1()==Content_InTextBox_new
                    assert DirectSalesQACoachingForm1.input_opportunities2()==Content_InTextBox_new
                    assert DirectSalesQACoachingForm1.input_plan1()==Content_InTextBox_new
                    assert DirectSalesQACoachingForm1.input_plan2()==Content_InTextBox_new

                    assert BasicInfo.get_ButtonName(1)=="Acknowledge Coaching"
                    assert BasicInfo.get_ButtonName(2)=="Back"
                    for index in range(3,6):
                        assert BasicInfo.Button_Displayed(index)==False
                    for index in range(2,KPInumber+1):
                        BasicInfo.click_anyKPIstatusofCheckBox_Agent(index)
                    assert BasicInfo.get_anyCheckBoxStatus_Agent(2)==self.CheckBox_UnCheckedStatus
                    assert BasicInfo.get_anyCheckBoxStatus_Agent(3)==self.CheckBox_UnCheckedStatus
                    assert BasicInfo.get_anyCheckBoxStatus_Agent(4)==self.CheckBox_CheckedStatus
                    assert BasicInfo.get_anyCheckBoxStatus_Agent(5)==self.CheckBox_CheckedStatus
                    for index in range(6,KPInumber+1):
                        assert BasicInfo.get_anyCheckBoxStatus_Agent(index)==self.CheckBox_UnCheckedStatus
                    assert DirectSalesQACoachingForm1.strengths__disabled()=="true"
                    assert DirectSalesQACoachingForm1.opportunities1__disabled()=="true"
                    assert DirectSalesQACoachingForm1.opportunities2__disabled()=="true"
                    assert DirectSalesQACoachingForm1.plan1__disabled()=="true"
                    assert DirectSalesQACoachingForm1.plan2__disabled()=="true"




                    
                    #Step3.18:Click Back button at page bottom.
                    BasicInfo.Click_Button(2)#Click Back button 
                    '''Check18:1.Return to Coaching list page,Status Drop-down :Completed is selected by default. 
                               2.This coaching record is shown by default.
                               3.All completed record coached to this agent are list.'''
                    assert CoachHome.get_status_selected()=="Completed"
                    assert CoachHome.get_anyCoach_attribute(1, 1)==SN_Actual
                    
                    #Step3.18:Open the  form again.
                    #CoachHome.click_eachcoach(SN_path)
                    CoachHome.click_eachcoach(1)
                    '''Check20: 1.The third and the fourth KPIs is shown checked status.
                                2.Other KPI shown unchecked status.'''
                    assert BasicInfo.get_anyCheckBoxStatus_Agent(2)==self.CheckBox_UnCheckedStatus
                    assert BasicInfo.get_anyCheckBoxStatus_Agent(3)==self.CheckBox_UnCheckedStatus
                    assert BasicInfo.get_anyCheckBoxStatus_Agent(4)==self.CheckBox_CheckedStatus
                    assert BasicInfo.get_anyCheckBoxStatus_Agent(5)==self.CheckBox_CheckedStatus
                    for index in range(6,KPInumber+1):
                        assert BasicInfo.get_anyCheckBoxStatus_Agent(index)==self.CheckBox_UnCheckedStatus
                        
                    #Step3.19:Click "Acknowledge Coaching" button;
                    BasicInfo.Click_Button(1)#click_AcknowledgeCoachingButton
                    Acknowledge_Date_FromServer=GetConfig.get_ServerCurrentDate().replace("-","/")
                    total_PageandCoachnumber_tablet_Dic21=CoachPublic.get_Total_PageandCoachnumber()
                    Total_coachnumber_tablet21=total_PageandCoachnumber_tablet_Dic21['Total_coachnumber_tablet']
                    hr_id=Agent_hrid
                    sql_coach="select * from coach  where  hr_id="+hr_id+"  and classification=0 and status=1 order by id desc"
                    Datalist21=HMysql.Get_datafromDB(self.hostindex, lobname, sitename, self.dbuser, self.dbpassword, sql_coach)
                    Total_coachnumber_database21=Datalist21[0]
                    '''Check19:1.Return to Coaching list page,Status Drop-down: Completed is selected by default.
                               2.The coaching record is not shown in default list.
                               3.On search main page,all completed record coached to this agent are list.'''
                    assert CoachHome.get_status_selected()=="Completed"
                    assert CoachHome.get_anyCoach_attribute(1, 1)!=SN_Actual
                    print "Total_coachnumber_tablet21==Total_coachnumber_database21:",Total_coachnumber_tablet21,Total_coachnumber_database21
                    assert Total_coachnumber_tablet21==Total_coachnumber_database21
                    
                    #Step3.19: 2.Status Drop-down:Select Status = Acknowledged;
                            #3.Click Filter;
                            #4.Open the  form again;
                            #5.Try to edit the  form.
                    CoachHome.select_status("Acknowledged")
                    CoachHome.click_filterbutton()
                    #CoachHome.click_eachcoach(SN_path)
                    CoachHome.click_eachcoach(1)
                    '''Check19:On this  form:
                               1.Status = Acknowledged;
                               2.Completed Date = The date when the form is completed;
                               3.Acknowledged Date = The date when the form is acknowledged.
                               4.The third and the fourth KPIs in checked status;
                               5.Other KPI shown unchecked status.
                               6.Each of other fields content shown correct:SN, Employee Name,EmployeeID, Coaching Name, Create Date,each of text boxes,dates;
                               7.At the page bottom: only one button Back;
                               8.Agent cannot edit the form.(each of fields in uneditable status)'''
                    assert BasicInfo.get_status()=="Acknowledged"
                    assert BasicInfo.get_completeddate()==Completed_Date_FromServer
                    assert BasicInfo.get_acknowledgedDate()==Acknowledge_Date_FromServer
                    assert BasicInfo.get_anyCheckBoxStatus_Agent(2)==self.CheckBox_UnCheckedStatus
                    assert BasicInfo.get_anyCheckBoxStatus_Agent(3)==self.CheckBox_UnCheckedStatus
                    assert BasicInfo.get_anyCheckBoxStatus_Agent(4)==self.CheckBox_CheckedStatus
                    assert BasicInfo.get_anyCheckBoxStatus_Agent(5)==self.CheckBox_CheckedStatus
                    for index in range(6,KPInumber+1):
                        assert BasicInfo.get_anyCheckBoxStatus_Agent(index)==self.CheckBox_UnCheckedStatus
                    assert BasicInfo.get_SN()==SN_coachhomepage
                    assert BasicInfo.get_employeename()==Agent_name
                    assert BasicInfo.get_employeeHrid()==employee_hrid_database
                    assert BasicInfo.get_coachname()==coach_name_Actual
                    assert BasicInfo.get_createdate()==Created_Date_FromServer
                    if lobname != "AOL":
                        assert BasicInfo.get_callrecordingnumber()==call_Recording_Number_new
                    assert DirectSalesQACoachingForm1.select_Discover()=="no"
                    assert DirectSalesQACoachingForm1.select_Transition()=="no"
                    assert DirectSalesQACoachingForm1.select_Pitch()=="no"
                    assert DirectSalesQACoachingForm1.select_Overcome()=="na"
                    assert DirectSalesQACoachingForm1.select_Close()=="yes"
                    assert DirectSalesQACoachingForm1.input_strengths()==Content_InTextBox_new
                    assert DirectSalesQACoachingForm1.input_opportunities1()==Content_InTextBox_new
                    assert DirectSalesQACoachingForm1.input_opportunities2()==Content_InTextBox_new
                    assert DirectSalesQACoachingForm1.input_plan1()==Content_InTextBox_new
                    assert DirectSalesQACoachingForm1.input_plan2()==Content_InTextBox_new

                    assert BasicInfo.get_ButtonName(1)=="Back"
                    for index in range(2,6):
                        assert BasicInfo.Button_Displayed(index)==False   
                    for index in range(2,KPInumber+1):
                        BasicInfo.click_anyKPIstatusofCheckBox_Agent(index)
                    assert BasicInfo.get_anyCheckBoxStatus_Agent(2)==self.CheckBox_UnCheckedStatus
                    assert BasicInfo.get_anyCheckBoxStatus_Agent(3)==self.CheckBox_UnCheckedStatus
                    assert BasicInfo.get_anyCheckBoxStatus_Agent(4)==self.CheckBox_CheckedStatus
                    assert BasicInfo.get_anyCheckBoxStatus_Agent(5)==self.CheckBox_CheckedStatus
                    for index in range(6,KPInumber+1):
                        assert BasicInfo.get_anyCheckBoxStatus_Agent(index)==self.CheckBox_UnCheckedStatus
                    assert DirectSalesQACoachingForm1.strengths__disabled()=="true"
                    assert DirectSalesQACoachingForm1.opportunities1__disabled()=="true"
                    assert DirectSalesQACoachingForm1.opportunities2__disabled()=="true"
                    assert DirectSalesQACoachingForm1.plan1__disabled()=="true"
                    assert DirectSalesQACoachingForm1.plan2__disabled()=="true"
                    #Step3.19:6.Click BACK button at page button.
                    BasicInfo.Click_Button(1)#Back to coaching home page
                    total_PageandCoachnumber_tablet_Dic23=CoachPublic.get_Total_PageandCoachnumber()
                    Total_coachnumber_tablet23=total_PageandCoachnumber_tablet_Dic23['Total_coachnumber_tablet']
                    hr_id=Agent_hrid
                    sql_coach="select * from coach  where  hr_id="+hr_id+"  and classification=0 and status=4 order by id desc"
                    Datalist23=HMysql.Get_datafromDB(self.hostindex, lobname, sitename, self.dbuser, self.dbpassword, sql_coach)
                    Total_coachnumber_database23=Datalist23[0]
                    '''Check19:Return to Coaching list page
                               1.Status Drop-down: Acknowledged is selected by default.
                               2.The coaching record is shown in default list.
                               3.On search main page,all  acknowledged record coached to this agent are list.'''
                    assert CoachHome.get_status_selected()=="Acknowledged"
                    assert CoachHome.get_anyCoach_attribute(1, 1)==SN_coachhomepage
                    print "Total_coachnumber_tablet23==Total_coachnumber_database23:",Total_coachnumber_tablet23,Total_coachnumber_database23
                    assert Total_coachnumber_tablet23==Total_coachnumber_database23
                    
                    #Step3.20:1.Logout and Login tablet with TL1/OM1/LC account that added the  form;
                            # 2.Click Coaching icon;
                            # 3.Select Status = Acknowledged;
                            # 4.Click Filter;
                            # 5.Open the  form.
                            # 6.Try to edit the  form.
                    L.logout_tablet()
                    L.Login_tablet(self.tableturl, lobname, sitename, self.OMuserid, self.OMpassword)
                    Tablet.click_coachingcircle()
                    CoachHome.select_status("Acknowledged")
                    CoachHome.click_filterbutton()
                    SN_inAcknowledgedList=CoachHome.get_anyCoach_attribute(1, 1)
                    #CoachHome.click_eachcoach(SN_path)
                    CoachHome.click_eachcoach(1)
                    '''Check20:1.The  form is searched out with status shown 'acknowledged ';
                               2.Enter the  form detail page with title 'Coaching - Commendation';
                               3.Status = Acknowledged;
                               4.Completed Date = The date when the form is completed;
                               5.Acknowledged Date = The date when the form is acknowledged.
                               6.At page bottom, only two button shown: Print and BACK.
                               7.The form cannot be edited.(each of fields in uneditable status.)'''
                    assert SN_inAcknowledgedList==SN_coachhomepage
                    assert Header.get_HeaderTittle()==self.coachpagetitle
                    assert BasicInfo.get_status()=="Acknowledged"
                    assert BasicInfo.get_completeddate()==Completed_Date_FromServer
                    assert BasicInfo.get_acknowledgedDate()==Acknowledge_Date_FromServer
                    assert BasicInfo.get_ButtonName(1)=="Print"
                    assert BasicInfo.get_ButtonName(2)=="Back"
                    for index in range(3,6):
                        assert BasicInfo.Button_Displayed(index)==False
                    for index in range(2,KPInumber+1):
                        BasicInfo.click_anyKPIstatusofCheckBox(index)
                    assert BasicInfo.get_anyCheckBoxStatus(2)==self.CheckBox_UnCheckedStatus
                    assert BasicInfo.get_anyCheckBoxStatus(3)==self.CheckBox_UnCheckedStatus
                    assert BasicInfo.get_anyCheckBoxStatus(4)==self.CheckBox_CheckedStatus
                    assert BasicInfo.get_anyCheckBoxStatus(5)==self.CheckBox_CheckedStatus
                    for index in range(6,KPInumber+1):
                        assert BasicInfo.get_anyCheckBoxStatus(index)==self.CheckBox_UnCheckedStatus
                    assert DirectSalesQACoachingForm1.strengths__disabled()=="true"
                    assert DirectSalesQACoachingForm1.opportunities1__disabled()=="true"
                    assert DirectSalesQACoachingForm1.opportunities2__disabled()=="true"
                    assert DirectSalesQACoachingForm1.plan1__disabled()=="true"
                    assert DirectSalesQACoachingForm1.plan2__disabled()=="true"
                    
                    #Step3.21:Click button 'Print'.
                    #BasicInfo.Click_Button(1)#click print button
                    '''Check25:Print preview window is shown.'''#Need more time to do research
                    
                L.logout_tablet()
                    
                GetConfig.print_EndTest_message(lobname, sitename)    
                    

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()