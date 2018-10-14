'''
Created on Mar 29, 2017

@author: symbio
'''
from Tablet_pages import BasePage
from selenium.webdriver.common.by import By
import time
from public_method import Gl

class DeleteUploadedDataPage(BasePage.Action):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.password_inputbox_loc=(By.XPATH,"//*[@id='delete_dialog']/div/div[2]/div/div/label/input")
        self.delete_button_loc=(By.XPATH,"//*[@id='delete_dialog']/div/div[3]/a[1]")

        
    def click_warning_message(self,index):
        warning_checkbox=(By.XPATH,("//div[@id='delete_dialog']/div/div[2]/div/ul/li[%d]/div/label")%index)
        self.find_element(*warning_checkbox).click()
        time.sleep(Gl.waittime)

        
    def Input_password(self,OMpassword):
        self.find_element(*self.password_inputbox_loc).send_keys(OMpassword)
        time.sleep(Gl.waittime)
        
    def Click_delete_button(self):
        self.find_element(*self.delete_button_loc).click()
        time.sleep(Gl.waittime)