'''
Created on Aug 24, 2017

@author: symbio
'''

from public_method import Gl
from public_method.Get_configration_data import Get_configration_data
import MySQLdb
class HandleMySQL(object):
    '''
    classdocs
    '''
    def Get_DatabaseName(self,lobname,sitename):
        A=lobname.lower().replace(" ","")
        B=sitename.lower().replace("-","").replace(" ","")
        DatabaseName=A+"_"+B
        return DatabaseName
        
    
    
    def GetData_From92(self,lobname, sitename,dbuser,dbpassword,sql):
        Datalist=self.Get_datafromDB(92, lobname, sitename,dbuser,dbpassword,sql)
        return Datalist

    def CompareDataNumberFromThreeDB(self,lobname, sitename,dbuser,dbpassword,sql):
        print("********************Compare data number from three db************************")
        datanumber_from49=self.Get_datafromDB(49, lobname, sitename,dbuser,dbpassword,sql)[0]
        datanumber_from50=self.Get_datafromDB(50, lobname, sitename,dbuser,dbpassword,sql)[0]
        datanumber_from51=self.Get_datafromDB(51, lobname, sitename,dbuser,dbpassword,sql)[0]
        print("datanumber_from49:",datanumber_from49)
        print("datanumber_from50:",datanumber_from50)
        print("datanumber_from51:",datanumber_from51)
        assert datanumber_from49==datanumber_from50==datanumber_from51
        print("The number of data from all three DB are the same, it is tested OK!")
    def CompareDataContentFromThreeDB(self,lobname, sitename,dbuser,dbpassword,sql):
        print("********************Compare data content from three db************************")
        data_from49=self.Get_datafromDB(49, lobname, sitename,dbuser,dbpassword,sql)[1]
        data_from50=self.Get_datafromDB(50, lobname, sitename,dbuser,dbpassword,sql)[1]
        data_from51=self.Get_datafromDB(51, lobname, sitename,dbuser,dbpassword,sql)[1]
        for i in range(0,len(data_from49)):
            print("data_from49[",i,"]==data_from50[",i,"]==data_from51[",i,"]:")
            print(data_from49[i]) 
            print(data_from50[i]) 
            print(data_from51[i])
            assert  data_from49[i]==data_from50[i]==data_from51[i]
            print(i,":is tested Successfully!")
        print("All are the same and tested OK!")
    
    def Get_datafromDB(self,hostindex,lobname,sitename,dbuser,dbpassword,sql):
        GetData=Get_configration_data()
        Data_list=[]
        Nodehost=GetData.get_StageNodeHost(hostindex)   
        database_name=self.Get_DatabaseName(lobname, sitename)    
        conn=MySQLdb.connect(Nodehost,dbuser,dbpassword,database_name)
        cursor=conn.cursor()
        conn.autocommit(True)
        number=cursor.execute(sql)#Get all info of Coaching except coach_name
        data=cursor.fetchall()
        Data_list.append(number)
        Data_list.append(data)
        cursor.close()
        conn.close()
        return Data_list
        