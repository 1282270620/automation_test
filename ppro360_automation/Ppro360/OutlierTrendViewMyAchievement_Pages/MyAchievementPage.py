'''
Created on 20180228

@author: luming.zhao
'''

from selenium.webdriver.common.by import By
from Tablet_pages import BasePage
from public_method.Get_AnyText_ForNormal import Get_AnyText_ForNormal
from public_method import Gl
from public_method.KPI_method import KPI_method
import time

class MyAchievementPage(BasePage.Action):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.Weightname_path = "//*[@id='container']/div/section/div/div[2]/table/thead/tr/th[%d]" #%d start from 3
        self.WeightKPI_path = "//*[@id='container']/div/section/div/div[2]/table/tbody/tr[1]/td[%d]" # %d start from 2 
        self.GoalKPI_path = "//*[@id='container']/div/section/div/div[2]/table/tbody/tr[2]/td[%d]" # %d start from 2 
        self.PTeamKPI_path = "//*[@id='container']/div/section/div/div[2]/table/tbody/tr[3]/td[%d]/span" # %d start from 2 self.YourTeamKPI_path = "//*[@id='container']/div/section/div/div[2]/table/tbody/tr[3]/td[%d]" # %d start from 2 
        self.YourTeamKPI_path="//*[@id='container']/div/section/div/div[2]/table/tbody/tr[3]/td[%d]"
        self.AgentKPI_path = "//*[@id='container']/div/section/div/div[2]/table/tbody/tr[4]/td[%d]" # %d start from 2 
        self.backbutton_loc = (By.LINK_TEXT,"Back")
        self.timetab_path="//*[@id='container']/div/section/div/div[1]/ul/li[%d]"
        
    '''def get_WeightKPI(self,weightindex):
        self.anyWeightKPI_loc=(By.XPATH,self.WeightKPI_path %weightindex)
        anyWeightKPI=self.find_element(*self.anyWeightKPI_loc).text
        return anyWeightKPI'''
        
    def get_WeightKPI_page(self):
        Get_AnyText=Get_AnyText_ForNormal()
        WeightKPI_list=Get_AnyText.Get_Text_ForLoop(3, self.WeightKPI_path) #AchievementKPI is start from 2
        return WeightKPI_list
    
    '''
    def get_MyAchWeight_data_Expected(self):
        Weight_KPI={}
        KPIMethod=KPI_method()
        Weight_KPI=KPIMethod.Decimal_To_Percentage(Weight_KPI)
        
    
    def get_GoalKPI(self,goalindex):
        self.anyGoalKPI_loc=(By.XPATH,self.GoalKPI_path %goalindex)
        anyGoalKPI=self.find_element(*self.anyWeightKPI_loc).text 
        return anyGoalKPI 
        '''
    def get_allkpiname_page(self):
        Get_AnyText=Get_AnyText_ForNormal()
        AllKpiName_list=Get_AnyText.Get_Text_ForLoop(2, self.Weightname_path) #AchievementKPI is start from 2
        return AllKpiName_list
    
    
    def get_GoalKPI_page(self):
        Get_AnyText=Get_AnyText_ForNormal()
        GoalKPI_list=Get_AnyText.Get_Text_ForLoop(2, self.GoalKPI_path) #AchievementKPI is start from 2
        return GoalKPI_list
    
    def get_YourTeamKPI_page(self):
        Get_AnyText=Get_AnyText_ForNormal()
        YourTeamKPI_list=Get_AnyText.Get_Text_ForLoop(2, self.YourTeamKPI_path)
        return YourTeamKPI_list
    
    def get_PTeamKPI_page(self):
        Get_AnyText=Get_AnyText_ForNormal()
        PTeamKPI_list=Get_AnyText.Get_Text_ForLoop(2, self.PTeamKPI_path) 
        return PTeamKPI_list
    def get_AgentValue_page(self):
        Get_AnyText=Get_AnyText_ForNormal()
        Agent_list=Get_AnyText.Get_Text_ForLoop(2, self.AgentKPI_path) 
        return Agent_list
    
    
    def get_AgentKPI(self,goalindex):
        self.AgentKPI_loc=(By.XPATH,self.AgentKPI_path %goalindex)
        AgentKPI=self.find_element(*self.AgentKPI_loc).text 
        return AgentKPI    
    
    def click_back(self):
        self.find_element(*self.backbutton_loc).click()
        time.sleep(Gl.waittime)
        
    def click_timetab_MyAchievement(self,index):
        '''1-lasttwomonth,2-lastmonth,3-ytd,4-wtd,5-mtd;
           1-lasttwomonth,2-lastmonth,3-mtd'''
        timetab_loc=(By.XPATH,self.timetab_path % index)
        self.find_element(*timetab_loc).click()
        self.wait_loadingmask_disappear()
        
    def get_timetab_text_MyAchievement(self,index):
        '''1-lasttwomonth,2-lastmonth,3-ytd,4-wtd,5-mtd;
           1-lasttwomonth,2-lastmonth,3-mtd'''
        timetab_text_path=self.timetab_path+"/span"
        timetab_text_loc=(By.XPATH,timetab_text_path % index)
        print timetab_text_loc
        timetab_text=self.find_element(*timetab_text_loc).text
        return timetab_text
    
    def get_weightname_page(self):
        Get_AnyText=Get_AnyText_ForNormal()
        Weigthname_list=Get_AnyText.Get_Text_ForLoop(3, self.Weightname_path) #Achievement is start from 2
        return Weigthname_list
    
    
    
    
    
        
        