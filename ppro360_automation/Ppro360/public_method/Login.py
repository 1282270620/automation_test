'''
Created on Dec 21, 2016

@author: symbio
'''
#from selenium import webdriver
from AdminSystem_Pages.LoginAdminPage import LoginAdminPage
from Tablet_pages.LoginTabletPage import LogintabletPage
import time
from public_method import Gl
from Tablet_pages.HeaderPage import HeaderPage
from AdminSystem_Pages.AdminHomepage import AdminHomepage


class Login(object):



    #def __init__(self, url,lobname,sitename,userid,password):
        
        #self.url=url
        #self.tableturl=tableturl
        #self.lobname=lobname
        #self.sitename=sitename
        #self.userid=userid
        #self.password=password

        
    def __init__(self):
        pass
    def Login_admin(self,adminurl,lobname,sitename,OMuserid,OMpassword):        
        #login_page=LoginAdminPage(self.url,"Performance Pro 360",Gl.driver)
        login_page=LoginAdminPage(adminurl,Gl.driver)
        login_page.open()
        time.sleep(2*Gl.waittime)
        login_page.select_lob(lobname)
        login_page.select_site(sitename)
        login_page.input_userid(OMuserid)
        login_page.input_password(OMpassword)
        login_page.click_login()
        time.sleep(5*Gl.waittime)
        
    
        
    def Login_tablet(self,url,lobname,sitename,userid,password):
        #login_page=LogintabletPage(self.url,"Performance Pro 360",Gl.driver)
        login_page=LogintabletPage(url,Gl.driver)
        login_page.open()
        login_page.ScrollToBottom()
        login_page.click_lobname_box_dropdown()
        login_page.select_lob(lobname)
        login_page.click_sitename_box_dropdown()
        login_page.select_site(sitename)
        login_page.input_userid(userid)
        login_page.input_password(password)
        login_page.click_login()
    
    def logout_tablet(self):
        #login_page=LogintabletPage(self.url,"Performance Pro 360",Gl.driver)
        Header=HeaderPage()
        Header.click_settingButton()
        #time.sleep(Gl.waittime)
        Header.click_LogoutLink()
        #time.sleep(Gl.waittime)
        
    def VPSVPlogout_tablet(self): #the method is not used now
        Header=HeaderPage()
        Header.click_settingButton()
        Header.click_VPSVPLogoutLink()
        
    def logout_admin(self):
        #login_page=LoginAdminPage(self.url,"Performance Pro 360",Gl.driver)
        Admin=AdminHomepage()
        Admin.click_userhead()
        time.sleep(Gl.waittime)
        Admin.click_logout()
        time.sleep(Gl.waittime)
     
  
        
   

            