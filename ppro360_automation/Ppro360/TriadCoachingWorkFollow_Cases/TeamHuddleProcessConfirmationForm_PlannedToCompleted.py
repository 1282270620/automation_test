'''
Created on 2018.1.15

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
from CoachingAndTriadCoaching_Pages.TeamHuddleProcessConfirmationFormPage import TeamHuddleProcessConfirmationFormPage
from Tablet_pages.HeaderPage import HeaderPage
from public_method.Get_AllRoleAccountForTest import Get_AllRoleAccountForTest

class TeamHuddleProcessConfirmationForm_PlannedToCompleted(unittest.TestCase):


    def setUp(self):
        #Case ID
        self.caseID="TeamHuddleProcessConfirmationForm_PlannedToCompleted"
        
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
        self.coachhometitle="Triad Coaching"
        self.coachformname="Team Huddle Process Confirmation Form" 
        self.coachpagetitle="Triad Coaching - "+self.coachformname
        
        self.CheckBox_CheckedStatus="fa fa-check-circle radio-btn checked"
        self.CheckBox_UnCheckedStatus="fa fa-check-circle radio-btn"
        
        self.CheckButton_CheckedStatus='fa fa-check-square'
        self.CheckButton_UnCheckedStatus='fa fa-uncheck'
        #Cancel window info
        self.CancelWindow_title="Confirmation"
        self.CancelWindow_content="Please confirm you want to cancel this To-Do!"


    def test_TeamHuddleProcessConfirmationForm_PlannedToCompleted(self):
        GetConfig=Get_configration_data()
        Tablet=TabletHomepage()
        Ppage=PerformancePage()
        TCoach=Coach_Triad_General()
        CoachHome=Coachinghomepage()
        BasicInfo=BasicInfoforCoaching()
        Header=HeaderPage()
        TeamHuddleProcessConfirmationForm=TeamHuddleProcessConfirmationFormPage()
        Getaccount=Get_AllRoleAccountForTest()
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
                    userid=TeamHuddleProcessConfirmationForm.get_firstTL_HRID(1)
                    L.logout_tablet()
                    
                    TLInfo=Getaccount.get_TLandAgentInfofromAdmin(self.Adminurl, lobname, sitename, self.OMuserid, self.OMpassword, userid)
                    TL_Name=TLInfo["Name"]
                    TL_hrid=TLInfo["Hrid"]
                    TL_password=TLInfo["Password"]
                    
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
                    Ppage.select_AnyKpiOfTL(2)#select the first KPI
                    Ppage.click_addTriadcoachbutton()
                    TCoach.Add_AnyCoachOrTriad(self.coachformname)
                    Created_Date_FromServer=GetConfig.get_ServerCurrentDate().replace("-","/")
                    #Step4: #a.Enter triad coaching module.
                            #b.Select this coaching record to enter form detail page.
                    Header.click_backbutton()
                    Tablet.click_Triadcoachingcirecle()
                    SN_CoachHome=CoachHome.get_anyCoach_attribute(1, 1)
                   
                    CoachHome.click_eachcoach(1)
                    '''Check1:Enter form detail page with title Triad Coaching - CareCommitment'''
                    assert Header.get_HeaderTittle()==self.coachpagetitle
                    
                    #Step5:  4. Logout and login the TL  who is coached in this form;
                            #5. Enter triad Coach module.
                            #6. Select this coaching record to open this form detail page.
                            #7. Try to edit the form
                    L.logout_tablet()
                    L.Login_tablet(self.tableturl, lobname, sitename, TL_hrid, TL_password)
                    Tablet.click_TL_Triadcoachingcirecle()
                    SN_Actual=CoachHome.get_anyCoach_attribute(1, 1)
                    CoachHome.click_eachcoach(1)
                    '''Check2:1.This coaching record is shown by default.
                              2.TL cannot edit the form.(each of fields is uneditable)'''
                    assert SN_Actual==SN_CoachHome
                    if lobname != "AOL":
                        assert BasicInfo.callrecordingnumber_disabled()=="true"
                    assert TeamHuddleProcessConfirmationForm.DateComments_disabled(1)=='true'
                    assert TeamHuddleProcessConfirmationForm.DateComments_disabled(2)=='true'
                    '''
                    assert TeamHuddleProcessConfirmationForm.TimeButton_disabled(1)=='true'
                    assert TeamHuddleProcessConfirmationForm.TimeButton_disabled(2)=='true'
                    '''
                    assert TeamHuddleProcessConfirmationForm.KpiComments_disabled(1)=='true'
                    assert TeamHuddleProcessConfirmationForm.KpiComments_disabled(2)=='true'
                    assert TeamHuddleProcessConfirmationForm.TopicComments_disabled()=='true'
                    for num1 in range(2,39):
                        if num1==3 or num1==5 or num1==7 or num1==9 or num1==12 or num1==14 or num1==16 or num1==18 or num1==21 or num1==23 or num1==26 or num1==28 or num1==30 or num1==32 or num1==34 or num1==36 or num1==38:
                            assert TeamHuddleProcessConfirmationForm.LongComments_disabled(num1)=='true'
                    for num2 in range(2,39):
                        if num2==2 or num2==4 or num2==6 or num2==8 or num2==11 or num2==13 or num2==15 or num2==17 or num2==20 or num2==22 or num2==25 or num2==27 or num2==29 or num2==31 or num2==33 or num2==35 or num2==37:
                            TeamHuddleProcessConfirmationForm.click_RadioButton(num2, 1)
                            assert TeamHuddleProcessConfirmationForm.get_RadioButtonStatus(num2, 1)==self.CheckBox_UnCheckedStatus
                            TeamHuddleProcessConfirmationForm.click_RadioButton(num2, 2)
                            assert TeamHuddleProcessConfirmationForm.get_RadioButtonStatus(num2, 2)==self.CheckBox_UnCheckedStatus
                    for i2 in range(5,8):
                        assert TeamHuddleProcessConfirmationForm.LastLongComments_disabled(i2)=='true'

                    #Step6:8.logout->login with creater LC/OM.
                            #9.Enter triad coaching module to enter this coaching record detail page.
                            #10.Input value in all editable fileds with following content:
                                #1) CallRecordingNumber:test_number!~@#$%^&*()
                                #2) Check the last KPIs achievement.
                                            #Uncheck the first KPI.
                                #3) Text box: Performance pro test team to input content in text boxes ,alice_shu0823~!@#$%^&*();:'"?/\[]{},sabrina's@symbio.com.
                                #11.Click button 'Complete coaching'.
                                #12.On search main page, search with status option 'completed'.
                    L.logout_tablet()
                    L.Login_tablet(self.tableturl,lobname,sitename,self.OMuserid,self.OMpassword)
                    Tablet.click_Triadcoachingcirecle()
                    CoachHome.click_eachcoach(1)
                    CallRecordingNumber=self.CallRecordingNumber1                                       
                    BasicInfo.input_callrecordingnumber(CallRecordingNumber)                    
                    BasicInfo.click_anyKPIstatusofCheckBox(KPInumber)#Check the last KPIs achievement.
                    BasicInfo.click_anyKPIstatusofCheckBox(2)#Uncheck the first KPI.
                    TeamHuddleProcessConfirmationForm.Click_TimeButton(1)
                    TeamHuddleProcessConfirmationForm.Click_DayButton(1,1,1)
                    TeamHuddleProcessConfirmationForm.Click_TimeButton(2)
                    TeamHuddleProcessConfirmationForm.Click_DayButton(2,1,1)
                    TeamHuddleProcessConfirmationForm.Input_KpiComments(1, self.Shorttextboxesprefix1)
                    TeamHuddleProcessConfirmationForm.Input_KpiComments(2, self.Shorttextboxesprefix1)
                    TeamHuddleProcessConfirmationForm.Input_TopicComments(self.Shorttextboxesprefix1)
                    for j1 in range(2,39):
                        if j1==3 or j1==5 or j1==7 or j1==9 or j1==12 or j1==14 or j1==16 or j1==18 or j1==21 or j1==23 or j1==26 or j1==28 or j1==30 or j1==32 or j1==34 or j1==36 or j1==38:
                            TeamHuddleProcessConfirmationForm.Input_LongComments(j1, self.Longtextboxesprefix1)
                    for j3 in range(2,39):
                        if j3==2 or j3==4 or j3==6 or j3==8 or j3==11 or j3==13 or j3==15 or j3==17 or j3==20 or j3==22 or j3==25 or j3==27 or j3==29 or j3==31 or j3==33 or j3==35 or j3==37:
                            if j3==2 or j3==4 or j3==6 or j3==8 or j3==10:
                                TeamHuddleProcessConfirmationForm.click_RadioButton(j3, 1)
                            else:
                                TeamHuddleProcessConfirmationForm.click_RadioButton(j3, 2)     
                    for j2 in range(5,8):
                        TeamHuddleProcessConfirmationForm.Input_LastLongComments(j2, self.Longtextboxesprefix1)
                    
                    
                    
                        
                    BasicInfo.Click_Button(3) #click Completed Coaching button
                    Completed_Date_FromServer=GetConfig.get_ServerCurrentDate().replace("-","/")
                    CoachHome.select_status("Completed")
                    CoachHome.click_filterbutton()
                    '''Check3:2.Automatically back to search main page.
                              3.This coaching record is search out with completed status shown.'''
                    assert Header.get_HeaderTittle()==self.coachhometitle
                    assert CoachHome.get_anyCoach_attribute(1, 1)==SN_CoachHome
                    
                    #Step7:13.Enter this form detail page.
                    CoachHome.click_eachcoach(1)
                    '''Check4:13.On this CC form:
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
                    assert BasicInfo.get_anyCheckBoxStatus(KPInumber)==self.CheckButton_CheckedStatus
                    for index in range(2,KPInumber):
                        assert BasicInfo.get_anyCheckBoxStatus(index)==self.CheckButton_UnCheckedStatus
                    assert BasicInfo.get_SN()==SN_CoachHome
                    assert BasicInfo.get_employeename()==TL_Name
                    assert BasicInfo.get_employeeHrid()==TL_hrid
                    assert BasicInfo.get_coachname()==LoginName
                    assert BasicInfo.get_createdate()==Created_Date_FromServer
                    if lobname !="AOL":
                        assert BasicInfo.get_callrecordingnumber()==CallRecordingNumber
                    assert TeamHuddleProcessConfirmationForm.get_KpiComments(1)==self.Shorttextboxesprefix1
                    assert TeamHuddleProcessConfirmationForm.get_KpiComments(2)==self.Shorttextboxesprefix1
                    assert TeamHuddleProcessConfirmationForm.get_TopicComments()==self.Shorttextboxesprefix1
                    for k1 in range(2,39):
                        if k1==3 or k1==5 or k1==7 or k1==9 or k1==12 or k1==14 or k1==16 or k1==18 or k1==21 or k1==23 or k1==26 or k1==28 or k1==30 or k1==32 or k1==34 or k1==36 or k1==38:
                            assert TeamHuddleProcessConfirmationForm.get_LongComments(k1)==self.Longtextboxesprefix1
                    for k3 in range(2,39):    
                        if k3==2 or k3==4 or k3==6 or k3==8 or k3==11 or k3==13 or k3==15 or k3==17 or k3==20 or k3==22 or k3==25 or k3==27 or k3==29 or k3==31 or k3==33 or k3==35 or k3==37:
                            if k3==2 or k3==4 or k3==6 or k3==8 or k3==10:
                                assert TeamHuddleProcessConfirmationForm.get_RadioButtonStatus(k3, 1)
                            else:
                                assert TeamHuddleProcessConfirmationForm.get_RadioButtonStatus(k3, 2)
                    for k2 in range(5,8):
                        assert TeamHuddleProcessConfirmationForm.get_LastLongComments(k2)==self.Longtextboxesprefix1
                    
        
                    assert BasicInfo.get_ButtonName(1)=="Print"
                    assert BasicInfo.get_ButtonName(2)=="Back"
                    for index in range(3,6):
                        assert BasicInfo.Button_Displayed(index)==False


    def tearDown(self):
        Gl.driver.quit()
        
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
