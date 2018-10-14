'''
Created on Apr 24, 2017

@author: symbio
'''
from Tablet_pages import BasePage
from selenium.webdriver.common.by import By
from Tablet_pages.PerformancPage import PerformancePage
import time
from public_method import Gl

class OutlierPage(BasePage.Action):
    '''
    classdocs
    '''


    def __init__(self):
        self.mtd_loc=(By.XPATH,"//*[@id='container']/div/section/div/div[1]/ul/li[5]")
        self.wtd_loc=(By.XPATH,"//*[@id='container']/div/section/div/div[1]/ul/li[4]")
        self.ytd_loc=(By.XPATH,"//*[@id='container']/div/section/div/div[1]/ul/li[3]")
        self.timetab_path="//*[@id='container']/div/section/div/div[1]/ul/li[%d]"
        self.anyKPIname_path="//*[@id='container']/div/section/div/div[2]/table/thead/tr/th[%d]"
        self.anyKPIofTop20_path="//*[@id='container']/div/section/div/div[2]/div/table[1]/tbody/tr[%d]/td[%d]"
        self.anyKPIofBottom20_path="//*[@id='container']/div/section/div/div[2]/div/table[2]/tbody/tr[%d]/td[%d]"
        self.addcoachbutton_loc=(By.LINK_TEXT,"Add Coaching Form")
    def click_timetab_Outlier(self,index):
        timetab_loc=(By.XPATH,self.timetab_path % index)  
        self.find_element(*timetab_loc).click()  
        time.sleep(Gl.waittime)
    
    def click_ytd(self):   
        self.find_element(*self.ytd_loc).click()
        time.sleep(Gl.waittime)
    def click_wtd(self):   
        self.find_element(*self.wtd_loc).click()
        time.sleep(Gl.waittime)
    def click_mtd(self):   
        self.find_element(*self.mtd_loc).click()
        time.sleep(Gl.waittime)
    def click_anyKPIofTop20(self,Agentindex,kpiindex):
        self.anyKPIofTop20_path1=self.anyKPIofTop20_path+"/span"
        anyKPIofTop20_loc1=(By.XPATH,self.anyKPIofTop20_path %(Agentindex,kpiindex))
        anyKPIofTop20_loc2=(By.XPATH,self.anyKPIofTop20_path1 %(Agentindex,kpiindex))
        if self.Element_displayed(*anyKPIofTop20_loc2)==True:
            self.find_element(*anyKPIofTop20_loc2).click()
        else:
            self.find_element(*anyKPIofTop20_loc1).click()
        time.sleep(Gl.waittime)
    def click_anyKPIofBottom20(self,Agentindex,kpiindex):
        anyKPIofBottom20_loc=(By.XPATH,self.anyKPIofBottom20_path %(Agentindex,kpiindex))
        self.find_element(*anyKPIofBottom20_loc).click()
    def click_addCoachButton(self):
        self.find_element(*self.addcoachbutton_loc).click()
        time.sleep(Gl.waittime)
    def get_KPInumber(self):
        index=0
        flag=True
        while flag:
            KPInumber=index
            index=index+1 
            anyKPIname_loc=(By.XPATH,self.anyKPIname_path % index)
            flag=self.Element_displayed(*anyKPIname_loc) 
        return KPInumber
    def get_AllKPIname_List_Outlier(self,KPInumber):
        AllKPIname_List=[]
        for index in range(2,KPInumber+1):
            anyKPIname=self.get_anyKPIName_Outlier(index)
            AllKPIname_List.append(anyKPIname)
        return AllKPIname_List
            
    def get_anyKPIName_Outlier(self,index):
        anyKPIname_loc=(By.XPATH,self.anyKPIname_path % index)
        anyKPIname=self.find_element(*anyKPIname_loc).text
        return anyKPIname
    def get_anyKPIindex_Outlier(self,KPInumber,KPIname):
        for index in range(2,KPInumber+1):
            anyKPIname_loc=(By.XPATH,self.anyKPIname_path % index)
            anyKPIname=self.find_element(*anyKPIname_loc).text
            if anyKPIname==KPIname:
                KPIindex=index
                break
        return KPIindex
    def get_anyKPIofTop20(self,Agentindex,kpiindex):
        #anyKPIofTop20_loc1=(By.XPATH,("//*[@id='container']/div/section/div/div[2]/div/table[1]/tbody/tr[%d]/td[%d]/span") %(Agentindex,kpiindex))
        anyKPIofTop20_loc=(By.XPATH,self.anyKPIofTop20_path %(Agentindex,kpiindex))
        #Ppage=PerformancePage()
        #anyKPIofTop20_list=Ppage.Merge_ValueandStatusOfKPI(anyKPIofTop20_loc1, anyKPIofTop20_loc2, kpiindex)
        anyKPIofTop20=self.find_element(*anyKPIofTop20_loc).text
        #return anyKPIofTop20_list
        return anyKPIofTop20
    
    def get_anyKPIofBottom20(self,Agentindex,kpiindex):
        #anyKPIofBottom20_loc1=(By.XPATH,("//*[@id='container']/div/section/div/div[2]/div/table[2]/tbody/tr[%d]/td[%d]/span") %(Agentindex,kpiindex))
        anyKPIofBottom20_loc=(By.XPATH,self.anyKPIofBottom20_path %(Agentindex,kpiindex))
        #Ppage=PerformancePage()
        #anyKPIofBottom20_list=Ppage.Merge_ValueandStatusOfKPI(anyKPIofBottom20_loc1, anyKPIofBottom20_loc2, kpiindex)
        #return anyKPIofBottom20_list
        anyKPIofBottom20=self.find_element(*anyKPIofBottom20_loc).text
        return anyKPIofBottom20
        