'''
Created on Aug 24, 2017

@author: symbio
'''
import unittest
from public_method import Gl
from public_method.Get_configration_data import Get_configration_data
from public_method.HandleMySQL import HandleMySQL


class Commendation_AddFromOtherPage(unittest.TestCase):


    def setUp(self):
        GetData=Get_configration_data()
        #Database info
        self.dbuser=GetData.get_StageDatabaseUser()
        self.dbpassword=GetData.get_StageDatabasePassword()
        
        self.lobname="ISM"
        self.sitename="DAVAO"
        self.sql="select count(*) as user_role from user_role;"
        
       
   
    
    def test_CommpareThreeDBdata(self):
        HMysql=HandleMySQL()
        HMysql.CompareDataNumberFromThreeDB(self.lobname, self.sitename,self.dbuser,self.dbpassword,self.sql)
        HMysql.CompareDataContentFromThreeDB(self.lobname, self.sitename,self.dbuser,self.dbpassword,self.sql)    
    
    def tearDown(self):
        Gl.driver.quit()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()