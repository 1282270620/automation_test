'''
Created on 2018/2/8

@author: luming.zhao
'''
from Tablet_pages import BasePage
from selenium.webdriver.common.by import By
from public_method.Get_AnyText_ForNormal import Get_AnyText_ForNormal
class Loblist_ForvpOrsvp(BasePage.Action):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.LOB_checkbox_path = "/html/body/div[2]/div/div[2]/div/div/ul/li[%d]/input" #index is 1 to 20
        self.LOB_name_path = "/html/body/div[2]/div/div[2]/div/div/ul/li[%d]"
        self.SITE_name_path = "/html/body/div[2]/div/div[2]/div/div/ul/li[%d]/ul/li[%d]/div/input"
    def get_loblists_page(self):
        Get_AnyText=Get_AnyText_ForNormal()
        Alllobs_list=Get_AnyText.Get_Text_ForLoop(1, self.LOB_name_path)
        return Alllobs_list
    
    def select_AllLOB(self,MaxLOBindex):
        #self.LOB_path = "/html/body/div[2]/div/div[2]/div/div/ul/li[%d]/input"
        if MaxLOBindex >= 1:
            for lobindex in range(1,MaxLOBindex+1):
                lob_checkbox_loc=(By.XPATH,self.LOB_checkbox_path % lobindex)
                self.find_element(*lob_checkbox_loc).click()
        else:
            print "There is no lob to be selected."
            
            
    def get_siteslistpage(self):
        Get_AnyText=Get_AnyText_ForNormal()
        AllSites_list=Get_AnyText.Get_Text_ForLoop(1, self.SITE_name_path)
        return AllSites_list
    
    