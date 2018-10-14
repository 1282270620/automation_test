'''
Created on 2018.7.27

@author: yalan.yin
'''
from Tablet_pages import BasePage
from selenium.webdriver.common.by import By
#import time
#from public_method import Gl

class AddSitepage(BasePage.Action):
    '''
    classdocs
    '''


    def __init__(self):
        self.SiteName_loc=(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div[1]/div[2]/div/input")
        self.Addbutton_loc=(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/a")
        self.SiteNameinList_path="/html/body/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr[%d]/td[2]"
        self.YesButtonInConfirmationWindow_loc=(By.XPATH, "/html/body/div[4]/div/div/div[3]/ul/li[1]/a")
        self.SiteExistingMessage_loc=(By.CLASS_NAME, "alert ng-isolate-scope alert-warning alert-dismissible")
        self.SiteAddedSuccessMessage_loc=(By.CLASS_NAME, "alert ng-isolate-scope alert-success alert-dismissible")
        
        
    def Input_SiteName(self, sitename):
        self.find_element(*self.SiteName_loc).clear()
        self.find_element(*self.SiteName_loc).send_keys(sitename)
        
    def Click_AddButton(self):
        self.find_element(*self.Addbutton_loc).click()
        
    def Click_YesButton(self):
        self.find_element(*self.YesButtonInConfirmationWindow_loc).click()
        
    def Get_SiteNameinList(self, nameindex):
        SiteNamelist_loc=(By.XPATH, self.SiteNameinList_path % nameindex)
        return self.find_element(*SiteNamelist_loc).text
    def Site_isExist(self):
        pass
        
    def get_Sitenumber(self): #For getting tl numbers
        index=0
        flag=True
        while flag:
            Sitenumber=index
            index=index+1 
            anySitename_loc=(By.XPATH,self.SiteNameinList_path % index)
            flag=self.Element_displayed(*anySitename_loc) 
        return Sitenumber  
        
        
    def Is_sitenameExisting(self):
        #flag=self.isElementExist(*self.SiteExistingMessage_loc)
        flag=self.Element_displayed(*self.SiteExistingMessage_loc)
        print flag
        return flag
    def IS_siteddedsucessfully(self):
        flag=self.isElementExist(*self.SiteAddedSuccessMessage_loc)
        return flag
        
        