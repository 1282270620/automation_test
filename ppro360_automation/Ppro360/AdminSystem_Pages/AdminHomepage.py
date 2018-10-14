'''
Created on Dec 20, 2016

@author: symbio
'''
#import sys 
#sys.path.append("\test_cases") 
from Tablet_pages import BasePage
from selenium.webdriver.common.by import By
import time
from public_method import Gl





class AdminHomepage(BasePage.Action):
    
    
    def __init__(self):
        self.omaccounts_loc = (By.LINK_TEXT,"L3 Accounts")
        self.accountsbrowse_loc = (By.LINK_TEXT,"Browse")
        self.OMnameOntopright_loc=(By.XPATH,"/html/body/div[1]/div/div/a/div/div/dl/dt")
        self.Roster_loc=(By.XPATH,"/html/body/div[1]/div/ul/li[1]/a")
        self.RosterbrowseUH_loc=(By.XPATH,"//*[@id='top-menu']/li[2]/a")
        self.RosterUpload_loc=(By.XPATH,"//*[@id='top-menu']/li[1]/a")
        #self.Performance_loc=(By.XPATH,"/html/body/div[1]/div/ul/li[3]/a")
        self.Performance_loc=(By.LINK_TEXT,"Performance Data")
        self.TLAgentAccounts_loc=(By.XPATH,"/html/body/div[1]/div/ul/li[4]/a")
        self.TLAgentAccountsbrowse_loc=(By.LINK_TEXT,"Browse")
        
        #self.PerformancebrowseUH_loc=(By.XPATH,"//*[@id='top-menu']/li[2]/a")
        self.PerformancebrowseUH_loc=(By.XPATH,"(//a[contains(text(),'Browse Upload History')])[2]")
        self.PerformanceUpload_loc=(By.XPATH,"(//ul[@id='top-menu']/li/a)[4]")
        self.userhead_loc=(By.CSS_SELECTOR,"i.icon-user")
        self.logout_loc=(By.LINK_TEXT,"Logout")
        
        self.VPSVPaccounts_loc=(By.LINK_TEXT,"VP / SVP Accounts")
        self.BowseTLAgentAccounts_loc=(By.XPATH, 'html/body/div[1]/div/ul/li[4]/a')
        
        self.AddSite_loc=(By.LINK_TEXT, "Add Site")
        
    
        
    def Enter_BrowseTLAgentAccounts(self): #yalan added
        self.find_element(*self.BowseTLAgentAccounts_loc).click()
        time.sleep(Gl.waittime)
        self.find_element(*self.TLAgentAccountsbrowse_loc).click()
        time.sleep(Gl.waittime)
    
    def Enter_AddSite(self): 
        self.find_element(*self.AddSite_loc).click()
    
    
    def Enter_OMaccountbrowse(self):
        self.find_element(*self.omaccounts_loc).click()
        time.sleep(Gl.waittime)
        self.find_element(*self.accountsbrowse_loc).click()
        time.sleep(2*Gl.waittime)
    
    def Enter_TLAgentAccounts(self):
        self.find_element(*self.TLAgentAccounts_loc).click()
        time.sleep(Gl.waittime)
        self.find_element(*self.TLAgentAccountsbrowse_loc).click()
        time.sleep(Gl.waittime)
    
    def get_OMnameOntopright(self):
        return self.find_element(*self.OMnameOntopright_loc).text
    
    def Enter_Rosterhistory(self):
        self.find_element(*self.Roster_loc).click()
        time.sleep(Gl.waittime)
        self.find_element(*self.RosterbrowseUH_loc).click()
        time.sleep(Gl.waittime)
    
    def Enter_RoserUpload(self):
        self.find_element(*self.Roster_loc).click()
        time.sleep(Gl.waittime)
        self.find_element(*self.RosterUpload_loc).click()
        time.sleep(Gl.waittime)
        
    def Enter_Performancehistory(self):
        self.find_element(*self.Performance_loc).click()
        time.sleep(Gl.waittime)
        self.find_element(*self.PerformancebrowseUH_loc).click()
        time.sleep(Gl.waittime)
    
    def Enter_PerformanceUpload(self):
        self.find_element(*self.Performance_loc).click()
        time.sleep(Gl.waittime)
        self.find_element(*self.PerformanceUpload_loc).click()
        time.sleep(Gl.waittime)
        
    def Enter_VPSVPaccountbrowse(self):
        self.find_element(*self.VPSVPaccounts_loc).click()
        time.sleep(Gl.waittime)
        self.find_element(*self.accountsbrowse_loc).click()
        time.sleep(Gl.waittime)
         
        
    def click_userhead(self):
        self.find_element(*self.userhead_loc).click()
        time.sleep(Gl.waittime)
        
    def click_logout(self):
        self.find_element(*self.logout_loc).click()
        time.sleep(Gl.waittime)

        