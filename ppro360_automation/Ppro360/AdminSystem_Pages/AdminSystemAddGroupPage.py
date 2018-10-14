'''
Created on 2018/8/1

@author: hanyang.dong
'''
from Tablet_pages import BasePage
from selenium.webdriver.common.by import By
import time
from public_method import Gl
from public_method.Get_AnyText_ForNormal import Get_AnyText_ForNormal

class AdminSystemAddGroupPage(BasePage.Action):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self._loc=(By.XPATH,"")
        self._loc = (By.LINK_TEXT,"")
        
        
    
        self.SwitchLoBConfig_loc=(By.XPATH,"/html/body/div[1]/div/ul/li[2]/a")
        self.Browse_loc=(By.LINK_TEXT,'Browse')
        self.YOUNGSTOWNGroup_loc = (By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div/table/tbody/tr[2]/td[1]')
        self.Delete_loc = (By.LINK_TEXT,"Delete")
        self.Yes_loc = (By.LINK_TEXT,"Yes")
        self.Add_loc=(By.XPATH,"/html/body/div[2]/div/div[1]/div/div/a[1]")
        self.GroupName_loc=(By.XPATH,"/html/body/div[2]/div/div[2]/div/div/div[2]/div/input")
        self.siteYOUNGSTOWN_loc=(By.LINK_TEXT,"YOUNGSTOWN")
        
        self.SwitchAddLOBGroup_path="/html/body/div[2]/div/div[2]/div/div/ul/li[%d]/input"
        self.SwitchAddsiteGroup_path='/html/body/div[2]/div/div[2]/div/div/ul/li[12]/ul/li[%d]/div/input'
        
        self.Loblists_path='/html/body/div[2]/div/div[2]/div/div/ul/li[%d]'
        
        self.DTVDSSitelists_path='/html/body/div[2]/div/div[2]/div/div/ul/li[12]/ul/li[%d]/div'
        
        self.AddLoblists_path="/html/body/div[2]/div/div[2]/div/div/ul/li[%d]"

    def click_(self):
        self.find_element(*self._loc).click()
        time.sleep(Gl.waittime)
        
    def get_(self):
        return self.find_element(*self._loc).text
    
    def get_YOUNGSTOWNGroup(self):
        return self.find_element(*self.YOUNGSTOWNGroup_loc)
    def get_GroupName(self):
        return self.find_element(*self.GroupName_loc).text
    
    def click_SwitchLoBConfig(self):
        self.find_element(*self.SwitchLoBConfig_loc).click()
        time.sleep(1)
    def click_Browse(self):
        self.find_element(*self.Browse_loc).click()
        time.sleep(1)
    def click_YOUNGSTOWNGroup(self):
        self.find_element(*self.YOUNGSTOWNGroup_loc).click()
        time.sleep(1)
    def click_Delete(self):
        self.find_element(*self.Delete_loc).click()
        time.sleep(1)
    def click_Yes(self):
        self.find_element(*self.Yes_loc).click()
        time.sleep(1)
    def click_Add(self):
        self.find_element(*self.Add_loc).click()
        time.sleep(3)
    def click_GroupName(self):
        self.find_element(*self.GroupName_loc).click()
        time.sleep(1)
    def click_siteYOUNGSTOWN(self):
        self.find_element(*self.siteYOUNGSTOWN_loc).click()
        time.sleep(1)
        
    def click_SwitchAddLOBGroup(self,index):
        SwitchAddLOBGroup_loc=(By.XPATH,self.SwitchAddLOBGroup_path % index)
        self.find_element(*SwitchAddLOBGroup_loc).click()
        time.sleep(2)
        
    def click_SwitchAddsiteGroup(self,index):
        SwitchAddsiteGroup_loc=(By.XPATH,self.SwitchAddsiteGroup_path % index)
        self.find_element(*SwitchAddsiteGroup_loc).click()
        time.sleep(2)
        
    def input_GroupName(self,text):
        self.find_element(*self.GroupName_loc).send_keys(text);
        time.sleep(2)
        
    def get_AddLoblists(self,index):
        AddLoblists_loc=(By.XPATH,self.AddLoblists_path % index)
        return self.find_element(*AddLoblists_loc).text
        time.sleep(2)
    
    def get_alllobsInGroup(self):
        Get_Text=Get_AnyText_ForNormal()
        Any_path=self.Loblists_path
        lobs_list=Get_Text.Get_Text_ForLoop(1, Any_path)
        return lobs_list
        time.sleep(2)
    
    def get_dtvdssitesInGroup(self):
        Get_Text=Get_AnyText_ForNormal()
        Any_path=self.DTVDSSitelists_path
        dtvdssite_list=Get_Text.Get_Text_ForLoop(1, Any_path)
        return dtvdssite_list
        time.sleep(2)
        

        