'''
Created on 20171101

@author: lei.tan
'''
from selenium.webdriver.common.by import By
from Tablet_pages import BasePage

class PerformanceDiscussionDevelopmentForm(BasePage.Action):
    
    
    def __init__(self):
        
        self.firstfourinput_path="//*[@id='container']/div/section/div/form/div[2]/div[%d]/div[%d]/div/input"
        self.firstfourinput_title_path="//*[@id='container']/div/section/div/form/div[2]/div[%d]/div[%d]/label"
        self.discussiontypeinput_path="//*[@id='container']/div/section/div/form/div[2]/div[4]/div/div/input[%d]"
        self.discussiontypeinput_title_path="//*[@id='container']/div/section/div/form/div[2]/div[4]/div/div/label[%d]"
        self.detailsdiscussioninput_path="//*[@id='container']/div/section/div/form/div[2]/div[6]/div[%d]/div[%d]/div/input"
        self.detailsdiscussioninput_title_path="//*[@id='container']/div/section/div/form/div[2]/div[6]/div[%d]/div[%d]/label"
        self.longcomments_path="//*[@id='container']/div/section/div/form/div[2]/div[%d]/div/textarea"
        self.longcomments_title_path="//*[@id='container']/div/section/div/form/div[2]/div[%d]/label"
        self.dateofcall_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[6]/div[2]/div[2]/div/div/div[2]/input")
        self.timebutton_loc=(By.XPATH,"//*[@id='container']/div/section/div/form/div[2]/div[6]/div[2]/div[2]/div/div/div[2]/span/span")
        self.dayclick_path="//*[@id='container']/div/section/div/form/div[2]/div[6]/div[2]/div[2]/div/div/div[2]/ul/li/div/div/table/tbody/tr[%d]/td[%d]"
        
    
    def input_firstfourinput(self,lineindex,mid,text):
        self.firstfourinput_loc=(By.XPATH,self.firstfourinput_path %(lineindex,mid))
        self.Input_text(text,*self.firstfourinput_loc)
        
    def get_firstfourinput(self,lineindex,mid):
        self.firstfourinput_loc=(By.XPATH,self.firstfourinput_path %(lineindex,mid))
        return self.find_element(*self.firstfourinput_loc).get_attribute("value")
    
    def firstfourinput_disabled(self,lineindex,mid):
        self.firstfourinput_loc=(By.XPATH,self.firstfourinput_path %(lineindex,mid))
        flag=self.find_element(*self.firstfourinput_loc).get_attribute("disabled")
        return flag
    
    def get_firstfourinputBoxtitle(self,lineindex,mid):
        self.firstfourinput_title_loc=(By.XPATH,self.firstfourinput_title_path %(lineindex,mid))
        return self.find_element(*self.firstfourinput_title_loc).text
        
    def input_discussiontypeinput(self,lineindex,text):
        self.discussiontypeinput_loc=(By.XPATH,self.discussiontypeinput_path %lineindex)
        self.Input_text(text,*self.discussiontypeinput_loc)
        
    def get_discussiontypeinput(self,lineindex):
        self.discussiontypeinput_loc=(By.XPATH,self.discussiontypeinput_path %lineindex)
        return self.find_element(*self.discussiontypeinput_loc).get_attribute("value")
    
    def discussiontypeinput_disabled(self,lineindex):
        self.discussiontypeinput_loc=(By.XPATH,self.discussiontypeinput_path %lineindex)
        flag=self.find_element(*self.discussiontypeinput_loc).get_attribute("disabled")
        return flag
    
    def get_discussiontypeinputBoxtitle(self,lineindex):
        self.discussiontypeinput_title_loc=(By.XPATH,self.discussiontypeinput_title_path %lineindex)
        return self.find_element(*self.discussiontypeinput_title_loc).text
        
    def input_detailsdiscussioninput(self,lineindex,mid,text):
        self.detailsdiscussioninput_loc=(By.XPATH,self.detailsdiscussioninput_path %(lineindex,mid))
        self.Input_text(text,*self.detailsdiscussioninput_loc)
        
    def get_detailsdiscussioninput(self,lineindex,mid):
        self.detailsdiscussioninput_loc=(By.XPATH,self.detailsdiscussioninput_path %(lineindex,mid))
        return self.find_element(*self.detailsdiscussioninput_loc).get_attribute("value")
    
    def detailsdiscussioninput_disabled(self,lineindex,mid):
        self.detailsdiscussioninput_loc=(By.XPATH,self.detailsdiscussioninput_path %(lineindex,mid))
        flag=self.find_element(*self.detailsdiscussioninput_loc).get_attribute("disabled")
        return flag
    
    def get_detailsdiscussioninputBoxtitle(self,lineindex,mid):
        self.detailsdiscussioninput_title_loc=(By.XPATH,self.detailsdiscussioninput_title_path %(lineindex,mid))
        return self.find_element(*self.detailsdiscussioninput_title_loc).text
        
    def input_longcomments(self,lineindex,text):
        self.longcomments_loc=(By.XPATH,self.longcomments_path %lineindex)
        self.Input_text(text,*self.longcomments_loc)
        
    def get_longcomments(self,lineindex):
        self.longcomments_loc=(By.XPATH,self.longcomments_path %lineindex)
        return self.find_element(*self.longcomments_loc).get_attribute("value")
    
    def longcomments_disabled(self,lineindex):
        self.longcomments_loc=(By.XPATH,self.longcomments_path %lineindex)
        flag=self.find_element(*self.longcomments_loc).get_attribute("disabled")
        return flag
    
    def get_longcommentsBoxtitle(self,lineindex):
        self.longcomments_title_loc=(By.XPATH,self.longcomments_title_path %lineindex)
        return self.find_element(*self.longcomments_title_loc).text
        
    def get_dateofcall(self):
        return self.find_element(*self.dateofcall_loc).get_attribute("value")
    
    def dateofcall_disabled(self):
        flag=self.find_element(*self.dateofcall_loc).get_attribute("disabled")
        return flag
    
    def click_timebutton(self):
        self.find_element(*self.timebutton_loc).click()
    
    def timebutton_disabled(self):
        flag=self.find_element(self.timebutton_loc).get_attribute("disabled")
        return flag
    
    def click_dayclick(self,lineindex,mid):
        self.dayclick_loc=(By.XPATH,self.dayclick_path %(lineindex,mid))
        self.find_element(*self.dayclick_loc).click()
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    