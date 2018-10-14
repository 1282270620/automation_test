'''
Created on 2018.2.7

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
from CoachingAndTriadCoaching_Pages.MonthlyGoalSettingSupervisorPage import MonthlyGoalSettingSupervisorPage
from Tablet_pages.HeaderPage import HeaderPage
from public_method.Get_AllRoleAccountForTest import Get_AllRoleAccountForTest

class MonthlyGoalSettingSupervisor_PlannedToCompleted(unittest.TestCase):


    def setUp(self):
        #Case ID
        self.caseID="MonthlyGoalSettingSupervisor_PlannedToCompleted"
        
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
        self.coachformname="Monthly Goal Setting - Supervisor" 
        self.coachpagetitle="Triad Coaching - "+self.coachformname
        
        self.CheckBox_CheckedStatus="fa fa-check-square"
        self.CheckBox_UnCheckedStatus="fa fa-uncheck"
        
        #Cancel window info
        self.CancelWindow_title="Confirmation"
        self.CancelWindow_content="Please confirm you want to cancel this To-Do!"


    def test_GSPN_PlannedToCompleted(self):
        GetConfig=Get_configration_data()
        Tablet=TabletHomepage()
        Ppage=PerformancePage()
        TCoach=Coach_Triad_General()
        CoachHome=Coachinghomepage()
        BasicInfo=BasicInfoforCoaching()
        Header=HeaderPage()
        MonthlyGoalSettingSupervisorForm=MonthlyGoalSettingSupervisorPage()
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
                    userid=MonthlyGoalSettingSupervisorForm.get_firstTL_HRID(1)
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
                    '''Check1:Enter form detail page with title Triad Coaching - Goal Setting Plan and Notes Form'''
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
                    assert MonthlyGoalSettingSupervisorForm.ShortComments_disabled(2)=='true'
                    assert MonthlyGoalSettingSupervisorForm.ShortComments_disabled(6)=='true'
                    
                    assert MonthlyGoalSettingSupervisorForm.PreviousCurrentGoalComments_disabled(2, 2, 1)=='true'
                    assert MonthlyGoalSettingSupervisorForm.PreviousCurrentGoalComments_disabled(2, 2, 2)=='true'
                    assert MonthlyGoalSettingSupervisorForm.PreviousCurrentGoalComments_disabled(2, 3, 1)=='true'
                    assert MonthlyGoalSettingSupervisorForm.PreviousCurrentGoalComments_disabled(2, 3, 2)=='true'
                    assert MonthlyGoalSettingSupervisorForm.PreviousCurrentGoalComments_disabled(2, 4, 1)=='true'
                    assert MonthlyGoalSettingSupervisorForm.PreviousCurrentGoalComments_disabled(2, 4, 2)=='true'
                    assert MonthlyGoalSettingSupervisorForm.PreviousCurrentGoalComments_disabled(6, 2, 1)=='true'
                    assert MonthlyGoalSettingSupervisorForm.PreviousCurrentGoalComments_disabled(6, 2, 2)=='true'
                    assert MonthlyGoalSettingSupervisorForm.PreviousCurrentGoalComments_disabled(6, 3, 1)=='true'
                    assert MonthlyGoalSettingSupervisorForm.PreviousCurrentGoalComments_disabled(6, 3, 2)=='true'
                    assert MonthlyGoalSettingSupervisorForm.PreviousCurrentGoalComments_disabled(6, 4, 1)=='true'
                    assert MonthlyGoalSettingSupervisorForm.PreviousCurrentGoalComments_disabled(6, 4, 2)=='true'
                    
                    assert MonthlyGoalSettingSupervisorForm.LongComments1_disabled()=='true'
                    assert MonthlyGoalSettingSupervisorForm.LongComments2_disabled(4)=='true'
                    assert MonthlyGoalSettingSupervisorForm.LongComments2_disabled(5)=='true'
                    assert MonthlyGoalSettingSupervisorForm.LongComments2_disabled(7)=='true'
                    assert MonthlyGoalSettingSupervisorForm.LongComments2_disabled(8)=='true'
                    for i3 in range(10,15):
                        assert MonthlyGoalSettingSupervisorForm.LongComments3_disabled(i3, 2)=='true'
                        assert MonthlyGoalSettingSupervisorForm.LongComments3_disabled(i3, 3)=='true'
                        assert MonthlyGoalSettingSupervisorForm.LongComments3_disabled(i3, 5)=='true'
                        assert MonthlyGoalSettingSupervisorForm.LongComments3_disabled(i3, 6)=='true'
                    for i in range(10,15):
                        for j in range(1,6):
                            for k in range(1,3):
                                k1=0
                                if k==1:
                                    while(k1<7):
                                        k1=k1+1
                                        assert MonthlyGoalSettingSupervisorForm.GoalActualComments_disabled(i, k, j, k1)=='true'
                                else:
                                    while(k1<9):
                                        k1=k1+1
                                        assert MonthlyGoalSettingSupervisorForm.GoalActualComments_disabled(i, k, j, k1)=='true'
                                
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
                    MonthlyGoalSettingSupervisorForm.Input_ShortComments(2, self.Shorttextboxesprefix1)
                    MonthlyGoalSettingSupervisorForm.Input_ShortComments(6, self.Shorttextboxesprefix1)
                    MonthlyGoalSettingSupervisorForm.Input_LongComments1(self.Longtextboxesprefix1+MonthlyGoalSettingSupervisorForm.getLongTitle1())
                    MonthlyGoalSettingSupervisorForm.Input_LongComments2(4, (self.Longtextboxesprefix1+MonthlyGoalSettingSupervisorForm.getLongTitle2(4)))
                    MonthlyGoalSettingSupervisorForm.Input_LongComments2(5, (self.Longtextboxesprefix1+MonthlyGoalSettingSupervisorForm.getLongTitle2(5)))
                    MonthlyGoalSettingSupervisorForm.Input_LongComments2(7, (self.Longtextboxesprefix1+MonthlyGoalSettingSupervisorForm.getLongTitle2(7)))
                    MonthlyGoalSettingSupervisorForm.Input_LongComments2(8, (self.Longtextboxesprefix1+MonthlyGoalSettingSupervisorForm.getLongTitle2(8)))
                    for num in range(10,15):
                        MonthlyGoalSettingSupervisorForm.Input_LongComments3(num, 2, (self.Longtextboxesprefix1+MonthlyGoalSettingSupervisorForm.getLongTitle3(num, 2)))
                        MonthlyGoalSettingSupervisorForm.Input_LongComments3(num, 3, (self.Longtextboxesprefix1+MonthlyGoalSettingSupervisorForm.getLongTitle3(num, 3)))
                        MonthlyGoalSettingSupervisorForm.Input_LongComments3(num, 5, (self.Longtextboxesprefix1+MonthlyGoalSettingSupervisorForm.getLongTitle3(num, 5)))
                        MonthlyGoalSettingSupervisorForm.Input_LongComments3(num, 6, (self.Longtextboxesprefix1+MonthlyGoalSettingSupervisorForm.getLongTitle3(num, 6)))
                    MonthlyGoalSettingSupervisorForm.Input_PreviousCurrentGoalComments(2, 2, 1, self.Shorttextboxesprefix1)
                    MonthlyGoalSettingSupervisorForm.Input_PreviousCurrentGoalComments(2, 2, 2, self.Shorttextboxesprefix1)
                    MonthlyGoalSettingSupervisorForm.Input_PreviousCurrentGoalComments(2, 3, 1, self.Shorttextboxesprefix1)
                    MonthlyGoalSettingSupervisorForm.Input_PreviousCurrentGoalComments(2, 3, 2, self.Shorttextboxesprefix1)
                    MonthlyGoalSettingSupervisorForm.Input_PreviousCurrentGoalComments(2, 4, 1, self.Shorttextboxesprefix1)
                    MonthlyGoalSettingSupervisorForm.Input_PreviousCurrentGoalComments(2, 4, 2, self.Shorttextboxesprefix1)
                    MonthlyGoalSettingSupervisorForm.Input_PreviousCurrentGoalComments(6, 2, 1, self.Shorttextboxesprefix1)
                    MonthlyGoalSettingSupervisorForm.Input_PreviousCurrentGoalComments(6, 2, 2, self.Shorttextboxesprefix1)
                    MonthlyGoalSettingSupervisorForm.Input_PreviousCurrentGoalComments(6, 3, 1, self.Shorttextboxesprefix1)
                    MonthlyGoalSettingSupervisorForm.Input_PreviousCurrentGoalComments(6, 3, 2, self.Shorttextboxesprefix1)
                    MonthlyGoalSettingSupervisorForm.Input_PreviousCurrentGoalComments(6, 4, 1, self.Shorttextboxesprefix1)
                    MonthlyGoalSettingSupervisorForm.Input_PreviousCurrentGoalComments(6, 4, 2, self.Shorttextboxesprefix1)
                    
                    KpiValues1=('','KPI3','KPI5','KPI7','KPI9');
                    KpiValues2=('KPI2','KPI4','KPI6','KPI8','KPI10');
                    GoalValues1=('','1','5.26','1','1');
                    GoalValues2=('0','3.36','1','1','1.02');
                    ActualValues1=('','1','3.36','1','1.05');
                    ActualValues2=('1','5.26','1','10','1');
                    for n1 in range(10,15):
                        n2=1
                        for n3 in range(0,5):
                            MonthlyGoalSettingSupervisorForm.Input_GoalActualComments(n1, 1, n2,1, KpiValues1[n3])
                            MonthlyGoalSettingSupervisorForm.Input_GoalActualComments(n1, 1, n2,2, GoalValues1[n3])
                            MonthlyGoalSettingSupervisorForm.Input_GoalActualComments(n1, 1, n2,3, ActualValues1[n3])
                            MonthlyGoalSettingSupervisorForm.Input_GoalActualComments(n1, 1, n2,5, KpiValues2[n3])
                            MonthlyGoalSettingSupervisorForm.Input_GoalActualComments(n1, 1, n2,6, GoalValues2[n3])
                            MonthlyGoalSettingSupervisorForm.Input_GoalActualComments(n1, 1, n2,7, ActualValues2[n3])
                            n2=n2+1
                            
                    AgentValues=('','Agent9','','Agent5','Agent6');
                    T1GoalValues=('','93','','4','100');
                    T1ActualValues=('','90','','7','1000');
                    T2GoalValues=('','','','0','1');
                    T2ActualValues=('','','','3','1');
                    T3GoalValues=('','','','2','2');  
                    T3ActualValues=('','','','2','2');          
                    for m1 in range(10,15):
                        m2=1
                        for m3 in range(0,5):
                            MonthlyGoalSettingSupervisorForm.Input_GoalActualComments(m1, 2, m2, 1,AgentValues[m3])
                            MonthlyGoalSettingSupervisorForm.Input_GoalActualComments(m1, 2, m2, 2,T1GoalValues[m3])
                            MonthlyGoalSettingSupervisorForm.Input_GoalActualComments(m1, 2, m2, 3,T1ActualValues[m3])
                            MonthlyGoalSettingSupervisorForm.Input_GoalActualComments(m1, 2, m2, 5,T2GoalValues[m3])
                            MonthlyGoalSettingSupervisorForm.Input_GoalActualComments(m1, 2, m2, 6,T2ActualValues[m3])
                            MonthlyGoalSettingSupervisorForm.Input_GoalActualComments(m1, 2, m2, 8,T3GoalValues[m3])
                            MonthlyGoalSettingSupervisorForm.Input_GoalActualComments(m1, 2, m2, 9,T3ActualValues[m3])
                            m2=m2+1    
                    
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
                    '''Check4:13.On this GSPN form:
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
                    assert MonthlyGoalSettingSupervisorForm.get_ShortComments(2)==self.Shorttextboxesprefix1
                    assert MonthlyGoalSettingSupervisorForm.get_ShortComments(6)==self.Shorttextboxesprefix1
                    assert MonthlyGoalSettingSupervisorForm.get_PreviousCurrentGoalComments(2, 2, 1)==self.Shorttextboxesprefix1
                    assert MonthlyGoalSettingSupervisorForm.get_PreviousCurrentGoalComments(2, 2, 2)==self.Shorttextboxesprefix1
                    assert MonthlyGoalSettingSupervisorForm.get_PreviousCurrentGoalComments(2, 3, 1)==self.Shorttextboxesprefix1
                    assert MonthlyGoalSettingSupervisorForm.get_PreviousCurrentGoalComments(2, 3, 2)==self.Shorttextboxesprefix1
                    assert MonthlyGoalSettingSupervisorForm.get_PreviousCurrentGoalComments(2, 4, 1)==self.Shorttextboxesprefix1
                    assert MonthlyGoalSettingSupervisorForm.get_PreviousCurrentGoalComments(2, 4, 2)==self.Shorttextboxesprefix1
                    assert MonthlyGoalSettingSupervisorForm.get_PreviousCurrentGoalComments(6, 2, 1)==self.Shorttextboxesprefix1
                    assert MonthlyGoalSettingSupervisorForm.get_PreviousCurrentGoalComments(6, 2, 2)==self.Shorttextboxesprefix1
                    assert MonthlyGoalSettingSupervisorForm.get_PreviousCurrentGoalComments(6, 3, 1)==self.Shorttextboxesprefix1
                    assert MonthlyGoalSettingSupervisorForm.get_PreviousCurrentGoalComments(6, 3, 2)==self.Shorttextboxesprefix1
                    assert MonthlyGoalSettingSupervisorForm.get_PreviousCurrentGoalComments(6, 4, 1)==self.Shorttextboxesprefix1
                    assert MonthlyGoalSettingSupervisorForm.get_PreviousCurrentGoalComments(6, 4, 2)==self.Shorttextboxesprefix1
                    assert MonthlyGoalSettingSupervisorForm.get_LongComments1()==self.Longtextboxesprefix1+MonthlyGoalSettingSupervisorForm.getLongTitle1()
                    assert MonthlyGoalSettingSupervisorForm.get_LongComments2(4)==self.Longtextboxesprefix1+MonthlyGoalSettingSupervisorForm.getLongTitle2(4)
                    assert MonthlyGoalSettingSupervisorForm.get_LongComments2(5)==self.Longtextboxesprefix1+MonthlyGoalSettingSupervisorForm.getLongTitle2(5)
                    assert MonthlyGoalSettingSupervisorForm.get_LongComments2(7)==self.Longtextboxesprefix1+MonthlyGoalSettingSupervisorForm.getLongTitle2(7)
                    assert MonthlyGoalSettingSupervisorForm.get_LongComments2(8)==self.Longtextboxesprefix1+MonthlyGoalSettingSupervisorForm.getLongTitle2(8)
                    for num2 in range(10,15):
                        assert MonthlyGoalSettingSupervisorForm.get_LongComments3(num2, 2)==self.Longtextboxesprefix1+MonthlyGoalSettingSupervisorForm.getLongTitle3(num2, 2)
                        assert MonthlyGoalSettingSupervisorForm.get_LongComments3(num2, 3)==self.Longtextboxesprefix1+MonthlyGoalSettingSupervisorForm.getLongTitle3(num2, 3)
                        assert MonthlyGoalSettingSupervisorForm.get_LongComments3(num2, 5)==self.Longtextboxesprefix1+MonthlyGoalSettingSupervisorForm.getLongTitle3(num2, 5)
                        assert MonthlyGoalSettingSupervisorForm.get_LongComments3(num2, 6)==self.Longtextboxesprefix1+MonthlyGoalSettingSupervisorForm.getLongTitle3(num2, 6)                    
                    for num3 in range(10,15):
                        assert MonthlyGoalSettingSupervisorForm.get_GoalActualComments(num3, 1, 1, 1)==''
                        assert MonthlyGoalSettingSupervisorForm.get_GoalActualComments(num3, 1, 1, 2)==''
                        assert MonthlyGoalSettingSupervisorForm.get_GoalActualComments(num3, 1, 1, 3)==''
                        assert MonthlyGoalSettingSupervisorForm.get_GoalActualComments(num3, 1, 1, 4)==''
                        assert MonthlyGoalSettingSupervisorForm.get_GoalActualComments(num3, 1, 1, 5)=='KPI2'
                        assert MonthlyGoalSettingSupervisorForm.get_GoalActualComments(num3, 1, 1, 6)=='0'
                        assert MonthlyGoalSettingSupervisorForm.get_GoalActualComments(num3, 1, 1, 7)=='1'
                        assert MonthlyGoalSettingSupervisorForm.get_GoalActualComments(num3, 1, 1, 8)=='1.00'
                        assert MonthlyGoalSettingSupervisorForm.get_GoalActualComments(num3, 1, 2, 1)=='KPI3'
                        assert MonthlyGoalSettingSupervisorForm.get_GoalActualComments(num3, 1, 2, 2)=='1'
                        assert MonthlyGoalSettingSupervisorForm.get_GoalActualComments(num3, 1, 2, 3)=='1'
                        assert MonthlyGoalSettingSupervisorForm.get_GoalActualComments(num3, 1, 2, 4)=='0.00'
                        assert MonthlyGoalSettingSupervisorForm.get_GoalActualComments(num3, 1, 2, 5)=='KPI4'
                        assert MonthlyGoalSettingSupervisorForm.get_GoalActualComments(num3, 1, 2, 6)=='3.36'
                        assert MonthlyGoalSettingSupervisorForm.get_GoalActualComments(num3, 1, 2, 7)=='5.26'
                        assert MonthlyGoalSettingSupervisorForm.get_GoalActualComments(num3, 1, 2, 8)=='1.90'
                        assert MonthlyGoalSettingSupervisorForm.get_GoalActualComments(num3, 1, 3, 1)=='KPI5'
                        assert MonthlyGoalSettingSupervisorForm.get_GoalActualComments(num3, 1, 3, 2)=='5.26'
                        assert MonthlyGoalSettingSupervisorForm.get_GoalActualComments(num3, 1, 3, 3)=='3.36'
                        assert MonthlyGoalSettingSupervisorForm.get_GoalActualComments(num3, 1, 3, 4)=='-1.90'
                        assert MonthlyGoalSettingSupervisorForm.get_GoalActualComments(num3, 1, 3, 5)=='KPI6'
                        assert MonthlyGoalSettingSupervisorForm.get_GoalActualComments(num3, 1, 3, 6)=='1'
                        assert MonthlyGoalSettingSupervisorForm.get_GoalActualComments(num3, 1, 3, 7)=='1'
                        assert MonthlyGoalSettingSupervisorForm.get_GoalActualComments(num3, 1, 3, 8)=='0.00'
                        assert MonthlyGoalSettingSupervisorForm.get_GoalActualComments(num3, 1, 4, 1)=='KPI7'
                        assert MonthlyGoalSettingSupervisorForm.get_GoalActualComments(num3, 1, 4, 2)=='1'
                        assert MonthlyGoalSettingSupervisorForm.get_GoalActualComments(num3, 1, 4, 3)=='1'
                        assert MonthlyGoalSettingSupervisorForm.get_GoalActualComments(num3, 1, 4, 4)=='0.00'
                        assert MonthlyGoalSettingSupervisorForm.get_GoalActualComments(num3, 1, 4, 5)=='KPI8'
                        assert MonthlyGoalSettingSupervisorForm.get_GoalActualComments(num3, 1, 4, 6)=='1'
                        assert MonthlyGoalSettingSupervisorForm.get_GoalActualComments(num3, 1, 4, 7)=='10'
                        assert MonthlyGoalSettingSupervisorForm.get_GoalActualComments(num3, 1, 4, 8)=='9.00'
                        assert MonthlyGoalSettingSupervisorForm.get_GoalActualComments(num3, 1, 5, 1)=='KPI9'
                        assert MonthlyGoalSettingSupervisorForm.get_GoalActualComments(num3, 1, 5, 2)=='1'
                        assert MonthlyGoalSettingSupervisorForm.get_GoalActualComments(num3, 1, 5, 3)=='1.05'
                        assert MonthlyGoalSettingSupervisorForm.get_GoalActualComments(num3, 1, 5, 4)=='0.05'
                        assert MonthlyGoalSettingSupervisorForm.get_GoalActualComments(num3, 1, 5, 5)=='KPI10'
                        assert MonthlyGoalSettingSupervisorForm.get_GoalActualComments(num3, 1, 5, 6)=='1.02'
                        assert MonthlyGoalSettingSupervisorForm.get_GoalActualComments(num3, 1, 5, 7)=='1'
                        assert MonthlyGoalSettingSupervisorForm.get_GoalActualComments(num3, 1, 5, 8)=='-0.02'
                        
                        assert MonthlyGoalSettingSupervisorForm.get_GoalActualComments(num3, 2, 1, 1)==''
                        assert MonthlyGoalSettingSupervisorForm.get_GoalActualComments(num3, 2, 1, 2)==''
                        assert MonthlyGoalSettingSupervisorForm.get_GoalActualComments(num3, 2, 1, 3)==''
                        assert MonthlyGoalSettingSupervisorForm.get_GoalActualComments(num3, 2, 1, 4)==''
                        assert MonthlyGoalSettingSupervisorForm.get_GoalActualComments(num3, 2, 1, 5)==''
                        assert MonthlyGoalSettingSupervisorForm.get_GoalActualComments(num3, 2, 1, 6)==''
                        assert MonthlyGoalSettingSupervisorForm.get_GoalActualComments(num3, 2, 1, 7)==''
                        assert MonthlyGoalSettingSupervisorForm.get_GoalActualComments(num3, 2, 1, 8)==''
                        assert MonthlyGoalSettingSupervisorForm.get_GoalActualComments(num3, 2, 1, 9)==''
                        assert MonthlyGoalSettingSupervisorForm.get_GoalActualComments(num3, 2, 1, 10)==''
                        assert MonthlyGoalSettingSupervisorForm.get_GoalActualComments(num3, 2, 2, 1)=='Agent9'
                        assert MonthlyGoalSettingSupervisorForm.get_GoalActualComments(num3, 2, 2, 2)=='93'
                        assert MonthlyGoalSettingSupervisorForm.get_GoalActualComments(num3, 2, 2, 3)=='90'
                        assert MonthlyGoalSettingSupervisorForm.get_GoalActualComments(num3, 2, 2, 4)=='-3.00'
                        assert MonthlyGoalSettingSupervisorForm.get_GoalActualComments(num3, 2, 2, 5)==''
                        assert MonthlyGoalSettingSupervisorForm.get_GoalActualComments(num3, 2, 2, 6)==''
                        assert MonthlyGoalSettingSupervisorForm.get_GoalActualComments(num3, 2, 2, 7)==''
                        assert MonthlyGoalSettingSupervisorForm.get_GoalActualComments(num3, 2, 2, 8)==''
                        assert MonthlyGoalSettingSupervisorForm.get_GoalActualComments(num3, 2, 2, 9)==''
                        assert MonthlyGoalSettingSupervisorForm.get_GoalActualComments(num3, 2, 2, 10)==''
                        assert MonthlyGoalSettingSupervisorForm.get_GoalActualComments(num3, 2, 3, 1)==''
                        assert MonthlyGoalSettingSupervisorForm.get_GoalActualComments(num3, 2, 3, 2)==''
                        assert MonthlyGoalSettingSupervisorForm.get_GoalActualComments(num3, 2, 3, 3)==''
                        assert MonthlyGoalSettingSupervisorForm.get_GoalActualComments(num3, 2, 3, 4)==''
                        assert MonthlyGoalSettingSupervisorForm.get_GoalActualComments(num3, 2, 3, 5)==''
                        assert MonthlyGoalSettingSupervisorForm.get_GoalActualComments(num3, 2, 3, 6)==''
                        assert MonthlyGoalSettingSupervisorForm.get_GoalActualComments(num3, 2, 3, 7)==''
                        assert MonthlyGoalSettingSupervisorForm.get_GoalActualComments(num3, 2, 3, 8)==''
                        assert MonthlyGoalSettingSupervisorForm.get_GoalActualComments(num3, 2, 3, 9)==''
                        assert MonthlyGoalSettingSupervisorForm.get_GoalActualComments(num3, 2, 3, 10)==''
                        assert MonthlyGoalSettingSupervisorForm.get_GoalActualComments(num3, 2, 4, 1)=='Agent5'
                        assert MonthlyGoalSettingSupervisorForm.get_GoalActualComments(num3, 2, 4, 2)=='4'
                        assert MonthlyGoalSettingSupervisorForm.get_GoalActualComments(num3, 2, 4, 3)=='7'
                        assert MonthlyGoalSettingSupervisorForm.get_GoalActualComments(num3, 2, 4, 4)=='3.00'
                        assert MonthlyGoalSettingSupervisorForm.get_GoalActualComments(num3, 2, 4, 5)=='0'
                        assert MonthlyGoalSettingSupervisorForm.get_GoalActualComments(num3, 2, 4, 6)=='3'
                        assert MonthlyGoalSettingSupervisorForm.get_GoalActualComments(num3, 2, 4, 7)=='3.00'
                        assert MonthlyGoalSettingSupervisorForm.get_GoalActualComments(num3, 2, 4, 8)=='2'
                        assert MonthlyGoalSettingSupervisorForm.get_GoalActualComments(num3, 2, 4, 9)=='2'
                        assert MonthlyGoalSettingSupervisorForm.get_GoalActualComments(num3, 2, 4, 10)=='0.00'
                        assert MonthlyGoalSettingSupervisorForm.get_GoalActualComments(num3, 2, 5, 1)=='Agent6'
                        assert MonthlyGoalSettingSupervisorForm.get_GoalActualComments(num3, 2, 5, 2)=='100'
                        assert MonthlyGoalSettingSupervisorForm.get_GoalActualComments(num3, 2, 5, 3)=='1000'
                        assert MonthlyGoalSettingSupervisorForm.get_GoalActualComments(num3, 2, 5, 4)=='900.00'
                        assert MonthlyGoalSettingSupervisorForm.get_GoalActualComments(num3, 2, 5, 5)=='1'
                        assert MonthlyGoalSettingSupervisorForm.get_GoalActualComments(num3, 2, 5, 6)=='1'
                        assert MonthlyGoalSettingSupervisorForm.get_GoalActualComments(num3, 2, 5, 7)=='0.00'
                        assert MonthlyGoalSettingSupervisorForm.get_GoalActualComments(num3, 2, 5, 8)=='2'
                        assert MonthlyGoalSettingSupervisorForm.get_GoalActualComments(num3, 2, 5, 9)=='2'
                        assert MonthlyGoalSettingSupervisorForm.get_GoalActualComments(num3, 2, 5, 10)=='0.00'
                    
                    assert BasicInfo.get_ButtonName(1)=="Print"
                    assert BasicInfo.get_ButtonName(2)=="Back"
                    for index in range(3,6):
                        assert BasicInfo.Button_Displayed(index)==False


    def tearDown(self):
        Gl.driver.quit()
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()