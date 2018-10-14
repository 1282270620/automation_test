'''
Created on 2018.4.18

@author: yalan.yin
'''

from Tablet_pages import BasePage
from selenium.webdriver.common.by import By


class RosterHistoryPage(BasePage.Action):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.anyRosterRecord_path='/html/body/div[2]/div/div[2]/div/div/div[2]/div/table/tbody/tr[%d]/td[1]'
        self.activeRosterRecord_path='/html/body/div[2]/div/div[2]/div/div/div[2]/div/table/tbody/tr[%d]/td[1]/span'
        self.Download_path='/html/body/div[2]/div/div[2]/div/div/div[2]/div/table/tbody/tr[%d]/td[3]/div/a' #d=rosterindex
        
    def is_CurrentActiveExist(self,rosterindex):
        CurrentActiveRoster_loc=(By.XPATH, self.activeRosterRecord_path % rosterindex)
        flag=self.find_element(*CurrentActiveRoster_loc).get_attribute('class')
        return flag
    def Click_Download(self,rosterindex):
        Download_loc=(By.XPATH,self.Download_path % rosterindex)
        self.find_element(*Download_loc).click()
    def Click_anyRosterRecord(self,rosterindex):
        anyRosterRecord_loc=(By.XPATH, self.anyRosterRecord_path % rosterindex)
        self.find_element(*anyRosterRecord_loc).click()
        