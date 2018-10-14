'''
Created on 2018.3.1

@author: yalan.yin
'''
import time
from AdminSystem_Pages.TLandAgentAccountsPage import TLandAgentAccountsPage
from public_method import Gl


class TLandAgentAccount_PageNumber(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
   
    
    
        
        
    def get_Total_PageandAgentnumber(self):
        time.sleep(5*Gl.waittime)
        TLandAgentHome=TLandAgentAccountsPage()
        total_pagedic=self.get_Total_pagenumber()
        print(total_pagedic)
        total_pagenumber=int(total_pagedic['total_pagenumber'])
        lastbutton_pageindex=total_pagedic['lastbutton_pageindex']
        #pageindex=total_pagedic['lastpage_index']
        AccountNumberOnFirstPage=TLandAgentAccountsPage().get_TLAgentnumberOnePage(0)
        if AccountNumberOnFirstPage<30:
            Total_TLandAgentnumber_Onpage=TLandAgentHome.get_TLAgentnumberOnePage(self)
            total_pagenumber=1
        else:
            TLandAgentHome.click_Pagenumber(lastbutton_pageindex)
            Total_TLandAgentnumber_Onpage=30*(total_pagenumber-1)+TLandAgentHome.get_TLAgentnumberOnePage(self)  
            TLandAgentHome.click_Pagenumber(1)      
        total_PageandAgentnumber_Onpage_Dic={"total_pagenumber":total_pagenumber,"Total_TLandAgentnumber_Onpage":Total_TLandAgentnumber_Onpage}
        return total_PageandAgentnumber_Onpage_Dic 
    
    def get_Total_pagenumber(self):
        TLandAgentHome=TLandAgentAccountsPage()
        pageindex=3
        while TLandAgentHome.Pagenumber_exist(pageindex)==True:
            pageindex=pageindex+1
        
        
        lastbutton_pageindex=pageindex-1
        total_pagenumber=lastbutton_pageindex-4
        lastpage_index=int(lastbutton_pageindex)-2
        
        totalpage_numberandindex_dic={"total_pagenumber":total_pagenumber,"lastpage_index":lastpage_index,"lastbutton_pageindex":lastbutton_pageindex}
        
        return totalpage_numberandindex_dic
    