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
from CoachingAndTriadCoaching_Pages.CoachingRhythmProcessConfirmationPage import CoachingRhythmProcessConfirmationPage
from Tablet_pages.HeaderPage import HeaderPage
from public_method.Get_AllRoleAccountForTest import Get_AllRoleAccountForTest
from selenium.webdriver.common.by import By
from Tablet_pages import BasePage

class CoachingRhythmProcessConfirmation_PlannedToCompleted(unittest.TestCase):


    def setUp(self):
        #Case ID
        self.caseID="CoachingRhythmProcessConfirmation_PlannedToCompleted"
        
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
        self.coachformname="Coaching Rhythm Process Confirmation" 
        self.coachpagetitle="Triad Coaching - "+self.coachformname
        
        self.CheckBox_CheckedStatus="fa fa-check-square"
        self.CheckBox_UnCheckedStatus="fa fa-uncheck"
        
        #radiobutton status
        self.RadioButton_CheckedStatus='fa fa-check-circle radio-btn checked'
        self.RadioButton_UnCheckedStatus='fa fa-check-circle radio-btn'
        
        #Cancel window info
        self.CancelWindow_title="Confirmation"
        self.CancelWindow_content="Please confirm you want to cancel this To-Do!"
        
    def test_CoachingRhythmProcessConfirmation_PlannedToCompleted(self):
        GetConfig=Get_configration_data()
        Tablet=TabletHomepage()
        Ppage=PerformancePage()
        TCoach=Coach_Triad_General()
        CoachHome=Coachinghomepage()
        BasicInfo=BasicInfoforCoaching()
        Header=HeaderPage()
        CoachingRhythmProcessConfirmationForm=CoachingRhythmProcessConfirmationPage()
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
                    userid=CoachingRhythmProcessConfirmationForm.get_firstTL_HRID(1)
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
                    assert CoachingRhythmProcessConfirmationForm.LongComments_disable(3)=='true'
                    assert CoachingRhythmProcessConfirmationForm.LongComments_disable(4)=='true'
                    assert CoachingRhythmProcessConfirmationForm.LongComments_disable(5)=='true'
                    i=0
                    while i<18:
                        i=i+1
                        if i==1 or i==2 or i==5 or i==8 or i==9 or i==13 or i==16 or i==17:
                            assert CoachingRhythmProcessConfirmationForm.ShortComments_disable(i,4)=='true'
                        if i==3 or i==4 or i==6 or i==7 or i==10 or i==11 or i==12 or i==14 or i==15 or i==18:
                            assert CoachingRhythmProcessConfirmationForm.ShortComments_disable(i,3)=='true'
                    for line in range(1,19):
                        if line==1 or line==2 or line==5 or line==8 or line==9 or line==13 or line==16 or line==17:
                            CoachingRhythmProcessConfirmationForm.click_RadioButton(line, 3, 1)
                            CoachingRhythmProcessConfirmationForm.click_RadioButton(line, 3, 2)
                            CoachingRhythmProcessConfirmationForm.click_RadioButton(line, 5, 1)
                            CoachingRhythmProcessConfirmationForm.click_RadioButton(line, 5, 2)
                            assert CoachingRhythmProcessConfirmationForm.get_RadioButtonStatus(line,3,1)==self.RadioButton_UnCheckedStatus
                            assert CoachingRhythmProcessConfirmationForm.get_RadioButtonStatus(line,3,1)==self.RadioButton_UnCheckedStatus
                            assert CoachingRhythmProcessConfirmationForm.get_RadioButtonStatus(line,3,1)==self.RadioButton_UnCheckedStatus
                            assert CoachingRhythmProcessConfirmationForm.get_RadioButtonStatus(line,3,1)==self.RadioButton_UnCheckedStatus
                        if line==3 or line==4 or line==6 or line==7 or line==10 or line==11 or line==12 or line==14 or line==15 or line==18:
                            CoachingRhythmProcessConfirmationForm.click_RadioButton(line, 2, 1)
                            CoachingRhythmProcessConfirmationForm.click_RadioButton(line, 2, 2)
                            CoachingRhythmProcessConfirmationForm.click_RadioButton(line, 4, 1)
                            CoachingRhythmProcessConfirmationForm.click_RadioButton(line, 4, 2)
                            assert CoachingRhythmProcessConfirmationForm.get_RadioButtonStatus(line,2,1)==self.RadioButton_UnCheckedStatus
                            assert CoachingRhythmProcessConfirmationForm.get_RadioButtonStatus(line,2,2)==self.RadioButton_UnCheckedStatus
                            assert CoachingRhythmProcessConfirmationForm.get_RadioButtonStatus(line,4,1)==self.RadioButton_UnCheckedStatus
                            assert CoachingRhythmProcessConfirmationForm.get_RadioButtonStatus(line,4,2)==self.RadioButton_UnCheckedStatus
                    
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
                    CoachingRhythmProcessConfirmationForm.input_LongComments(3, (self.Longtextboxesprefix1+CoachingRhythmProcessConfirmationForm.getLongTiltle(3)))
                    CoachingRhythmProcessConfirmationForm.input_LongComments(4, (self.Longtextboxesprefix1+CoachingRhythmProcessConfirmationForm.getLongTiltle(4)))  
                    CoachingRhythmProcessConfirmationForm.input_LongComments(5, (self.Longtextboxesprefix1+CoachingRhythmProcessConfirmationForm.getLongTiltle(5)))
                    
                    k=0
                    while k<18:
                        k=k+1
                        if k==1 or k==2 or k==5 or k==8 or k==9 or k==13 or k==16 or k==17:
                            CoachingRhythmProcessConfirmationForm.Input_ShortComments(k, 4, (self.Shorttextboxesprefix1+CoachingRhythmProcessConfirmationForm.getShortTiltle(k,2)))

                        if k==3 or k==4 or k==6 or k==7 or k==10 or k==11 or k==12 or k==14 or k==15 or k==18:
                            CoachingRhythmProcessConfirmationForm.Input_ShortComments(k, 3, (self.Shorttextboxesprefix1+CoachingRhythmProcessConfirmationForm.getShortTiltle(k,1)))            
                    for line in range(1,19):
                        if line==1 or line==2 or line==5 or line==8 or line==9 or line==13 or line==16 or line==17:
                            CoachingRhythmProcessConfirmationForm.click_RadioButton(line, 3, 1)
                            CoachingRhythmProcessConfirmationForm.click_RadioButton(line, 5, 2)
                        if line==3 or line==4 or line==6 or line==7 or line==10 or line==11 or line==12 or line==14 or line==15 or line==18:
                            CoachingRhythmProcessConfirmationForm.click_RadioButton(line, 2, 1)
                            CoachingRhythmProcessConfirmationForm.click_RadioButton(line, 4, 2)
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
                    assert CoachingRhythmProcessConfirmationForm.get_LongComments(3)==self.Longtextboxesprefix1+CoachingRhythmProcessConfirmationForm.getLongTiltle(3)
                    assert CoachingRhythmProcessConfirmationForm.get_LongComments(4)==self.Longtextboxesprefix1+CoachingRhythmProcessConfirmationForm.getLongTiltle(4)
                    assert CoachingRhythmProcessConfirmationForm.get_LongComments(5)==self.Longtextboxesprefix1+CoachingRhythmProcessConfirmationForm.getLongTiltle(5)
                    m=0
                    while m<18:
                        m=m+1
                        if m==1 or m==2 or m==5 or m==8 or m==9 or m==13 or m==16 or m==17:
                            assert CoachingRhythmProcessConfirmationForm.get_ShortComments(m,4)==self.Shorttextboxesprefix1+CoachingRhythmProcessConfirmationForm.getShortTiltle(m,2);
                        if m==3 or m==4 or m==6 or m==7 or m==10 or m==11 or m==12 or m==14 or m==15 or m==18:
                            assert CoachingRhythmProcessConfirmationForm.get_ShortComments(m,3)==self.Shorttextboxesprefix1+CoachingRhythmProcessConfirmationForm.getShortTiltle(m,1);
                    for line in range(1,19):
                        if line==1 or line==2 or line==5 or line==8 or line==9 or line==13 or line==16 or line==17:
                            assert CoachingRhythmProcessConfirmationForm.get_RadioButtonStatus(line, 3, 1)==self.RadioButton_CheckedStatus
                            assert CoachingRhythmProcessConfirmationForm.get_RadioButtonStatus(line, 3, 2)==self.RadioButton_UnCheckedStatus
                            assert CoachingRhythmProcessConfirmationForm.get_RadioButtonStatus(line, 5, 1)==self.RadioButton_UnCheckedStatus
                            assert CoachingRhythmProcessConfirmationForm.get_RadioButtonStatus(line, 5, 2)==self.RadioButton_CheckedStatus
                        if line==3 or line==4 or line==6 or line==7 or line==10 or line==11 or line==12 or line==14 or line==15 or line==18:
                            assert CoachingRhythmProcessConfirmationForm.get_RadioButtonStatus(line, 2, 1)==self.RadioButton_CheckedStatus
                            assert CoachingRhythmProcessConfirmationForm.get_RadioButtonStatus(line, 2, 2)==self.RadioButton_UnCheckedStatus
                            assert CoachingRhythmProcessConfirmationForm.get_RadioButtonStatus(line, 4, 1)==self.RadioButton_UnCheckedStatus
                            assert CoachingRhythmProcessConfirmationForm.get_RadioButtonStatus(line, 4, 2)==self.RadioButton_CheckedStatus
                    assert BasicInfo.get_ButtonName(1)=="Print"
                    assert BasicInfo.get_ButtonName(2)=="Back"
                    for index in range(3,6):
                        assert BasicInfo.Button_Displayed(index)==False


    def tearDown(self):
        Gl.driver.quit()
    
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()