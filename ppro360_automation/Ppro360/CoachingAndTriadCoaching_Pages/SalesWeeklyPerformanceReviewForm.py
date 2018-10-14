'''
Created on 20170411

@author: luming.zhao
'''

from selenium.webdriver.common.by import By
from Tablet_pages import BasePage


class SalesWeeklyPerformanceReviewForm(BasePage.Action):
    '''
    classdocs
    '''
   
    def __init__(self):
        '''
        Constructor
        '''
        #Any week or Monthly
        self.anyOtherMETRICname_path="//*[@id='container']/div/section/div/form/div[2]/div[2]/div/table/tbody/tr[%d]/td[1]/input"#%nameindex11-13
        self.anyMETRICOfanyWeekOrmonthly_path="//*[@id='container']/div/section/div/form/div[2]/div[2]/div/table/tbody/tr[%d]/td[%d]/input"#%METRICindex %Weekindex(2,7)
        #Question of week ending WeekEndingindex from 1
        self.Question1OfanyWeekEnding_path="//*[@id='container']/div/section/div/form/div[2]/div[3]/div[%d]/div[2]/div[1]/textarea" #%WeekEndingindex
        self.Question2OfanyWeekEnding_path="//*[@id='container']/div/section/div/form/div[2]/div[3]/div[%d]/div[2]/div[2]/textarea" #%WeekEndingindex
        self.Question3OfanyWeekEnding_path="//*[@id='container']/div/section/div/form/div[2]/div[3]/div[%d]/div[4]/div[1]/textarea" #%WeekEndingindex
        self.Question4OfanyWeekEnding_path="//*[@id='container']/div/section/div/form/div[2]/div[3]/div[%d]/div[4]/div[2]/textarea" #%WeekEndingindex
        self.Question5OfanyWeekEnding_path="//*[@id='container']/div/section/div/form/div[2]/div[3]/div[%d]/div[6]/div/textarea" #%WeekEndingindex
        self.anyButtonOfanyWeekEnding_path="//*[@id='container']/div/section/div/form/div[2]/div[3]/div[%d]/div[7]/div/button[%d]" #%WeekEndingindex Buttonindex(1,2)
        
        self.Question1OfanyWeekEnding_title_path="//*[@id='container']/div/section/div/form/div[2]/div[3]/div[%d]/div[1]/div[1]/label" #%WeekEndingindex
        self.Question2OfanyWeekEnding_title_path="//*[@id='container']/div/section/div/form/div[2]/div[3]/div[%d]/div[1]/div[2]/label" #%WeekEndingindex
        self.Question3OfanyWeekEnding_title_path="//*[@id='container']/div/section/div/form/div[2]/div[3]/div[%d]/div[3]/div[1]/label" #%WeekEndingindex
        self.Question4OfanyWeekEnding_title_path="//*[@id='container']/div/section/div/form/div[2]/div[3]/div[%d]/div[3]/div[2]/label" #%WeekEndingindex
        self.Question5OfanyWeekEnding_title_path="//*[@id='container']/div/section/div/form/div[2]/div[3]/div[%d]/div[5]/div/label" #%WeekEndingindex
        
        self.AnyQuestion_TLSign_text_path="//*[@id='container']/div/section/div/form/div[2]/div[3]/div[%d]/div[7]/div[1]/label"#%WeekEndingindex
        self.AnyQuestion_TLSign_Date_path="//*[@id='container']/div/section/div/form/div[2]/div[3]/div[%d]/div[7]/div[1]/date"#%WeekEndingindex
        self.AnyQuestion_RoleSign_text_path="//*[@id='container']/div/section/div/form/div[2]/div[3]/div[%d]/div[7]/div[%d]/label"#%WeekEndingindex,Roleindex(1-TL,2-Agent)
        self.AnyQuestion_RoleSign_Date_path="//*[@id='container']/div/section/div/form/div[2]/div[3]/div[%d]/div[7]/div[%d]/date"#%WeekEndingindex,Roleindex(1-TL,2-Agent)
        
        self.OtherQuestion_title_path1="//*[@id='container']/div/section/div/form/div[2]/div[%d]/label"#%d=(4-8),question6,7,8,10,11
        self.OtherQuestion_inputbox_path1="//*[@id='container']/div/section/div/form/div[2]/div[%d]/div/textarea"#%d=(4-8),question6,7,8,10,11
        self.OtherQuestion_title_path2="//*[@id='container']/div/section/div/form/div[2]/table[%d]/tbody/tr[1]/th/label"#%d=(1-2),question9,12
        self.OtherQuestion_subtitle_path2="//*[@id='container']/div/section/div/form/div[2]/table[%d]/tbody/tr[%d]/td[1]/label"#%d1=table(1,2),%d2=subquestion(from 2 to start)
        self.OtherQuestion_subinputbox_path2="//*[@id='container']/div/section/div/form/div[2]/table[%d]/tbody/tr[%d]/td[2]/div/textarea"#%d1=table(1,2),%d2=subquestion(from 2 to start)
    
    def get_OtherQuestion_title(self,QuestionNumber,partnumber):
        OtherQuestion_title_loc1=(By.XPATH,self.OtherQuestion_title_path1 % QuestionNumber)#QuestionNumber=(4-8),question6,7,8,10,11
        OtherQuestion_title_loc2=(By.XPATH,self.OtherQuestion_title_path2 % QuestionNumber)#QuestionNumber=(1-2),question9,12
        if partnumber==1:
            return self.find_element(*OtherQuestion_title_loc1).text
        elif partnumber==2:
            return self.find_element(*OtherQuestion_title_loc2).text
    def OtherQuestion_inputbox_disabled(self,QuestionNumber):
        OtherQuestion_inputbox_loc=(By.XPATH,self.OtherQuestion_inputbox_path1 % QuestionNumber)#QuestionNumber=(4-8),question6,7,8,10,11
        return self.find_element(*OtherQuestion_inputbox_loc).get_attribute("disabled")
    def input_OtherQuestion(self,QuestionNumber,text):
        OtherQuestion_inputbox_loc=(By.XPATH,self.OtherQuestion_inputbox_path1 % QuestionNumber)#QuestionNumber=(4-8),question6,7,8,10,11
        self.Input_text(text,*OtherQuestion_inputbox_loc)
    def get_OtherQuestion_content(self,QuestionNumber):
        OtherQuestion_inputbox_loc=(By.XPATH,self.OtherQuestion_inputbox_path1 % QuestionNumber)#QuestionNumber=(4-8),question6,7,8,10,11
        return self.find_element(*OtherQuestion_inputbox_loc).text
           
    def get_SubQuestion_title(self,TableNumber,SubQuestionNumber):
        SubQuestion_tilte_loc=(By.XPATH,self.OtherQuestion_subtitle_path2 % (TableNumber,SubQuestionNumber))
        return self.find_element(*SubQuestion_tilte_loc).text
    def SubQuestion_inputbox_disabled(self,TableNumber,SubQuestionNumber):
        SubQuestion_inputbox_loc=(By.XPATH,self.OtherQuestion_subinputbox_path2 % (TableNumber,SubQuestionNumber))
        return self.find_element(*SubQuestion_inputbox_loc).get_attribute("disabled")
    def input_SubQuestion(self,TableNumber,SubQuestionNumber,text):
        SubQuestion_inputbox_loc=(By.XPATH,self.OtherQuestion_subinputbox_path2 % (TableNumber,SubQuestionNumber))#TableNumber=table(1,2),SubQuestionNumber=subquestion(from 2 to start)
        self.Input_text(text,*SubQuestion_inputbox_loc)
    def get_SubQuestion_content(self,TableNumber,SubQuestionNumber):
        SubQuestion_inputbox_loc=(By.XPATH,self.OtherQuestion_subinputbox_path2 % (TableNumber,SubQuestionNumber))#TableNumber=table(1,2),SubQuestionNumber=subquestion(from 2 to start)
        return self.find_element(*SubQuestion_inputbox_loc).text
    
    
    
    
    
    
    def anyOtherMETRICname_disabled(self,nameindex):
        '''Other METRICindex from 11-13'''
        anyOtherMETRICname_loc=(By.XPATH,self.anyOtherMETRICname_path % nameindex)
        flag=self.find_element(*anyOtherMETRICname_loc).get_attribute("disabled")
        return flag
        
    def anyMETRICOfanyWeekOrmonthly_disabled(self,METRICindex,Weekindex):
        '''METRICindex from 1,Weekindex from 2'''
        anyMETRICOfanyWeekOrmonthly_loc=(By.XPATH,self.anyMETRICOfanyWeekOrmonthly_path % (METRICindex,Weekindex))
        flag=self.find_element(*anyMETRICOfanyWeekOrmonthly_loc).get_attribute("disabled")
        return flag
    def input_anyMETRICOfanyWeekOrmonthly(self,METRICindex,Weekindex,text):
        anyMETRICOfanyWeekOrmonthly_loc=(By.XPATH,self.anyMETRICOfanyWeekOrmonthly_path % (METRICindex,Weekindex))
        self.Input_text(text,*anyMETRICOfanyWeekOrmonthly_loc)
    def Get_anyMETRICOfanyWeekOrmonthly(self,METRICindex,Weekindex):
        anyMETRICOfanyWeekOrmonthly_loc=(By.XPATH,self.anyMETRICOfanyWeekOrmonthly_path % (METRICindex,Weekindex))
        return self.find_element(*anyMETRICOfanyWeekOrmonthly_loc).get_attribute("value")
        
    def Get_METRICnumber(self):
        METRICindex=0
        flag=True
        while flag:
            METRICnumber=METRICindex
            METRICindex=METRICindex+1 
            anyMETRICOfanyWeekOrmonthly_loc=(By.XPATH,self.anyMETRICOfanyWeekOrmonthly_path % (METRICindex,2))
            flag=self.Element_displayed(*anyMETRICOfanyWeekOrmonthly_loc) 
        return METRICnumber
    def get_AnyQuestionsOfAnyWeekEnding_title(self,QuestionNumber,WeekEndingIndex):
        if QuestionNumber==1:
            question_path=self.Question1OfanyWeekEnding_title_path
        elif QuestionNumber==2:
            question_path=self.Question2OfanyWeekEnding_title_path
        elif QuestionNumber==3:
            question_path=self.Question3OfanyWeekEnding_title_path
        elif QuestionNumber==4:
            question_path=self.Question4OfanyWeekEnding_title_path
        elif QuestionNumber==5:
            question_path=self.Question5OfanyWeekEnding_title_path
        question_loc=(By.XPATH,question_path % WeekEndingIndex)
        return self.find_element(*question_loc).text
    def input_AnyQuestionsOfAnyWeekEnding(self,QuestionNumber,WeekEndingIndex,text):
        if QuestionNumber==1:
            question_path=self.Question1OfanyWeekEnding_path
        elif QuestionNumber==2:
            question_path=self.Question2OfanyWeekEnding_path
        elif QuestionNumber==3:
            question_path=self.Question3OfanyWeekEnding_path
        elif QuestionNumber==4:
            question_path=self.Question4OfanyWeekEnding_path
        elif QuestionNumber==5:
            question_path=self.Question5OfanyWeekEnding_path
        question_loc=(By.XPATH,question_path % WeekEndingIndex)
        self.Input_text(text,*question_loc)
    def get_AnyQuestionsOfAnyWeekEnding_text(self,QuestionNumber,WeekEndingIndex):
        if QuestionNumber==1:
            question_path=self.Question1OfanyWeekEnding_path
        elif QuestionNumber==2:
            question_path=self.Question2OfanyWeekEnding_path
        elif QuestionNumber==3:
            question_path=self.Question3OfanyWeekEnding_path
        elif QuestionNumber==4:
            question_path=self.Question4OfanyWeekEnding_path
        elif QuestionNumber==5:
            question_path=self.Question5OfanyWeekEnding_path
        question_loc=(By.XPATH,question_path % WeekEndingIndex)
        return self.find_element(*question_loc).text
    
    
    def Get_AnyQuestion_RoleSign_text(self,WeekEndingIndex,Roleindex):#(Roleindex:1-TL,2-Agent)
        AnyQuestion_RoleSign_text_loc=(By.XPATH,self.AnyQuestion_RoleSign_text_path % (WeekEndingIndex,Roleindex))
        return self.find_element(*AnyQuestion_RoleSign_text_loc).text
    def Get_AnyQuestion_RoleSign_date(self,WeekEndingIndex,Roleindex):#(Roleindex:1-TL,2-Agent)
        AnyQuestion_RoleSign_date_loc=(By.XPATH,self.AnyQuestion_RoleSign_Date_path % (WeekEndingIndex,Roleindex))
        return self.find_element(*AnyQuestion_RoleSign_date_loc).text
    
    def AnyQuestionsOfAnyWeekEnding_disabled(self,QuestionNumber,WeekEndingIndex):
        if QuestionNumber==1:
            question_path=self.Question1OfanyWeekEnding_path
        elif QuestionNumber==2:
            question_path=self.Question2OfanyWeekEnding_path
        elif QuestionNumber==3:
            question_path=self.Question2OfanyWeekEnding_path
        elif QuestionNumber==4:
            question_path=self.Question2OfanyWeekEnding_path
        elif QuestionNumber==5:
            question_path=self.Question2OfanyWeekEnding_path
        question_loc=(By.XPATH,question_path % WeekEndingIndex)
        flag=self.find_element(*question_loc).get_attribute("disabled")
        return flag
    def anyButtonOfAnyWeekEnding_disabled(self,WeekEndingIndex,ButtonIndex):
        anyButtonOfAnyWeekEnding_loc=(By.XPATH,self.anyButtonOfanyWeekEnding_path % (WeekEndingIndex,ButtonIndex))
        flag=self.find_element(*anyButtonOfAnyWeekEnding_loc).get_attribute("disabled")
        return flag
    
    def Get_ButtonNameOfAnyWeekEnding(self,WeekEndingIndex,ButtonIndex):
        anyButtonOfAnyWeekEnding_loc=(By.XPATH,self.anyButtonOfanyWeekEnding_path % (WeekEndingIndex,ButtonIndex))
        return self.find_element(*anyButtonOfAnyWeekEnding_loc).text
    def click_SaveOrSignButtonOfAnyWeekEnding(self,WeekEndingIndex,ButtonIndex):
        anyButtonOfAnyWeekEnding_loc=(By.XPATH,self.anyButtonOfanyWeekEnding_path % (WeekEndingIndex,ButtonIndex))
        self.find_element(*anyButtonOfAnyWeekEnding_loc).click()
        self.wait_loadingmask_disappear()
        
    def Get_SaveOrSignButtonOfAnyWeekEnding_text(self,WeekEndingIndex,ButtonIndex):#The ButtonIndex of Agent Sign is 2
        anyButtonOfAnyWeekEnding_loc=(By.XPATH,self.anyButtonOfanyWeekEnding_path % (WeekEndingIndex,ButtonIndex))
        return self.find_element(*anyButtonOfAnyWeekEnding_loc).text
    def SaveOrSignButtonOfAnyWeekEnding_exist(self,WeekEndingIndex,ButtonIndex):
        anyButtonOfAnyWeekEnding_loc=(By.XPATH,self.anyButtonOfanyWeekEnding_path % (WeekEndingIndex,ButtonIndex))
        flag=self.Element_displayed(*anyButtonOfAnyWeekEnding_loc)
        return flag
    
        
        
        
    
    
    
    
    
    
        