'''
Created on 20171211

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
from CoachingAndTriadCoaching_Pages.DirectSalesQACoachingForm import DirectSalesQACoachingForm
from public_method.Coaching_PublicFunction import Coaching_PublicFunction
from Tablet_pages.HeaderPage import HeaderPage
from public_method.Get_AllRoleAccountForTest import Get_AllRoleAccountForTest
from Tablet_pages.CancelCoachingWindow import CancelCoachingWindow


class DirectSalesQACoachingForm_PlannedToCompleted(unittest.TestCase):


    def setUp(self):
        #Case ID
        self.caseID="DirectSalesQACoachingForm_PlannedToCompleted"
        
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
        #Get FormCommonParameter
        FormCommonParameter_Dic=GetData.get_FormCommonParameter()
        self.CallRecordingNumber1=FormCommonParameter_Dic["CallRecordingNumber1"]
        self.CallRecordingNumber2=FormCommonParameter_Dic["CallRecordingNumber2"]
        self.Shorttextboxesprefix1=FormCommonParameter_Dic["Shorttextboxesprefix1"]
        self.Shorttextboxesprefix2=FormCommonParameter_Dic["Shorttextboxesprefix2"]
        self.Longtextboxesprefix1=FormCommonParameter_Dic["Longtextboxesprefix1"]
        self.Longtextboxesprefix2=FormCommonParameter_Dic["Longtextboxesprefix2"]
        
        #coaching or Coaching
        self.coachtype="Coaching"  
        #Coachformname
        self.coachhometitle="Coaching"
        self.coachformname="Direct Sales QA/Coaching Form" 
        self.coachpagetitle="Coaching - "+self.coachformname
        
        self.CheckBox_CheckedStatus="fa fa-check-square"
        self.CheckBox_UnCheckedStatus="fa fa-uncheck"
        self.checkstatus="fa fa-check-circle radio-btn checked"
        self.uncheckstatus="fa fa-check-circle radio-btn"
        
        #Cancel window info
        self.CancelWindow_title="Confirmation"
        self.CancelWindow_content="Please confirm you want to cancel this To-Do!"


    def test_DirectSalesQACoachingForm_PlannedToCompleted(self):
        GetConfig=Get_configration_data()
        Tablet=TabletHomepage()
        Ppage=PerformancePage()
        TCoach=Coach_Triad_General()
        CoachHome=Coachinghomepage()
        BasicInfo=BasicInfoforCoaching()
        Header=HeaderPage()
        DirectSalesQACoachingForm1=DirectSalesQACoachingForm()
        Getaccount=Get_AllRoleAccountForTest()
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
                    AgentInfo_Dic=Getaccount.get_AgentInfoFromTablet(self.tableturl, lobname, sitename, self.OMuserid, self.OMpassword,"Month-To-Date")
                    Agent_name=AgentInfo_Dic["AgentName"]
                    Agent_hrid=AgentInfo_Dic["AgentHrid"]
                    Agent_password=AgentInfo_Dic["AgentPassword"]
                    L=Login()
                    L.Login_tablet(self.tableturl,lobname,sitename,self.OMuserid,self.OMpassword)
                    time.sleep(Gl.waittime)
                    #Step2:1. Login with LC/OM  account to enter performance dashboard Month-To-Date page.

                    Tablet.click_performancecircle()
                   
                    #Step3:2. Select one TL ->select the first KPI to add this form;
                    print "Start=====Monthly-To-Day is in testing",
                    Ppage.select_Agentkpi()
                    Ppage.unselect_Agentkpi()
                    if lobname in Gl.DoubleKPIname_lob:
                        KPInumber=Ppage.get_KPInumber_All()
                    else:
                        KPInumber=Ppage.get_KPInumber()
                    
                    if lobname in Gl.performancefor_MultiTimeTab_lob:
                        Ppage.click_timetab_performance(5)#Ppage.click_mtd()
                    else:    
                        Ppage.click_timetab_performance(3)#Ppage.click_mtd()
                    Ppage.select_AnyKpiOfAgent_OM(2)#select the first KPI
                    Ppage.click_addcoachbutton()
                    TCoach.Add_AnyCoachOrTriad(self.coachformname)
                    Created_Date_FromServer=GetConfig.get_ServerCurrentDate().replace("-","/")
                    #Step4: #a.Enter coaching module.
                            #b.Select this coaching record to enter form detail page.
                    Header.click_backbutton()
                    Tablet.click_coachingcircle()
                    SN_CoachHome=CoachHome.get_anyCoach_attribute(1, 1)
                   
                    CoachHome.click_eachcoach(1)
                    '''Check1:Enter form detail page with title Triad Coaching - Commendation'''
                    assert Header.get_HeaderTittle()==self.coachpagetitle
                    
                    #Step5:  4. Logout and login the TL  who is coached in this form;
                            #5. Enter triad Coach module.
                            #6. Select this coaching record to open this form detail page.
                            #7. Try to edit the form
                    L.logout_tablet()
                    L.Login_tablet(self.tableturl, lobname, sitename, Agent_hrid, Agent_password)
                    Tablet.click_Agent_coachingcircle()
                    #MonthlyGoalSettingAgentForm.click_CoachName()
                    #MonthlyGoalSettingAgentForm.click_CoachNameselect()
                    CoachHome.click_filterbutton()
                    SN_Actual=CoachHome.get_anyCoach_attribute(1, 1)
                    CoachHome.click_eachcoach(1)
                    '''Check2:1.This coaching record is shown by default.
                              2.TL cannot edit the form.(each of fields is uneditable)'''
                    assert SN_Actual==SN_CoachHome
                    if lobname != "AOL":
                        assert BasicInfo.callrecordingnumber_disabled()=="true"
                    
                    #assert DirectSalesQACoachingForm1.discover_disabled(1, 2)=="true"
                    #assert DirectSalesQACoachingForm1.transition_disabled(1, 2)=="true"
                    #assert DirectSalesQACoachingForm1.pitch_disabled(4, 2)=="true"
                    #assert DirectSalesQACoachingForm1.overcome_disabled(1)=="true"
                    #assert DirectSalesQACoachingForm1.close_disabled(2, 2)=="true"
                    assert DirectSalesQACoachingForm1.strengths__disabled()=="true"
                    assert DirectSalesQACoachingForm1.opportunities1__disabled()=="true"
                    assert DirectSalesQACoachingForm1.opportunities2__disabled()=="true" 
                    assert DirectSalesQACoachingForm1.plan1__disabled()=="true" 
                    assert DirectSalesQACoachingForm1.plan2__disabled()=="true"

                    
                    
                    
                    #Step6:8.logout->login with creater LC/OM.
                            #9.Enter triad coaching module to enter this coaching record detail page.
                            #10.Input value in all editable fileds with following content:
                                #1) CallRecordingNumber:test_number!~@#$%^&*()
                                #1) CallRecordingID:callRecordingID_001&002
                                #2) Date and Time of Call: select yesterday.
                                #3) Check the last KPIs achievement.
                                            #Uncheck the first KPI.
                                #4) Text box: Performance pro test team to input content in text boxes ,alice_shu0823~!@#$%^&*();:'"?/\[]{},sabrina's@symbio.com.
                                #11.Click button 'Complete coaching'.
                                #12.On search main page, search with status option 'completed'.
                    L.logout_tablet()
                    L.Login_tablet(self.tableturl,lobname,sitename,self.OMuserid,self.OMpassword)
                    Tablet.click_coachingcircle()
                    CoachHome.click_eachcoach(1)
                    CallRecordingNumber=self.CallRecordingNumber1
                    #GoalPeriod=self.Shorttextboxesprefix1+MonthlyGoalSettingAgentForm.get_GoalPeriodBoxTitle
                    
                    
                    strengths=self.Longtextboxesprefix1+DirectSalesQACoachingForm1.get_strengthsBoxTitle()
                    opportunities1=self.Longtextboxesprefix1+DirectSalesQACoachingForm1.get_opportunities1BoxTitle()
                    opportunities2=self.Longtextboxesprefix1+DirectSalesQACoachingForm1.get_opportunities2BoxTitle()
                    plan1=self.Longtextboxesprefix1+DirectSalesQACoachingForm1.get_plan1BoxTitle()
                    plan2=self.Longtextboxesprefix1+DirectSalesQACoachingForm1.get_plan2BoxTitle()
                       


                    if lobname != "AOL":
                        BasicInfo.input_callrecordingnumber(CallRecordingNumber)
                    a1=0
                    while a1<5:
                        a1=a1+1
                        DirectSalesQACoachingForm1.select_discover(a1, 1)
                    b1=0
                    while b1<2:
                        b1=b1+1
                        DirectSalesQACoachingForm1.select_transition(b1, 1)
                    c1=0
                    while c1<8:
                        c1=c1+1
                        DirectSalesQACoachingForm1.select_pitch(c1, 1)    
                    d1=0
                    while d1<3:
                        d1=d1+1
                        DirectSalesQACoachingForm1.select_close(d1, 3)     
                     
                  
                    #DirectSalesQACoachingForm1.select_discover(1, 1)
                    #DirectSalesQACoachingForm1.select_transition(1, 1)
                    #DirectSalesQACoachingForm1.select_pitch(1, 1)
                    DirectSalesQACoachingForm1.select_overcome(2)
                    #DirectSalesQACoachingForm1.select_close(1, 3)
                    
                    DirectSalesQACoachingForm1.input_strengths(strengths)
                    DirectSalesQACoachingForm1.input_opportunities1(opportunities1)
                    DirectSalesQACoachingForm1.input_opportunities2(opportunities2)
                    DirectSalesQACoachingForm1.input_plan1(plan1)
                    DirectSalesQACoachingForm1.input_plan2(plan2)
                    

                    
                    BasicInfo.click_anyKPIstatusofCheckBox(KPInumber) #Check the last KPIs achievement.
                    BasicInfo.click_anyKPIstatusofCheckBox(2)#Uncheck the first KPI.
                    BasicInfo.Click_Button(3)
                    Completed_Date_FromServer=GetConfig.get_ServerCurrentDate().replace("-","/")
                    CoachHome.select_status("Completed")
                    CoachHome.click_filterbutton()
                    '''Check3:2.Automatically back to search main page.
                              3.This coaching record is search out with completed status shown.'''
                    assert Header.get_HeaderTittle()==self.coachhometitle
                    assert CoachHome.get_anyCoach_attribute(1, 1)==SN_CoachHome
                    
                    #Step7:13.Enter this form detail page.
                    CoachHome.click_eachcoach(1)
                    '''Check4:13.On this Commendation form:
                                1)  Status of the form is Completed;
                                2)  Completed Date =The date when the form is completed
                                3)   Acknowledged Date is blank.
                                4) Following KPIs in checked status: 
                                                the last KPIs.
                                5) Other KPI shown unchecked status.
                                6)  Each of other fields shown correct:
                                  SN, Employee Name,EmployeeID, Coaching Name, Create Date
                                  each of text boxes
                                  Call Recording Number 
                                Noted:CallRecordingNumber is not in AOL LOB.
                                7)  At page bottom: There are only two buttons: Print and Back'''
                    assert BasicInfo.get_status()=="Completed"
                    assert BasicInfo.get_completeddate()==Completed_Date_FromServer
                    assert BasicInfo.get_acknowledgedDate()==""
                    assert BasicInfo.get_anyCheckBoxStatus(KPInumber)==self.CheckBox_CheckedStatus
                    for index in range(2,KPInumber):
                        assert BasicInfo.get_anyCheckBoxStatus(index)==self.CheckBox_UnCheckedStatus
                    assert BasicInfo.get_SN()==SN_CoachHome
                    assert BasicInfo.get_employeename()==Agent_name
                    assert BasicInfo.get_employeeHrid()==Agent_hrid
                    assert BasicInfo.get_coachname()==Header.get_loginName()
                    assert BasicInfo.get_createdate()==Created_Date_FromServer
                    if lobname != "AOL":
                        assert BasicInfo.get_callrecordingnumber()==CallRecordingNumber
                    #assert MonthlyGoalSettingAgentForm.get_GoalPeriod==GoalPeriod
                   
                    
                    #assert DirectSalesQACoachingForm1.get_discovertatus(1, 1)==self.checkstatus
                    #assert DirectSalesQACoachingForm1.get_transitiontatus(1, 1)=="checkstatus"
                    #assert DirectSalesQACoachingForm1.get_pitchtatus(1, 1)=="checkstatus"
                    assert DirectSalesQACoachingForm1.get_overcometatus(2)==self.checkstatus
                    #assert DirectSalesQACoachingForm1.get_closetatus(1, 3)=="checkstatus"
                    assert DirectSalesQACoachingForm1.get_strengths()==strengths
                    assert DirectSalesQACoachingForm1.get_opportunities1()==opportunities1
                    assert DirectSalesQACoachingForm1.get_opportunities2()==opportunities2
                    assert DirectSalesQACoachingForm1.get_plan1()==plan1
                    assert DirectSalesQACoachingForm1.get_plan2()==plan2                         

                    
                    a2=0
                    while a2<5:
                        a2=a2+1
                        if DirectSalesQACoachingForm1.select_discover(a2, 2):
                            assert DirectSalesQACoachingForm1.get_discovertatus(a2, 2)==self.uncheckstatus
                            assert DirectSalesQACoachingForm1.get_discovertatus(a2, 1)==self.checkstatus
                       
                        
                    b2=0
                    while b2<2:
                        b2=b2+1
                        if DirectSalesQACoachingForm1.select_transition(b2, 2):
                            assert DirectSalesQACoachingForm1.get_transitiontatus(b2, 2)==self.uncheckstatus
                            assert DirectSalesQACoachingForm1.get_transitiontatus(b2, 1)==self.checkstatus
                    c2=0
                    while c2<8:
                        c2=c2+1
                        if DirectSalesQACoachingForm1.select_pitch(c2, 2):
                            assert DirectSalesQACoachingForm1.get_pitchtatus(c2, 2)==self.uncheckstatus
                            assert DirectSalesQACoachingForm1.get_pitchtatus(c2, 1)==self.checkstatus
                        
                    d2=0
                    while d2<3:
                        d2=d2+1
                        if DirectSalesQACoachingForm1.select_close(d2, 2):
                            assert DirectSalesQACoachingForm1.get_closetatus(d2, 2)==self.uncheckstatus
                            assert DirectSalesQACoachingForm1.get_closetatus(d2, 3)==self.checkstatus

                 


                    
                    
                    assert BasicInfo.get_ButtonName(1)=="Print"
                    assert BasicInfo.get_ButtonName(2)=="Back"
                    for index in range(3,6):
                        assert BasicInfo.Button_Displayed(index)==False


    #def tearDown(self):
        #Gl.driver.quit()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()