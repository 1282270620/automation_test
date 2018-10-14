'''
Created on 2018.2.7

@author: haodong.liu
'''
from selenium.webdriver.common.by import By
from Tablet_pages import BasePage


class MonthlyGoalSettingSupervisorPage(BasePage.Action):
    
    def __init__(self):
        self.KPIcheckbox_path='//*[@id="container"]/div/section/div/form/div[2]/div[1]/div/table/tbody/tr[4]/td[%d]/i'
        self.ShortComments_path='//*[@id="container"]/div/section/div/form/div[2]/div[%d]/div[1]/div[2]/div/input'
        self.LongComments_path1=(By.XPATH,'//*[@id="container"]/div/section/div/form/div[2]/div[3]/div/textarea')
        self.LongComments_path2='//*[@id="container"]/div/section/div/form/div[2]/div[%d]/div[2]/textarea'
        self.LongComments_path3='//*[@id="container"]/div/section/div/form/div[2]/div[%d]/div[%d]/div[2]/textarea'
        self.PreviousCurrentGoalComments_path='//*[@id="container"]/div/section/div/form/div[2]/div[%d]/div[%d]/div[%d]/div[2]/input'
        self.GoalActualComments_path='//*[@id="container"]/div/section/div/form/div[2]/div[%d]/table[%d]/tbody/tr[%d]/td[%d]/input'
        self.LongTtile_path1=(By.XPATH,'//*[@id="container"]/div/section/div/form/div[2]/div[3]/label')
        self.LongTtile_path2='//*[@id="container"]/div/section/div/form/div[2]/div[%d]/div[1]'
        self.LongTtile_path3='//*[@id="container"]/div/section/div/form/div[2]/div[%d]/div[%d]/div[1]'
    
    def get_firstTL_HRID(self,TLindex):
        FisrtTL_loc=(By.XPATH,("//*[@id='container']/div/section/div/div[2]/div/table/tbody/tr[%d]") %TLindex)
        return self.find_element(*FisrtTL_loc).get_attribute("data-id")
    
    def ClickKpiBox(self,index):
        self.ClickKpiBox_loc=(By.XPATH,self.KPIcheckbox_path %index)
        self.find_element(*self.ClickKpiBox_loc).click()
    
    def getLongTitle1(self):
        return self.find_element(*self.LongTtile_path1).text
    def getLongTitle2(self,index):
        self.LongTitle=(By.XPATH,self.LongTtile_path2 %index)
        return self.find_element(*self.LongTitle).text
    def getLongTitle3(self,index1,index2):
        self.LongTitle=(By.XPATH,self.LongTtile_path3 %(index1,index2))
        return self.find_element(*self.LongTitle).text
    
    def Input_ShortComments(self,index,text):
        self.ShortComments_loc=(By.XPATH,self.ShortComments_path %index)
        self.find_element(*self.ShortComments_loc).send_keys(text)
    def get_ShortComments(self,index):
        self.ShortComments_loc=(By.XPATH,self.ShortComments_path %index)
        return self.find_element(*self.ShortComments_loc).get_attribute('value')
    def ShortComments_disabled(self,index):
        self.ShortComments_loc=(By.XPATH,self.ShortComments_path %index)
        flag=self.find_element(*self.ShortComments_loc).get_attribute('disabled')
        return flag
    
    def Input_LongComments1(self,text):
        self.find_element(*self.LongComments_path1).send_keys(text)
    def get_LongComments1(self):
        return self.find_element(*self.LongComments_path1).text
    def LongComments1_disabled(self):
        flag=self.find_element(*self.LongComments_path1).get_attribute('disabled')
        return flag
    
    def Input_LongComments2(self,index,text):
        self.LongComments_loc=(By.XPATH,self.LongComments_path2 %index)
        self.find_element(*self.LongComments_loc).send_keys(text)
    def get_LongComments2(self,index):
        self.LongComments_loc=(By.XPATH,self.LongComments_path2 %index)
        return self.find_element(*self.LongComments_loc).text
    def LongComments2_disabled(self,index):
        self.LongComments_loc=(By.XPATH,self.LongComments_path2 %index)
        flag=self.find_element(*self.LongComments_loc).get_attribute('disabled')
        return flag
    
    def Input_LongComments3(self,index1,index2,text):
        self.LongComments_loc=(By.XPATH,self.LongComments_path3 %(index1,index2))
        self.find_element(*self.LongComments_loc).send_keys(text)
    def get_LongComments3(self,index1,index2):
        self.LongComments_loc=(By.XPATH,self.LongComments_path3 %(index1,index2))
        return self.find_element(*self.LongComments_loc).text
    def LongComments3_disabled(self,index1,index2):
        self.LongComments_loc=(By.XPATH,self.LongComments_path3 %(index1,index2))
        flag=self.find_element(*self.LongComments_loc).get_attribute('disabled')
        return flag
    
    def Input_PreviousCurrentGoalComments(self,index1,index2,index3,text):
        self.PreviousCurrentGoalComments_loc=(By.XPATH,self.PreviousCurrentGoalComments_path %(index1,index2,index3))
        self.find_element(*self.PreviousCurrentGoalComments_loc).send_keys(text)
    def get_PreviousCurrentGoalComments(self,index1,index2,index3):
        self.PreviousCurrentGoalComments_loc=(By.XPATH,self.PreviousCurrentGoalComments_path %(index1,index2,index3))
        return self.find_element(*self.PreviousCurrentGoalComments_loc).get_attribute('value')
    def PreviousCurrentGoalComments_disabled(self,index1,index2,index3):
        self.PreviousCurrentGoalComments_loc=(By.XPATH,self.PreviousCurrentGoalComments_path %(index1,index2,index3))
        flag=self.find_element(*self.PreviousCurrentGoalComments_loc).get_attribute('disabled')
        return flag
    
    def Input_GoalActualComments(self,index1,index2,index3,index4,text):
        self.GoalActualComments_loc=(By.XPATH,self.GoalActualComments_path %(index1,index2,index3,index4))
        self.find_element(*self.GoalActualComments_loc).send_keys(text)
    def get_GoalActualComments(self,index1,index2,index3,index4):
        self.GoalActualComments_loc=(By.XPATH,self.GoalActualComments_path %(index1,index2,index3,index4))
        return self.find_element(*self.GoalActualComments_loc).get_attribute('value')
    def GoalActualComments_disabled(self,index1,index2,index3,index4):
        self.GoalActualComments_loc=(By.XPATH,self.GoalActualComments_path %(index1,index2,index3,index4))
        flag=self.find_element(*self.GoalActualComments_loc).get_attribute('disabled')
        return flag