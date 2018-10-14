'''
Created on Mar 10, 2017

@author: symbio
'''
from Tablet_pages import BasePage
from selenium.webdriver.common.by import By
import time
from public_method import Gl
class MyTeamInfoPage(BasePage.Action):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.nametitle_loc=(By.XPATH,"//*[@id='container']/div/section/div/div/table/thead/tr/th[1]")
        self.hridtitle_loc=(By.XPATH,"//*[@id='container']/div/section/div/div/table/thead/tr/th[2]")
        #self.passwordtitle_loc=(By.XPATH,"//*[@id='container']/div/section/div/div/table/thead/tr/th[3]")
        
        self.roletitle_loc=(By.XPATH,"//*[@id='container']/div/section/div/div/table/thead/tr/th[3]")
        self.activatedDatetitle_loc=(By.XPATH,"//*[@id='container']/div/section/div/div/table/thead/tr/th[4]")
        
        #self.exportbutton_loc=(By.XPATH,"//*[@id='container']/div/section/div/div/div/")
        self.exportbutton_loc=(By.XPATH,'//*[@id="container"]/div/section/div/div/div/a')
                                         
    #yalan added bellow
        self.anyTLname_path='//*[@id="container"]/div/section/div/div/table/tbody/tr[%d]/td[1]' #each tl's path
        
        
    
    def Nametitleexisting(self):
        return self.find_element(*self.nametitle_loc).get_attribute('class')
    def hridtitleexisting(self):
        return self.find_element(*self.hridtitle_loc).get_attribute('class')
    def roletitleexisting(self):
        return self.find_element(*self.roletitle_loc).get_attribute('class')
    def activateddateexisting(self):
        return self.find_element(*self.activatedDatetitle_loc).get_attribute('class')
    def get_TLnumber(self): #For getting tl numbers
        index=0
        flag=True
        while flag:
            TLnumber=index
            index=index+1 
            anyTLname_loc=(By.XPATH,self.anyTLname_path % index)
            flag=self.Element_displayed(*anyTLname_loc) 
        return TLnumber
        
    #yalan added above
    
        
    def get_nametitle(self):
        return self.find_element(*self.nametitle_loc).text
    def get_hridtitle(self):
        return self.find_element(*self.hridtitle_loc).text
    def get_passwordtitle(self):
        return self.find_element(*self.passwordtitle_loc).text
    def get_roletitle(self):
        return self.find_element(*self.roletitle_loc).text
    def get_activateddatetitle(self):
        return self.find_element(*self.activatedDatetitle_loc).text
    
    def get_eachusername(self,lineindex):
        eachusername_loc=(By.XPATH,("//*[@id='container']/div/section/div/div/table/tbody/tr[%d]/td[1]")% lineindex)
        return self.find_element(*eachusername_loc).text
    def get_eachhrid(self,lineindex):
        eachhrid_loc=(By.XPATH,("//*[@id='container']/div/section/div/div/table/tbody/tr[%d]/td[2]") % lineindex)
        return self.find_element(*eachhrid_loc).text

    def get_eachpwd(self,lineindex):
        eachpwd_loc=(By.XPATH,("//*[@id='container']/div/section/div/div/table/tbody/tr[%d]/td[3]") % lineindex)
        return self.find_element(*eachpwd_loc).text
    def get_eachrole(self,lineindex):
        eachrole_loc=(By.XPATH,("//*[@id='container']/div/section/div/div/table/tbody/tr[%d]/td[4]") % lineindex)
        return self.find_element(*eachrole_loc).text
    def get_eachactivateddate(self,lineindex):
        eachactiveddate_loc=(By.XPATH,("//*[@id='container']/div/section/div/div/table/tbody/tr[%d]/td[5]") % lineindex)
        return self.find_element(*eachactiveddate_loc).text

    
    def click_exportbutton(self):
        self.find_element(*self.exportbutton_loc).click()
        time.sleep(Gl.waittime)