'''
Created on 20171010

@author: lei.tan
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
from CoachingAndTriadCoaching_Pages.LeadershipHuddleProcessConfirmation import LeadershipHuddleProcessConfirmation
from public_method.Coaching_PublicFunction import Coaching_PublicFunction
from Tablet_pages.HeaderPage import HeaderPage
from public_method.Get_AllRoleAccountForTest import Get_AllRoleAccountForTest
from Tablet_pages.CancelCoachingWindow import CancelCoachingWindow


class LeadershipHuddleProcessConfirmation_PlannedToCompleted(unittest.TestCase):


    def setUp(self):
        #Case ID
        self.caseID="LeadershipHuddleProcessConfirmation_PlannedToCompleted"
        
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
        self.coachformname="Leadership Huddle Process Confirmation" 
        self.coachpagetitle="Triad Coaching - "+self.coachformname
        
        self.CheckBox_CheckedStatus="fa fa-check-square"
        self.CheckBox_UnCheckedStatus="fa fa-uncheck"
        #self.CheckBox_CheckedStatus2="fa fa-check-circle radio-btn checked"
        #self.CheckBox_UnCheckedStatus2="fa fa-check-circle radio-btn"
        
        
        #Cancel window info
        self.CancelWindow_title="Confirmation"
        self.CancelWindow_content="Please confirm you want to cancel this To-Do!"


    def test_LeadershipHuddleProcessConfirmation_PlannedToCanceled(self):
        GetConfig=Get_configration_data()
        Tablet=TabletHomepage()
        Ppage=PerformancePage()
        TCoach=Coach_Triad_General()
        CoachHome=Coachinghomepage()
        BasicInfo=BasicInfoforCoaching()
        Header=HeaderPage()
        LeadershipHuddleProcessConfirmationForm=LeadershipHuddleProcessConfirmation()
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
                    '''Check1:Enter form detail page with title Triad Coaching - Commendation'''
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
                    assert LeadershipHuddleProcessConfirmationForm.specialtopic_disabled()=="true"
                    assert LeadershipHuddleProcessConfirmationForm.lastthreeinput_disabled(2)=="true"
                    assert LeadershipHuddleProcessConfirmationForm.lastthreeinput_disabled(3)=="true"
                    assert LeadershipHuddleProcessConfirmationForm.lastthreeinput_disabled(4)=="true"
                    f=2
                    while f<10:
                                f=f+2
                                assert LeadershipHuddleProcessConfirmationForm.otherinput_disabled(f)=="true"
                                
                    f1=11
                    while f1<19:
                                f1=f1+2
                                assert LeadershipHuddleProcessConfirmationForm.otherinput_disabled(f1)=="true"
                    f2=20
                    while f2<24:
                                f2=f2+2
                                assert LeadershipHuddleProcessConfirmationForm.otherinput_disabled(f2)=="true"
                    f3=25
                    while f3<39:
                                f3=f3+2
                                assert LeadershipHuddleProcessConfirmationForm.otherinput_disabled(f3)=="true"
                    assert LeadershipHuddleProcessConfirmationForm.otherinput_disabled(42)=="true"

                    
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
                    Tablet.click_Triadcoachingcirecle()
                    CoachHome.click_eachcoach(1)
                    CallRecordingNumber=self.CallRecordingNumber1
                    specialtopicBoxTitle=self.Longtextboxesprefix1+LeadershipHuddleProcessConfirmationForm.get_specialtopicBoxTitle()
                    lastthreeinputBoxTitle2=self.Longtextboxesprefix1+LeadershipHuddleProcessConfirmationForm.get_lastthreeinputBoxTitle(2)
                    lastthreeinputBoxTitle3=self.Longtextboxesprefix1+LeadershipHuddleProcessConfirmationForm.get_lastthreeinputBoxTitle(3)
                    lastthreeinputBoxTitle4=self.Longtextboxesprefix1+LeadershipHuddleProcessConfirmationForm.get_lastthreeinputBoxTitle(4)
                    otherinputBoxTitle1=self.Longtextboxesprefix1+LeadershipHuddleProcessConfirmationForm.get_otherinputBoxTitle(42)
                   

                    #DateandTimeofCall=The first day of date picker
                    #BasicInfo.input_callrecordingnumber(CallRecordingNumber)
                    if lobname != "AOL":
                        BasicInfo.input_callrecordingnumber(CallRecordingNumber)
                    LeadershipHuddleProcessConfirmationForm.input_lastthreeinput(2,lastthreeinputBoxTitle2)
                    LeadershipHuddleProcessConfirmationForm.input_lastthreeinput(3,lastthreeinputBoxTitle3)
                    LeadershipHuddleProcessConfirmationForm.input_lastthreeinput(4,lastthreeinputBoxTitle4)
                    LeadershipHuddleProcessConfirmationForm.input_specialtopic(specialtopicBoxTitle)
                    LeadershipHuddleProcessConfirmationForm.input_otherinput(42,otherinputBoxTitle1)
                    b=2
                    while b<10:
                                b=b+2
                                otherinputBoxTitle=self.Longtextboxesprefix1+LeadershipHuddleProcessConfirmationForm.get_otherinputBoxTitle(b)
                                LeadershipHuddleProcessConfirmationForm.input_otherinput(b,otherinputBoxTitle)
                                
                                
                    b1=11
                    while b1<19:
                                b1=b1+2
                                otherinputBoxTitle=self.Longtextboxesprefix1+LeadershipHuddleProcessConfirmationForm.get_otherinputBoxTitle(b1)
                                LeadershipHuddleProcessConfirmationForm.input_otherinput(b1,otherinputBoxTitle)
                                

                                
                    b2=20
                    while b2<24:
                                b2=b2+2
                                otherinputBoxTitle=self.Longtextboxesprefix1+LeadershipHuddleProcessConfirmationForm.get_otherinputBoxTitle(b2)
                                LeadershipHuddleProcessConfirmationForm.input_otherinput(b2,otherinputBoxTitle)
                                

                                
                    b3=25
                    while b3<39:
                                b3=b3+2
                                otherinputBoxTitle=self.Longtextboxesprefix1+LeadershipHuddleProcessConfirmationForm.get_otherinputBoxTitle(b3)
                                LeadershipHuddleProcessConfirmationForm.input_otherinput(b3,otherinputBoxTitle)
                      
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
                    assert BasicInfo.get_employeename()==TL_Name
                    assert BasicInfo.get_employeeHrid()==TL_hrid
                    assert BasicInfo.get_coachname()==LoginName
                    assert BasicInfo.get_createdate()==Created_Date_FromServer
                    if lobname != "AOL":
                        assert BasicInfo.get_callrecordingnumber()==CallRecordingNumber
                        
                    assert LeadershipHuddleProcessConfirmationForm.get_lastthreeinput(2)==lastthreeinputBoxTitle2
                    assert LeadershipHuddleProcessConfirmationForm.get_lastthreeinput(3)==lastthreeinputBoxTitle3
                    assert LeadershipHuddleProcessConfirmationForm.get_lastthreeinput(4)==lastthreeinputBoxTitle4
                    assert LeadershipHuddleProcessConfirmationForm.get_otherinput(42)==otherinputBoxTitle1  
                    e=2
                    while e<10:
                                e=e+2
                                otherinputBoxTitle=self.Longtextboxesprefix1+LeadershipHuddleProcessConfirmationForm.get_otherinputBoxTitle(e)
                                assert LeadershipHuddleProcessConfirmationForm.get_otherinput(e)==otherinputBoxTitle
                                
                                
                    e1=11
                    while e1<19:
                                e1=e1+2
                                otherinputBoxTitle=self.Longtextboxesprefix1+LeadershipHuddleProcessConfirmationForm.get_otherinputBoxTitle(e1)
                                assert LeadershipHuddleProcessConfirmationForm.get_otherinput(e1)==otherinputBoxTitle
                                

                                
                    e2=20
                    while e2<24:
                                e2=e2+2
                                otherinputBoxTitle=self.Longtextboxesprefix1+LeadershipHuddleProcessConfirmationForm.get_otherinputBoxTitle(e2)
                                assert LeadershipHuddleProcessConfirmationForm.get_otherinput(e2)==otherinputBoxTitle
                                

                                
                    e3=25
                    while e3<39:
                                e3=e3+2
                                otherinputBoxTitle=self.Longtextboxesprefix1+LeadershipHuddleProcessConfirmationForm.get_otherinputBoxTitle(e3)
                                assert LeadershipHuddleProcessConfirmationForm.get_otherinput(e3)==otherinputBoxTitle
                                
                            
                    assert BasicInfo.get_ButtonName(1)=="Print"
                    assert BasicInfo.get_ButtonName(2)=="Back"
                    for index in range(3,6):
                        assert BasicInfo.Button_Displayed(index)==False


    #def tearDown(self):
        #Gl.driver.quit()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()