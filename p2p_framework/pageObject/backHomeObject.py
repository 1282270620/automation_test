'''
Created on 2018年6月29日
后台首页
@author: Administrator
'''

from pageObject.BasePage import BasePage
from selenium.webdriver.common.by import By


class BackHomePage(BasePage):
    pend_approval = (By.XPATH,"html/body/div[2]/div/div[2]/div[1]/a/p")
    menu_preapproval = (By.XPATH,".//li[@class='active']/a")
    info_verify = (By.XPATH,".//*[@id='DataTables_Table_0']/tbody/tr[1]/td")
    to_examine = (By.XPATH,".//tbody[@aria-relevant='all']/tr[1]/td[8]/a[1]")
    examine_submit = (By.XPATH,".//*[@id='content']/form/div/div[2]/button")
    ass_point = (By.XPATH,".//*[@id='content']/form/div/div[2]/button")
    
    def into_examine(self):
        self.click(self.pend_approval)
        self.click(self.menu_preapproval)
    def info_list(self):
        self.ass_point = []
        elements_iterator = self.find_elements(self.info_verify)
        for element_iterator in elements_iterator:
            self.ass_point.append(element_iterator.text)
        return self.ass_point  
    def examine_click(self):
        self.click(self.to_examine)    
        self.click(self.examine_submit)
    
    
    