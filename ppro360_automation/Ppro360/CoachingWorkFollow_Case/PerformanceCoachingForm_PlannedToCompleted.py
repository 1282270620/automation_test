'''
Created on Jul 26, 2017

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
from CoachingAndTriadCoaching_Pages.PerformanceCoachingForm import PerformanceCoachingForm
from public_method.Coaching_PublicFunction import Coaching_PublicFunction
from Tablet_pages.HeaderPage import HeaderPage
from public_method.Get_AllRoleAccountForTest import Get_AllRoleAccountForTest
from Tablet_pages.CancelCoachingWindow import CancelCoachingWindow


class PerformanceCoachingForm_PlannedToCompleted(unittest.TestCase):


    def setUp(self):
        #Case ID
        self.caseID="PerformanceCoachingForm_PlannedToCompleted"
        
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
        
        #coaching or Triad coaching
        self.coachtype="triad coaching"  
        #Coachformname
        self.coachhometitle="Coaching"
        self.coachformname="Performance Coaching Form" 
        self.coachpagetitle="Coaching - "+self.coachformname
        
        self.CheckBox_CheckedStatus="fa fa-check-square"
        self.CheckBox_UnCheckedStatus="fa fa-uncheck"
        self.checkstatus="fa fa-check-circle radio-btn checked"
        self.uncheckstatus="fa fa-check-circle radio-btn"
        
        #Cancel window info
        self.CancelWindow_title="Confirmation"
        self.CancelWindow_content="Please confirm you want to cancel this To-Do!"


    def test_PerformanceCoachingForm_PlannedToCanceled(self):
        GetConfig=Get_configration_data()
        Tablet=TabletHomepage()
        Ppage=PerformancePage()
        TCoach=Coach_Triad_General()
        CoachHome=Coachinghomepage()
        BasicInfo=BasicInfoforCoaching()
        Header=HeaderPage()
        PerformanceCoachingFormForm=PerformanceCoachingForm()
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
                    #Step4: #a.Enter triad coaching module.
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
                    #PerformanceCoachingFormForm.click_CoachName()
                    #PerformanceCoachingFormForm.click_CoachNameselect()
                    CoachHome.click_filterbutton()
                    SN_Actual=CoachHome.get_anyCoach_attribute(1, 1)
                    CoachHome.click_eachcoach(1)
                    '''Check2:1.This coaching record is shown by default.
                              2.TL cannot edit the form.(each of fields is uneditable)'''
                    assert SN_Actual==SN_CoachHome
                    if lobname != "AOL":
                        assert BasicInfo.callrecordingnumber_disabled()=="true"
                    assert PerformanceCoachingFormForm.shortcomments_disabled(2,1)=="true"
                    assert PerformanceCoachingFormForm.shortcomments_disabled(3,1)=="true"
                    assert PerformanceCoachingFormForm.shortcomments_disabled(3,2)=="true"
                    assert PerformanceCoachingFormForm.shortcomments_disabled(4,1)=="true"
                    assert PerformanceCoachingFormForm.calldate_disabled()=="true"
                    a=4
                    while a<10:
                        a=a+1
                        assert PerformanceCoachingFormForm.longcomments_disabled(a)=="true"
                    b=1
                    while b<7:
                        b=b+1
                        assert PerformanceCoachingFormForm.remarkscomments_disabled(b)=="true"
                        b1=0
                        while b1<2:
                            b1=b1+1
                            assert PerformanceCoachingFormForm.get_chooseclicktatus(b, b1)==self.uncheckstatus
                            

                    
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
                    commentsTitle1=self.Shorttextboxesprefix1+PerformanceCoachingFormForm.get_shortcommentsBoxtitle(2,1)
                    commentsTitle2=self.Shorttextboxesprefix1+PerformanceCoachingFormForm.get_shortcommentsBoxtitle(3, 1)
                    commentsTitle3=self.Shorttextboxesprefix1+PerformanceCoachingFormForm.get_shortcommentsBoxtitle(3, 2)
                    commentsTitle4=self.Shorttextboxesprefix1+PerformanceCoachingFormForm.get_shortcommentsBoxtitle(4, 1)

                    #DateandTimeofCall=The first day of date picker
                    #BasicInfo.input_callrecordingnumber(CallRecordingNumber)
                    if lobname != "AOL":
                        BasicInfo.input_callrecordingnumber(CallRecordingNumber)
                    PerformanceCoachingFormForm.input_shortcomments(2, 1,commentsTitle1 )
                    PerformanceCoachingFormForm.input_shortcomments(3, 1, commentsTitle2)
                    PerformanceCoachingFormForm.input_shortcomments(3, 2, commentsTitle3)
                    PerformanceCoachingFormForm.input_shortcomments(4, 1,commentsTitle4 )
                    a1=4
                    while a1<10:
                        a1=a1+1
                        comments=self.Longtextboxesprefix1+PerformanceCoachingFormForm.get_longcommentsBoxtitle(a1)
                        PerformanceCoachingFormForm.input_longcomments(a1, comments)
                    b2=1
                    while b2<7:
                        b2=b2+1
                        comments2=self.Shorttextboxesprefix1+PerformanceCoachingFormForm.get_remarkscommentsBoxtitle(b2)
                        PerformanceCoachingFormForm.input_remarkscomments(b2, comments2)
                        if b2<4:
                            PerformanceCoachingFormForm.click_chooseclick(b2, 2)
                        if b2>=4:
                            PerformanceCoachingFormForm.click_chooseclick(b2,1)
                    PerformanceCoachingFormForm.click_timebutton()
                    PerformanceCoachingFormForm.click_dayclick(1, 1)
                    timedate=PerformanceCoachingFormForm.get_calldate()     
                    BasicInfo.click_anyKPIstatusofCheckBox(KPInumber)#Check the last KPIs achievement.
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
                    assert PerformanceCoachingFormForm.get_shortcomments(2, 1)==commentsTitle1
                    assert PerformanceCoachingFormForm.get_shortcomments(3, 1)==commentsTitle2
                    assert PerformanceCoachingFormForm.get_shortcomments(3, 2)==commentsTitle3
                    assert PerformanceCoachingFormForm.get_shortcomments(4,1 )==commentsTitle4
                    assert PerformanceCoachingFormForm.get_calldate()==timedate
                    a2=4
                    while a2<10:
                        a2=a2+1
                        comments3=self.Longtextboxesprefix1+PerformanceCoachingFormForm.get_longcommentsBoxtitle(a2)
                        assert PerformanceCoachingFormForm.get_longcomments(a2)==comments3
                    b3=1
                    while b3<7:
                        b3=b3+1
                        comments4=self.Shorttextboxesprefix1+PerformanceCoachingFormForm.get_remarkscommentsBoxtitle(b3)
                        assert PerformanceCoachingFormForm.get_remarkscomments(b3)==comments4
                        if b3<4:
                            assert PerformanceCoachingFormForm.get_chooseclicktatus(b3, 1)==self.uncheckstatus
                            assert PerformanceCoachingFormForm.get_chooseclicktatus(b3, 2)==self.checkstatus
                        if b3>=4:
                            assert PerformanceCoachingFormForm.get_chooseclicktatus(b3, 1)==self.checkstatus
                            assert PerformanceCoachingFormForm.get_chooseclicktatus(b3, 2)==self.uncheckstatus
                    assert BasicInfo.get_ButtonName(1)=="Print"
                    assert BasicInfo.get_ButtonName(2)=="Back"
                    for index in range(3,6):
                        assert BasicInfo.Button_Displayed(index)==False


    #def tearDown(self):
        #Gl.driver.quit()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()