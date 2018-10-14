'''
Created on 20170307

@author: luming.zhao
'''

from selenium.webdriver.common.by import By
from Tablet_pages import BasePage
import time
from public_method import Gl

class Commendation(BasePage.Action):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.callRecordingID_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div/div/input")
        self.callRecordingID_title_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div[1]/div[1]/label")
        #self.dateandtime_pick=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div/div[2]/div/div/div[2]/span/span")
        self.dateandtime_date=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div/div[2]/div/div/div[2]/ul/li/div/div/table/tbody/tr[2]/td[2]")
        self.commendation_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div[2]/div/textarea")
        self.commendation_title_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div[2]/label")
        self.savebutton_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[3]/a[2]")
        self.DateandTimeofCall_input_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[2]/div[1]/div[2]/div/div/div[2]/input")
        self.DateandTimeofCall_selection_loc=(By.CSS_SELECTOR,"span.glyphicon.glyphicon-calendar")
        self.TheFirstTime_select_loc=(By.XPATH,"//div[@id='container']/div/section/div/form/div[2]/div[2]/div/div[2]/div/div/div[2]/ul/li/div/div/table/tbody/tr/td")
        self.anyDateTimeOfCall_path="//div[@id='container']/div/section/div/form/div[2]/div[2]/div[1]/div[2]/div/div/div[2]/ul/li[1]/div/div/table/tbody/tr[%d]/td[%d]"
     
     
    def input_DateandTimeofCall(self,text):
        self.find_element(*self.DateandTimeofCall_input_loc).send_keys(text)  
        time.sleep(Gl.waittime)  
    def get_DateandTimeofCall(self):
        return self.find_element(*self.DateandTimeofCall_input_loc).get_attribute("value")
    def DateandTimeofCall__disabled(self):
        flag=self.find_element(*self.DateandTimeofCall_input_loc).get_attribute("disabled")
        return flag
    def select_ThefirstTimeOfDateandTimeofCall(self):
        self.find_element(*self.DateandTimeofCall_selection_loc).click()
        self.find_element(*self.TheFirstTime_select_loc).click()
        time.sleep(Gl.waittime)
    def select_anyDateTimeOfCall(self,lineindex,dateindex):#lineindex is from 1 to 6;dateindex is from 1 to 7
        self.find_element(*self.DateandTimeofCall_selection_loc).click()
        anyDateTimeOfCall_loc=(By.XPATH,self.anyDateTimeOfCall_path % (lineindex,dateindex))
        self.find_element(*anyDateTimeOfCall_loc).click()
        time.sleep(Gl.waittime)
        
    def get_callRecordingIDBoxTitle(self):
        return self.find_element(*self.callRecordingID_title_loc).text 
    
    def input_callRecordingID(self,text):
        self.Input_text(text,*self.callRecordingID_loc)
        time.sleep(Gl.waittime)
    def get_callRecordingID(self):
        return self.find_element(*self.callRecordingID_loc).get_attribute("value")
    def callRecordingID_disabled(self):
        flag=self.find_element(*self.callRecordingID_loc).get_attribute("disabled")
        return flag
        
    def get_commendationBoxTitle(self):
        return self.find_element(*self.commendation_title_loc).text
    
    def input_commendation(self,text):
        self.Input_text(text,*self.commendation_loc)
        time.sleep(Gl.waittime)
    def get_commendation(self):
        return self.find_element(*self.commendation_loc).text
    def commendation__disabled(self):
        flag=self.find_element(*self.commendation_loc).get_attribute("disabled")
        return flag
        
    def click_dateandtimepick(self):
        self.find_element(*self.dateandtime_pick).click()
        
    def click_dateandtimedate(self):
        self.find_element(*self.dateandtime_date).click()
        
    def click_savebutton(self):
        self.find_element(*self.savebutton_loc).click()    
        
        
        
        
