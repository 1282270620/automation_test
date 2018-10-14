'''
Created on 2018.8.3

@author: haodong.liu
'''

from selenium.webdriver.common.by import By
from Tablet_pages import BasePage
from public_method.Get_AnyText_ForNormal import Get_AnyText_ForNormal
from Tkconstants import DISABLED

class RedemptionReport_Page(BasePage.Action):
    
    def __init__(self):
        self.CoachName_dropdown_path="//*[@id='container']/div/section/div/div/div/div[1]/div/div/ul/li[%d]/a"
        self.LeftArrow_path='//*[@id="container"]/div/section/div/div/div/div[2]/div/div[%d]/div/div/div[2]/ul/li/div/div/table/thead/tr[1]/th[1]/span' #In first datepicker :1
        self.RightArrow_path='//*[@id="container"]/div/section/div/div/div/div[2]/div/div[%d]/div/div/div[2]/ul/li/div/div/table/thead/tr[1]/th[3]/span' #In first datepicker :2
        self.StartDatePicker_loc='//*[@id="container"]/div/section/div/div/div/div[2]/div/div[1]/div/div/div[2]/span/span' #In first datepicker index:1
        self.EndDatePicker_loc='//*[@id="container"]/div/section/div/div/div/div[2]/div/div[2]/div/div/div[2]/span/span' #In first datepicker index:2
        
        self.StartDateInput_loc='//*[@id="container"]/div/section/div/div/div/div[2]/div/div[1]/div/div/div[2]/input'
        self.EndDateInput_loc='//*[@id="container"]/div/section/div/div/div/div[2]/div/div[2]/div/div/div[2]/input'
        self.RedemptionDateInDatePicker_path='//*[@id="container"]/div/section/div/div/div/div[2]/div/div[%d]/div/div/div[2]/ul/li/div/div/table/tbody/tr[%d]/td[%d]' #StartEndeindex,lineindex,dateindex
    
    def Get_ClassValue_RedemptionDateInDatePicker(self,StartEndeindex,lineindex,dateindex):#StartEndeindex=[1,2];lineindex=[1,6];dateindex=[1,7]
        DateInDatePicker_loc=(By.XPATH,self.RedemptionDateInDatePicker_path % (StartEndeindex,lineindex,dateindex))
        return self.find_element(*DateInDatePicker_loc).get_attribute("class")
    def Get_RedemptionDateInDatePicker(self,StartEndeindex,lineindex,Dateindex):#StartEndeindex=[1,2];lineindex=[1,6];dateindex=[1,7]
        DateInDatePicker_loc=(By.XPATH,self.RedemptionDateInDatePicker_path % (StartEndeindex,lineindex,Dateindex))
        return self.find_element(*DateInDatePicker_loc).text
    
    def Click_TLNameDropDown(self):
        self.find_element(By.XPATH,'//*[@id="container"]/div/section/div/div/div/div[1]/div/div/span').click()
    def get_TLNameDefaultValue(self):
        return self.find_element(By.XPATH,'//*[@id="container"]/div/section/div/div/div/div[1]/div/div/span').text
    def get_DatefaultValue(self,index):
        return self.find_element(By.XPATH,'//*[@id="container"]/div/section/div/div/div/div[2]/div/div[%d]/div/div/div[2]/input' %index).get_attribute("value")
    def get_DatafaultValue(self):
        return self.find_element(By.XPATH,'//*[@id="container"]/div/section/div/table/thead').find_element_by_tag_name("tr")
    def get_FilterButtonDatafaultStutus(self):
        return self.find_element(By.XPATH,'//*[@id="container"]/div/section/div/div/div/div[3]/button[1]').get_attribute("disabled")
    def Click_FilterButton(self):
        self.find_element(By.XPATH,'//*[@id="container"]/div/section/div/div/div/div[3]/button[1]').click()
    def get_ExportButtonDatafaultStutus(self):
        return self.find_element(By.XPATH,'//*[@id="container"]/div/section/div/div/div/div[3]/button[2]').get_attribute("disabled")
    def Click_ExportButton(self):
        self.find_element(By.XPATH,'//*[@id="container"]/div/section/div/div/div/div[3]/button[2]').click()
    def Select_TL(self,index):
        self.find_element(By.XPATH,'//*[@id="container"]/div/section/div/div/div/div[1]/div/div/ul/li[%d]' %index).click()
    def get_OneFilterInfo(self,index):
        self.Info_loc1=self.find_element(By.XPATH,'//*[@id="container"]/div/section/div/table/tbody/tr/td[%d]' %index)
        return self.find_element(self.Info_loc1).text
    def get_ALLFilterInfo(self,index1,index2):
        self.Info_loc2=self.find_element(By.XPATH,'//*[@id="container"]/div/section/div/table/tbody/tr[%d]/td[%d]' %(index1,index2))
        return self.find_element(self.Info_loc2).text
    
    def get_all_TLName(self):
        '''index=1:Filter
           index=2:All'''   
        GetText=Get_AnyText_ForNormal()
        FirstCoachName_loc=(By.XPATH,self.CoachName_dropdown_path % 1)
        if self.Element_displayed(*FirstCoachName_loc)==True:
            CoachNameList=GetText.Get_Text_ForLoop(2,self.CoachName_dropdown_path)
        else:
            CoachNameList=GetText.Get_Text_ForLoop(3,self.CoachName_dropdown_path)
        '''
        if CoachNameList[0]=="All":
            CoachNameList=CoachNameList[1:]
        else:
            CoachNameList=CoachNameList[2:]'''
        return CoachNameList
    
    