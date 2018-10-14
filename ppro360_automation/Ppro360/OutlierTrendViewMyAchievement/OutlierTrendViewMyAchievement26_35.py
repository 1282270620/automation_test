'''
Created on 2, 27, 2012

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
from OutlierTrendViewMyAchievement.OutlierTrendViewMyAchievementpage import OutlierTrendViewMyAchievementpage
from OutlierTrendViewMyAchievement.Outlierpage import Outlierpage
from public_method.Coaching_PublicFunction import Coaching_PublicFunction
from Tablet_pages.HeaderPage import HeaderPage
from public_method.Get_AllRoleAccountForTest import Get_AllRoleAccountForTest
#from public_method.Login import Login
from idlelib.IOBinding import blank_re


class OutlierTrendViewMyAchievement(unittest.TestCase):


    def setUp(self):
        #Case ID
        self.caseID="OutlierTrendViewMyAchievement26_35"
        
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
        self.coachtype="triad coaching"  
        #Coachformname
        self.coachhometitle="Triad Coaching"
        self.coachformname="Quality Assurance" 
        self.coachpagetitle="Coaching - "+self.coachformname
        
        
    def test_LeadershipHuddleProcessConfirmation_PlannedToCanceled(self):
        GetConfig=Get_configration_data()
        Tablet=TabletHomepage()
        Ppage=PerformancePage()
        TCoach=Coach_Triad_General()
        CoachHome=Coachinghomepage()
        BasicInfo=BasicInfoforCoaching()
        Header=HeaderPage()
        OAform=OutlierTrendViewMyAchievementpage()
        OApage=Outlierpage()
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
                   
                    #Step1:Login tablet,and Get TLInfo using for testing
                    userid=Getaccount.get_TLInfoFromMyteamInfo(self.tableturl, lobname, sitename, self.OMuserid, self.OMpassword)
                    TLInfo_Dic=Getaccount.get_TLandAgentInfofromAdmin(self.Adminurl,lobname, sitename, self.OMuserid, self.OMpassword,userid)
                    TL_Name=TLInfo_Dic["Name"]
                    TL_hrid=TLInfo_Dic["Hrid"]
                    TL_password=TLInfo_Dic["Password"]
                    L=Login()
                    L.Login_tablet(self.tableturl,lobname,sitename,TL_hrid,TL_password)
                    time.sleep(Gl.waittime)
                    LoginName=Header.get_loginName()
                    Tablet.click_LeadershipAcademyCoachingScores(2)
                    OApage.click_selectagent(1,2)
                    agentname=OApage.get_selectagent(1,1)
                    OApage.click_addcoach()
                    print OApage.get_addorcancle(1)
                    OApage.click_addorcancle(2)
                    print OApage.get_addorcancle(1)
                    OApage.click_addcoach()
                    a=0
                    coachname=True
                    while coachname==True:
                        a=a+1
                        if OApage.get_formname(a)==self.coachformname:
                            OApage.click_form(a)
                            print a
                            b=a
                            coachname=False
                    OApage.click_addorcancle(1)
                    completed_Date_FromServer=GetConfig.get_ServerCurrentDate().replace("-","/")
                    time.sleep(3)
                    timedate=time.strftime('%Y/%m/%d',time.localtime(time.time()))
                    assert OAform.get_formtitle()==self.coachpagetitle
                    assert OAform.get_sn()=="" 
                    assert OAform.get_employeeName()==agentname+" "
                    assert OAform.get_coachname()==TL_Name+" "
                    assert OAform.get_backbutton()=="Back"
                    assert OAform.get_completeddate()==timedate
                    assert OAform.get_callRecordingNumber()==""
                    assert OAform.get_loginrole()==TL_Name+" (TL)"
                    assert OAform.get_loginlobandsite()==lobname+", "+sitename
                    assert OAform.get_threebutton(1)=="Print"
                    assert OAform.get_threebutton(2)=="Add Coaching"
                    assert OAform.get_threebutton(3)=="Cancel"
                    OAform.click_threebutton(3)
                    time.sleep(3)
                    print OAform.get_formtitle()
                    assert OAform.get_formtitle()=="Outlier"
                    print OApage.get_warnmessage()
                    OApage.click_addcoach()
                    OApage.click_form(b)
                    OApage.click_addorcancle(1)
                    OAform.click_threebutton(2)
                    assert OAform.get_warnmessage(1)=="Error"
                    assert OAform.get_warnmessage(2)=="SN can't be empty."
                    Confirmation1="Are you sure to add this Quality Assurance coaching with the following information?"
                    Confirmation2=""
                    sn="qwer"
                    callRecordingNumber="123456"
                    OAform.input_sn(sn)
                    OAform.input_callRecordingNumber(callRecordingNumber)
                    OAform.click_threebutton(2)
                    assert OAform.get_Confirmation(1)==Confirmation1
                    #list=[]
                    #print list.append(OAform.get_Confirmation(2))
                    actualmessage1="""SN: """+sn
                    actualmessage11=actualmessage1.replace(" ","")
                    actualmessage2="""Employee Name: """+OAform.get_employeeName()
                    actualmessage22=actualmessage2.replace(" ","")
                    actualmessage3="""Coaching Name: """+OAform.get_coachname()
                    actualmessage33=actualmessage3.replace(" ","")
                    actualmessage4="""Call Recording Number: """+callRecordingNumber
                    actualmessage44=actualmessage4.replace(" ","")
                    Confirmation=OAform.get_Confirmation(2).replace(" ","")
                    print Confirmation
                    assert actualmessage11 in Confirmation
                    assert actualmessage22 in Confirmation
                    assert actualmessage33 in Confirmation
                    assert actualmessage44 in Confirmation
                    OAform.click_yesorno(2)
                    assert OAform.get_formtitle()=="Coaching - Quality Assurance"
                    time.sleep(3)
                    OAform.click_threebutton(2)
                    OAform.click_yesorno(1)
                    assert OApage.get_addmessage()=="Coaching Added"
                    time.sleep(2)
                    OAform.click_backbutton()
                    Tablet.click_LeadershipAcademyCoachingScores(3)
                    OAform.click_typeandstatusclick(1)
                    c=0
                    coachname=True
                    while coachname==True:
                        c=c+1
                        if OAform.get_typeandstatuschoose(1, c)==self.coachformname:
                            OAform.click_typeandstatuschoose(1, c)
                            print c
                            d=c
                            coachname=False
                    OAform.click_typeandstatusclick(2)
                    OAform.click_typeandstatuschoose(2,5)
                    OAform.click_fillter()
                    time.sleep(2)
                    CoachHome.click_eachcoach(1)
                    assert OAform.get_formtitle()==self.coachpagetitle
                    assert OAform.get_sn()==sn
                    assert OAform.get_employeeName()==agentname
                    assert OAform.get_coachname()==TL_Name
                    assert OAform.get_backbutton()=="Back"
                    assert OAform.get_completeddate()==timedate
                    assert OAform.get_callRecordingNumber()==callRecordingNumber
                    assert OAform.get_threebutton(1)=="Print"
                    assert OAform.get_threebutton(2)=="Back"
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()       