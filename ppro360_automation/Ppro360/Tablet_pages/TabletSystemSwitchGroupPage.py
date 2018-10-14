'''
Created on 2018/8/1

@author: hanyang.dong
'''

from Tablet_pages import BasePage
from selenium.webdriver.common.by import By
import time
from public_method import Gl
from public_method.Get_AnyText_ForNormal import Get_AnyText_ForNormal

class TabletSystemSwitchGroupPage(BasePage.Action):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    
        self.Setbutton_loc = (By.XPATH,'//*[@id="container"]/div/nav/ul/li/a/i')
        self.Switch_loc = (By.LINK_TEXT,"Switch Lob")
        
        
        self.SwitchLob_svpAndvpRole_loc=(By.XPATH,'//*[@id="logout-menu"]/li[2]/a')
        self.SwitchLob_otherrrole_loc=(By.XPATH,'//*[@id="logout-menu"]/li[1]/a')

        
        self.Switchlists_svpAndvpRole_path='//*[@id="container"]/div/div[4]/div/section/div/ul/li[%d]/a'
        self.Switchlists_otherrole_path='//*[@id="container"]/div/div[3]/div/section/div/ul/li[%d]/a'

        self.Switchlist_svpAndvpRole_loc=(By.XPATH,'//*[@id="container"]/div/div[4]/div/section/div/span')
        self.Switchlist_otherrole_loc=(By.XPATH,'//*[@id="container"]/div/div[3]/div/section/div/span')

        self.Switchlist_loc=(By.XPATH,'//*[@id="container"]/div/div[3]/div/section/div/span')
        
        self.Switchbutton_svpAndvpRole_loc=(By.XPATH,'//*[@id="container"]/div/div[4]/div/footer/ul/li[1]/a')
        self.Switchbutton_otherrole_loc=(By.XPATH,'//*[@id="container"]/div/div[3]/div/footer/ul/li[1]/a')

        self.Switchlob_cancel_svpAndvpRole_loc=(By.XPATH,'//*[@id="container"]/div/div[4]/div/header/a')
        self.Switchlob_cancel_otherroleloc=(By.XPATH,'//*[@id="container"]/div/div[3]/div/header/a')
        
        self.Lobsite_loc = (By.XPATH,'//*[@id="container"]/div/nav/ul/li/a/div/div/dl/dd')
        
       
        
        self._loc=(By.XPATH,'')
        self._loc = (By.LINK_TEXT,"")
        
    def click_(self):
        self.find_element(*self._loc).click()
        time.sleep(Gl.waittime)
        
    def get_(self):
        return self.find_element(*self._loc).text        
        
    def click_Setbutton(self):
        self.find_element(*self.Setbutton_loc).click()
        time.sleep(Gl.waittime)
        
    def get_alllobsInGroup(self,role):
        Get_Text=Get_AnyText_ForNormal()
        if role=="VP" or role=="SVP":
            Any_path=self.Switchlists_svpAndvpRole_path
        else:
            Any_path=self.Switchlists_otherrole_path
        lobs_list=Get_Text.Get_Text_ForLoop(1, Any_path)
        return lobs_list
        
    def click_SwitchLob(self,role):
        if role=="VP" or role=="SVP":
            self.find_element(*self.SwitchLob_svpAndvpRole_loc).click()
        else:
            self.find_element(*self.SwitchLob_otherrrole_loc).click()
        time.sleep(1)
        
    def click_Switchlist(self,role):
        if role=="VP" or role=="SVP":
            self.find_element(*self.Switchlist_svpAndvpRole_loc).click()
        else:
            self.find_element(*self.Switchlist_otherrole_loc).click()
        time.sleep(1)
        
    #def click_Switchlist(self):
        #self.find_element(*self.Switchlist_loc).click()
        #time.sleep(1)
        
    def click_Switchlob_cancel_loc(self,role):
        if role=="VP" or role=="SVP":
            self.find_element(*self.Switchlob_cancel_svpAndvpRole_loc).click()
        else:
            self.find_element(*self.Switchlob_cancel_otherroleloc).click()
        time.sleep(3)
  
        
    def click_Switchlists(self,index,role):
        if role=="VP" or role=="SVP":
            self.Switchlists_loc=(By.XPATH,self.Switchlists_svpAndvpRole_path % index)
            self.find_element(*self.Switchlists_loc).click()
        else:
            self.Switchlists_loc=(By.XPATH,self.Switchlists_otherrole_path % index)
            self.find_element(*self.Switchlists_loc).click()
        time.sleep(2)


    def click_Switchbutton(self,role):
        if role=="VP" or role=="SVP":
            self.find_element(*self.Switchbutton_svpAndvpRole_loc).click()
        else:
            self.find_element(*self.Switchbutton_otherrole_loc).click()
        time.sleep(2)

    