'''
Created on Mar 17, 2017

@author: symbio
'''
from Tablet_pages.ChangePasswordPage import ChangePasswordPage
from AdminSystem_Pages.OMAddPage import OMAddPage
from AdminSystem_Pages.AddOMWarnningpage import AddOMWarningpage
class AddOrChangeUserInfo():
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    def AddOMatAdmin(self,OMfirstname,OMlastname,NewOMhrid):
        OMadd=OMAddPage()
        OMadd.input_fisrtname(OMfirstname)
        OMadd.input_lastname(OMlastname)
        OMadd.input_hrid(NewOMhrid)
        OMadd.click_addOM()
        i=0
        AddWarn=AddOMWarningpage()
        while OMadd.warningwidonw_ispopup()==True:
            AddWarn.click_OK()
            OMadd.clear_hrid()
            NewOMhrid=NewOMhrid+str(i)
            OMadd.input_hrid(NewOMhrid)
            OMadd.click_addOM()
            i=i+1
        return NewOMhrid

    
    def InputPassword(self,currentPassword,newPassword,reNewPassword): #Only for Tablet
        ChangePWD=ChangePasswordPage()   
        ChangePWD.currentPassword_Input(currentPassword)
        ChangePWD.newPassword_Input(newPassword)
        ChangePWD.reNewPassword_Input(reNewPassword)
        
    def ChangePassword_Cancel(self,currentPassword,newPassword,reNewPassword):#Only for Tablet
        ChangePWD=ChangePasswordPage()
        self.InputPassword(currentPassword, newPassword, reNewPassword)
        ChangePWD.click_Cancelbutton()
        
    def ChangePassword_Save(self,currentPassword,newPassword,reNewPassword):#Only for Tablet
        ChangePWD=ChangePasswordPage()
        self.InputPassword(currentPassword, newPassword, reNewPassword)
        ChangePWD.click_Submitbutton() 
    