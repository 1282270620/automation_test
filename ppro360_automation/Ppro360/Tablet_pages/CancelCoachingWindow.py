'''
Created on Jul 26, 2017

@author: symbio
'''
from Tablet_pages import BasePage
from selenium.webdriver.common.by import By
import time
from public_method import Gl
class CancelCoachingWindow(BasePage.Action):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.windwontitle_loc=(By.XPATH,"//*[@id='disable-todo-modal']/header")
        self.windwoncontent_loc=(By.XPATH,"//*[@id='disable-todo-modal']/section/p[2]")
        self.button_path="//*[@id='disable-todo-modal']/footer/ul/li[%d]/a"#1-yes,2-cancel
        self.Yesbutton_loc=(By.XPATH,"//*[@id='disable-todo-modal']/footer/ul/li[1]/a")
        self.Cancelbutton_loc=(By.XPATH,"//*[@id='disable-todo-modal']/footer/ul/li[1]/a")
        
    def get_windowtitle(self):
        title=self.find_element(*self.windwontitle_loc).text
        title=title[0:12]
        return title
    def window_exist(self):
        return self.Element_displayed(*self.windwontitle_loc)
    
    def get_windowcontent(self):
        return self.find_element(*self.windwoncontent_loc).text
    
    def get_button_text(self,index):#1-yes,2-cancel
        button_loc=(By.XPATH,self.button_path % index)
        return self.find_element(*button_loc).text
    
    
    def click_Button(self,index):#1-yes,2-cancel
        button_loc=(By.XPATH,self.button_path % index)
        self.find_element(*button_loc).click()
        self.wait_loadingmask_disappear()