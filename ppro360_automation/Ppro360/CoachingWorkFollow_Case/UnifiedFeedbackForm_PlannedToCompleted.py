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
from CoachingAndTriadCoaching_Pages.UnifiedFeedbackForm import UnifiedFeedbackForm
from public_method.Coaching_PublicFunction import Coaching_PublicFunction
from Tablet_pages.HeaderPage import HeaderPage
from public_method.Get_AllRoleAccountForTest import Get_AllRoleAccountForTest
from Tablet_pages.CancelCoachingWindow import CancelCoachingWindow


class UnifiedFeedbackForm_PlannedToCompleted(unittest.TestCase):


    def setUp(self):
        #Case ID
        self.caseID="UnifiedFeedbackForm_PlannedToCompleted"
        
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
        self.coachformname="Unified Feedback Form" 
        self.coachpagetitle="Coaching - "+self.coachformname
        
        self.CheckBox_CheckedStatus="fa fa-check-square"
        self.CheckBox_UnCheckedStatus="fa fa-uncheck"
        self.checkstatus="fa fa-check-circle radio-btn checked"
        self.uncheckstatus="fa fa-check-circle radio-btn"
        
        #Cancel window info
        self.CancelWindow_title="Confirmation"
        self.CancelWindow_content="Please confirm you want to cancel this To-Do!"


    def test_UnifiedFeedbackForm_PlannedToCanceled(self):
        GetConfig=Get_configration_data()
        Tablet=TabletHomepage()
        Ppage=PerformancePage()
        TCoach=Coach_Triad_General()
        CoachHome=Coachinghomepage()
        BasicInfo=BasicInfoforCoaching()
        Header=HeaderPage()
        UnifiedFeedbackFormForm=UnifiedFeedbackForm()
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
                    #UnifiedFeedbackFormForm.click_CoachName()
                    #UnifiedFeedbackFormForm.click_CoachNameselect()
                    CoachHome.click_filterbutton()
                    SN_Actual=CoachHome.get_anyCoach_attribute(1, 1)
                    CoachHome.click_eachcoach(1)
                    '''Check2:1.This coaching record is shown by default.
                              2.TL cannot edit the form.(each of fields is uneditable)'''
                    assert SN_Actual==SN_CoachHome
                    if lobname != "AOL":
                        assert BasicInfo.callrecordingnumber_disabled()=="true"
                    assert UnifiedFeedbackFormForm.shortinput_disabled(2,2)=="true"
                    assert UnifiedFeedbackFormForm.shortinput_disabled(3,1)=="true"
                    assert UnifiedFeedbackFormForm.shortinput_disabled(3,2)=="true"
                    assert UnifiedFeedbackFormForm.longinput_disabled(2)=="true"
                    assert UnifiedFeedbackFormForm.longinput_disabled(6)=="true"
                    assert UnifiedFeedbackFormForm.midinput_disabled(1, 1)=="true"
                    assert UnifiedFeedbackFormForm.midinput_disabled(1,2)=="true"
                    #assert UnifiedFeedbackFormForm.timebutton_disabled()=="true"
                    assert UnifiedFeedbackFormForm.auditpurpose_disabled()=="true"
                    assert UnifiedFeedbackFormForm.detractorbehavior_disabled()=="true"
                    UnifiedFeedbackFormForm.click_pointchoose(16, 1, 1)
                    UnifiedFeedbackFormForm.click_pointchoose(16, 2, 1)
                    assert UnifiedFeedbackFormForm.get_pointchoose(16,1, 3)==self.checkstatus
                    assert UnifiedFeedbackFormForm.get_pointchoose(16,2, 3)==self.checkstatus
                    a=5
                    while a<17:
                        a=a+2
                        assert UnifiedFeedbackFormForm.observationnotes_disabled(a)=="true"
                    b=4
                    while b<14:
                        b=b+2
                        c=0
                        while c<3:
                            c=c+1
                            UnifiedFeedbackFormForm.click_pointchoose(b,c,1)
                            assert UnifiedFeedbackFormForm.get_pointchoose(b, c,1)==self.uncheckstatus
                            assert UnifiedFeedbackFormForm.get_pointchoose(b, c,3)==self.checkstatus
                    d=0
                    while d<4:
                        d=d+1
                        e=0
                        while e<2:
                            e=e+1
                            UnifiedFeedbackFormForm.click_chooseclick(d,e,1)
                            assert UnifiedFeedbackFormForm.get_chooseclick(d,e,1)==self.uncheckstatus
                            assert UnifiedFeedbackFormForm.get_chooseclick(d,e,3)==self.checkstatus
                    f=2
                    while f<5:
                        f=f+1
                        g=0
                        while g<2:
                            g=g+1
                            assert UnifiedFeedbackFormForm.midinput_disabled(f,g)=="true"
                          
                        
                            

                    
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
                    commentsTitle1=self.Shorttextboxesprefix1+UnifiedFeedbackFormForm.get_shortinputBoxtitle(2,2)
                    commentsTitle2=self.Shorttextboxesprefix1+UnifiedFeedbackFormForm.get_shortinputBoxtitle(3,1)
                    commentsTitle3=self.Shorttextboxesprefix1+UnifiedFeedbackFormForm.get_shortinputBoxtitle(3,2)
                    longinput1=self.Longtextboxesprefix1+UnifiedFeedbackFormForm.get_longinputBoxtitle(2)
                    longinput2=self.Longtextboxesprefix1+UnifiedFeedbackFormForm.get_longinputBoxtitle(6)
                    midinput1=self.Longtextboxesprefix1+UnifiedFeedbackFormForm.get_midinputBoxtitle(1,1)
                    midinput2=self.Longtextboxesprefix1+UnifiedFeedbackFormForm.get_midinputBoxtitle(1,2)
                    point1="10"
                    point2="20"
                    point3="20"
                    point4="25"
                    point5="20"
                    point6="5"
                    point7="0"
                    auditpurpose="Live Audit"
                    detractorbehavior="[Agent] Agent Behavior | Condescending/Rudeness"
                    #DateandTimeofCall=The first day of date picker
                    #BasicInfo.input_callrecordingnumber(CallRecordingNumber)
                    if lobname != "AOL":
                        BasicInfo.input_callrecordingnumber(CallRecordingNumber)
                    UnifiedFeedbackFormForm.input_longinput(2, longinput1)
                    UnifiedFeedbackFormForm.input_longinput(6, longinput2)
                    UnifiedFeedbackFormForm.input_midinput(1,1, midinput1)
                    UnifiedFeedbackFormForm.input_midinput(1,2, midinput2)
                    a1=5
                    while a1<17:
                        a1=a1+2
                        observationnotes=self.Longtextboxesprefix1+UnifiedFeedbackFormForm.get_observationnotesBoxtitle(a1)
                        UnifiedFeedbackFormForm.input_observationnotes(a1, observationnotes)
                    b1=4
                    while b1<14:
                        b1=b1+2
                        c1=0
                        while c1<3:
                            c1=c1+1
                            UnifiedFeedbackFormForm.click_pointchoose(b1,c1,1)
                    d1=0
                    while d1<3:
                        d1=d1+1
                        e1=0
                        while e1<2:
                            e1=e1+1
                            UnifiedFeedbackFormForm.click_chooseclick(d1,e1,1)
                    UnifiedFeedbackFormForm.click_chooseclick(4,1,2)
                    UnifiedFeedbackFormForm.click_chooseclick(4,2,1)
                    f1=2
                    while f1<5:
                        f1=f1+1
                        g1=0
                        while g1<2:
                            g1=g1+1
                            midcomments=self.Longtextboxesprefix1+UnifiedFeedbackFormForm.get_midinputBoxtitle(f1,g1)
                            UnifiedFeedbackFormForm.input_midinput(f1,g1,midcomments)
                    UnifiedFeedbackFormForm.click_pointchoose(16,1 , 1)
                    UnifiedFeedbackFormForm.click_pointchoose(16,2, 1)
                    UnifiedFeedbackFormForm.click_auditpurpose()
                    UnifiedFeedbackFormForm.click_auditpurposechoose(2)
                    UnifiedFeedbackFormForm.click_detractorbehavior()
                    UnifiedFeedbackFormForm.click_detractorbehaviorchoose(3)      
                    UnifiedFeedbackFormForm.click_timebutton()
                    UnifiedFeedbackFormForm.click_hourbutton()
                    UnifiedFeedbackFormForm.click_ampmbutton()
                    UnifiedFeedbackFormForm.click_hourdownarrow()
                    UnifiedFeedbackFormForm.click_minutedownarrow()
                    UnifiedFeedbackFormForm.click_backbutton()
                    UnifiedFeedbackFormForm.click_dayclick(1, 1)
                    timedate=UnifiedFeedbackFormForm.get_datebox()
                    UnifiedFeedbackFormForm.input_shortinput(2, 2, commentsTitle1)
                    UnifiedFeedbackFormForm.input_shortinput(3, 1, commentsTitle2)
                    UnifiedFeedbackFormForm.input_shortinput(3, 2, commentsTitle3)     
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
                    assert UnifiedFeedbackFormForm.get_shortinput(2,2)==commentsTitle1
                    assert UnifiedFeedbackFormForm.get_shortinput(3,1)==commentsTitle2
                    assert UnifiedFeedbackFormForm.get_shortinput(3,2)==commentsTitle3
                    assert UnifiedFeedbackFormForm.get_longinput(2)==longinput1
                    assert UnifiedFeedbackFormForm.get_longinput(6)==longinput2
                    assert UnifiedFeedbackFormForm.get_midinput(1,1)==midinput1
                    assert UnifiedFeedbackFormForm.get_midinput(1,2)==midinput2
                    assert UnifiedFeedbackFormForm.get_pointchoose(16, 1, 1)==self.checkstatus
                    assert UnifiedFeedbackFormForm.get_pointchoose(16, 1, 2)==self.uncheckstatus
                    assert UnifiedFeedbackFormForm.get_pointchoose(16, 1, 3)==self.uncheckstatus
                    assert UnifiedFeedbackFormForm.get_pointchoose(16, 2, 1)==self.checkstatus
                    assert UnifiedFeedbackFormForm.get_pointchoose(16, 2, 2)==self.uncheckstatus
                    assert UnifiedFeedbackFormForm.get_pointchoose(16, 2, 3)==self.uncheckstatus
                    assert UnifiedFeedbackFormForm.get_pointrecievedvalue(6)==point1
                    assert UnifiedFeedbackFormForm.get_pointrecievedvalue(8)==point2
                    assert UnifiedFeedbackFormForm.get_pointrecievedvalue(10)==point3
                    assert UnifiedFeedbackFormForm.get_pointrecievedvalue(12)==point4
                    assert UnifiedFeedbackFormForm.get_pointrecievedvalue(14)==point5
                    assert UnifiedFeedbackFormForm.get_pointrecievedvalue(16)==point6
                    assert UnifiedFeedbackFormForm.get_totalpointvalue()==point7
                    assert UnifiedFeedbackFormForm.detractorbehaviorvalue()==detractorbehavior
                    assert UnifiedFeedbackFormForm.auditpurposevalue()==auditpurpose
                    a2=5
                    while a2<17:
                        a2=a2+2
                        observationnotes2=self.Longtextboxesprefix1+UnifiedFeedbackFormForm.get_observationnotesBoxtitle(a2)
                        assert UnifiedFeedbackFormForm.get_observationnotes(a2)==observationnotes2
                    b2=4
                    while b2<14:
                        b2=b2+2
                        c2=0
                        while c2<3:
                            c2=c2+1
                        assert UnifiedFeedbackFormForm.get_pointchoose(b2, c2, 1)==self.checkstatus
                        assert UnifiedFeedbackFormForm.get_pointchoose(b2, c2, 2)==self.uncheckstatus
                        assert UnifiedFeedbackFormForm.get_pointchoose(b2, c2, 3)==self.uncheckstatus
                    d2=0
                    while d2<3:
                        d2=d2+1
                        e2=0
                        while e2<2:
                            e2=e2+1
                            assert UnifiedFeedbackFormForm.get_chooseclick(d2, e2, 1)==self.checkstatus
                            assert UnifiedFeedbackFormForm.get_chooseclick(d2, e2, 2)==self.uncheckstatus
                            assert UnifiedFeedbackFormForm.get_chooseclick(d2, e2, 3)==self.uncheckstatus
                    assert UnifiedFeedbackFormForm.get_chooseclick(4,1,1)==self.uncheckstatus
                    assert UnifiedFeedbackFormForm.get_chooseclick(4,1,2)==self.checkstatus
                    assert UnifiedFeedbackFormForm.get_chooseclick(4,1,3)==self.uncheckstatus
                    assert UnifiedFeedbackFormForm.get_chooseclick(4,2,1)==self.checkstatus
                    assert UnifiedFeedbackFormForm.get_chooseclick(4,2,2)==self.uncheckstatus
                    assert UnifiedFeedbackFormForm.get_chooseclick(4,2,3)==self.uncheckstatus
                    f2=2
                    while f2<5:
                        f2=f2+1
                        g2=0
                        while g1<2:
                            g2=g2+1
                            midcomments2=self.Longtextboxesprefix1+UnifiedFeedbackFormForm.get_midinputBoxtitle(f2,g2)
                            assert UnifiedFeedbackFormForm.get_midinput(f2,e2)==midcomments2   
                        
                    assert BasicInfo.get_ButtonName(1)=="Print"
                    assert BasicInfo.get_ButtonName(2)=="Back"
                    for index in range(3,6):
                        assert BasicInfo.Button_Displayed(index)==False


    #def tearDown(self):
        #Gl.driver.quit()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()