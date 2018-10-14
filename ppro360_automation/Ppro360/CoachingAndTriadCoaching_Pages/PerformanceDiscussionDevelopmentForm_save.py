
'''
Created on 2017/07/17

@author: luming.zhao
'''

import unittest
import time
from public_method.Login import Login
from public_method import Gl
from public_method.Get_configration_data import Get_configration_data
from public_method.Coach_Triad_General import Coach_Triad_General
from Tablet_pages.PerformanceDiscussionDevelopmentFormPage import PerformanceDiscussionDevelopmentFormPage
from Tablet_pages.PerformancPage import PerformancePage
from Tablet_pages.HeaderPage import HeaderPage
from Tablet_pages.TabletHomepage import TabletHomepage
from Tablet_pages.Coachinghomepage import Coachinghomepage
from public_method.Input_Allcoaching import Input_Allcoaching
from Tablet_pages.Popupaddcoachpage import Popupaddcoachpage




class PerformanceDiscussionDevelopmentFormPage_save(unittest.TestCase):
    
    
    def setUp(self):
        #Case ID
        self.caseID="PerformanceDiscussionDevelopmentFormPage_save"
        
        GetData=Get_configration_data()
        #Get URL
        self.tableturl=GetData.get_TabletUrl()
       
        #Get OM account
        OMaccount=GetData.get_OMaccount()
        self.OMuserid=OMaccount["OMuserid"]
        self.OMpassword=OMaccount["OMpassword"]
        
        #Get all lobs from CSV
        self.testLOBSITE_list=GetData.get_LOBSITEtoTest(self.caseID)

        #coaching or Triad coaching
        self.coachtype="coaching"
        
        #Get coachpopuptittle
        self.title=GetData.get_AddCoachingFormTitle()
        
        #text for each coaching
        self.text='Testing'
        
        #Coachformname
        self.coachformname="Performance Discussion & Development Form" 
        self.coachpagetitle="Coaching - "+self.coachformname
        
    def tearDown(self):
        pass
        
    def test_PerformanceDiscussionDevelopmentForm(self):
        GetConfig=Get_configration_data()
        Tablet=TabletHomepage()
        TCoach=Coach_Triad_General()
        Ppage=PerformancePage()
        CoachHome=Coachinghomepage()
        Header=HeaderPage()
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
                    coach_list=GetConfig.get_CoachingFormList(lobname)
   
                    #Step1:Login tablet
                    L=Login()
                    L.Login_tablet(self.tableturl,lobname,sitename,self.OMuserid,self.OMpassword)
                    
                    #Step2:Enter performance
                    Tablet.click_performancecircle()
                        
                        
                    #Step3:Select one Agent to add coaching to follow Planed to Acknowledged
                    print "Start=====Monthly-To-Day is in testing",
                    Ppage.select_AnyKpiOfAgent_OM(4)#Select three KPI
                    Ppage.click_addcoachbutton()
                    print "Choose Performance Discussion & Development Form"
                    TCoach.Add_AnyCoachOrTriad(self.coachformname)
                       
                    '''
                    #Check1:check the add coach message
                    message=Ppage.get_messageOfaddCoachOrtriad()
                    print message
                    assert message=="Coaching Added"
                    '''
                    Ppage.click_backbutton()
                    Tablet.click_coachingcircle()
#
                    CH=Coachinghomepage()
                    eachcoach_loc="/html/body/div/div/section/div/div[2]/table/tbody/tr[1]/td[1]"
                    CH.click_eachcoach(eachcoach_loc)
                    
                     
                    #Step4:Input and save form
                    
                    InputCoaching=Input_Allcoaching()
                    lineindex=7
                    checkboxorderindex=6
                    InputCoaching.Input_PerformanceDiscussionDevelopmentFormPage(self.text,lineindex,checkboxorderindex)
                    PDDPage=PerformanceDiscussionDevelopmentFormPage()
                    PDDPage.click_savebutton()
                    
                        
                        
                        
                        

    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()                
        
        
        