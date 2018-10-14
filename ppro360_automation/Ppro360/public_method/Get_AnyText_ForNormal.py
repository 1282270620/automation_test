'''
Created on Jar 31, 2018

@author: symbio
'''
from Tablet_pages import BasePage
from selenium.webdriver.common.by import By
class Get_AnyText_ForNormal(BasePage.Action):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    def Get_Text_ForLoop(self,index,Any_path):
        TextList=[]
        Flag=True
        while Flag:
            Any_loc=(By.XPATH,Any_path%index)
            if self.Element_displayed(*Any_loc)==True:
                each_Text=self.find_element(*Any_loc).text
                TextList.append(each_Text)
                index=index+1
                Flag=True
            else:
                Flag=False
        return TextList
        