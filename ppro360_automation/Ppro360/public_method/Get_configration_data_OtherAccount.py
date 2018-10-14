'''
Created on 2018/8/1

@author: hanyang.dong
'''
import xlrd
#import os
from public_method import Gl
from public_method.Get_file import Get_file
from public_method.Get_AnyText_ForNormal import Get_AnyText_ForNormal
from public_method.Get_configration_data import Get_configration_data
import getpass 
import pytz
import datetime
import calendar

class Get_configration_data_OtherAccount():
    
    def __init__(self):
        GetData=Get_configration_data()
        self.Accountsheetname="Account"
        self.BASE_CONFIGURATIONsheetname="BASE-CONFIGURATION"
        self.CASE_LOBSITEsheetname="CASE-LOBSITE"
        
        
        self.SuperAdminuserid="SuperAdminuserid"
        self.SuperAdminpassword="SuperAdminpassword"
        self.L2userid="L2userid"
        self.L2pwd="L2password"
        self.TLuserid="TLuserid"
        self.TLpwd="TLpassword"
        self.Agentuserid="Agentuserid"
        self.Agentpwd="Agentpassword"
        
        
        
        self.AllLOBs="All-LOBs"
    

 
    def get_AllLOBs_list(self):
        AllLOBs_list=self.get_data_needed(self.BASE_CONFIGURATIONsheetname, self.AllLOBs).split(",")
        return AllLOBs_list
    
    def get_SuperAdminaccount(self):
        SuperAdminuserid=str(self.get_data_needed(self.Accountsheetname, self.SuperAdminuserid)).replace(".0","")
        SuperAdminpassword=str(self.get_data_needed(self.Accountsheetname, self.SuperAdminpassword)).replace(".0","")
        SuperAdminaccount={"SuperAdminuserid":SuperAdminuserid,"SuperAdminpassword":SuperAdminpassword}
        return SuperAdminaccount
        
    def get_L2account(self):
        L2userid=str(self.get_data_needed(self.Accountsheetname, self.L2userid)).replace(".0","")
        L2password=str(self.get_data_needed(self.Accountsheetname, self.L2pwd)).replace(".0","")
        L2account={"L2userid":L2userid,"L2password":L2password}
        return L2account
        
    def get_TLaccount(self):
        TLuserid=str(self.get_data_needed(self.Accountsheetname, self.TLuserid)).replace(".0","")
        TLpassword=str(self.get_data_needed(self.Accountsheetname, self.TLpwd)).replace(".0","")
        TLaccount={"TLuserid":TLuserid,"TLpassword":TLpassword}
        return TLaccount
    
    def get_Agentaccount(self):
        Agentuserid=str(self.get_data_needed(self.Accountsheetname, self.Agentuserid)).replace(".0","")
        Agentpassword=str(self.get_data_needed(self.Accountsheetname, self.Agentpwd)).replace(".0","")
        Agentaccount={"Agentuserid":Agentuserid,"Agentpassword":Agentpassword}
        return Agentaccount
        
    def get_data_needed(self,sheetname,testitem): 
        global dataneeded
        
        G=Get_file()
        Configurationfile=G.Get_fileaddress(Gl.configrationfilename)
    
        Cdata=xlrd.open_workbook(Configurationfile)
        table = Cdata.sheet_by_name(sheetname)
        nrows=table.nrows
        for i in range(0,nrows):
            item=table.row_values(i)[0]
            if item == testitem:
                dataneeded=table.row_values(i)[1]
        return dataneeded    