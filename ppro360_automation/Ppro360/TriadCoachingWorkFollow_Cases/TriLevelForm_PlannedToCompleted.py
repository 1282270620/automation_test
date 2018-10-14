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
from CoachingAndTriadCoaching_Pages.TriLevelFormPage import TriLevelFormPage
from Tablet_pages.HeaderPage import HeaderPage
from public_method.Get_AllRoleAccountForTest import Get_AllRoleAccountForTest
from selenium.webdriver.common.by import By
from Tablet_pages import BasePage

class TriLevelForm_PlannedToCompleted(unittest.TestCase):


    def setUp(self):
        #Case ID
        self.caseID="TriLevelForm_PlannedToCompleted"
        
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
        self.coachformname="Tri-Level Form" 
        self.coachpagetitle="Triad Coaching - "+self.coachformname
        
        self.CheckBox_CheckedStatus="fa fa-check-square"
        self.CheckBox_UnCheckedStatus="fa fa-uncheck"
        
        #radiobutton status
        self.RadioButton_CheckedStatus='fa fa-check-circle radio-btn checked'
        self.RadioButton_UnCheckedStatus='fa fa-check-circle radio-btn'
        
        #Cancel window info
        self.CancelWindow_title="Confirmation"
        self.CancelWindow_content="Please confirm you want to cancel this To-Do!"
        
    def test_TriLevelForm_PlannedToCompleted(self):
        GetConfig=Get_configration_data()
        Tablet=TabletHomepage()
        Ppage=PerformancePage()
        TCoach=Coach_Triad_General()
        CoachHome=Coachinghomepage()
        BasicInfo=BasicInfoforCoaching()
        Header=HeaderPage()
        TriLevelForm=TriLevelFormPage()
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
                    userid=TriLevelForm.get_firstTL_HRID(1)
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
                    assert TriLevelForm.GoalsImprovementCommitmentComments_disabled(1,3)=='true'
                    assert TriLevelForm.GoalsImprovementCommitmentComments_disabled(1,4)=='true'
                    assert TriLevelForm.GoalsImprovementCommitmentComments_disabled(2,2)=='true'
                    assert TriLevelForm.GoalsImprovementCommitmentComments_disabled(2,3)=='true'
                    assert TriLevelForm.GoalsImprovementCommitmentComments_disabled(2,5)=='true'
                    assert TriLevelForm.GoalsImprovementCommitmentComments_disabled(2,6)=='true'
                    assert TriLevelForm.LastComments_disabled()=='true'
                    for i1 in range(1,3):
                        assert TriLevelForm.ShortComments_disabled(i1)=='true'
                    for i2 in range(6,22):
                        assert TriLevelForm.KeyElementComments_disabled(i2)=='true'
                    for i3 in range(6,22):
                        TriLevelForm.click_RadioButton(i3, 1)
                        assert TriLevelForm.get_RadioButtonStatus(i3, 1)==self.RadioButton_UnCheckedStatus
                        TriLevelForm.click_RadioButton(i3, 2)
                        assert TriLevelForm.get_RadioButtonStatus(i3, 2)==self.RadioButton_UnCheckedStatus
                    
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
                    '''                                       
                    BasicInfo.input_callrecordingnumber(CallRecordingNumber)
                    '''                    
                    BasicInfo.click_anyKPIstatusofCheckBox(KPInumber)#Check the last KPIs achievement.
                    BasicInfo.click_anyKPIstatusofCheckBox(2)#Uncheck the first KPI.
                    
                    TriLevelForm.InputShortComments(1, TL_Name)
                    TriLevelForm.InputShortComments(2, '60001')
                    TriLevelForm.InputGoalsImprovementCommitmentComments(1, 3,(self.Longtextboxesprefix1+TriLevelForm.getGoalsImprovementCommitmentTitle(1, 2)))
                    TriLevelForm.InputGoalsImprovementCommitmentComments(1, 4,(self.Longtextboxesprefix1+TriLevelForm.getGoalsImprovementCommitmentTitle(1, 2)))
                    TriLevelForm.InputGoalsImprovementCommitmentComments(2, 2,(self.Longtextboxesprefix1+TriLevelForm.getGoalsImprovementCommitmentTitle(2, 4)))
                    TriLevelForm.InputGoalsImprovementCommitmentComments(2, 3,(self.Longtextboxesprefix1+TriLevelForm.getGoalsImprovementCommitmentTitle(2, 4)))
                    TriLevelForm.InputGoalsImprovementCommitmentComments(2, 5,(self.Longtextboxesprefix1+TriLevelForm.getGoalsImprovementCommitmentTitle(2, 4)))
                    TriLevelForm.InputGoalsImprovementCommitmentComments(2, 6,(self.Longtextboxesprefix1+TriLevelForm.getGoalsImprovementCommitmentTitle(2, 4)))
                    for i in range(6,22):
                        TriLevelForm.InputKeyElementComments(i, (self.Longtextboxesprefix1+TriLevelForm.getKeyTitle(i)))
                        
                    TriLevelForm.InputLastComments(self.Longtextboxesprefix1+TriLevelForm.getLastTitle())
                    for j in range(6,22):
                        if j%2==0:
                            TriLevelForm.click_RadioButton(j, 1)
                        else:
                            TriLevelForm.click_RadioButton(j, 2)
                            
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
                    assert TriLevelForm.get_acknowledgedDate()==""
                    assert BasicInfo.get_anyCheckBoxStatus(KPInumber)==self.CheckBox_CheckedStatus
                    for index in range(2,KPInumber):
                        assert BasicInfo.get_anyCheckBoxStatus(index)==self.CheckBox_UnCheckedStatus
                    assert BasicInfo.get_SN()==SN_CoachHome
                    assert BasicInfo.get_employeename()==TL_Name
                    assert BasicInfo.get_employeeHrid()==TL_hrid
                    assert BasicInfo.get_coachname()==LoginName
                    assert BasicInfo.get_createdate()==Created_Date_FromServer
                    if lobname !="AOL":
                        assert BasicInfo.get_callrecordingnumber()==CallRecordingNumber
                    assert TriLevelForm.get_ShortComments(1)==TL_Name
                    assert TriLevelForm.get_ShortComments(2)=='60001'
                    assert TriLevelForm.get_GoalsImprovementCommitmentComments(1, 3)==self.Longtextboxesprefix1+TriLevelForm.getGoalsImprovementCommitmentTitle(1, 2)
                    assert TriLevelForm.get_GoalsImprovementCommitmentComments(1, 4)==self.Longtextboxesprefix1+TriLevelForm.getGoalsImprovementCommitmentTitle(1, 2)
                    assert TriLevelForm.get_GoalsImprovementCommitmentComments(2, 2)==self.Longtextboxesprefix1+TriLevelForm.getGoalsImprovementCommitmentTitle(2, 4)
                    assert TriLevelForm.get_GoalsImprovementCommitmentComments(2, 3)==self.Longtextboxesprefix1+TriLevelForm.getGoalsImprovementCommitmentTitle(2, 4)
                    assert TriLevelForm.get_GoalsImprovementCommitmentComments(2, 5)==self.Longtextboxesprefix1+TriLevelForm.getGoalsImprovementCommitmentTitle(2, 4)
                    assert TriLevelForm.get_GoalsImprovementCommitmentComments(2, 6)==self.Longtextboxesprefix1+TriLevelForm.getGoalsImprovementCommitmentTitle(2, 4)
                    for m in range(6,22):
                        assert TriLevelForm.get_KeyElementComments(m)==self.Longtextboxesprefix1+TriLevelForm.getKeyTitle(m)
                        
                    assert TriLevelForm.get_LastComments()==self.Longtextboxesprefix1+TriLevelForm.getLastTitle()
                    for n in range(6,22):
                        if j%2==0:
                            assert TriLevelForm.get_RadioButtonStatus(j, 1)==self.RadioButton_CheckedStatus
                            assert TriLevelForm.get_RadioButtonStatus(j, 2)==self.RadioButton_UnCheckedStatus
                        else:
                            assert TriLevelForm.get_RadioButtonStatus(j, 1)==self.RadioButton_UnCheckedStatus
                            assert TriLevelForm.get_RadioButtonStatus(j, 2)==self.RadioButton_CheckedStatus
                        
                    
                    assert BasicInfo.get_ButtonName(1)=="Print"
                    assert BasicInfo.get_ButtonName(2)=="Back"
                    for index in range(3,6):
                        assert BasicInfo.Button_Displayed(index)==False


    def tearDown(self):
        Gl.driver.quit()
    
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()