'''
Created on Aug 2, 2017

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
from Tablet_pages.CancelCoachingWindow import CancelCoachingWindow



class SalesWeeklyPerformanceReviewForm_PlannedToAcknowledged_OMLC(unittest.TestCase):


    def setUp(self):
        #Case ID
        self.caseID="SalesWeeklyPerformanceReviewForm_PlannedToAcknowledged_OMLC"
        
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
        self.dbuser=GetData.get_StageDatabaseUser()
        self.dbpassword=GetData.get_StageDatabasePassword()
        #Get coachpopuptittle
        self.title=GetData.get_AddCoachingFormTitle()
        #coaching or Triad coaching
        self.coachtype="triad coaching"  
        #Coachformname
        self.coachhometitle="Triad Coaching"
        self.coachformname="Sales Weekly Performance Review Form" 
        self.coachpagetitle="Triad Coaching - "+self.coachformname
        
        self.KPIbox_title="Coaching KPIs(%s):"
        
        self.CheckBox_CheckedStatus="fa fa-check-square"
        self.CheckBox_UnCheckedStatus="fa fa-uncheck"
        
        #Cancel window info
        self.CancelWindow_title="Confirmation"
        self.CancelWindow_content="Please confirm you want to cancel this To-Do!"


    def tearDown(self):
        pass


    def test_SalesWeeklyPerformanceReviewForm_PlannedToAcknowledged_OM(self):
        UserRole="OM"
        self.SalesWeeklyPerformanceReviewForm_PlannedToAcknowledged(self.OMuserid, self.OMpassword, UserRole)
    def test_SalesWeeklyPerformanceReviewForm_PlannedToAcknowledged_LC(self):
        pass
    
    def SalesWeeklyPerformanceReviewForm_PlannedToAcknowledged(self,userid,password,UserRole):
        GetConfig=Get_configration_data()
        Tablet=TabletHomepage()
        Ppage=PerformancePage()
        TCoach=Coach_Triad_General()
        CoachHome=Coachinghomepage()
        BasicInfo=BasicInfoforCoaching()
        CoachPublic=Coaching_PublicFunction()
        Header=HeaderPage()
        SWPR=SalesWeeklyPerformanceReviewForm()
        Getaccount=Get_AllRoleAccountForTest()
        CancelWindow=CancelCoachingWindow()
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
                   
                    #Step0:Login tablet,and Get TLInfo using for testing
                    TLInfo_Dic=Getaccount.get_TLInfoandAgentHridFromPerformance(self.tableturl, lobname, sitename, self.OMuserid, self.OMpassword,"Month-To-Date")
                    TL_Name=TLInfo_Dic["TLName"]
                    TL_hrid=TLInfo_Dic["TLHrid"]
                    TL_password=TLInfo_Dic["TLPassword"]
                    
                    
                    #Step1:  1. Login with an OM/LC account;
                            #2. Enter performance module->Select an TL->select first three KPs to add this form 
                            #3. Enter triad Coaching list page.
                            #4. Click the  form in coaching list.
                    L=Login()
                    L.Login_tablet(self.tableturl,lobname,sitename,userid,password)
                    time.sleep(Gl.waittime)
                    GetConfig.print_StartTest_message(lobname, sitename)
                    
                    LoginName=Header.get_loginName()
                    Tablet.click_performancecircle()
                    
                    print "Start=====Monthly-To-Day is in testing",
                    Ppage.select_Agentkpi()
                    Ppage.unselect_Agentkpi()
                    if lobname in Gl.DoubleKPIname_lob:
                        KPInumber=Ppage.get_KPInumber_All()
                    else:
                        KPInumber=Ppage.get_KPInumber()
                    KPIname_FromPerformancePage_list=Ppage.get_KPIname_list(KPInumber)
                    KPIofGoal_FromPerformancePage_list=Ppage.get_AllKPIsofGoal_list(KPInumber)
                    KPIofSite_FromPerformancePage_list=Ppage.get_AllKPIsofSite_list(KPInumber)
                    KPIofTL_FromPerformancePage_list=Ppage.get_AllKPIsofTL_list(KPInumber)  
                    
                    if lobname in Gl.performancefor_MultiTimeTab_lob:
                        Ppage.click_timetab_performance(5)
                        timetab_text=Ppage.get_timetab_text_performance(5)
                    else:
                        Ppage.click_timetab_performance(3)
                        timetab_text=Ppage.get_timetab_text_performance(3)
                    Ppage.select_AnyKpiOfTL(4)#select first three KPs to add this form
                    Ppage.click_addTriadcoachbutton()
                    TCoach.Add_AnyCoachOrTriad(self.coachformname)
                    Created_Date_FromServer=GetConfig.get_ServerCurrentDate().replace("-","/")
                    Header.click_backbutton()
                    Tablet.click_Triadcoachingcirecle()
                    SN_CoachHome=CoachHome.get_anyCoach_attribute(1, 1)
                    '''Check1:1.The newly added record should be automatically shown in search result list page.
                              2.Enter this form detail page.'''
                    assert CoachHome.get_anyCoach_attribute(1, 5)==self.coachformname
                    assert CoachHome.get_anyCoach_attribute(1, 7)==Created_Date_FromServer
                    SN_name_list=SN_CoachHome.split("-")
                    assert len(SN_name_list)==4
                    
                    CoachHome.click_eachcoach(1)
                    #Step2: 5.Check all the following contents on this detail page:
                            #1) Page title,logged-in user info
                            
                    '''Check2: 1.Page title :'Triad Coaching - Sales Weekly Performance Review Meeting'.
                                  Shown logged-in User info as folllows:
                                    Antonette Corpus (OM/LC)
                                      DTVDS, YOUNGSTOWN'''
                    assert Header.get_HeaderTittle()==self.coachpagetitle
                    assert Header.get_loginLob()==lobname
                    assert Header.get_loginSite()==sitename
                    assert Header.get_loginName()==BasicInfo.get_coachname()
                    assert Header.get_loginRole()==UserRole
                    
                    #Step2:2)Basic information section.
                            #[SN, Employee Name, Employee HRID, Status, Coaching Name, Call Recording Number, Create Date, Completed Date, Acknowledged Date]
                    
                    '''Check2:2.The data of SN, Employee Name,  Employee HRID, Coaching Name, Create Date are correct;
                                Status is "Planned";
                                Call Recording Number, Completed Date and Acknowledged Date are blank'''
                    assert BasicInfo.get_SN()==SN_CoachHome
                    assert BasicInfo.get_employeename()==TL_Name
                    assert BasicInfo.get_employeeHrid()==TL_hrid
                    assert BasicInfo.get_coachname()==LoginName
                    assert BasicInfo.get_status()=="Planned"
                    assert BasicInfo.get_createdate()==Created_Date_FromServer
                    assert BasicInfo.get_completeddate()==""
                    assert BasicInfo.get_acknowledgedDate()==""
                    if lobname !="AOL":
                        assert BasicInfo.get_callrecordingnumber()==""
                    
                    #Step2:3) Check Coaching KPIs (Month to Date) section
                            #[Coaching forms added at Performance page with Month-to-Date table selected]
                    '''Check2:3.Show header name 'Coaching KPIs(Month-To-Date)'
                                 All KPI data of Goal, Site,TL should be the same as those on the corresponding performance page.
                                 The first three KPIs are checked by default.'''  
                    assert BasicInfo.get_KPIboxTitle()==self.KPIbox_title % timetab_text
                    assert BasicInfo.get_KPIofGoal_list(KPInumber)==KPIofGoal_FromPerformancePage_list
                    assert BasicInfo.get_KPIofSite_list(KPInumber)==KPIofSite_FromPerformancePage_list
                    assert BasicInfo.get_KPIofTeam_list(KPInumber)==KPIofTL_FromPerformancePage_list
                    for index in range(2,5):
                        assert BasicInfo.get_anyCheckBoxStatus(index)==self.CheckBox_CheckedStatus
                    for index in range(5,KPInumber+1):
                        assert BasicInfo.get_anyCheckBoxStatus(index)==self.CheckBox_UnCheckedStatus
                        
                    #Step3:6) Other sections:
                    '''Check3:1)  All content should be shown the same as UI design.
                                  'Week1' section: is editable.
                                  'WEEK ENDING 1' section: 
                                   is editable
                                   Two buttons 'Save','OM Sign'  or 'LC Sign' '''
                    METRICnumber=SWPR.Get_METRICnumber()
                    for METRICindex in range(1,METRICnumber+1):
                        assert SWPR.anyMETRICOfanyWeekOrmonthly_disabled(METRICindex, 2)==None 
                    for QuestionNumber in range(1,6):
                        assert SWPR.AnyQuestionsOfAnyWeekEnding_disabled(QuestionNumber, 1)==None 
                    assert SWPR.Get_ButtonNameOfAnyWeekEnding(1, 1)=="Save"
                    assert SWPR.anyButtonOfAnyWeekEnding_disabled(1, 1)==None #Save button is enabled
                    if UserRole=="OM":
                        assert SWPR.Get_ButtonNameOfAnyWeekEnding(1, 2)=="OM Sign"
                    elif UserRole=="LC":
                        assert SWPR.Get_ButtonNameOfAnyWeekEnding(1, 2)=="LC Sign"
                    assert SWPR.anyButtonOfAnyWeekEnding_disabled(1, 2)!="true" #Sign button is enabled   
                    '''Check3:2) Following sectinos are uneditable:
                                 WEEK2-WEEK5, MONTHLY PERFORMANCE RESULTS.
                                 WEEK ENDING2- WEEK ENDING 5
                                 Under each section of WEEK ENDING2- WEEK ENDING 5:
                                      1) Show two buttons 'Save', 'OM Sign' , but disabled.
                                      2) If create by LC, show  button: 'save' , 'LC sign' ,but disabled.'''   
                    for METRICindex in range(1,METRICnumber+1):#WEEK2-WEEK5, MONTHLY PERFORMANCE RESULTS sectinos are uneditable
                        assert SWPR.anyMETRICOfanyWeekOrmonthly_disabled(METRICindex, 3)=="true"  
                        assert SWPR.anyMETRICOfanyWeekOrmonthly_disabled(METRICindex, 4)=="true"
                        assert SWPR.anyMETRICOfanyWeekOrmonthly_disabled(METRICindex, 5)=="true"
                        assert SWPR.anyMETRICOfanyWeekOrmonthly_disabled(METRICindex, 6)=="true"  
                        assert SWPR.anyMETRICOfanyWeekOrmonthly_disabled(METRICindex, 7)=="true"  
                    for QuestionNumber in range(1,6):#Under each section of WEEK ENDING2- WEEK ENDING 5 are uneditable
                        assert SWPR.AnyQuestionsOfAnyWeekEnding_disabled(QuestionNumber, 2)=="true"
                        assert SWPR.AnyQuestionsOfAnyWeekEnding_disabled(QuestionNumber, 3)=="true"
                        assert SWPR.AnyQuestionsOfAnyWeekEnding_disabled(QuestionNumber, 4)=="true"
                        assert SWPR.AnyQuestionsOfAnyWeekEnding_disabled(QuestionNumber, 5)=="true"
                    for WeekEndingIndex in range(2,6):
                        assert SWPR.Get_ButtonNameOfAnyWeekEnding(WeekEndingIndex, 1)=="Save"
                        assert SWPR.anyButtonOfAnyWeekEnding_disabled(WeekEndingIndex, 1)=="true" #Save button is uneditable
                        if UserRole=="OM":
                            assert SWPR.Get_ButtonNameOfAnyWeekEnding(WeekEndingIndex, 2)=="OM Sign"
                        elif UserRole=="LC":
                            assert SWPR.Get_ButtonNameOfAnyWeekEnding(WeekEndingIndex, 2)=="LC Sign"
                            assert SWPR.anyButtonOfAnyWeekEnding_disabled(WeekEndingIndex, 2)=="true" #Sign button is uneditable   
                    '''Check3:3) Page bottom showing five buttons: 
                                 Print, 
                                 Save and Continue Later,
                                 Complete Coaching (disabled), 
                                 Cancel Coaching, 
                                 Quit Without Save'''
                    assert BasicInfo.get_ButtonName(1)=="Print"
                    assert BasicInfo.get_ButtonName(2)=="Save and Continue Later"
                    assert BasicInfo.get_ButtonName(3)=="Complete Coaching"
                    assert BasicInfo.get_ButtonName(4)=="Cancel Coaching"
                    assert BasicInfo.get_ButtonName(5)=="Quit Without Save"
                    for index in range(1,6):
                        if index==3:
                            assert BasicInfo.Button_disabled(3)=="true"#Complete Coaching (disabled)
                        else:
                            assert BasicInfo.Button_disabled(index)==None
                            
                    #Step4:Click "Quit without Saving"
                    BasicInfo.Click_Button(5)
                    total_PageandCoachnumber_tablet_Dic1=CoachPublic.get_Total_PageandCoachnumber()
                    Total_coachnumber_tablet1=total_PageandCoachnumber_tablet_Dic1['Total_coachnumber_tablet']
                    #Connect database to get data
                    database_name=lobname.lower()+'_'+sitename.lower().replace("-","")   
                    conn=MySQLdb.connect(self.host,self.dbuser,self.dbpassword,database_name)
                    cursor=conn.cursor()
                    conn.autocommit(True)
                    sql_coach1="select * from coach  where  assign_to_id="+userid+"  and classification=1 and status in (0,3) order by id desc"
                    Total_coachnumber_database1=cursor.execute(sql_coach1)
                    '''Check4:Return to Coaching list page
                                1)All incompleted triad coaching is listed.
                                2)On search fields section:
                                   CoachingName=OM(logged-in)
                                   EmployeeName=All
                                   Status=Incompleted.
                                   Type=All
                                3)This coach record is shown by default  with  status 'Planned' '''
                    assert CoachHome.get_CoachName()==LoginName
                    assert CoachHome.get_EmployeeName()=="All"
                    assert CoachHome.get_status_selected()=="Incompleted"
                    assert CoachHome.get_typename_selected()=="All"
                    assert Total_coachnumber_tablet1==Total_coachnumber_database1
                    assert CoachHome.get_anyCoach_attribute(1, 1)==SN_CoachHome
                    assert CoachHome.get_anyCoach_attribute(1, 6)=="Planned"
                    
                    #Step5: Select the SWPRM form to enter the detail page again.
                    CoachHome.click_eachcoach(1)
                    '''Check5:1.Enter this form detail page with title 'Triad Coaching - Sales Weekly Performance Review Form' 
                              2.The data of SN, Employee Name,EmployeeID, Coaching Name, Create Date are correct;
                                  Status is "Planned";
                                  Completed Date and Acknowledged Date are blank
                              3.All KPI data of Goal, Site,TL should be the same as those on the corresponding performance page.
                              4.The first three KPIs are checked by default.'''
                    assert Header.get_HeaderTittle()==self.coachpagetitle
                    assert BasicInfo.get_SN()==SN_CoachHome
                    assert BasicInfo.get_employeename()==TL_Name
                    assert BasicInfo.get_employeeHrid()==TL_hrid
                    assert BasicInfo.get_coachname()==LoginName
                    assert BasicInfo.get_status()=="Planned"
                    assert BasicInfo.get_createdate()==Created_Date_FromServer
                    assert BasicInfo.get_completeddate()==""
                    assert BasicInfo.get_acknowledgedDate()==""
                    if lobname !="AOL":
                        assert BasicInfo.get_callrecordingnumber()==""
                    assert BasicInfo.get_KPIofGoal_list(KPInumber)==KPIofGoal_FromPerformancePage_list
                    assert BasicInfo.get_KPIofSite_list(KPInumber)==KPIofSite_FromPerformancePage_list
                    assert BasicInfo.get_KPIofTeam_list(KPInumber)==KPIofTL_FromPerformancePage_list
                    for index in range(2,5):
                        assert BasicInfo.get_anyCheckBoxStatus(index)==self.CheckBox_CheckedStatus
                    for index in range(5,KPInumber+1):
                        assert BasicInfo.get_anyCheckBoxStatus(index)==self.CheckBox_UnCheckedStatus
                    #Step6:8.Input content in following editable fields:
                                #1)  a. Uncheck the third KPI,
                                    #b.  Check the fouth KPI.;
                                #2)input call Recording Number
                    BasicInfo.click_anyKPIstatusofCheckBox(4)
                    BasicInfo.click_anyKPIstatusofCheckBox(5)
                    
                    
                          
                      
                


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()