'''
Created on Mar 22, 2017

@author: symbio
'''
from selenium.webdriver.common.by import By
from Tablet_pages import BasePage
import time
from public_method import Gl

class PerformanceUploadPage(BasePage.Action):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.BrowseFile_button_loc=(By.XPATH,"/html/body/div[2]/div/div[2]/div/div/p[1]/label")
        
        self.BrowseFile_input_loc=(By.XPATH,"//html/body/div[2]/div/div[2]/div/div/p[1]/label/input")
        
        self.Upload_message_loc=(By.XPATH,"/html/body/div[2]/div/div[2]/div/div/p[2]/span")
        
        self.Upload_success_icon_loc=(By.CLASS_NAME,"icon-view success")
        self.Upload_loading_circle_loc=(By.CLASS_NAME,"icon-view ng-hide loading")
        self.BroweUploadHistory_link_loc=(By.LINK_TEXT,"Browse Upload history")
        self.UploadAnother_link_loc=(By.LINK_TEXT,"Upload Another")
        self.TryAgain_link_loc=(By.LINK_TEXT,"Try Again")
        #self.progressbar_loc=(By.XPATH,"/html/body/div[2]/div/div[2]/div/div/div/span/i")#/span/
        #self.progressbar_loc=(By.XPATH,"//*[@class='center relative'/span")
        
    def Click_BrowseFlie(self):
        self.find_element(*self.BrowseFile_button_loc).click()
        time.sleep(2*Gl.waittime)
    
   
    def get_upload_message(self):
        flag=True
        while flag:
            uploadmessage=self.find_element(*self.Upload_message_loc).text
            if uploadmessage=="Data is being processed...":
                flag=True
            else:
                flag=False
        return uploadmessage
    
        
        
    def BroweUploadHistory_link_displayed(self):
        Flag=self.find_element(*self.BroweUploadHistory_link_loc).is_displayed()
        return Flag
    def UploadAnother_link_displayed(self):
        Flag=self.find_element(*self.UploadAnother_link_loc).is_displayed()
        return Flag
    def TryAgain_link_displayed(self):
        Flag=self.find_element(*self.TryAgain_link_loc).is_displayed()
        return Flag
