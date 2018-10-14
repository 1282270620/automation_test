'''
Created on 20170823

@author: luming.zhao
'''

import unittest
from public_method import Gl
from public_method.Get_configration_data import Get_configration_data
from public_method.Coach_Triad_General import Coach_Triad_General
from Tablet_pages.PerformancPage import PerformancePage
from public_method.Login import Login
from Tablet_pages.TabletHomepage import TabletHomepage
from Tablet_pages.Coachinghomepage import Coachinghomepage
from CoachingAndTriadCoaching_Pages.BasicInfoforCoaching import BasicInfoforCoaching
from CoachingAndTriadCoaching_Pages.SettingExpectations import SettingExpectations
from public_method.Coaching_PublicFunction import Coaching_PublicFunction
from Tablet_pages.HeaderPage import HeaderPage
from public_method.Get_AllRoleAccountForTest import Get_AllRoleAccountForTest
from Tablet_pages.CancelCoachingWindow import CancelCoachingWindow


class SettingExpectations_OngoingToCanceled(unittest.TestCase):


    def setUp(self):
        #Case ID
        self.caseID="SettingExpectations_OngoingToCanceled"
        
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
        self.coachtype="coaching"  
        #Coachformname
        self.coachhometitle="Coaching"
        self.coachformname="Setting Expectations" 
        self.coachpagetitle="Coaching - "+self.coachformname
        
        self.CheckBox_CheckedStatus="fa fa-check-square"
        self.CheckBox_UnCheckedStatus="fa fa-uncheck"


    def test_SettingExpectations_OngoingToCanceled(self):
        GetConfig=Get_configration_data()
        Tablet=TabletHomepage()
        Ppage=PerformancePage()
        TCoach=Coach_Triad_General()
        CoachHome=Coachinghomepage()
        BasicInfo=BasicInfoforCoaching()
        Header=HeaderPage()
        SettingExpectationsForm=SettingExpectations()
        Getaccount=Get_AllRoleAccountForTest()
        CancelWindow=CancelCoachingWindow()

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
                    print (lobname,sitename)
                   
                    #Step1:Login tablet,and Get AgentInfo using for testing
                    AgentInfo_Dic=Getaccount.get_AgentInfoFromTablet(self.tableturl, lobname, sitename, self.OMuserid, self.OMpassword,"Month-To-Date")
                    Agent_name=AgentInfo_Dic["AgentName"]
                    Agent_hrid=AgentInfo_Dic["AgentHrid"]
                    Agent_password=AgentInfo_Dic["AgentPassword"]
                    #Step1:1.Login with creater LC/OM/TL to enter performance Month-To-Date page.
                            #2.Select an agent->select the second KPI to add this form.
                            #3.Enter coaching module to enter this coaching record detail page.
                            #4.Input value in all editable fileds with following content:
                            #1) CallRecordingNumber:
                            #2) Select the other all KPIs.
                            #3) Text box: Performance pro test team to input content in text boxes ,alice_shu0823~!@#$%^&*();:'?/\[]{},sabrina's@symbio.com.
    
                            #5.Click button 'Save and continue later'.
                            #6.Again enter this coaching record detail page.
                            #7.a.Click button 'Print'.
                    L=Login()
                    L.Login_tablet(self.tableturl,lobname,sitename,self.OMuserid,self.OMpassword)
                    LoginName=Header.get_loginName()
                    Tablet.click_performancecircle()
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
                      
                    Ppage.select_AnyKpiOfAgent_OM(3)#select the first and second KPI 
                    Ppage.unfold_anyTL(1)
                    Ppage.select_AnyKpiOfAgent_OM(2)#unselect the first, and remain the second kpi to add form
                    Ppage.click_addcoachbutton()
                    TCoach.Add_AnyCoachOrTriad(self.coachformname)
                    Created_Date_FromServer=GetConfig.get_ServerCurrentDate().replace("-","/")
                    Header.click_backbutton()
                    Tablet.click_coachingcircle()
                    SN_coachhome=CoachHome.get_anyCoach_attribute(1, 1)
                    CoachHome.click_eachcoach(1)
                    Content_InTextBox=self.Longtextboxesprefix1+SettingExpectationsForm.get_establishExpectationBoxTitle()
                    Content_InTextBox=self.Longtextboxesprefix1+SettingExpectationsForm.get_reasonBoxTitle()
                    Content_InTextBox=self.Longtextboxesprefix1+SettingExpectationsForm.get_resourcesBoxTitle()
                    Content_InTextBox=self.Longtextboxesprefix1+SettingExpectationsForm.get_verifyCommitmentBoxTitle()
                    Content_InTextBox=self.Longtextboxesprefix1+SettingExpectationsForm.get_verifyUnderstandingBoxTitle()
                    Content_InTextBox=self.Longtextboxesprefix1+SettingExpectationsForm.get_confidenceBuilderBoxTitle()
                    Content_InTextBox=self.Longtextboxesprefix1+SettingExpectationsForm.get_otherNotesAndRemarksBoxTitle()
                    
 
                  
                    BasicInfo.click_anyKPIstatusofCheckBox(2)#Select the other all KPIs.
                    for index in range(4,KPInumber+1):#Select the other all KPIs.
                        BasicInfo.click_anyKPIstatusofCheckBox(index)
                    #text="test_number123!~@#$%^&*()"
                    BasicInfo.input_callrecordingnumber(self.CallRecordingNumber1)
                    
                    SettingExpectationsForm.input_establishExpectation(Content_InTextBox)
                    SettingExpectationsForm.input_reason(Content_InTextBox)
                    SettingExpectationsForm.input_resources(Content_InTextBox)
                    SettingExpectationsForm.input_verifyUnderstanding(Content_InTextBox)
                    SettingExpectationsForm.input_verifyCommitment(Content_InTextBox)
                    SettingExpectationsForm.input_confidenceBuilder(Content_InTextBox)
                    SettingExpectationsForm.input_otherNotesAndRemarks(Content_InTextBox)

                    BasicInfo.Click_Button(2)#Click button 'Save and continue later'.
                    #Step2:  8.Logout and login the Agent who is coached in the form;
                            #9.Enter coaching module to open this form detail page.
                            #10. Try to edit the form.
                    L.logout_tablet()
                    L.Login_tablet(self.tableturl, lobname, sitename, Agent_hrid, Agent_password)
                    Tablet.click_Agent_coachingcircle()
                    CoachHome.click_eachcoach(1)
                    '''Check1:1.Agent cannot edit any info:All fields shown in uneditable status including check-box.
                              2.On this  form:
                                1)  Status = Ongoing;
                                2)  Created Date = The date when the form is created;
                                3)  Completed Date, Acknowledged Date shown blank.
                                4) All KPIs are shown in checked status.
                              3.Each of other fields content shown correct:
                                1) SN, Employee Name,EmployeeID, Coaching Name,
                                2) each of text boxes,dates
                                3) Call Recording Number is blank (not for AOL)
                              4.At the page bottom:show only one button:  Back'''
                    if lobname != "AOL":
                        assert BasicInfo.callrecordingnumber_disabled()=="true"
                    assert SettingExpectationsForm.establishExpectation__disabled()=="true"
                    assert SettingExpectationsForm.reason__disabled()=="true"
                    assert SettingExpectationsForm.resources__disabled()=="true"
                    assert SettingExpectationsForm.verifyUnderstanding__disabled()=="true"
                    assert SettingExpectationsForm.verifyCommitment__disabled()=="true"
                    assert SettingExpectationsForm.confidenceBuilder__disabled()=="true"
                    assert SettingExpectationsForm.otherNotesAndRemarks__disabled()=="true"
                    
                    
                    
                    for index in range(2,KPInumber+1):#1
                        BasicInfo.click_anyKPIstatusofCheckBox_Agent(index)
                    
                    assert BasicInfo.get_status()=="Ongoing"
                    assert BasicInfo.get_createdate()==Created_Date_FromServer
                    assert BasicInfo.get_completeddate()==''
                    assert BasicInfo.get_acknowledgedDate()==''
                    for index in range(2,KPInumber+1):#After 1, all are still checked status
                        assert BasicInfo.get_anyCheckBoxStatus_Agent(index)==self.CheckBox_CheckedStatus  
                        
                    assert BasicInfo.get_SN()==SN_coachhome
                    assert BasicInfo.get_employeeHrid()==Agent_hrid
                    assert BasicInfo.get_employeename()==Agent_name
                    assert BasicInfo.get_coachname()==LoginName
                    if lobname != "AOL":
                        assert BasicInfo.get_callrecordingnumber()==self.CallRecordingNumber1

                    assert SettingExpectationsForm.get_establishExpectation()==Content_InTextBox
                    assert SettingExpectationsForm.get_reason()==Content_InTextBox
                    assert SettingExpectationsForm.get_resources()==Content_InTextBox
                    assert SettingExpectationsForm.get_verifyUnderstanding()==Content_InTextBox
                    assert SettingExpectationsForm.get_verifyCommitment()==Content_InTextBox
                    assert SettingExpectationsForm.get_confidenceBuilder()==Content_InTextBox
                    assert SettingExpectationsForm.get_otherNotesAndRemarks()==Content_InTextBox
                    
                    
                    
                    assert BasicInfo.get_ButtonName(1)=="Back"
                    for index in range(2,6):
                        assert BasicInfo.Button_Displayed(index)==False
                        
                    #Step3:  11.logout->Login with creater OM/LC/TL Again  to  enter this form->Click button 'Cancel Coaching'..
                            #12.From confirmation pop-up window:Click Yes button.
                            #13.On search main page, filter with status option 'canceled'.
                            #14.Enter this record detail page.
                    L.logout_tablet()
                    L.Login_tablet(self.tableturl, lobname, sitename, self.OMuserid, self.OMpassword)
                    Tablet.click_coachingcircle()
                    CoachHome.click_eachcoach(1)
                    BasicInfo.Click_Button(4)#Click button 'Cancel Coaching'
                    Canceled_Date_FromServer=GetConfig.get_ServerCurrentDate().replace("-","/")
                    CancelWindow.click_Button(1)#From confirmation pop-up window:Click Yes button.
                    CoachHome.select_status("Canceled")
                    CoachHome.click_filterbutton()
                    '''Check3:1.Back to coaching search main page with waring message shown:Coaching canceled successful
                              2.This coaching record is searched out with status 'Canceled' shown.
                              3.Canceled Date = The date when the form is canceled.'''
                    print CoachHome.get_anyCoach_attribute(1, 1),SN_coachhome
                    assert CoachHome.get_anyCoach_attribute(1, 1)==SN_coachhome
                    CoachHome.click_eachcoach(1)
                    assert BasicInfo.get_status()=="Canceled"
                    assert BasicInfo.get_canceleddate()==Canceled_Date_FromServer
                    L.logout_tablet()

    
    def tearDown(self):
        Gl.driver.quit()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_Commendation_OngoingToCanceled']
    unittest.main()