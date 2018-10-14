'''
Created on 2018.3.28

@author: haodong.liu
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
from CoachingAndTriadCoaching_Pages.CustomerBeforeCompanyPage import CustomerBeforeCompanyPage
from public_method.Coaching_PublicFunction import Coaching_PublicFunction
from Tablet_pages.HeaderPage import HeaderPage
from public_method.Get_AllRoleAccountForTest import Get_AllRoleAccountForTest
from Tablet_pages.CancelCoachingWindow import CancelCoachingWindow


class CustomerBeforeCompany_PlannedToCompleted(unittest.TestCase):


    def setUp(self):
        #Case ID
        self.caseID="CustomerBeforeCompany_PlannedToCompleted"
        
        GetData=Get_configration_data()
        #Get URL 
        self.tableturl=GetData.get_TabletUrl()
        self.Adminurl=GetData.get_AdminUrl()
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
        self.coachformname="Customer Before Company" 
        self.coachpagetitle="Coaching - "+self.coachformname
        
        self.CheckBox_CheckedStatus="fa fa-check-square"
        self.CheckBox_UnCheckedStatus="fa fa-uncheck"
        self.checkstatus="fa fa-check-circle radio-btn checked"
        self.uncheckstatus="fa fa-check-circle radio-btn"
        
        #Cancel window info
        self.CancelWindow_title="Confirmation"
        self.CancelWindow_content="Please confirm you want to cancel this To-Do!"


    def test_CustomerBeforeCompany_PlannedToCompleted(self):
        GetConfig=Get_configration_data()
        Tablet=TabletHomepage()
        Ppage=PerformancePage()
        TCoach=Coach_Triad_General()
        CoachHome=Coachinghomepage()
        BasicInfo=BasicInfoforCoaching()
        Header=HeaderPage()
        CustomerBeforeCompanyForm=CustomerBeforeCompanyPage()
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
                    
                    #Login tablet,and Get HRID using for testing
                    L=Login()
                    L.Login_tablet(self.tableturl,lobname,sitename,self.OMuserid,self.OMpassword)
                    time.sleep(Gl.waittime)
                    LoginName=Header.get_loginName()
                    Tablet.click_performancecircle()
                    Ppage.select_Agentkpi()
                    Ppage.unselect_Agentkpi()
                    userid=Ppage.get_FirstAgentofAnyTL_hrid(1)
                    L.logout_tablet()
                    
                    TLInfo=Getaccount.get_TLandAgentInfofromAdmin(self.Adminurl, lobname, sitename, self.OMuserid, self.OMpassword, userid)
                    Agent_Name=TLInfo["Name"]
                    Agent_hrid=TLInfo["Hrid"]
                    Agent_password=TLInfo["Password"]
                    
                    L=Login()
                    L.Login_tablet(self.tableturl,lobname,sitename,self.OMuserid,self.OMpassword)
                    time.sleep(Gl.waittime)
                    LoginName=Header.get_loginName()
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
                    assert CustomerBeforeCompanyForm.TextBoxesUnderCustomerBeforeCompany_disabled(2)=='true'
                    assert CustomerBeforeCompanyForm.TextBoxesUnderCustomerBeforeCompany_disabled(3)=='true'
                    assert CustomerBeforeCompanyForm.TextBoxesUnderCustomerBeforeCompany_disabled(4)=='true'
                    assert CustomerBeforeCompanyForm.get_AuditPurposeDropdownDefault()=='Detractor Audit'
                    assert CustomerBeforeCompanyForm.get_CallDispositionDropdownDefault()=='Cold Transferred'
                    assert CustomerBeforeCompanyForm.get_DetractorRCADropdownDefault()=='[Agent | Agent Behavior | Agent Behavior] Refused to Listen/Interrupting the Customer'
                    assert CustomerBeforeCompanyForm.get_ReasonForCallingDropdownDefault()=='Billing Inquiry - High Bill - Internet Overage Usage'
                    for i in range(1,26):
                        assert CustomerBeforeCompanyForm.TextBoxesUnderCustomerBeforeCompany_disabled(i)=='true'
                    assert CustomerBeforeCompanyForm.get_Dropdown1Default()=='IPTV'
                    assert CustomerBeforeCompanyForm.get_Dropdown2Default()=='IPTV'
                    assert CustomerBeforeCompanyForm.get_Dropdown3Default()=='Self-Fluff'
                    assert CustomerBeforeCompanyForm.get_Dropdown4Default()=='Within 24 hrs'
                    assert CustomerBeforeCompanyForm.get_Dropdown5Default()=='Elderly'
                    assert CustomerBeforeCompanyForm.get_Dropdown6Default()=='Call Back'
                    for i2 in range(1,13):
                        CustomerBeforeCompanyForm.click_YesButton(i2)
                        assert CustomerBeforeCompanyForm.get_YesButtonStatus(i2)==self.uncheckstatus
                        assert CustomerBeforeCompanyForm.get_NoButtonStatus(i2)==self.uncheckstatus
                        assert CustomerBeforeCompanyForm.get_NAButtonStatus(i2)==self.checkstatus
                    clickNum=[14,16,19,20,21,24,25]
                    for i3 in clickNum:
                        CustomerBeforeCompanyForm.click_YesButton(i3)
                        assert CustomerBeforeCompanyForm.get_YesButtonStatus(i3)==self.uncheckstatus
                        assert CustomerBeforeCompanyForm.get_NoButtonStatus(i3)==self.uncheckstatus
                        assert CustomerBeforeCompanyForm.get_NAButtonStatus(i3)==self.checkstatus

                    
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

                    #DateandTimeofCall=The first day of date picker
                    #BasicInfo.input_callrecordingnumber(CallRecordingNumber)
                    if lobname != "AOL":
                        BasicInfo.input_callrecordingnumber(CallRecordingNumber)
                    CustomerBeforeCompanyForm.input_TextBoxesUnderCoachingKPIs(2, self.Shorttextboxesprefix1)
                    CustomerBeforeCompanyForm.input_TextBoxesUnderCoachingKPIs(3, self.Shorttextboxesprefix1)
                    CustomerBeforeCompanyForm.input_TextBoxesUnderCoachingKPIs(4, self.Shorttextboxesprefix1)
                    CustomerBeforeCompanyForm.click_DateTimePicker()
                    CustomerBeforeCompanyForm.click_Date()
                    CustomerBeforeCompanyForm.click_AuditPurposeDropdownDefault()
                    CustomerBeforeCompanyForm.click_AuditPurposeDropdownList(2)
                    CustomerBeforeCompanyForm.click_CallDispositionDropdownDefault()
                    CustomerBeforeCompanyForm.click_CallDispositionDropdownList(2)
                    CustomerBeforeCompanyForm.click_DetractorRCADropdownDefault()
                    CustomerBeforeCompanyForm.click_DetractorRCADropdownList(2)
                    CustomerBeforeCompanyForm.click_ReasonForCallingDropdownDefault()
                    CustomerBeforeCompanyForm.click_ReasonForCallingDropdownList(2)
                    for j in range(1,13):
                        CustomerBeforeCompanyForm.input_TextBoxesUnderCustomerBeforeCompany(j, self.Longtextboxesprefix1)
                    CustomerBeforeCompanyForm.input_TextBoxesUnderCustomerBeforeCompany(13, self.Longtextboxesprefix1)
                    CustomerBeforeCompanyForm.click_Dropdown1Default()
                    CustomerBeforeCompanyForm.click_Dropdown1List(2)
                    CustomerBeforeCompanyForm.input_TextBoxesUnderCustomerBeforeCompany(14, self.Longtextboxesprefix1)
                    CustomerBeforeCompanyForm.input_TextBoxesUnderCustomerBeforeCompany(15, self.Longtextboxesprefix1)
                    CustomerBeforeCompanyForm.click_Dropdown2Default()
                    CustomerBeforeCompanyForm.click_Dropdown2List(2)
                    CustomerBeforeCompanyForm.input_TextBoxesUnderCustomerBeforeCompany(16, self.Longtextboxesprefix1)
                    CustomerBeforeCompanyForm.input_TextBoxesUnderCustomerBeforeCompany(17, self.Longtextboxesprefix1)
                    CustomerBeforeCompanyForm.click_Dropdown3Default()
                    CustomerBeforeCompanyForm.click_Dropdown3List(2)
                    CustomerBeforeCompanyForm.input_TextBoxesUnderCustomerBeforeCompany(18, self.Longtextboxesprefix1)
                    CustomerBeforeCompanyForm.click_Dropdown4Default()
                    CustomerBeforeCompanyForm.click_Dropdown4List(2)
                    CustomerBeforeCompanyForm.input_TextBoxesUnderCustomerBeforeCompany(19, self.Longtextboxesprefix1)
                    CustomerBeforeCompanyForm.input_TextBoxesUnderCustomerBeforeCompany(20, self.Longtextboxesprefix1)
                    CustomerBeforeCompanyForm.input_TextBoxesUnderCustomerBeforeCompany(21, self.Longtextboxesprefix1)
                    CustomerBeforeCompanyForm.input_TextBoxesUnderCustomerBeforeCompany(22, self.Longtextboxesprefix1)
                    CustomerBeforeCompanyForm.click_Dropdown5Default()
                    CustomerBeforeCompanyForm.click_Dropdown5List(2)
                    CustomerBeforeCompanyForm.input_TextBoxesUnderCustomerBeforeCompany(23, self.Longtextboxesprefix1)
                    CustomerBeforeCompanyForm.click_Dropdown6Default()
                    CustomerBeforeCompanyForm.click_Dropdown6List(2)
                    CustomerBeforeCompanyForm.input_TextBoxesUnderCustomerBeforeCompany(24, self.Longtextboxesprefix1)
                    CustomerBeforeCompanyForm.input_TextBoxesUnderCustomerBeforeCompany(25, self.Longtextboxesprefix1)
                    for j1 in range(1,13):
                        CustomerBeforeCompanyForm.click_YesButton(j1)
                    num2=[14,16,19,20,21,24,25]
                    for j2 in num2:
                        CustomerBeforeCompanyForm.click_YesButton(j2)
                    
   
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
                    assert BasicInfo.get_employeename()==Agent_Name
                    assert BasicInfo.get_employeeHrid()==Agent_hrid
                    assert BasicInfo.get_coachname()==Header.get_loginName()
                    assert BasicInfo.get_createdate()==Created_Date_FromServer
                    if lobname != "AOL":
                        assert BasicInfo.get_callrecordingnumber()==CallRecordingNumber
                    assert CustomerBeforeCompanyForm.get_TextBoxesUnderCoachingKPIs(2)==self.Shorttextboxesprefix1
                    assert CustomerBeforeCompanyForm.get_TextBoxesUnderCoachingKPIs(3)==self.Shorttextboxesprefix1
                    assert CustomerBeforeCompanyForm.get_TextBoxesUnderCoachingKPIs(4)==self.Shorttextboxesprefix1
                    assert CustomerBeforeCompanyForm.get_DateComments()!=''
                    assert CustomerBeforeCompanyForm.get_AuditPurposeDropdownDefault()=='Live Audit'
                    assert CustomerBeforeCompanyForm.get_DetractorRCADropdownDefault()=='[Agent | Agent Behavior | Condescending/Rudeness]'
                    assert CustomerBeforeCompanyForm.get_CallDispositionDropdownDefault()=='Warm Transferred'
                    assert CustomerBeforeCompanyForm.get_ReasonForCallingDropdownDefault()=='Billing Inquiry - High Bill - Miscellaneous Charges'
                    for k in range(1,26):
                        assert CustomerBeforeCompanyForm.get_TextBoxesUnderCustomerBeforeCompany(k)==self.Longtextboxesprefix1
                    for k1 in range(1,13):
                        assert CustomerBeforeCompanyForm.get_YesButtonStatus(k1)==self.checkstatus
                        assert CustomerBeforeCompanyForm.get_NoButtonStatus(k1)==self.uncheckstatus
                        assert CustomerBeforeCompanyForm.get_NAButtonStatus(k1)==self.uncheckstatus
                    num3=[14,16,19,20,21,24,25]
                    for k2 in num3:
                        assert CustomerBeforeCompanyForm.get_YesButtonStatus(k2)==self.checkstatus
                        assert CustomerBeforeCompanyForm.get_NoButtonStatus(k2)==self.uncheckstatus
                        assert CustomerBeforeCompanyForm.get_NAButtonStatus(k2)==self.uncheckstatus
                    assert CustomerBeforeCompanyForm.get_Dropdown1Default()=='BB'
                    assert CustomerBeforeCompanyForm.get_Dropdown2Default()=='BB'
                    assert CustomerBeforeCompanyForm.get_Dropdown3Default()=='Transfer'
                    assert CustomerBeforeCompanyForm.get_Dropdown4Default()=='Within 1-7 days'
                    assert CustomerBeforeCompanyForm.get_Dropdown5Default()=='Extremely Dissatisfied'
                    assert CustomerBeforeCompanyForm.get_Dropdown6Default()=='Adjustment'


                    assert BasicInfo.get_ButtonName(1)=="Print"
                    assert BasicInfo.get_ButtonName(2)=="Back"
                    for index in range(3,6):
                        assert BasicInfo.Button_Displayed(index)==False


    def tearDown(self):
        Gl.driver.quit()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()