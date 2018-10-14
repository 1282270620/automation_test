'''
Created on 2017.8.18

@author: yalan.yin
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
from CoachingAndTriadCoaching_Pages.DFMCoachingpage import DFMCoachingpage
from Tablet_pages.HeaderPage import HeaderPage
from public_method.Get_AllRoleAccountForTest import Get_AllRoleAccountForTest



class DFM_PlannedToCompleted(unittest.TestCase):


    def setUp(self):
        #Case ID
        self.caseID="DFM_PlannedToCompleted"
        
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
        self.coachhometitle="Triad Coaching"
        self.coachformname="DFM" 
        self.coachpagetitle="Triad Coaching - "+self.coachformname
        
        self.CheckBox_CheckedStatus="fa fa-check-square"
        self.CheckBox_UnCheckedStatus="fa fa-uncheck"
        
        #Cancel window info
        self.CancelWindow_title="Confirmation"
        self.CancelWindow_content="Please confirm you want to cancel this To-Do!"


    def test_DFM_PlannedToCanceled(self):
        GetConfig=Get_configration_data()
        Tablet=TabletHomepage()
        Ppage=PerformancePage()
        TCoach=Coach_Triad_General()
        CoachHome=Coachinghomepage()
        BasicInfo=BasicInfoforCoaching()
        Header=HeaderPage()
        DFMForm=DFMCoachingpage()
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
                   
                    #Step1:Login tablet,and Get TLInfo using for testing
                    TLInfo_Dic=Getaccount.get_TLInfoandAgentHridFromPerformance(self.tableturl, lobname, sitename, self.OMuserid, self.OMpassword,"Month-To-Date")
                    TL_Name=TLInfo_Dic["TLName"]
                    TL_hrid=TLInfo_Dic["TLHrid"]
                    TL_password=TLInfo_Dic["TLPassword"]
                    
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
                    
                    Ppage.click_mtd()
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
                    '''Check1:Enter form detail page with title Triad Coaching - DFM'''
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
                    assert DFMForm.agentOpinion_disabled()=="true"
                    assert DFMForm.leaderSuggestion_disabled()=='true'
                    assert DFMForm.improvementSuggestion_disabled()=='true'
                    assert DFMForm.agentImprovement_disabled()=='true'
                    assert DFMForm.actionDetail_disabled()=='true'
                    assert DFMForm.addtionalComments_disabled()=='true' 
                    
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
                    DFMForm.input_agentOpinion(self.Longtextboxesprefix1+DFMForm.get_TextboxTitle(2))
                    DFMForm.input_leaderSuggestion(self.Longtextboxesprefix1+DFMForm.get_TextboxTitle(3))
                    DFMForm.input_agentImprovement(self.Longtextboxesprefix1+DFMForm.get_TextboxTitle(4))
                    DFMForm.input_improvementSuggestion(self.Longtextboxesprefix1+DFMForm.get_TextboxTitle(5))
                    DFMForm.input_actionDetail(self.Longtextboxesprefix1+DFMForm.get_TextboxTitle(6))
                    DFMForm.input_addtionalComments(self.Longtextboxesprefix1+DFMForm.get_TextboxTitle(7))
                    
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
                    '''Check4:13.On this DFM form:
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
                    assert DFMForm.get_agentOpinion()==self.Longtextboxesprefix1+DFMForm.get_TextboxTitle(2)
                    assert DFMForm.get_leaderSuggestion()==self.Longtextboxesprefix1+DFMForm.get_TextboxTitle(3)
                    assert DFMForm.get_agentImprovement()==self.Longtextboxesprefix1+DFMForm.get_TextboxTitle(4)
                    assert DFMForm.get_improvementSuggestion()==self.Longtextboxesprefix1+DFMForm.get_TextboxTitle(5)
                    assert DFMForm.get_actionDetail()==self.Longtextboxesprefix1+DFMForm.get_TextboxTitle(6)
                    assert DFMForm.get_addtionalComments()==self.Longtextboxesprefix1+DFMForm.get_TextboxTitle(7)
                    assert BasicInfo.get_ButtonName(1)=="Print"
                    assert BasicInfo.get_ButtonName(2)=="Back"
                    for index in range(3,6):
                        assert BasicInfo.Button_Displayed(index)==False


    def tearDown(self):
        Gl.driver.quit()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()