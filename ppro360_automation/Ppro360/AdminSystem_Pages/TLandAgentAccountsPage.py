'''
Created on Jan 8, 2018

@author: symbio
'''
from Tablet_pages import BasePage
from selenium.webdriver.common.by import By
from public_method import Gl
import time


class TLandAgentAccountsPage(BasePage.Action):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.Back_loc = (By.LINK_TEXT,"Back to home")
        self.TLAgentInfoItem_path = "/html/body/div[2]/div/div[2]/div/div[1]/div[2]/table/tbody/tr[%d]/td[%d]"
        self.ExportButton_path='/html/body/div[2]/div/div[2]/div/div[2]/a/span'
        self.EachAccountName_path='/html/body/div[2]/div/div[2]/div/div[1]/div[2]/table/tbody/tr[%d]/td[1]'
        self.EachAccountHRID_path='/html/body/div[2]/div/div[2]/div/div[1]/div[2]/table/tbody/tr[%d]/td[2]'
        self.PageIndex_path='/html/body/div[2]/div/div[2]/div/div[1]/ul/li[%d]/a' #d>=3
        self.EachRoleTitleName_path='/html/body/div[2]/div/div[2]/div/div[1]/div[2]/table/tbody/tr[%d]/td[4]'
       
        
    def get_TLAgentInfoItem(self,d1,d2):
        '''d2=1:name
           d2=2:hrid
           d2=3:password
           d2=4:title
           d2=6:Activatied Date'''
        TLAgentInfoItem_loc=(By.XPATH,self.TLAgentInfoItem_path % (d1,d2))
        return self.find_element(*TLAgentInfoItem_loc).text
    
    def click_ExportButton(self): 
        ExportButton_loc=(By.XPATH,self.ExportButton_path)
        self.find_element(*ExportButton_loc).click()
        time.sleep(3*Gl.waittime)
    def get_PageNumber(self,index):
        index=0
        flag=True
        while flag:
            PageNumber=index
            index=index+1
            anyPageNumber_loc=(By.XPATH, self.PageIndex_path %index)  
            flag=self.Element_displayed(*anyPageNumber_loc)
            return PageNumber
        
    def click_Pagenumber(self,pageindex):
        '''First:pageindex=1;Previous:pageindex=2;1:pageindex=3.......'''
        Pagenumber_loc=(By.XPATH, self.PageIndex_path %pageindex)
        self.find_element(*Pagenumber_loc).click()
        self.wait_loadingmask_disappear()
        
    def Pagenumber_exist(self,pageindex):
        '''First:pageindex=1;Previous:pageindex=2;1:pageindex=3.......'''
        Pagenumber_loc=(By.XPATH, self.PageIndex_path %pageindex)
        flag=self.Element_displayed(*Pagenumber_loc)
        return flag
    def TLandAgent_exist(self,index):
        TLandAgent_loc=(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[1]/div[2]/table/tbody/tr[%d]/td[1]" %index)
        flag=self.find_element(*TLandAgent_loc)
        return flag
    
    
    def get_TLandAgentInfoList_anypage(self):
        AllTLAgentInfoList_Adminpage=[]
        index=1
        flag=True
        while flag:
            Lineindex=index
            #print Lineindex
            TLAgentName=self.get_TLAgentInfoItem(Lineindex, 1)
            TLAgentHrid=self.get_TLAgentInfoItem(Lineindex, 2)
            Oneaccountinfo=[TLAgentName, TLAgentHrid]
            print("Oneaccountinfo:", Oneaccountinfo)            
            AllTLAgentInfoList_Adminpage.append(Oneaccountinfo)
            index=index+1
            flag=self.TLandAgent_exist(index)
        return AllTLAgentInfoList_Adminpage
    
   
    def get_TLAgentnumberOnePage(self,d):
        d=0
        flag=True
        while flag:
            TLAgentnumber=d
            d=d+1
            anyTLAgentname_loc=(By.XPATH,self.EachAccountName_path %d)
            flag=self.Element_displayed(*anyTLAgentname_loc)
        return TLAgentnumber
    
    
            
        
    def get_anyTLAgentinfo(self,Lineindex):
        #for Itemindex in range (1,3):
        Itemindex=1
        flag=True
        anyTLAgentinfoList=[]
        while flag:
            anyTLAgent_loc=(By.XPATH,self.TLAgentInfoItem_path % (Lineindex,Itemindex))
            ItemInfo=self.find_element(*anyTLAgent_loc).text
            anyTLAgentinfoList.append(ItemInfo)
            Itemindex=Itemindex+1
            flag=self.isElementExist(*anyTLAgent_loc)
            
        return anyTLAgentinfoList
    
    def get_L2Hrid(self,lineindex):
        EachRoleTitleName_loc=(By.XPATH, self.EachRoleTitleName_path %lineindex)
        
        
    

    