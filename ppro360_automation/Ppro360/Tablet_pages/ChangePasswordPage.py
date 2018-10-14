'''
Created on Mar 2, 2017

@author: Alice
'''
from selenium.webdriver.common.by import By
from Tablet_pages import BasePage
import time
#from operator import contains
from public_method import Gl

class ChangePasswordPage(BasePage.Action):
    
    def __init__(self):   
        self.currentPasswod_loc=(By.NAME,"password")
        self.newPassword_loc=(By.NAME,"newPassword")
        self.reNewPassword_loc=(By.NAME,"reNewPassword")
        self.submitButton_loc=(By.CSS_SELECTOR,"button.btn.primary")
        self.cancelButton_loc=(By.CSS_SELECTOR,"button.btn.btn-default")
        self.ChangeSuccesspopup_loc=(By.XPATH,"//*[@id='container']/div/section/section/div/div")
        self.changeSuccessTextLocation_loc=(By.XPATH,"//*[@id='container']/div/section/section//div/section/p")
        self.confirmOKButton_loc=(By.XPATH,"//div[@id='msg-modal']/footer/ul/li/a")
        self.newpassword_message_loc=(By.XPATH,"//*[@id='container']/div/section/section/form/div[2]/p")
        self.currentpassword_message_loc=(By.XPATH,"//*[@id='container']/div/section/section/form/div[1]/p")
        #self.currentpassword_message_loc=(By.XPATH,"//*[@id='container']/div/div[2]/div[1]/p[2]")
        self.Error_message_loc=(By.XPATH,"//*[@id='container']/div/div[2]/div[1]/p")
        self.Incorrectpassword_message_loc=(By.XPATH,"//*[@id='container']/div/div[2]/div[1]/p[2]")
        self.renewpassword_message_loc=(By.XPATH,"//*[@id='container']/div/section/section/form/div[3]/p")
        
    def currentPassword_Input(self,currentPassword):
        self.send_keys(self.currentPasswod_loc, currentPassword)
        time.sleep(Gl.waittime)
    def get_currentpasswordmessage(self):
        return self.find_element(*self.currentpassword_message_loc).text
    
    def get_Incorrectpasswordmessage(self):
        error_message=self.find_element(*self.Error_message_loc).text
        Incorrect_message=self.find_element(*self.Incorrectpassword_message_loc).text
        error_incorrect_message=error_message+" "+Incorrect_message
        return error_incorrect_message
        #return self.find_element(*self.Incorrectpassword_message_loc).text
        
    def newPassword_Input(self,newPassword):
        self.send_keys(self.newPassword_loc, newPassword)
        time.sleep(Gl.waittime)
    def get_newpasswordmessage(self):
        return self.find_element(*self.newpassword_message_loc).text
        
    def reNewPassword_Input(self,NewPassword):
        self.send_keys(self.reNewPassword_loc, NewPassword)
        time.sleep(Gl.waittime)
    def get_renewpasswordmessage(self):
        return self.find_element(*self.renewpassword_message_loc).text
        
    def click_Submitbutton(self):
        self.find_element(*self.submitButton_loc).click()
        time.sleep(Gl.waittime)
    
    def click_Cancelbutton(self):
        self.find_element(*self.cancelButton_loc).click()
        time.sleep(Gl.waittime)
    
    
    