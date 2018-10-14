'''
Created on 20180115

@author: luming.zhao
'''

from Tablet_pages import BasePage
from selenium.webdriver.common.by import By
from public_method.Get_AnyText_ForNormal import Get_AnyText_ForNormal


class LOBlistPage(BasePage.Action):
    
    def _init_(self):#get lobs and their sites number
        self.LOB_path = "/html/body/div[2]/div/div[2]/div/div/ul/li[%d]/input" #index is 1 to 20
        self.LOB_name_path = "/html/body/div[2]/div/div[2]/div/div/ul/li[%d]"
        self.LOBMAXlen_loc=(By.XPATH,"/html/body/div[2]/div/div[2]/div/div/ul/li[20]")
        self.ICMsite_path = "/html/body/div[2]/div/div[2]/div/div/ul/li[1]/ul/li[%d]/div/input"
        self.UBIZsite_path = "/html/body/div[2]/div/div[2]/div/div/ul/li[2]/ul/li[%d]/div/input"
        self.ISMsite_path = "/html/body/div[2]/div/div[2]/div/div/ul/li[3]/ul/li[%d]/div/input"
        self.ISMServicesite_path = "/html/body/div[2]/div/div[2]/div/div/ul/li[4]/ul/li[%d]/div/input"
        self.ISMHFCsite_path = "/html/body/div[2]/div/div[2]/div/div/ul/li[5]/ul/li[%d]/div/input"
        self.BGILITEsite_path = "/html/body/div[2]/div/div[2]/div/div/ul/li[6]/ul/li[%d]/div/input"
        self.BGIDTVsite_path = "/html/body/div[2]/div/div[2]/div/div/ul/li[7]/ul/li[%d]/div/input"
        self.ISMCLGsite_path = "/html/body/div[2]/div/div[2]/div/div/ul/li[8]/ul/li[%d]/div/input"
        self.SPANISHsite_path = "/html/body/div[2]/div/div[2]/div/div/ul/li[9]/ul/li[%d]/div/input"
        self.ATTBLUEsite_path = "/html/body/div[2]/div/div[2]/div/div/ul/li[10]/ul/li[%d]/div/input"
        self.BLUEsite_path = "/html/body/div[2]/div/div[2]/div/div/ul/li[11]/ul/li[%d]/div/input"
        self.DTVDSsite_path = "/html/body/div[2]/div/div[2]/div/div/ul/li[12]/ul/li[%d]/div/input"
        self.LCBBsite_path = "/html/body/div[2]/div/div[2]/div/div/ul/li[13]/ul/li[%d]/div/input"
        self.DTVSSsite_path = "/html/body/div[2]/div/div[2]/div/div/ul/li[14]/ul/li[%d]/div/input"
        self.DTVRCXsite_path = "/html/body/div[2]/div/div[2]/div/div/ul/li[15]/ul/li[%d]/div/input"
        self.DBSsite_path = "/html/body/div[2]/div/div[2]/div/div/ul/li[16]/ul/li[%d]/div/input"
        self.GREENsite_path = "/html/body/div[2]/div/div[2]/div/div/ul/li[17]/ul/li[%d]/div/input"
        self.PAYPALsite_path = "/html/body/div[2]/div/div[2]/div/div/ul/li[18]/ul/li[%d]/div/input"
        self.IPsite_path = "/html/body/div[2]/div/div[2]/div/div/ul/li[19]/ul/li[%d]/div/input"
        self.VXIIPsite_path = "/html/body/div[2]/div/div[2]/div/div/ul/li[20]/ul/li[%d]/div/input"
    
    def get_LOBnumber_page(self):
        #self.LOB_path = "/html/body/div[2]/div/div[2]/div/div/ul/li[%d]/input" #index is 1 to 20
        index=1
        Flag=True
        while Flag:
            print self.LOB_path % index
            LOB_loc=(By.XPATH,self.LOB_path % index)
            if self.Element_displayed(*LOB_loc)==True:
                index=index+1
                Flag=True
            else:
                Flag=False
                LOBnumber=index-1
        return LOBnumber
   
    def get_loblists_page(self):
        Get_AnyText=Get_AnyText_ForNormal()
        Alllobs_list=Get_AnyText.Get_Text_ForLoop(1, self.LOB_name_path)
        return Alllobs_list
    '''
        LOBnumber=self.get_LOBnumber_page()
        AllLOBlists=[]
        for index in range(1,LOBnumber+1):
            LOB_loc=(By.XPATH,self.LOB_name_path %index)
            each_lob=self.find_element(*LOB_loc).text
            AllLOBlists.append(each_lob)
        return AllLOBlists'''
            
    
   
    def select_AllLOB(self,MaxLOBindex):
        #self.LOB_path = "/html/body/div[2]/div/div[2]/div/div/ul/li[%d]/input"
        if MaxLOBindex >= 1:
            LastLOBName_loc=(By.XPATH,self.LOB_path % MaxLOBindex)
            self.find_element(*LastLOBName_loc).click()

            for LOBindex in range(1,MaxLOBindex+1):
                anyLOBName_loc=(By.XPATH,self.LOB_path  % LOBindex)
                self.find_element(*anyLOBName_loc).click()
        else:
            print "There is no lob to be selected."
            '''
            LastLOBName_loc=(By.XPATH,self.LOB_path  % MaxLOBindex)
            self.find_element(*LastLOBName_loc).click()'''
        
    def get_eachLOB_ALL(self):
        index=0
        flag=True
        while flag:
            LOBnumber=index
            index=index+1
            anyLOB_loc=()
            flag=self.Element_displayed(*anyLOB_loc)
        return LOBnumber
    
    def get_allLOBs_frompage(self):
        Get_AnyText=Get_AnyText_ForNormal()
        Alllobs_list=Get_AnyText.Get_Text_ForLoop(1, self.LOB_name_path)
        return Alllobs_list
            

       
       
       
       
       
    def select_ICMsite(self,siteindex1): #siteindex1 is 1 to 6
        self.ICM_loc=(By.XPATH,self.ICMsite_path %siteindex1)
        self.find_element(*self.ICM_loc).click()
    def select_UBIZsite(self,siteindex2): #siteindex2 is 1 to 2
        self.UBIZ_loc=(By.XPATH,self.UBIZsite_path %siteindex2)
        self.find_element(*self.UBIZ_loc).click()
    def select_ISMsite(self,siteindex3): #siteindex3 is 1 to 6
        self.ISM_loc=(By.XPATH,self.ISMsite_path %siteindex3)
        self.find_element(*self.ISM_loc).click()
    def select_ISMServicesite(self,siteindex4): #siteindex4 is 1 to 3
        self.ISMService_loc=(By.XPATH,self.ISMServicesite_path %siteindex4)
        self.find_element(*self.ISMService_loc).click()
    def select_ISMHFCsite(self,siteindex5): #siteindex5 is 1
        self.ISMHFC_loc=(By.XPATH,self.ISMHFCsite_path %siteindex5)
        self.find_element(*self.ISMHFC_loc).click()
    def select_BGILITEsite(self,siteindex6): #siteindex6 is 1
        self.BGILITE_loc=(By.XPATH,self.BGILITEsite_path %siteindex6)
        self.find_element(*self.BGILITE_loc).click()
    def select_BGIDTVsite(self,siteindex7): #siteindex7 is 1 
        self.BGIDTV_loc=(By.XPATH,self.BGIDTVsite_path %siteindex7)
        self.find_element(*self.BGIDTV_loc).click()
    def select_ISMCLGsite(self,siteindex8): #siteindex8 is 1 
        self.ISMCLG_loc=(By.XPATH,self.ISMCLGsite_path %siteindex8)
        self.find_element(*self.ISMCLG_loc).click()
    def select_SPANISHsite(self,siteindex9): #siteindex9 is 1 
        self.SPANISH_loc=(By.XPATH,self.SPANISHsite_path %siteindex9)
        self.find_element(*self.SPANISH_loc).click()
    def select_ATTBLUEsite(self,siteindex10): #siteindex10 is 1 to 3
        self.ATTBLUE_loc=(By.XPATH,self.ATTBLUEsite_path %siteindex10)
        self.find_element(*self.ATTBLUE_loc).click()
    def select_BLUEsite(self,siteindex11): #siteindex11 is 1 to 6
        self.BLUE_loc=(By.XPATH,self.BLUEsite_path %siteindex11)
        self.find_element(*self.BLUE_loc).click()
    def select_DTVDSsite(self,siteindex12): #siteindex12 is 1 to 7
        self.DTVDS_loc=(By.XPATH,self.DTVDSsite_path %siteindex12)
        self.find_element(*self.DTVDS_loc).click()
    def select_LCBBsite(self,siteindex13): #siteindex13 is 1 to 3
        self.LCBB_loc=(By.XPATH,self.LCBBsite_path %siteindex13)
        self.find_element(*self.LCBB_loc).click()
    def select_DTVSSsite(self,siteindex14): #siteindex14 is 1 to 4
        self.DTVSS_loc=(By.XPATH,self.DTVSSsite_path %siteindex14)
        self.find_element(*self.DTVSS_loc).click()
    def select_DTVRCXsite(self,siteindex15): #siteindex15 is 1 to 4 
        self.DTVRCX_loc=(By.XPATH,self.DTVRCXsite_path %siteindex15)
        self.find_element(*self.DTVRCX_loc).click()
    def select_DBSsite(self,siteindex16): #siteindex16 is 1 to 2
        self.DBS_loc=(By.XPATH,self.DBSsite_path %siteindex16)
        self.find_element(*self.DBS_loc).click()
    def select_GREENsite(self,siteindex17): #siteindex17 is 1 
        self.GREEN_loc=(By.XPATH,self.GREENsite_path %siteindex17)
        self.find_element(*self.GREEN_loc).click()
    def select_PAYPALsite(self,siteindex18): #siteindex18 is 1 
        self.PAYPAL_loc=(By.XPATH,self.PAYPALsite_path %siteindex18)
        self.find_element(*self.PAYPAL_loc).click()
    def select_IPsite(self,siteindex19): #siteindex19 is 1 
        self.IP_loc=(By.XPATH,self.IPsite_path %siteindex19)
        self.find_element(*self.IP_loc).click()
    def select_VXIIPsite(self,siteindex20): #siteindex12 is 1 
        self.VXIIP_loc=(By.XPATH,self.VXIIPsite_path %siteindex20)
        self.find_element(*self.VXIIP_loc).click()
        
        
        