'''
Created on Mar 16, 2017

@author: symbio
'''
from public_method.Login import Login
from AdminSystem_Pages.AdminHomepage import AdminHomepage
from AdminSystem_Pages.OMaccountPage import OMaccountPage
from AdminSystem_Pages.TLandAgentAccountsPage import TLandAgentAccountsPage
from Tablet_pages.PerformancPage import PerformancePage
from Tablet_pages.MyTeamInfoPage import MyTeamInfoPage
from Tablet_pages.TabletHomepage import TabletHomepage
from public_method import Gl
import time


class Get_AllRoleAccountForTest():
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    def get_LCInfo(self,Adminurl,lobname,sitename,OMuserid,OMpassword,LCuserid):    
        L=Login()
        L.Login_admin(Adminurl,lobname, sitename, OMuserid, OMpassword)
        LC_AccountInfo=self.get_AccountFromAdmin(LCuserid)
        L.logout_admin()
        return LC_AccountInfo
    def get_TLandAgentInfofromAdmin(self,Adminurl,lobname, sitename, OMuserid, OMpassword,userid):
        L=Login()
        L.Login_admin(Adminurl,lobname, sitename, OMuserid, OMpassword)
        Admin=AdminHomepage()
        Admin.Enter_TLAgentAccounts()
        TAindex=1
        Flag=True
        while Flag:
            TAa=TLandAgentAccountsPage()
           
            if TAa.get_TLAgentInfoItem(TAindex, 2)==userid:
                AccountInfo={"TAindex":TAindex,"Name":TAa.get_TLAgentInfoItem(TAindex, 1),"Password":TAa.get_TLAgentInfoItem(TAindex, 3),"Hrid":TAa.get_TLAgentInfoItem(TAindex, 2)}
                return AccountInfo
                Flag=False
                break
            else:
                TAindex=TAindex+1
                continue 
            
        L.logout_admin()
    def get_TLandAgentInfofromAdmin_Byrole(self,Adminurl,lobname, sitename, OMuserid, OMpassword,role):
        L=Login()
        L.Login_admin(Adminurl,lobname, sitename, OMuserid, OMpassword)
        Admin=AdminHomepage()
        Admin.Enter_TLAgentAccounts()
        TAindex=1
        Flag=True
        while Flag:
            TAa=TLandAgentAccountsPage()
           
            if TAa.get_TLAgentInfoItem(TAindex, 4)==role=="L1":
                TLInfo={"TAindex":TAindex,"Name":TAa.get_TLAgentInfoItem(TAindex, 1),"Password":TAa.get_TLAgentInfoItem(TAindex, 3),"Hrid":TAa.get_TLAgentInfoItem(TAindex, 2)}
                return TLInfo
                Flag=False
                break
            elif TAa.get_TLAgentInfoItem(TAindex, 4)==role=="L2":
                TLInfo={"TAindex":TAindex,"Name":TAa.get_TLAgentInfoItem(TAindex, 1),"Password":TAa.get_TLAgentInfoItem(TAindex, 3),"Hrid":TAa.get_TLAgentInfoItem(TAindex, 2)}
                return TLInfo
                Flag=False
                break
            elif TAa.get_TLAgentInfoItem(TAindex, 4)==role=="Agent":
                AgentInfo={"TAindex":TAindex,"Name":TAa.get_TLAgentInfoItem(TAindex, 1),"Password":TAa.get_TLAgentInfoItem(TAindex, 3),"Hrid":TAa.get_TLAgentInfoItem(TAindex, 2)}
                return AgentInfo
                Flag=False
                break
            else:
                TAindex=TAindex+1
                continue 
        L.logout_admin()    
    
    
        
    def get_TLInfoFromMyteamInfo(self,tableturl,lobname, sitename, OMuserid, OMpassword):
        L=Login()
        L.Login_tablet(tableturl,lobname, sitename, OMuserid, OMpassword)
        Tablet=TabletHomepage()
        Tablet.click_Myteaminfocircle()
        #Get the first TL info from my team info from tablet
        TeamNameandHrid=self.Get_MyTeamInfo(1)
        userid=TeamNameandHrid["Hrid"]
        L.logout_tablet()
        #AccountInfo=self.get_TLandAgentInfofromAdmin(Adminurl, lobname, sitename, OMuserid, OMpassword, userid)
        return userid
    def get_TLInfoFromPerformance(self,tableturl,lobname, sitename, OMuserid, OMpassword,timetap,adminurl):
        L=Login()
        L.Login_tablet(tableturl,lobname, sitename, OMuserid, OMpassword)
        Tablet=TabletHomepage()
        Tablet.click_performancecircle()
        Ppage=PerformancePage()
        if lobname in Gl.performancefor_MultiTimeTab_lob:
            if timetap=="LastTwoMonth":
                Ppage.click_timetab_performance(1)
            elif timetap=="LastMonth":
                Ppage.click_timetab_performance(2)
            elif timetap=="Yesterday":
                Ppage.click_timetab_performance(3)
            elif timetap=="Week-To-Date":
                Ppage.click_timetab_performance(4)
            elif timetap=="Month-To-Date":
                Ppage.click_timetab_performance(5)
        elif lobname in Gl.performancefor_3TimeTab_lob:
            if timetap=="LastTwoMonth":
                Ppage.click_timetab_performance(1)
            elif timetap=="LastMonth":
                Ppage.click_timetab_performance(2)
            elif timetap=="Month-To-Date":
                Ppage.click_timetab_performance(3)
        else:
            if timetap=="Yesterday":
                Ppage.click_timetab_performance(1)
            elif timetap=="Week-To-Date":
                Ppage.click_timetab_performance(2)
            elif timetap=="Month-To-Date":
                Ppage.click_timetab_performance(3)
            
                
        #Get the first TL info from performance of yesterday/MTD
        TeamHrid=self.Get_TeamHridFromPerformance()
        L.logout_tablet()
        TLHrid=TeamHrid["TL_hrid"]
        TLInfo=self.get_TLandAgentInfofromAdmin(adminurl, lobname, sitename, OMuserid, OMpassword, TLHrid)
        return TLInfo
        
    '''    
    def get_TLInfoandAgentHridFromPerformance(self,tableturl,lobname, sitename, OMuserid, OMpassword,timetap):
        L=Login()
        L.Login_tablet(tableturl,lobname, sitename, OMuserid, OMpassword)
        Tablet=TabletHomepage()
        Tablet.click_performancecircle()
        Ppage=PerformancePage()
        if lobname in Gl.performancefor_MultiTimeTab_lob:
            if timetap=="LastTwoMonth":
                Ppage.click_timetab_performance(1)
            elif timetap=="LastMonth":
                Ppage.click_timetab_performance(2)
            elif timetap=="Yesterday":
                Ppage.click_timetab_performance(3)
            elif timetap=="Week-To-Date":
                Ppage.click_timetab_performance(4)
            elif timetap=="Month-To-Date":
                Ppage.click_timetab_performance(5)
        elif lobname in Gl.performancefor_3TimeTab_lob:
            if timetap=="LastTwoMonth":
                Ppage.click_timetab_performance(1)
            elif timetap=="LastMonth":
                Ppage.click_timetab_performance(2)
            elif timetap=="Month-To-Date":
                Ppage.click_timetab_performance(3)
        else:
            if timetap=="Yesterday":
                Ppage.click_timetab_performance(1)
            elif timetap=="Week-To-Date":
                Ppage.click_timetab_performance(2)
            elif timetap=="Month-To-Date":
                Ppage.click_timetab_performance(3)
            
                
        #Get the first TL info from performance of yesterday/MTD
        TeamHrid=self.Get_TeamHridFromPerformance()
        TLHrid=TeamHrid["TL_hrid"]
        AgentHrid=TeamHrid["FisrtAgent_hrid"]
        Ppage.click_backbutton()
                        
        Tablet.click_Myteaminfocircle()
        lineindex=self.Get_lineindex(TLHrid)
        TLInfo=self.Get_MyTeamInfo(lineindex)
        TLPassword=TLInfo["Password"]
        TLName=TLInfo["Name"]
        TLInfoandAgentHrid={"TLName":TLName,"TLHrid":TLHrid,"TLPassword":TLPassword,"AgentHrid":AgentHrid}
        L.logout_tablet()
        return TLInfoandAgentHrid
        time.sleep(Gl.waittime)
    '''
    def get_AgentInfoFromTablet(self,tableturl,lobname, sitename,OMuserid, OMpassword,timetap,adminurl):  
        L=Login()
        L.Login_tablet(tableturl,lobname, sitename, OMuserid, OMpassword)
        Tablet=TabletHomepage()
        Tablet.click_performancecircle()
        Ppage=PerformancePage()
        if lobname in Gl.performancefor_MultiTimeTab_lob:
            if timetap=="LastTwoMonth":
                Ppage.click_timetab_performance(1)
            elif timetap=="LastMonth":
                Ppage.click_timetab_performance(2)
            elif timetap=="Yesterday":
                Ppage.click_timetab_performance(3)
            elif timetap=="Week-To-Date":
                Ppage.click_timetab_performance(4)
            elif timetap=="Month-To-Date":
                Ppage.click_timetab_performance(5)
        elif lobname in Gl.performancefor_3TimeTab_lob:
            if timetap=="LastTwoMonth":
                Ppage.click_timetab_performance(1)
            elif timetap=="LastMonth":
                Ppage.click_timetab_performance(2)
            elif timetap=="Month-To-Date":
                Ppage.click_timetab_performance(3)
        else:
            if timetap=="Yesterday":
                Ppage.click_timetab_performance(1)
            elif timetap=="Week-To-Date":
                Ppage.click_timetab_performance(2)
            elif timetap=="Month-To-Date":
                Ppage.click_timetab_performance(3)
        #Get the first TL info from performance of yesterday/MTD
        TeamHrid=self.Get_TeamHridFromPerformance()
        AgentHrid=TeamHrid["FisrtAgent_hrid"]
        L.logout_tablet()
        AgentInfo=self.get_TLandAgentInfofromAdmin(adminurl, lobname, sitename, OMuserid, OMpassword, AgentHrid)
        return AgentInfo
        
        '''  
        TLInfoandAgentHrid=self.get_TLInfoandAgentHridFromPerformance(tableturl, lobname, sitename, OMuserid, OMpassword,timetap)
        TLHrid=TLInfoandAgentHrid["TLHrid"]
        TLPassword=TLInfoandAgentHrid["TLPassword"]
        AgentHrid=TLInfoandAgentHrid["AgentHrid"]
        L=Login()
        L.Login_tablet(tableturl,lobname, sitename,TLHrid, TLPassword)
        Tablet=TabletHomepage()
        Tablet.click_TL_Myteaminfocircle()
        lineindex1=self.Get_lineindex(AgentHrid)
        AgentInfo=self.Get_MyTeamInfo(lineindex1)
        AgentPassword=AgentInfo["Password"]
        AgentName=AgentInfo["Name"]
        AgentInfo={"AgentHrid":AgentHrid,"AgentPassword":AgentPassword,"AgentName":AgentName}
        L.logout_tablet()
        return AgentInfo
        #time.sleep(2*Gl.waittime)     ''' 
    
    def get_AgentInfoFrom_TLMyteamInfo(self,tableturl,lobname, sitename,TLuserid, TLpassword): 
        L=Login()
        L.Login_tablet(tableturl,lobname, sitename,TLuserid, TLpassword)
        Tablet=TabletHomepage()
        Tablet.click_TL_Myteaminfocircle()
        AgentInfo=self.Get_MyTeamInfo(1)
        L.logout_tablet()
        return AgentInfo
        time.sleep(2*Gl.waittime)          
    #Below***********************Get OM(1,4) or LC method from Admin**************************************    
    def get_AccountFromAdmin(self,userid):
        Admin=AdminHomepage()
        Admin.Enter_OMaccountbrowse()
        OMindex=1
        Flag=True
        while Flag:
            OMa=OMaccountPage(OMindex)
            if OMa.get_newOMhrid()==userid:
                AccountInfo={"OMindex":OMindex,"Name":OMa.get_newOMname(),"Password":OMa.get_newOMpwd(),"Hrid":OMa.get_newOMhrid(),"Modified_Date":OMa.get_modifydate()}
                return AccountInfo
                Flag=False
                break
            else:
                OMindex=OMindex+1
                continue 
    #Above***********************Get OM(1,4) or LC method from Admin**************************************        
    
    
    
    #Below************************Get TL or Agent account method from Tablet *********************************
    def Get_TeamHridFromPerformance(self):
        PerPage=PerformancePage()
        TLindex=1
        PerPage.unfold_anyTL(TLindex)
        while PerPage.FisrtAgent_Notexist(TLindex):
            PerPage.unfold_anyTL(TLindex)#foldTL
            TLindex=TLindex+2
            PerPage.unfold_anyTL(TLindex)#unfold the next TL
            continue
        FisrtAgent_hrid=PerPage.get_FirstAgentofAnyTL_hrid(TLindex)
        TL_hrid=PerPage.get_anyTL_hrid(TLindex)
        TeamHrid={"FisrtAgent_hrid":FisrtAgent_hrid,"TL_hrid":TL_hrid}
        return TeamHrid
        
    def Get_lineindex(self,hrid):
        lineindex=1
        Myteam=MyTeamInfoPage()
        while hrid!=Myteam.get_eachhrid(lineindex):
            lineindex=lineindex+1
        return lineindex
        
    def Get_MyTeamInfo(self,lineindex):
        #lineindex=self.Get_lineindex(hrid)
        MyTeam=MyTeamInfoPage()
        Name=MyTeam.get_eachusername(lineindex)
        Hrid=MyTeam.get_eachhrid(lineindex)
        #Password=MyTeam.get_eachpwd(lineindex)
        #TeamInfo={"Name":Name,"Hrid":Hrid,"Password":Password}
        TeamInfo={"Name":Name,"Hrid":Hrid}
        return TeamInfo
    #Above************************Get TL or Agent account method from Tablet *********************************
    