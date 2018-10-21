import unittest,MySQLdb,time
from public_method.Get_configration_data import Get_configration_data
from public_method.Get_AllRoleAccountForTest import Get_AllRoleAccountForTest
from public_method import Gl
from public_method.Login import Login
from public_method.AddOrChangeUserInfo import AddOrChangeUserInfo

from AdminSystem_Pages.OMAddPage import OMAddPage
from AdminSystem_Pages.OMaccountPage import OMaccountPage
from AdminSystem_Pages.LoginAdminPage import LoginAdminPage
from Tablet_pages.HeaderPage import HeaderPage
from Tablet_pages.ChangPwd_warningPage import ChangPwd_warningPage

class AddOrChangCommonAccountForScript(unittest.TestCase):
    def setUp(self):
        #Case ID
        self.caseID="AddOrChangCommonAccountForScript"
        
        GetData=Get_configration_data()
        #Get OM account
        OMaccount=GetData.get_OMaccount()
        self.OMuserid=OMaccount["OMuserid"]
        self.OMpassword=OMaccount["OMpassword"]
        self.cur_OMpassword="123456"
        #Get LC account
        LCaccount=GetData.get_LCaccount()
        self.LCuserid=LCaccount["LCuserid"]
        self.LCpassword=LCaccount["LCpassword"]
        #Get L2 account
        L2account=GetData.get_L2account()
        self.L2userid=L2account["L2userid"]
        self.L2password=L2account["L2password"]
        
        #get database info
        self.dbuser=GetData.get_StageDatabaseUser()
        self.dbpassword=GetData.get_StageDatabasePassword()
        
        #Get all lobs from CSV
        self.testLOBSITE_list=GetData.get_LOBSITEtoTest(self.caseID)
    def tearDown(self):
        #Gl.driver.quit()
        pass
    
    def test_ChangeOM_password(self):
        Log = Login()
        GetConfig = Get_configration_data()
        GARATest = Get_AllRoleAccountForTest()
        OMAPage = OMAddPage()
        
        for i in range(0,len(self.testLOBSITE_list)):
            Flag=GetConfig.get_LOBSITE_STATUS(self.testLOBSITE_list[i])

            if Flag==True:
                each_LOBSITE=self.testLOBSITE_list[i].split(":")
                lobname=each_LOBSITE[0]

                ##GET THE CORRECT URL#####
                adminurl=GetConfig.get_Test_AdminUrl(lobname)
                tableturl=GetConfig.get_Test_Tablet(lobname)
                host = GetConfig.get_Test_Hostindex(lobname)
                
                #Get Site to test
                site_list=each_LOBSITE[1].split("*")
                for n in range(0,len(site_list)):
                    sitename=site_list[n]
                    GetConfig.print_StartTest_message(lobname, sitename)
                    
                    Log.Login_admin(adminurl, lobname, sitename, self.OMuserid, self.OMpassword)
                    
                    #Reset OM password
                    if self.get_loginpermission(adminurl)==False:
                        self.chang_Password(tableturl, lobname, sitename, self.OMuserid, self.cur_OMpassword,self.OMpassword)
                        print "Reset OM password successful!"
                    else:
                        print "No need to reset the OM password"
                        Log.logout_admin()
                    
                    #Reset L2 password
                    L2Info = self.judge_L2exist(adminurl, lobname, sitename, self.OMuserid, self.OMpassword, self.L2userid)
                    if L2Info != False:
                        L2pwd = L2Info["Password"]
                        if L2pwd != self.L2password:
                            self.chang_Password(tableturl, lobname, sitename, self.L2userid, L2pwd,self.L2password)
                            print "Reset L2 password successful!"
                        else:
                            print "No need to reset the L2 password!"
                    else:
                        print "L2 account doesn't exist"
                    
                        
                    ##Reset or Add/Reset password
                    LCInfo = self.judge_LCexist(adminurl, lobname, sitename, self.OMuserid, self.OMpassword, self.LCuserid)
                    if LCInfo != False:
                        LCpwd = LCInfo["Password"]
                    else:
                        OMAPage.click_addOM()
                        OMAPage.input_fisrtname("LC")
                        OMAPage.input_lastname("TEST")
                        OMAPage.input_hrid(self.LCuserid)
                        OMAPage.click_addOM()
                        OMaPage = OMaccountPage(1)
                        LCpwd = OMaPage.get_newOMpwd()
                        Log.logout_admin()
                        print "Add LC account successful!"
                    LCrole_sql = "update user_role set role_id=(select id from role where name='LC') where user_id = '88888888' order by role_id desc limit 1;"
                    lobsitename = GetConfig.get_LobSiteDBName(lobname, sitename)
                    database_name = lobsitename["lobname_database"]+"_"+lobsitename["sitename_database"]
                    self.exe_Sql(host, self.dbuser,self.dbpassword,database_name,LCrole_sql)
                    if LCpwd != self.LCpassword:
                        self.chang_Password(tableturl, lobname, sitename, self.LCuserid, LCpwd,self.LCpassword)
                        print "Reset LC password successful!"
                    else:
                        print "No need to reset the LC password!"
    
    def judge_L2exist(self,adminurl, lobname, sitename, OMuserid, OMpassword, L2userid):
        try:
            L2Info=Get_AllRoleAccountForTest().get_TLandAgentInfofromAdmin(adminurl, lobname, sitename, OMuserid, OMpassword, L2userid)
            return L2Info
        except:
            return False
        
    def judge_LCexist(self,adminurl, lobname, sitename, OMuserid, OMpassword, LCuserid):
        try:
            LCInfo = Get_AllRoleAccountForTest().get_LCInfo(adminurl, lobname, sitename, OMuserid, OMpassword, LCuserid)
            return LCInfo
        except:
            return False
        
    def get_loginpermission(self,adminurl):
        try:
            LAPage = LoginAdminPage(adminurl,Gl.driver)
            LAPage.get_nopermission()
        except:
            return True#means login successful:OMuserid and OMpassword correct
        return False#means login failure:OMuserid and OMpassword incorrect
         
    def chang_Password(self,url, lobname, sitename, userid, password,newPassword):
        Log = Login()
        HPage = HeaderPage()
        ACUInfo = AddOrChangeUserInfo()
        CPWPage = ChangPwd_warningPage()
        
        Log.Login_tablet(url, lobname, sitename, userid, password)
        HPage.click_settingButton()
        HPage.click_changePasswordLink()
        ACUInfo.ChangePassword_Save(password, newPassword, newPassword)
        CPWPage.click_OKbutton()
        
    def exe_Sql(self,host,dbuser,dbpassword,database_name,sql):
        GetData = Get_configration_data()
        Nodehost=GetData.get_StageNodeHost(host)
        conn=MySQLdb.connect(Nodehost,dbuser,dbpassword,database_name)
        cursor=conn.cursor()
        conn.autocommit(True)
        cursor.execute(sql)
        cursor.close()
        conn.close()


