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
import MySQLdb
from Tablet_pages.MeetGreetGTNKProcessConfirmation import MeetGreetGTNKProcessConfirmation
from public_method.Coaching_PublicFunction import Coaching_PublicFunction
from Tablet_pages.HeaderPage import HeaderPage
from public_method.Get_AllRoleAccountForTest import Get_AllRoleAccountForTest
from Tablet_pages.CancelCoachingWindow import CancelCoachingWindow


class MeetGreetGTNKProcessConfirmation_PlannedToCanceled(unittest.TestCase):


    def setUp(self):
        #Case ID
        self.caseID="MeetGreetGTNKProcessConfirmation_PlannedToCanceled"
        
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
        #coaching or Triad coaching
        self.coachtype="coaching"  
        #Coachformname
        self.coachhometitle="Coaching"
        self.coachformname="Meet & Greet - GTNY Process Confirmation" 
        self.coachpagetitle="Coaching - "+self.coachformname
        
        self.CheckBox_CheckedStatus="fa fa-check-square"
        self.CheckBox_UnCheckedStatus="fa fa-uncheck"
        
        #Cancel window info
        self.CancelWindow_title="Confirmation"
        self.CancelWindow_content="Please confirm you want to cancel this To-Do!"


    def test_MeetGreetGTNKProcessConfirmation_PlannedToCanceled(self):
        GetConfig=Get_configration_data()
        Tablet=TabletHomepage()
        Ppage=PerformancePage()
        TCoach=Coach_Triad_General()
        CoachHome=Coachinghomepage()
        BasicInfo=BasicInfoforCoaching()
        CoachPublic=Coaching_PublicFunction()
        Header=HeaderPage()
        MeetGreetGTNKProcessConfirmationForm=MeetGreetGTNKProcessConfirmation()
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
                   
                    #Step1:Login tablet,and Get AgentInfo using for testing
                    AgentInfo_Dic=Getaccount.get_AgentInfoFromTablet(self.tableturl, lobname, sitename, self.OMuserid, self.OMpassword,"Month-To-Date")
                    Agent_name=AgentInfo_Dic["AgentName"]
                    Agent_hrid=AgentInfo_Dic["AgentHrid"]
                    Agent_password=AgentInfo_Dic["AgentPassword"]
                    L=Login()
                    L.Login_tablet(self.tableturl,lobname,sitename,self.OMuserid,self.OMpassword)
                    time.sleep(Gl.waittime)
                    LoginName=Header.get_loginName()
                    #Step2:Enter performance 'Month-To-Date' page
                    Tablet.click_performancecircle()
                   
                    #Step3:select agent->select all KPIs to add  this  form.
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
                    Ppage.select_AnyKpiOfAgent_OM(KPInumber)#select all KPIs
                    Ppage.click_addcoachbutton()
                    TCoach.Add_AnyCoachOrTriad(self.coachformname)
                    Created_Date_FromServer=GetConfig.get_ServerCurrentDate().replace("-","/")
                    #Step4:Enter Coaching module.And Open this Commendation coaching form.
                    Header.click_backbutton()
                    Tablet.click_coachingcircle()
                    
                    
                    SN_CoachHome=CoachHome.get_anyCoach_attribute(1, 1)
                    CoachHome.click_eachcoach(1)
                    '''Check1:Enter form detail page with title Coaching - Commendation'''
                    assert Header.get_HeaderTittle()==self.coachpagetitle
                    
                    #Step5:Click button "Cancel Coaching"
                    BasicInfo.Click_Button(4)
                    '''Check2: 1.Pop up window with  title 'Comfirmation'.
                               2.Content 'Please confirm you want to cancel this To-Do!'
                               3.Show two buttons:Yes,Cancel'''
                    assert CancelWindow.get_windowtitle()==self.CancelWindow_title
                    assert CancelWindow.get_windowcontent()==self.CancelWindow_content
                    assert CancelWindow.get_button_text(1)=="Yes"
                    assert CancelWindow.get_button_text(2)=="Cancel"  
                    
                    #Step6:From pop-up confirmation window:
                        #a.Click button 'Cancel'.
                        #b.Click button 'Yes'.  
                    CancelWindow.click_Button(2)  #Click button 'Cancel'.
                    '''Check3:1.This pop-up window disappeared.
                              2.Back to this form detail page.'''
                    assert CancelWindow.window_exist()==False
                    assert BasicInfo.Button_Displayed(4)==True
                    
                    BasicInfo.Click_Button(4)#Click button "Cancel Coaching"
                    CancelWindow.click_Button(1)  #Click button 'Yes'.
                    #warning_message=CoachHome.get_StatusChangedWarning()
                    Canceled_Date_FromServer=GetConfig.get_ServerCurrentDate().replace("-","/")
                    '''Check3:3.TBack to coaching search main page with waring message shown:Coaching canceled successful'''
                    #assert warning_message=="Coaching canceled successful"
                    
                    #Step7:On coaching search main page,Filter with Status option = Canceled;
                    CoachHome.select_status("Canceled")
                    CoachHome.click_filterbutton()
                    '''Check4:This coaching record is searched out with 'Canceled' status shown.'''
                    assert CoachHome.get_anyCoach_attribute(1, 1)==SN_CoachHome
                    assert CoachHome.get_anyCoach_attribute(1, 6)=="Canceled"
                    
                    #Step8:Select this record to enter form detail page.
                    CoachHome.click_eachcoach(1)#Click the first coach in coaching home
                    
                    '''Check5:On this  form detail page:
                              1)  Status = Canceled;
                              2)  Created Date = The date when the form is created;
                              3)  Canceled Date = The date when the form is canceled.
                              4)  All KPIs are shown in checked status.
                              5)  Each of other fields content shown correct:
                                    a.SN, Employee Name,EmployeeID, Coaching Name,
                                    b.each of text boxes,dates
                                    c.Call Recording Number is blank (not for AOL)
                              6)  At the page bottom: show two buttons: Print and Back
                              7)  All fields are in uneditable status.'''
                    assert BasicInfo.get_status()=="Canceled"
                    assert BasicInfo.get_createdate()==Created_Date_FromServer
                    assert BasicInfo.get_canceleddate()==Canceled_Date_FromServer
                    for index in range(2,KPInumber+1):
                        assert BasicInfo.get_anyCheckBoxStatus(index)==self.CheckBox_CheckedStatus
                    assert BasicInfo.get_SN()==SN_CoachHome
                    assert BasicInfo.get_employeename()==Agent_name
                    assert BasicInfo.get_employeeHrid()==Agent_hrid
                    assert BasicInfo.get_coachname()==LoginName
                    if lobname != "AOL":
                        assert BasicInfo.get_callrecordingnumber()==""
                    assert MeetGreetGTNKProcessConfirmationForm.get_comments(3)==""
                    assert MeetGreetGTNKProcessConfirmationForm.get_comments(5)==""
                    assert MeetGreetGTNKProcessConfirmationForm.get_comments(7)==""
                    assert MeetGreetGTNKProcessConfirmationForm.get_comments(9)==""
                    assert MeetGreetGTNKProcessConfirmationForm.get_comments(11)==""
                    assert MeetGreetGTNKProcessConfirmationForm.get_comments(13)==""
                    assert MeetGreetGTNKProcessConfirmationForm.get_comments(14)==""
                    assert BasicInfo.get_ButtonName(1)=="Print"
                    assert BasicInfo.get_ButtonName(2)=="Back"
                    for index in range(3,6):
                        assert BasicInfo.Button_Displayed(index)==False
                    if lobname != "AOL":
                        assert BasicInfo.callrecordingnumber_disabled()=="true"
                    assert MeetGreetGTNKProcessConfirmationForm.comments_disabled(3)=="true"
                    assert MeetGreetGTNKProcessConfirmationForm.comments_disabled(5)=="true"
                    assert MeetGreetGTNKProcessConfirmationForm.comments_disabled(7)=="true"
                    assert MeetGreetGTNKProcessConfirmationForm.comments_disabled(9)=="true"
                    assert MeetGreetGTNKProcessConfirmationForm.comments_disabled(11)=="true"
                    assert MeetGreetGTNKProcessConfirmationForm.comments_disabled(13)=="true"
                    assert MeetGreetGTNKProcessConfirmationForm.comments_disabled(14)=="true"
                    
                    
                    #Step9:Click BACK button from top left page.
                    Header.click_backbutton()
                    
                    '''Check6:1)Back to search main page.
                              2)Status drop-down 'Canceled' is selected by default.
                              3)This coaching record is shown by default.
                              4) On search main page, shown all canceled records.'''
                    assert Header.get_HeaderTittle()==self.coachhometitle
                    assert CoachHome.get_status_selected()=="Canceled"
                    assert CoachHome.get_anyCoach_attribute(1, 1)==SN_CoachHome
                    
                    #Get Total_coachnumber from coaching home page
                    total_PageandCoachnumber_tablet_Dic1=CoachPublic.get_Total_PageandCoachnumber()
                    Total_coachnumber_tablet1=total_PageandCoachnumber_tablet_Dic1['Total_coachnumber_tablet']
                    
                    #Get Total_coachnumber from database
                    database_name=lobname.lower()+'_'+sitename.lower().replace("-","")   
                    conn=MySQLdb.connect(self.host,self.dbuser,self.dbpassword,database_name)
                    cursor=conn.cursor()
                    conn.autocommit(True)
                    sql_coach1="select * from coach  where  assign_to_id="+self.OMuserid+"  and classification=0 and status=2 order by id desc;"
                    Total_coachnumber_database1=cursor.execute(sql_coach1)
                    assert Total_coachnumber_tablet1==Total_coachnumber_database1
                    
                    #Step10:CLick button 'Print'.
                    '''Check7:Print preview window is shown.'''
                    
                    #Step11:a.Logout->login with Agent who is coached in the form.
                            #b.Enter coaching module,filter with status option 'Cancel'.
                            #c. Open this form from coach module.
                            #d.Try to edit the form.
                    L.logout_tablet()
                    L.Login_tablet(self.tableturl, lobname, sitename, Agent_hrid, Agent_password)
                    Tablet.click_Agent_coachingcircle()
                    CoachHome.select_status("Canceled")
                    CoachHome.click_filterbutton()
                    CoachHome.click_eachcoach(1)
                    
                    '''Check8:1.Enter form detail page with title 'Coaching - Commendation'
                              2.At form page bottom, there is only one button BACK.
                              3.Agent cannot edit the form(all fields are in uneditable status)'''
                    assert Header.get_HeaderTittle()==self.coachpagetitle
                    assert BasicInfo.get_ButtonName(1)=="Back"
                    for index in range(2,6):
                        assert BasicInfo.Button_Displayed(index)==False
                    if lobname != "AOL":
                        assert BasicInfo.callrecordingnumber_disabled()=="true"
                    assert MeetGreetGTNKProcessConfirmationForm.comments_disabled(3)=="true"
                    assert MeetGreetGTNKProcessConfirmationForm.comments_disabled(5)=="true"
                    assert MeetGreetGTNKProcessConfirmationForm.comments_disabled(7)=="true"
                    assert MeetGreetGTNKProcessConfirmationForm.comments_disabled(9)=="true"
                    assert MeetGreetGTNKProcessConfirmationForm.comments_disabled(11)=="true"
                    assert MeetGreetGTNKProcessConfirmationForm.comments_disabled(13)=="true"
                    assert MeetGreetGTNKProcessConfirmationForm.comments_disabled(14)=="true"
                    
                    #Step12:Click BACK button at page bottom.
                    BasicInfo.Click_Button(1)
                    '''Check9:1)Back to search main page.
                              2)Status drop-down 'Canceled' is selected by default.
                              3)This coaching record is shown by default.
                              4)On search main page, shown all canceled records that coached to this agent.'''
                    assert Header.get_HeaderTittle()==self.coachhometitle
                    assert CoachHome.get_status_selected()=="Canceled"
                    assert CoachHome.get_anyCoach_attribute(1, 1)==SN_CoachHome
                    
                    #Get Total_coachnumber from coaching home page
                    total_PageandCoachnumber_tablet_Dic2=CoachPublic.get_Total_PageandCoachnumber()
                    Total_coachnumber_tablet2=total_PageandCoachnumber_tablet_Dic2['Total_coachnumber_tablet']
                    
                    #Get Total_coachnumber from database
                    sql_coach2="select * from coach  where  hr_id="+Agent_hrid+"  and classification=0 and status=2 order by id desc"
                    Total_coachnumber_database2=cursor.execute(sql_coach2)
                    assert Total_coachnumber_tablet2==Total_coachnumber_database2
                    L.logout_tablet()
                    GetConfig.print_EndTest_message(lobname, sitename)
                             
                    
                    
                      


    #def tearDown(self):
        #Gl.driver.quit()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()