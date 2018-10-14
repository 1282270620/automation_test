'''
Created on 2018.6.22

@author: yalan.yin
'''
from public_method.Get_AnyText_ForNormal import Get_AnyText_ForNormal
from public_method import Gl
from Tablet_pages import BasePage

class AgentPerformancePage(BasePage.Action):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.kpiName_path='//*[@id="container"]/div/section/div/div[2]/table/thead/tr/th[%d]'
        self.GoalValue_path='//*[@id="container"]/div/section/div/div[2]/table/tbody/tr[1]/td[%d]/span' #start from 2
        #self.Goal_KPITitle_path='//*[@id="container"]/div/section/div/div[2]/table/tbody/tr[2]/td[%d]'
        self.Goal_KPITitle_path='//*[@id="container"]/div/section/div/div[2]/table/tbody/tr[1]/td[%d]'
        self.teamValue_path='//*[@id="container"]/div/section/div/div[2]/table/tbody/tr[3]/td[%d]/span' #start from 2
        self.team_KPITitle_path='//*[@id="container"]/div/section/div/div[2]/table/tbody/tr[3]/td[%d]'
        self.AgentValue_path='//*[@id="container"]/div/section/div/div[2]/div/table/tbody/tr/td[%d]/span' #start from 2
        self.Agent_KPITitle_path='//*[@id="container"]/div/section/div/div[2]/div/table/tbody/tr/td[%d]' 
    
    def get_kpiName(self):
        Get_AnyText=Get_AnyText_ForNormal()
        KpiName_list=Get_AnyText.Get_Text_ForLoop(2, self.kpiName_path)
        return KpiName_list
    
    def get_GoalValue_page(self):
        Get_AnyText=Get_AnyText_ForNormal()
        GoalValue_list=Get_AnyText.Get_Text_ForLoop(2, self.GoalValue_path)
        return GoalValue_list
    def get_GoalTitle_page(self,kpiindex):
        flag=self.find_element(*self.Goal_KPITitle_path %kpiindex).text
        return flag
    
    
    def get_TeamValue_page(self):
        Get_AnyText=Get_AnyText_ForNormal()
        TeamValue_list=Get_AnyText.Get_Text_ForLoop(2, self.teamValue_path)
        return TeamValue_list
    
    
    def get_AgentValue_page(self):
        Get_AnyText=Get_AnyText_ForNormal()
        AgentValue_list=Get_AnyText.Get_Text_ForLoop(2, self.AgentValue_path)
        return AgentValue_list
    
    