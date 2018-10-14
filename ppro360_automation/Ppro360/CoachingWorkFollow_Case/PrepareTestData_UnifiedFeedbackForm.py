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
from public_method.LeadershipAcademyCoachingScoresPage import  LeadershipAcademyCoachingScoresPage
from Tablet_pages.CancelCoachingWindow import CancelCoachingWindow



class PrepareTestData_UnifiedFeedbackForm(unittest.TestCase):


    def setUp(self):
        #Case ID
        self.caseID="PrepareTestData_UnifiedFeedbackForm"
        
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


    def test_CreatUnifiedFeedbackFormDate(self):
        GetConfig=Get_configration_data()
        Tablet=TabletHomepage()
        Ppage=PerformancePage()
        TCoach=Coach_Triad_General()
        CoachHome=Coachinghomepage()
        BasicInfo=BasicInfoforCoaching()
        LeadershipAcademyCoachingScoresPagex=LeadershipAcademyCoachingScoresPage()
        Header=HeaderPage()
        UnifiedFeedbackFormForm=UnifiedFeedbackForm()
        Getaccount=Get_AllRoleAccountForTest()
        CancelWindow=CancelCoachingWindow()
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
                    #TLInfo_Dic=Getaccount.get_TLInfoandAgentHridFromPerformance(self.tableturl, lobname, sitename, self.OMuserid, self.OMpassword,"Month-To-Date")
                    #TL_Name=TLInfo_Dic["TLName"]
                    #TL_hrid=TLInfo_Dic["TLHrid"]
                    #TL_password="111111"
                    
                    #TL_password=TLInfo_Dic["TLPassword"]
                    #AgentInfo_Dic=Getaccount.get_AgentInfoFromTablet(self.tableturl, lobname, sitename, self.OMuserid, self.OMpassword,"Month-To-Date")
                    #Agent_name=AgentInfo_Dic["AgentName"]
                    #Agent_hrid=AgentInfo_Dic["AgentHrid"]
                    #Agent_password="111111"
                    #Agent_password=AgentInfo_Dic["AgentPassword"]
                    TL_Name="Tl2 Test"
                    TL_hrid="64135"
                    TL_password="111111"
                    Agent_name="Agent 12"
                    Agent_hrid="169919"
                    Agent_password="9/Ax474M"
                    LC_Name="LC 1"
                    LC_hrid="88888888"
                    LC_password="111111"
                    L=Login()
                    L.Login_tablet(self.tableturl, lobname, sitename, TL_hrid, TL_password)
                    time.sleep(Gl.waittime)
                    #Step2:1. Login with LC/OM  account to enter performance dashboard Month-To-Date page.

                    Tablet.click_performancecircle()
                   
                    #Step3:2. Select one TL ->select the first KPI to add this form;
                    print "Start=====Monthly-To-Day is in testing",
                    #Ppage.select_Agentkpi()
                    #Ppage.unselect_Agentkpi()
                    if lobname in Gl.DoubleKPIname_lob:
                        KPInumber=Ppage.get_KPInumber_All()
                    else:
                        KPInumber=Ppage.get_KPInumber()
                    
                    if lobname in Gl.performancefor_MultiTimeTab_lob:
                        Ppage.click_timetab_performance(5)#Ppage.click_mtd()
                    else:    
                        Ppage.click_timetab_performance(3)#Ppage.click_mtd()
                    Ppage.select_AnyKpiOfAgent_TL(1,2)#select the first KPI
                    Ppage.click_addcoachbutton()
                    TCoach.Add_AnyCoachOrTriad(self.coachformname)
                    Created_Date_FromServer=GetConfig.get_ServerCurrentDate().replace("-","/")
                    #Step4: #a.Enter triad coaching module.
                            #b.Select this coaching record to enter form detail page.
                    Header.click_backbutton()
                    '''Tablet.click_LeadershipAcademyCoachingScores(7)
                    assert LeadershipAcademyCoachingScoresPagex.get_datevalu(1, 1)==""
                    assert LeadershipAcademyCoachingScoresPagex.get_datevalu(2, 1)==""
                    assert LeadershipAcademyCoachingScoresPagex.get_datevalu(1, 2)==""
                    assert LeadershipAcademyCoachingScoresPagex.get_statusvalue()=="Acknowledged"
                    LeadershipAcademyCoachingScoresPagex.click_status()
                    LeadershipAcademyCoachingScoresPagex.click_selectstatus(1)
                    assert LeadershipAcademyCoachingScoresPagex.get_statusvalue()=="completed"
                    LeadershipAcademyCoachingScoresPagex.click_status()
                    LeadershipAcademyCoachingScoresPagex.click_selectstatus(2)
                    assert LeadershipAcademyCoachingScoresPagex.get_statusvalue()=="Acknowledged"
                    LeadershipAcademyCoachingScoresPagex.click_status()
                    LeadershipAcademyCoachingScoresPagex.click_selectstatus(3)
                    assert LeadershipAcademyCoachingScoresPagex.get_statusvalue()=="Completed and Acknowledged"'''
                    
                    #SN_CoachHome=CoachHome.get_anyCoach_attribute(1, 1)
                    #LeadershipAcademyCoachingScoresPagex.click_back()
                    #CoachHome.click_eachcoach(6)
                    '''Step1:creat "planned"status form of UnifiedFeedbackForm(TL)'''
                    #assert Header.get_HeaderTittle()==self.coachpagetitle
                    
                    #Step5:  4. Logout and login the TL  who is coached in this form;
                            #5. Enter triad Coach module.
                            #6. Select this coaching record to open this form detail page.
                            #7. Try to edit the form
                    Tablet.click_performancecircle()
                    if lobname in Gl.DoubleKPIname_lob:
                        KPInumber=Ppage.get_KPInumber_All()
                    else:
                        KPInumber=Ppage.get_KPInumber()
                    
                    if lobname in Gl.performancefor_MultiTimeTab_lob:
                        Ppage.click_timetab_performance(5)#Ppage.click_mtd()
                    else:    
                        Ppage.click_timetab_performance(3)#Ppage.click_mtd()
                    Ppage.select_AnyKpiOfAgent_TL(1,2)#select the first KPI
                    Ppage.click_addcoachbutton()
                    TCoach.Add_AnyCoachOrTriad(self.coachformname)
                    Created_Date_FromServer=GetConfig.get_ServerCurrentDate().replace("-","/")
                    #Step4: #a.Enter triad coaching module.
                            #b.Select this coaching record to enter form detail page.
                    Header.click_backbutton()
                    Tablet.click_TL_coachingcircle()
                    CoachHome.click_filterbutton()
                    SN_Actual=CoachHome.get_anyCoach_attribute(1, 1)
                    CoachHome.click_eachcoach(1)
                    commentsTitle1=self.Shorttextboxesprefix1+UnifiedFeedbackFormForm.get_shortinputBoxtitle(2,2)
                    commentsTitle2=self.Shorttextboxesprefix1+UnifiedFeedbackFormForm.get_shortinputBoxtitle(3,1)
                    commentsTitle3=self.Shorttextboxesprefix1+UnifiedFeedbackFormForm.get_shortinputBoxtitle(3,2)
                    longinput1=self.Longtextboxesprefix1+UnifiedFeedbackFormForm.get_longinputBoxtitle(2)
                    longinput2=self.Longtextboxesprefix1+UnifiedFeedbackFormForm.get_longinputBoxtitle(6)
                    midinput1=self.Longtextboxesprefix1+UnifiedFeedbackFormForm.get_midinputBoxtitle(1,1)
                    midinput2=self.Longtextboxesprefix1+UnifiedFeedbackFormForm.get_midinputBoxtitle(1,2)
                    UnifiedFeedbackFormForm.input_longinput(2, longinput1)
                    UnifiedFeedbackFormForm.input_longinput(6, longinput2)
                    UnifiedFeedbackFormForm.input_midinput(1,1, midinput1)
                    UnifiedFeedbackFormForm.input_midinput(1,2, midinput2)
                    UnifiedFeedbackFormForm.click_pointchoose(16,2, 2)
                    UnifiedFeedbackFormForm.click_pointchoose(6,1,1)
                    UnifiedFeedbackFormForm.click_pointchoose(6,2,1)
                    UnifiedFeedbackFormForm.click_pointchoose(8,1,1)
                    UnifiedFeedbackFormForm.click_pointchoose(8,2,1)
                    UnifiedFeedbackFormForm.click_pointchoose(8,3,1)
                    UnifiedFeedbackFormForm.click_pointchoose(10,2,1)
                    UnifiedFeedbackFormForm.click_pointchoose(10,3,1)
                    UnifiedFeedbackFormForm.click_pointchoose(12,1,1)
                    UnifiedFeedbackFormForm.click_pointchoose(12,2,1)
                    UnifiedFeedbackFormForm.click_pointchoose(12,3,1)
                    UnifiedFeedbackFormForm.click_pointchoose(14,2,1)
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
                    BasicInfo.Click_Button(2)
                    #Step3:2. Select one TL ->select the first KPI to add this form;
                    '''Step2:creat "Ongoing"status form of UnifiedFeedbackForm(TL)'''
                    L.logout_tablet()
                    L=Login()
                    L.Login_tablet(self.tableturl, lobname, sitename, TL_hrid, TL_password)
                    time.sleep(Gl.waittime)
                    Tablet.click_performancecircle()
                    if lobname in Gl.DoubleKPIname_lob:
                        KPInumber=Ppage.get_KPInumber_All()
                    else:
                        KPInumber=Ppage.get_KPInumber()
                    
                    if lobname in Gl.performancefor_MultiTimeTab_lob:
                        Ppage.click_timetab_performance(5)#Ppage.click_mtd()
                    else:    
                        Ppage.click_timetab_performance(3)#Ppage.click_mtd()
                    Ppage.select_AnyKpiOfAgent_TL(1,2)#select the first KPI
                    Ppage.click_addcoachbutton()
                    TCoach.Add_AnyCoachOrTriad(self.coachformname)
                    Created_Date_FromServer=GetConfig.get_ServerCurrentDate().replace("-","/")
                    Header.click_backbutton()
                    Tablet.click_TL_coachingcircle()
                    CoachHome.click_filterbutton()
                    SN_Actual=CoachHome.get_anyCoach_attribute(1, 1)
                    CoachHome.click_eachcoach(1)
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
                    UnifiedFeedbackFormForm.input_longinput(2, longinput1)
                    UnifiedFeedbackFormForm.input_longinput(6, longinput2)
                    UnifiedFeedbackFormForm.input_midinput(1,1, midinput1)
                    UnifiedFeedbackFormForm.input_midinput(1,2, midinput2)
                    UnifiedFeedbackFormForm.click_pointchoose(16,1, 1)
                    UnifiedFeedbackFormForm.click_pointchoose(16,2, 1)
                    b1=4
                    while b1<14:
                        b1=b1+2
                        c1=0
                        while c1<3:
                            c1=c1+1
                            UnifiedFeedbackFormForm.click_pointchoose(b1,c1,1)
                    BasicInfo.Click_Button(3)
                    L.logout_tablet()
                    L.Login_tablet(self.tableturl, lobname, sitename, Agent_hrid, Agent_password)
                    Tablet.click_Agent_coachingcircle()
                    CoachHome.select_status("Completed")
                    CoachHome.click_filterbutton()
                    SN_inAgentCoachHomepage=CoachHome.get_anyCoach_attribute(1, 1)
                    CoachHome.click_eachcoach(1)
                    BasicInfo.Click_Button(1)
                    #Header.click_backbutton()
                    #Tablet.click_LeadershipAcademyCoachingScores(4)
                    assert LeadershipAcademyCoachingScoresPagex.get_datevalu(1, 1)==""
                    assert LeadershipAcademyCoachingScoresPagex.get_datevalu(2, 1)==""
                    assert LeadershipAcademyCoachingScoresPagex.get_datevalu(1, 2)==""
                    assert LeadershipAcademyCoachingScoresPagex.get_statusvalue()=="Acknowledged"
                    LeadershipAcademyCoachingScoresPagex.click_status()
                    LeadershipAcademyCoachingScoresPagex.click_selectstatus(1)
                    assert LeadershipAcademyCoachingScoresPagex.get_statusvalue()=="completed"
                    LeadershipAcademyCoachingScoresPagex.click_status()
                    LeadershipAcademyCoachingScoresPagex.click_selectstatus(2)
                    assert LeadershipAcademyCoachingScoresPagex.get_statusvalue()=="Acknowledged"
                    LeadershipAcademyCoachingScoresPagex.click_status()
                    LeadershipAcademyCoachingScoresPagex.click_selectstatus(3)
                    assert LeadershipAcademyCoachingScoresPagex.get_statusvalue()=="Completed and Acknowledged"
                    
                    #SN_CoachHome=CoachHome.get_anyCoach_attribute(1, 1)
                    LeadershipAcademyCoachingScoresPagex.click_back()
                    '''Step3:creat "Acknowledged"status form of UnifiedFeedbackForm(TL)'''
                    L.logout_tablet()
                    L=Login()
                    L.Login_tablet(self.tableturl, lobname, sitename, LC_hrid, LC_password)
                    time.sleep(Gl.waittime)
                    Tablet.click_performancecircle()
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
                    Header.click_backbutton()
                    Tablet.click_coachingcircle()
                    CoachHome.click_filterbutton()
                    SN_Actual=CoachHome.get_anyCoach_attribute(1, 1)
                    CoachHome.click_eachcoach(1)
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
                    UnifiedFeedbackFormForm.input_longinput(2, longinput1)
                    UnifiedFeedbackFormForm.input_longinput(6, longinput2)
                    UnifiedFeedbackFormForm.input_midinput(1,1, midinput1)
                    UnifiedFeedbackFormForm.input_midinput(1,2, midinput2)
                    UnifiedFeedbackFormForm.click_pointchoose(16,1, 2)
                    UnifiedFeedbackFormForm.click_pointchoose(16,2, 2)
                    UnifiedFeedbackFormForm.click_pointchoose(10,2, 2)
                    UnifiedFeedbackFormForm.click_pointchoose(12,1, 2)
                    UnifiedFeedbackFormForm.click_pointchoose(12,3, 2)
                    BasicInfo.Click_Button(3)
                    '''Step4:creat "completed"status form of UnifiedFeedbackForm(LC)'''
                    L.logout_tablet()
                    L=Login()
                    L.Login_tablet(self.tableturl, lobname, sitename, self.OMuserid, self.OMpassword)
                    time.sleep(Gl.waittime)
                    Tablet.click_performancecircle()
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
                    Header.click_backbutton()
                    Tablet.click_coachingcircle()
                    CoachHome.click_filterbutton()
                    SN_Actual=CoachHome.get_anyCoach_attribute(1, 1)
                    CoachHome.click_eachcoach(1)
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
                    UnifiedFeedbackFormForm.input_longinput(2, longinput1)
                    UnifiedFeedbackFormForm.input_longinput(6, longinput2)
                    UnifiedFeedbackFormForm.input_midinput(1,1, midinput1)
                    UnifiedFeedbackFormForm.input_midinput(1,2, midinput2)
                    UnifiedFeedbackFormForm.click_pointchoose(16,1, 2)
                    UnifiedFeedbackFormForm.click_pointchoose(6,2, 1)
                    UnifiedFeedbackFormForm.click_pointchoose(6,3, 1)
                    UnifiedFeedbackFormForm.click_pointchoose(8,1, 1)
                    UnifiedFeedbackFormForm.click_pointchoose(8,2, 1)
                    UnifiedFeedbackFormForm.click_pointchoose(8,3, 1)
                    UnifiedFeedbackFormForm.click_pointchoose(10,1, 1)
                    UnifiedFeedbackFormForm.click_pointchoose(10,3, 1)
                    UnifiedFeedbackFormForm.click_pointchoose(12,1, 1)
                    UnifiedFeedbackFormForm.click_pointchoose(12,2, 1)
                    UnifiedFeedbackFormForm.click_pointchoose(12,3, 1)
                    BasicInfo.Click_Button(2)
                    CoachHome.click_eachcoach(1)
                    BasicInfo.Click_Button(4)#Click button 'Cancel Coaching'
                    CancelWindow.click_Button(1)
                    '''Step5:creat "canceled"status form of UnifiedFeedbackForm(OM)'''
    #def tearDown(self):
        #Gl.driver.quit()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()