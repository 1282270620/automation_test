'''
Created on Jan 3, 2017

@author: symbio
'''
#import sys 
#sys.path.append("\test_cases") 
from Tablet_pages import BasePage
from selenium.webdriver.common.by import By
import time
from public_method import Gl

class TabletHomepage(BasePage.Action):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.back_loc=(By.CSS_SELECTOR,"div.nav-btn-text-inner")
        self.performancecircle_loc=(By.CSS_SELECTOR,"p.circle-chart-value")
        self.performancename_loc=(By.XPATH,"//*[@id='container']/div/section/section/a[1]/p")
        self.performancecircle_Achiev_loc=(By.XPATH,"//*[@id='container']/div/section/section/a[1]/div/div/p")
        
    
        #self.coachingcircle_loc=(By.XPATH,"//*[@id='container']/div/section/section/a[2]/div/div/p/img")
        self.coachingcircle_loc=(By.LINK_TEXT,"Coaching")
        self.coachingname_loc=(By.XPATH,"//*[@id='container']/div/section/section/a[2]/p")
        self.coachingname_TL_loc=(By.XPATH,"//*[@id='container']/div/section/section/a[3]/p")
        self.coachingcircle_TL_loc=(By.XPATH,"//*[@id='container']/div/section/section/a[3]/div/div/p/img")
        self.coachingcircle_Agent_loc=(By.XPATH,"//*[@id='container']/div/section/section/a[3]/div/div/p/img")
        self.coachingname_Agent_loc=(By.XPATH,"//*[@id='container']/div/section/section/a[3]/p")
        
        self.Triadcoachingcircle_loc=(By.XPATH,"//div[@id='container']/div/section/section/a[3]/div/div/p/img")
        self.Triadcoachingname_loc=(By.XPATH,"//*[@id='container']/div/section/section/a[3]/p")
        self.Triadcoachingname_TL_loc=(By.XPATH,"//*[@id='container']/div/section/section/a[4]/p")
        
        self.Triadcoachingcircle_TL_loc=(By.XPATH,"//div[@id='container']/div/section/section/a[4]/div/div/p/img")
        #self.Myteaminfocircle_loc=(By.XPATH,"//div[@id='container']/div/section/section/a[4]/div/div/p/img")
        self.Myteaminfocircle_loc=(By.XPATH,"//*[@id='container']/div/section/section/a[4]/div/div/p/img")
        self.Myteaminfoname_loc=(By.XPATH,"//*[@id='container']/div/section/section/a[4]/p")
        self.Myteaminfocircle_TL_loc=(By.XPATH,"//*[@id='container']/div/section/section/a[5]/div/div/p/img")
        self.Myteaminfoname_TL_loc=(By.XPATH,"//*[@id='container']/div/section/section/a[5]/p")
        
        self.Adaptationcircle_loc=(By.XPATH,"//div[@id='container']/div/section/section/a[5]/div/div/p/img")
        self.Adaptationname_loc=(By.XPATH,"//*[@id='container']/div/section/section/a[5]/p")
        
        
        self.Adaptationcircle_LC_loc=(By.XPATH,"//*[@id='container']/div/section/section/a[1]/div/div/p")
        self.Adaptationname_LC_loc=(By.XPATH,"//*[@id='container']/div/section/section/a[4]/p")
        
        self.CoachingExportcircle_OM_loc=(By.XPATH,"//*[@id='container']/div/section/section/a[5]/div/div/p/img")
        self.CoachingExportname_OM_loc=(By.XPATH,"//*[@id='container']/div/section/section/a[5]/p")
        
        self.CoachingExportcircle_LC_loc=(By.XPATH,"//*[@id='container']/div/section/section/a[4]/div/div/p/img")
        self.CoachingExportname_LC_loc=(By.XPATH,"//*[@id='container']/div/section/section/a[4]/p")
        
        self.LeadershipAcademyCoachingScorescicle_LC_loc=(By.XPATH,"//*[@id='container']/div/section/section/a[6]/div/div/p/img")
        self.LeadershipAcademyCoachingScoresname_LC_loc=(By.XPATH,"//*[@id='container']/div/section/section/a[6]/p")
        self.LeadershipAcademyCoachingScoresname_Agent_loc=(By.XPATH,"//*[@id='container']/div/section/section/a[4]/p")
        self.LeadershipAcademyCoachingScoresname_TL_loc=(By.XPATH,"//*[@id='container']/div/section/section/a[7]/p")
        self.LeadershipAcademyCoachingScoresname_OM_loc=(By.XPATH,"//*[@id='container']/div/section/section/a[6]/p")
        
        self.LeadersAcademyCoachingLeaderScores_loc=(By.LINK_TEXT,"Leaders Academy Coaching Leader Scores")
        
        self.CoachingExportcircle_TL_loc=(By.XPATH,"//*[@id='container']/div/section/section/a[6]/div/div/p/img")
        self.CoachingExportname_TL_loc=(By.XPATH,"//*[@id='container']/div/section/section/a[6]/p")
    
        self.Outliercircle_TL_loc=(By.XPATH,"//*[@id='container']/div/section/section/a[2]/div/div")
        self.Outliername_TL_loc=(By.XPATH,"//*[@id='container']/div/section/section/a[2]/p")
        
        self.MyAchievementcircle_Agent_loc=(By.XPATH,"//*[@id='container']/div/section/section/a[2]/div/div")
        self.MyAchievementname_Agent_loc=(By.XPATH,"//*[@id='container']/div/section/section/a[2]/p")
    
        self.Satisfaction_loc=(By.LINK_TEXT,"Satisfaction")
        
        self.CoachDueReports_loc=(By.LINK_TEXT,"Coach Due Reports")
        
        self.MyInfo_loc=(By.LINK_TEXT,"My Info")
        
        self.RedemptionReport_loc=(By.LINK_TEXT,"Redemption Report")
        
        self.TabletCircle_path="//*[@id='container']/div/section/section/a[%d]/p"
        
        
        

    #yalan added bellow:
        self.LeadershipAcademyCoachingScorescircle_TL_OMleaderScorescircle_loc=(By.XPATH, '//*[@id="container"]/div/section/section/a[7]/div/div/p/img')
        self.LeadershipAcademyCoachingScoresname_TL_OMleadersScoresname_loc=(By.XPATH, '//*[@id="container"]/div/section/section/a[7]/p')
        self.LeadershipAcademyCoachingScorescircle_OM_loc=(By.XPATH, '//*[@id="container"]/div/section/section/a[6]/div/div/p/img')
        self.LeadershipAcademyCoachingScoresname_OM_loc=(By.XPATH, '//*[@id="container"]/div/section/section/a[6]/p')
        self.LeadershipAcademyCoachingScorescircle_LCandVPSVP_loc=(By.XPATH, '//*[@id="container"]/div/section/section/a[6]/div/div/p/img')
        self.LeadershipAcademyCoachingScoresname_LCandVPSVP_loc=(By.XPATH, '//*[@id="container"]/div/section/section/a[6]/p')
        self.LeadershipAcademyCoachingScorescircle_Agent_loc=(By.XPATH, '//*[@id="container"]/div/section/section/a[4]/div/div/p/img')
        self.LeadershipAcademyCoachingScoresname_Agent_loc=(By.XPATH, '//*[@id="container"]/div/section/section/a[4]/p')
    
    def get_TabletCircleName(self,index):
        TabletCircle_loc=(By.XPATH,self.TabletCircle_path % index)
        return self.find_element(*TabletCircle_loc).text
    
    def get_AllTabletCircleName(self):
        CircleName=[]
        index=1
        while self.Element_displayed(*(By.XPATH,self.TabletCircle_path %index)):
            TabletCircle_loc=(By.XPATH,self.TabletCircle_path % index)
            name=self.find_element(*TabletCircle_loc).text
            CircleName.append(name)
            index=index+1
        return CircleName
    
    def get_LeadershipAcademyCoachingScoresname_TL_OMLeaderScoresname(self):
        return self.find_element(*self.LeadershipAcademyCoachingScoresname_TL_OMleadersScoresname_loc).text
    def get_LeadershipAcademyCoachingScoresname_OM(self):
        return self.find_element(*self.LeadershipAcademyCoachingScoresname_OM_loc).text  
    #yalan added above
    def get_Achiev_performancecircle(self):
        return self.find_element(*self.performancecircle_Achiev_loc).text 
    
    def Enter_LeadersAcademyCoachingLeaderScoresPage(self):
        self.find_element(*self.LeadersAcademyCoachingLeaderScores_loc).click() 
        
        
    
    def click_performancecircle(self):
        self.find_element(*self.performancecircle_loc).click()
        self.wait_loadingmask_disappear()
        #time.sleep(Gl.waittime)
    
    def get_performancename(self):
        return self.find_element(*self.performancename_loc).text
    
    def click_TL_outliercircle(self):
        self.find_element(*self.Outliercircle_TL_loc).click()
        self.wait_loadingmask_disappear()
    def get_TL_outliername(self):
        return self.find_element(*self.Outliername_TL_loc).text
    
    def click_coachingcircle(self):
        self.find_element(*self.coachingcircle_loc).click()
        self.wait_loadingmask_disappear()
    def click_OM_coachingExportcircle(self):    
        self.find_element(*self.CoachingExportcircle_OM_loc).click()
        self.wait_loadingmask_disappear()
    def click_LC_coachingExportcircle(self):    
        self.find_element(*self.CoachingExportcircle_LC_loc).click()
        self.wait_loadingmask_disappear()
    def click_TL_coachingExportcircle(self):    
        self.find_element(*self.CoachingExportcircle_TL_loc).click()
        self.wait_loadingmask_disappear()    
    
        
                
        
    def get_coachingname(self):
        return self.find_element(*self.coachingname_loc).text
    
    def click_TL_coachingcircle(self):
        self.find_element(*self.coachingcircle_TL_loc).click()
        self.wait_loadingmask_disappear()
    def get_TL_coachingname(self):
        return self.find_element(*self.coachingname_TL_loc).text
        
    
    def click_Agent_coachingcircle(self):
        self.find_element(*self.coachingcircle_Agent_loc).click()
        self.wait_loadingmask_disappear()
    def get_Agent_coachingname(self):
        return self.find_element(*self.coachingname_Agent_loc).text
        
    def click_Triadcoachingcirecle(self):
        self.find_element(*self.Triadcoachingcircle_loc).click()
        self.wait_loadingmask_disappear()
    def get_TL_triadcoachingname(self):
        return self.find_element(*self.Triadcoachingname_TL_loc).text
        
    def get_triadcoachingname(self):
        return self.find_element(*self.Triadcoachingname_loc).text
    
    def click_TL_Triadcoachingcirecle(self):
        self.find_element(*self.Triadcoachingcircle_TL_loc).click()
        self.wait_loadingmask_disappear()
        
    def click_Myteaminfocircle(self):
        self.find_element(*self.Myteaminfocircle_loc).click()
        self.wait_loadingmask_disappear()
        
    def get_myteaminfoname(self):
        return self.find_element(*self.Myteaminfoname_loc).text
    
    def click_TL_Myteaminfocircle(self):
        self.find_element(*self.Myteaminfocircle_TL_loc).click()
        self.wait_loadingmask_disappear()
        
    def get_TL_myteaminfoname(self):
        return self.find_element(*self.Myteaminfoname_TL_loc).text
    
    def MyteamInfo_Exist(self):
        return self.isElementExist(*self.Myteaminfocircle_loc)
    
    def click_Adaptationcircle(self):
        self.find_element(*self.Adaptationcircle_loc).click()
        self.wait_loadingmask_disappear()
    def click_Adaptationcircle_LC(self):
        self.find_element(*self.Adaptationcircle_LC_loc).click()
        self.wait_loadingmask_disappear()
    
    def get_adaptationname(self):
        return self.find_element(*self.Adaptationname_loc).text
    def get_adaptationname_LC(self):
        return self.find_element(*self.Adaptationname_LC_loc).text
    
    def click_MyAchievementcircle(self):
        self.find_element(*self.MyAchievementcircle_Agent_loc).click()
        self.wait_loadingmask_disappear()
    def get_MyAchievementname(self):
        return self.find_element(*self.MyAchievementname_Agent_loc).text
    
    def get_CoachingExportname_LCVPSVP(self):
        return self.find_element(*self.CoachingExportname_LC_loc).text
    
    def get_CoachingExportname_OM(self):
        return self.find_element(*self.CoachingExportname_OM_loc).text
    
    def get_CoachingExportname_TL(self):
        return self.find_element(*self.CoachingExportname_TL_loc).text
        
    def get_LeadershipAcademyCoachingScoresname_LC(self):
        return self.find_element(*self.LeadershipAcademyCoachingScoresname_LC_loc).text  
    def get_LeadershipAcademyCoachingScoresname_Agent(self):
        return self.find_element(*self.LeadershipAcademyCoachingScoresname_Agent_loc).text
  
    def click_LeadershipAcademyCoachingScores_Agent(self):
        self.find_element(*self.LeadershipAcademyCoachingScoresname_Agent_loc).click()
        time.sleep(Gl.waittime)
    
    def click_LeadershipAcademyCoachingScores_TL(self):
        self.find_element(*self.LeadershipAcademyCoachingScoresname_TL_loc).click()
        
    def click_LeadershipAcademyCoachingScores_OM(self):
        self.find_element(*self.LeadershipAcademyCoachingScoresname_OM_loc).click()
        
    
    def click_Back(self):
        self.find_element(*self.back_loc).click()