'''
Created on 2017.6.26

@author: yalan.yin
'''

from selenium.webdriver.common.by import By
from Tablet_pages import BasePage

class DateTimeSelectorPage(BasePage):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        
        self.MonthYearTitle_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[3]/div[1]/div/div/div[2]/ul/li[1]/div/div/table/thead/tr[1]/th[2]')
        self.YearTitle_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[3]/div[1]/div/div/div[2]/ul/li[1]/div/div/table/thead/tr/th[2]')
        self.ClockIcon_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[3]/div[1]/div/div/div[2]/ul/li[2]/span')
        self.CalenderIcon_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[3]/div[1]/div/div/div[2]/ul/li[1]/span')
        self.LeftBigArrow_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[3]/div[1]/div/div/div[2]/ul/li[1]/div/div/table/thead/tr[1]/th[1]')
        self.LeftSmallArrow_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[3]/div[1]/div/div/div[2]/ul/li[1]/div/div/table/thead/tr/th[1]')
        self.RightBigArrow_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[3]/div[1]/div/div/div[2]/ul/li[1]/div/div/table/thead/tr[1]/th[3]')
        self.RightSmallArrow_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[3]/div[1]/div/div/div[2]/ul/li[1]/div/div/table/thead/tr/th[3]')
        self.AMOrPMbutton_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[3]/div[1]/div/div/div[2]/ul/li[2]/div/div/table/tbody/tr[2]/td[5]/button')
        self.UpHourSelectArrow_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[3]/div[1]/div/div/div[2]/ul/li[2]/div/div/table/tbody/tr[1]/td[1]/a/span')
        self.UpMinuteSelectArrow_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[3]/div[1]/div/div/div[2]/ul/li[2]/div/div/table/tbody/tr[1]/td[3]/a/span')
        self.DownHourSelectArrow_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[3]/div[1]/div/div/div[2]/ul/li[2]/div/div/table/tbody/tr[3]/td[1]/a/span')
        self.DownMinuteSelectArrow_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[3]/div[1]/div/div/div[2]/ul/li[2]/div/div/table/tbody/tr[3]/td[3]/a/span')
        
        
        
        
    def click_FirstLineDate (self, DayIndex):
        self.Date_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[3]/div[1]/div/div/div[2]/ul/li[1]/div/div/table/tbody/tr[1]/td[%d]' %DayIndex)
        self.find_element(*self.FirstLineDate_loc).click()
        
    def click_SecondLineDate (self, DayIndex):
        self.SecondLineDate_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[3]/div[1]/div/div/div[2]/ul/li[1]/div/div/table/tbody/tr[2]/td[%d]' %DayIndex)
        self.find_element(*self.SecondLineDate_loc).click()
        
    def click_ThridLineDate(self, DayIndex):
        self.ThridLineDate_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[3]/div[1]/div/div/div[2]/ul/li[1]/div/div/table/tbody/tr[3]/td[%d]' %DayIndex)
        self.find_element(*self.ThridLineDate_loc).click()
        
    def click_ForthLineDate (self, DayIndex):
        self.ForthLineDate_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[3]/div[1]/div/div/div[2]/ul/li[1]/div/div/table/tbody/tr[4]/td[%d]' %DayIndex)
        self.find_element(*self.ForthLineDate_loc).click()
        
    def click_FifthLineDate (self, DayIndex):
        self.FifthLineDate_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[3]/div[1]/div/div/div[2]/ul/li[1]/div/div/table/tbody/tr[5]/td[%d]' %DayIndex)
        self.find_element(*self.FifthLineDate_loc).click()
        
    def click_SixthLineDate (self, DayIndex):
        self.SixthLineDate_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[3]/div[1]/div/div/div[2]/ul/li[1]/div/div/table/tbody/tr[6]/td[%d]' %DayIndex)
        self.find_element(*self.SixthLineDate_loc).click()

    def click_MonthOrYear (self, MonthOrYearIndex):
        self.MonthOrYear_loc=(By.XPATH, '//*[@id="container"]/div/section/div/form/div[2]/div[3]/div[1]/div/div/div[2]/ul/li[1]/div/div/table/tbody/tr/td/span[%]' %MonthOrYearIndex)
        self.find_element(*self.MonthOrYear_loc).click()
    
    def click_MonthYearTitle (self):
        self.find_element(*self.MonthYearTitle_loc).click()
    
    def click_YearTitle (self):
        self.find_element(*self.YearTitle_loc).click()
    
    def click_ClockIcon (self):
        self.find_element(*self.ClockIcon_loc).click()

    def click_CalenderIcon (self):
        self.find_element(*self.CalenderIcon_loc).click()
        
    def click_LeftBigArrow (self):
        self.find_element(*self.LeftBigArrow_loc).click()
    
    def click_LeftSmallArrow (self):
        self.find_element(*self.LeftSmallArrow_loc).click()
        
    def click_RightBigArrow (self):
        self.find_element(*self.RightBigArrow_loc).click()
        
    def click_RightSmallArrow (self):
        self.find_element(*self.RightSmallArrow_loc).click()
    
    def click_AMOrPmButton (self):
        self.find_element(*self.AMOrPMbutton_loc).click()
        
    def click_UpHourSelectArrow (self):
        self.find_element(*self.UpHourSelectArrow_loc).click()
        
    def click_UpMinuteSelectArrow (self):
        self.find_element(*self.UpMinuteSelectArrow_loc).click()
        
    def click_DownMinuteSelectArrow (self):
        self.find_element(*self.DownMinuteSelectArrow_loc).click()
        
    def click_DownHourSelectArrow (self):
        self.find_element(*self.DownHourSelectArrow_loc).click()


       
    




            
    