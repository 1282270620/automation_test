'''
Created on 2018.07.30

@author: haodong.liu
'''
import unittest
import time
from public_method import Gl
from public_method.Get_configration_data import Get_configration_data
from public_method.Login import Login
from public_method.Coach_Triad_General import Coach_Triad_General
from Tablet_pages.TabletHomepage import TabletHomepage
from Tablet_pages.Coachinghomepage import Coachinghomepage
from CoachingAndTriadCoaching_Pages.BasicInfoforCoaching import BasicInfoforCoaching
from OutlierTrendViewMyAchievement.OutlierTrendViewMyAchievementpage import OutlierTrendViewMyAchievementpage
from OutlierTrendViewMyAchievement.Outlierpage import Outlierpage
from Tablet_pages.HeaderPage import HeaderPage
from public_method.Get_AllRoleAccountForTest import Get_AllRoleAccountForTest
from CoachingAndTriadCoaching_Pages.QualityAssurancePage import QualityAssurancePage


class Outlier_AddQualityAssuanceForm(unittest.TestCase):


    def setUp(self):
        #Case ID
        self.caseID="Outlier_AddQualityAssuanceForm"
        
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
        #Coachformname
        self.coachhometitle="Coaching"
        self.coachformname="Quality Assurance" 
        self.coachpagetitle="Coaching - "+self.coachformname
        
    def test_Outlier_AddQualityAssuanceForm(self):
        GetConfig=Get_configration_data()
        Tablet=TabletHomepage()
        CoachHome=Coachinghomepage()
        BasicInfo=BasicInfoforCoaching()
        Header=HeaderPage()
        Coach=Coach_Triad_General()
        QAPage=QualityAssurancePage()
        OutlierpageT=Outlierpage()
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
                    userid=QAPage.get_firstTLHRID(1)
                    L.logout_tablet()
                    
                    TLInfo=Getaccount.get_TLandAgentInfofromAdmin(self.Adminurl, lobname, sitename, self.OMuserid, self.OMpassword, userid)
                    TL_Name=TLInfo["Name"]
                    TL_hrid=TLInfo["Hrid"]
                    TL_password=TLInfo["Password"]
                    time.sleep(5)

                    L=Login()
                    L.Login_tablet(self.tableturl,lobname,sitename,TL_hrid,TL_password)
                    time.sleep(5)
                    LoginName=Header.get_loginName()
                    
                    Tablet.click_TL_outliercircle()
                    #get Agent HRID
                    Agent_HRID=QAPage.get_firstAgentID()
                    
                    '''
                    #getAgent Info from admin
                    L.logout_tablet
                    AgentInfo=Getaccount.get_TLandAgentInfofromAdmin(self.Adminurl, lobname, sitename, self.OMuserid, self.OMpassword,Agent_userid)
                    Agent_hrid=AgentInfo["Hrid"]
                    L.logout_admin()
                    L=Login()
                    L.Login_tablet(self.tableturl,lobname,sitename,TL_hrid,TL_password)
                    time.sleep(5)
                    Tablet.click_TL_outliercircle()
                    '''
                    #Select Form and Cancel
                    OutlierpageT.click_selectagent(1,1)
                    AgentName=OutlierpageT.get_AgentName(1,1)
                    
                    OutlierpageT.click_addCoachButton()
                    time.sleep(5)
                    OutlierpageT.click_addorcancle(2)
                    
                    #Select Form and agian Add
                    time.sleep(5)
                    OutlierpageT.click_addCoachButton()
                    Coach.Add_AnyCoachOrTriad(self.coachformname)
                    ServerTime=GetConfig.get_ServerCurrentDate().replace("-","/")
                    assert self.coachpagetitle=='Coaching - Quality Assurance'
                    assert QAPage.get_sn()==''
                    assert QAPage.get_EmployeeName()==AgentName+' '
                    assert QAPage.get_CoachName()==LoginName+' '
                    assert QAPage.get_CompletedDate()==time.strftime("%Y/%m/%d", time.localtime())
                    assert QAPage.get_CallRecordingNumber()==''
                    
                    assert QAPage.get_ButtonName(1)=='Print'
                    assert QAPage.get_ButtonName(2)=='Add Coaching'
                    assert QAPage.get_ButtonName(3)=='Cancel'
                    
                    QAPage.Click_Button(2)
                    assert QAPage.get_Error1()+QAPage.get_Error2()=="Error"+"SN can't be empty."
                    
                    #Manually close the prompt messgae
                    QAPage.Close_ErrorButton()
                    
                    QAPage.input_sn('QA-001-()test')
                    QAPage.input_callrecordingnumber('test_number123!~@#$%^&*()')
                    QAPage.Click_Button(2)
                    #Check Coach info
                    InfoTitle=QAPage.get_AddQACoachingInfoTitle()
                    InfoTitleActual=InfoTitle[0:0+12]
                    assert InfoTitleActual=='Confirmation'
                    assert QAPage.get_AddQACoachingPromptInfo()=='Are you sure to add this Quality Assurance coaching with the following information?'
                    assert QAPage.get_AddQAInfo()=='SN: QA-001-()test\n'+'Employee Name: Agent 14\n'+'Coaching Name: Tl2 Test\n'+'Call Recording Number: test_number123!~@#$%^&*()'
                    
                    QAPage.click_yes()
                    assert QAPage.get_AddSuccessInfo()=='Coaching Added'
                    Header.click_backbutton()
                    #Into Coaching modules and into detail page
                    Tablet.click_coachingcircle()
                    CoachHome.click_statusbox()
                    time.sleep(5)
                    #CoachHome.select_status('Completed')
                    QAPage.click_CompletedSection()
                    CoachHome.click_filterbutton()
                    #Check Coaching list info
                    assert QAPage.get_CoachpageInfo(4)==Agent_HRID
                    assert QAPage.get_CoachpageInfo(5)=='Quality Assurance'
                    assert QAPage.get_CoachpageInfo(6)=='Completed'
                    assert QAPage.get_CoachpageInfo(8)==ServerTime
                    assert QAPage.get_CoachpageInfo(9)==ServerTime
                    
                    CoachHome.click_eachcoach(1)
                    #Check QA detail Info
                    assert QAPage.SN_disabled()=='true'
                    assert QAPage.EmployeeName_disabled()=='true'
                    assert QAPage.CoachName_disabled()=='true'
                    assert QAPage.CallRecordingNumber_disabled()=='true'
                    assert QAPage.CompletedDate_disabled()=='true'
                    assert QAPage.get_sn()=='QA-001-()test'
                    assert QAPage.get_EmployeeName()==AgentName
                    assert QAPage.get_CoachName()==LoginName
                    assert QAPage.get_CallRecordingNumber()=='test_number123!~@#$%^&*()'
                    assert QAPage.get_CompletedDate()==ServerTime
                    assert QAPage.get_ButtonName2(1)=='Print'
                    assert QAPage.get_ButtonName2(2)=='Back'
                    
    def tearDown(self):
        Gl.driver.quit()                
                    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()       