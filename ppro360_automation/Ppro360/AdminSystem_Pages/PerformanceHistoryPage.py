'''
Created on Mar 29, 2017

@author: symbio
'''
from Tablet_pages import BasePage
from selenium.webdriver.common.by import By
import time
from public_method import Gl

class PerformanceHistoryPage(BasePage.Action):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.Performancefilename_path1="/html/body/div[2]/div/div[2]/div/div/div[2]/div/table/tbody/tr[%d]/td[2]"#For ISM etc
        self.Performancefilename_path2="/html/body/div[2]/div/div[2]/div/div/div[2]/div/table/tbody/tr[%d]/td[1]"#For ICM etc
        self.DownloadOrDeletebutton_path1="/html/body/div[2]/div/div[2]/div/div/div[2]/div/table/tbody/tr[%d]/td[3]/div/a[%d]"
        self.DownloadOrDeletebutton_path2="/html/body/div[2]/div/div[2]/div/div/div[2]/div/table/tbody/tr[%d]/td[4]/div/a[%d]"
    def get_PerformanceFilename(self,lobname,lineindex):  #ISM&LCBB:lobindex=2***************Other LOBs:lobindex=1
        if lobname in Gl.SevralFilefor_lob:
            performancefilename_path=self.Performancefilename_path1
        else:
            performancefilename_path=self.Performancefilename_path2
        filename_loc=(By.XPATH,performancefilename_path % lineindex)
        return self.find_element(*filename_loc).text
    
    def click_PerformanceFilename(self,lobname,lineindex):  
        if lobname in Gl.SevralFilefor_lob:
            performancefilename_path=self.Performancefilename_path1
        else:
            performancefilename_path=self.Performancefilename_path2
        filename_loc=(By.XPATH,performancefilename_path % lineindex)
        self.find_element(*filename_loc).click()
        time.sleep(Gl.waittime)
        
    def click_Delete_button(self,lobname,lineindex):#ISM&LCBB:lobindex=4***************Other LOBs:lobindex=3
        if lobname in Gl.SevralFilefor_lob:
            DownloadOrDeletebutton_path=self.DownloadOrDeletebutton_path2
        else:
            DownloadOrDeletebutton_path=self.DownloadOrDeletebutton_path1
        delete_button_loc=(By.XPATH,DownloadOrDeletebutton_path%(lineindex,2))
        self.find_element(*delete_button_loc).click()
        time.sleep(Gl.waittime)
        
    def Download_Performancefile(self,lobname,lineindex):
        if lobname in Gl.SevralFilefor_lob:
            DownloadOrDeletebutton_path=self.DownloadOrDeletebutton_path2
        else:
            DownloadOrDeletebutton_path=self.DownloadOrDeletebutton_path1
        download_button_loc=(By.XPATH,DownloadOrDeletebutton_path % (lineindex,1))
        self.find_element(*download_button_loc).click()
        time.sleep(Gl.waittime)
        