'''
Created on Jul 3, 2017

@author: symbio
'''
from Tablet_pages.Coachinghomepage import Coachinghomepage
import time
from public_method import Gl
class Coaching_PublicFunction():
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    
    def Get_AnyattributeofAllCoach_tablet(self,total_pagenumber,Total_coachnumber_tablet):#attrindex=1:SN,attrindex=2:CoachName,attrindex=3:EmployeeName
        CoachHome=Coachinghomepage()
        Attribute_All_Coach_tablet_Dic={}
        if Total_coachnumber_tablet==0:
            Attribute_All_Coach_tablet_Dic={}
        elif Total_coachnumber_tablet<=20:
            pageindex=0
            coachindex=Total_coachnumber_tablet
            Attribute_All_Coach_tablet_Dic=self.Get_AnyattributeofEachCoach_tablet(pageindex,coachindex)
        else:
            coachnumber_lastpage=Total_coachnumber_tablet%20
            nextbutton_pageindex=CoachHome.get_SpecialPage_index(5, 8, "Next")
            for pageindex in range(1,total_pagenumber+1):
                print "pageindex_getstatus=",pageindex
                if pageindex==total_pagenumber:
                    dic_lastpage=self.Get_AnyattributeofEachCoach_tablet(pageindex,coachnumber_lastpage)
                    Attribute_All_Coach_tablet_Dic=dict(Attribute_All_Coach_tablet_Dic.items()+dic_lastpage.items())
                    #CoachHome.click_NextPage()
                else:
                    dic_page=self.Get_AnyattributeofEachCoach_tablet(pageindex,20)
                    Attribute_All_Coach_tablet_Dic=dict(Attribute_All_Coach_tablet_Dic.items()+dic_page.items())
                    CoachHome.click_Pagenumber(nextbutton_pageindex)
            CoachHome.click_Pagenumber(1)#Back to the first page
                
        
        return Attribute_All_Coach_tablet_Dic
                
            
    def Get_AnyattributeofEachCoach_tablet(self,pageindex,coachnumber):
        CoachHome=Coachinghomepage()
        Coach_tablet_Dic={}
        #print "coachnumber=",
        #print coachnumber
        for coachindex in range(1,coachnumber+1):
            #print coachindex
            SNofCoach_tablet=CoachHome.get_anyCoach_attribute(coachindex, 1)
            CoachNameofCoach_tablet=CoachHome.get_anyCoach_attribute(coachindex, 2)
            EmployeeNameofCoach_tablet=CoachHome.get_anyCoach_attribute(coachindex, 3)
            Hrid_tablet=CoachHome.get_anyCoach_attribute(coachindex, 4)
            Type_tablet=CoachHome.get_anyCoach_attribute(coachindex, 5)
            Status_tablet=CoachHome.get_anyCoach_attribute(coachindex,6)
            CreatedDate_tablet=CoachHome.get_anyCoach_attribute(coachindex,7)
            CompletedDate_tablet=CoachHome.get_anyCoach_attribute(coachindex,8)
            AcknowledgeDate_tablet=CoachHome.get_anyCoach_attribute(coachindex,9)
            '''The number of each Coach'attribute in Info_EachCoach_List must be the same with it in tablet, so the first one 'Placeholder item' is set in list'''
            Info_EachCoach_List=["Placeholder item",SNofCoach_tablet,CoachNameofCoach_tablet,EmployeeNameofCoach_tablet,Hrid_tablet,Type_tablet,Status_tablet,CreatedDate_tablet,CompletedDate_tablet,AcknowledgeDate_tablet]
            key=pageindex*20+(coachindex-1)
            Coach_tablet_Dic[key]=Info_EachCoach_List
        return Coach_tablet_Dic
    
    
    
    
    
    
    
    
    
    def get_Total_PageandCoachnumber(self):
        time.sleep(5*Gl.waittime)
        CoachHome=Coachinghomepage()
        total_pagedic=self.get_Total_pagenumber()
        print total_pagedic
        total_pagenumber=int(total_pagedic['total_pagenumber'])
        lastbutton_pageindex=total_pagedic['lastbutton_pageindex']
        pageindex=total_pagedic['lastpage_index']
        if pageindex==3:
            Total_coachnumber_tablet=self.get_coachnumber_onepage()
        else:
            CoachHome.click_Pagenumber(lastbutton_pageindex)
            Total_coachnumber_tablet=20*(total_pagenumber-1)+self.get_coachnumber_onepage()  
            CoachHome.click_Pagenumber(1)      
        total_PageandCoachnumber_tablet_Dic={"total_pagenumber":total_pagenumber,"Total_coachnumber_tablet":Total_coachnumber_tablet}
        return total_PageandCoachnumber_tablet_Dic 
    
    def get_Total_pagenumber(self):
        CoachHome=Coachinghomepage()
        pageindex=3
        if CoachHome.Pagenumber_exist(pageindex)==False:#Check the fist page button exsit
            total_pagenumber=1
            lastpage_index=pageindex
            lastbutton_pageindex=""
        else:
            lastbutton_pageindex=CoachHome.get_SpecialPage_index(6, 9, "Last")
            lastpage_index=int(lastbutton_pageindex)-2
            CoachHome.click_Pagenumber(lastbutton_pageindex)#Click Last button to get the coaching number of the last page
            total_pagenumber=CoachHome.get_Pagenumber(lastpage_index)
            CoachHome.click_Pagenumber(1)#Click first button, back to the first page
        totalpage_numberandindex_dic={"total_pagenumber":total_pagenumber,"lastpage_index":lastpage_index,"lastbutton_pageindex":lastbutton_pageindex}
        return totalpage_numberandindex_dic
        
            
    '''       
    def get_Total_pagenumber(self):
        CoachHome=Coachinghomepage()
        pageindex=3
        if CoachHome.Pagenumber_exist(pageindex)==False:
            total_pagenumber=1
            last_pageindex=""
        else:
            while CoachHome.Pagenumber_exist(pageindex)==True:
                pageindex=pageindex+1
            pageindex=pageindex-1#The last pageindex of elements does not exist.
            last_number_pageindex=pageindex-2
            CoachHome.click_Pagenumber(pageindex)
            total_pagenumber=CoachHome.get_Pagenumber(last_number_pageindex)
        pagedic={'pagenumber':total_pagenumber,'pageindex':last_number_pageindex}
        return pagedic  '''
    
    def get_coachnumber_onepage(self):
        CoachHome=Coachinghomepage()
        coachindex=1
        if CoachHome.Coach_line_exist(coachindex)==False:
            coachnumber_onepage=coachindex-1
        else:
            while CoachHome.Coach_line_exist(coachindex)==True:
                coachindex=coachindex+1
            coachnumber_onepage=coachindex-1
        return coachnumber_onepage  
        
    