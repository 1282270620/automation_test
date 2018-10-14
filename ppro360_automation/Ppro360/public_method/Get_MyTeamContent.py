'''
Created on 2018.1.29

@author: yalan.yin
'''
import xlrd
from public_method.Get_file import Get_file
from public_method.Get_configration_data import Get_configration_data

class Get_MyTeamContent(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
        GetData=Get_configration_data()
        self.downloadpath=GetData.get_DefaultDownloadPath()
        
    
    def Get_TotalUserNumber(self,filename_prefix,sheetname):
        table_content=self.get_ExcelContent(filename_prefix,sheetname)
        UserN=0
        nrows=table_content.nrows
        for i in range(1,nrows):
            if table_content.row_values(i)!="":
                if table_content.row_values(i)[0]!="":
                    UserN=UserN+1
        return UserN
    
    def Get_MyTeamHeader(self,filename_prefix,sheetname):
        table_content=self.get_ExcelContent(filename_prefix,sheetname)
        source_list=table_content.row_values(0)
        null_list=self.get_null_list(source_list)
        if null_list==[]:
            headerlist=source_list
        else:
            print(source_list)
            print(null_list)
        return headerlist
    
    '''
    def Get_MyTeamsubHeader(self,filename_prefix,sheetname):
        table_content=self.get_ExcelContent(filename_prefix,sheetname)
        source_list=table_content.row_values(0)
        null_list=self.get_null_list(source_list)
        if null_list==[]:
            headerlist=source_list
        else:
            print source_list
            print null_list
            #for a in null_list:
            for i in range(0,len(null_list)):
                print source_list[null_list[i]]
                #print source_list[a+1]
                #del source_list[a+1]
                del source_list[null_list[i]]
            headerlist=source_list
            for a in null_list:
                headerlist.append(table_content.row_values(1)[a])               
        return headerlist  
    '''
    def get_null_list(self,source_list):
        null_list=[]
        for i in range(0,len(source_list)):
            if source_list[i]=="":
                null_list.append(i)
        return null_list
    def get_subheader(self):
        pass        
          
    
    def Get_Name(self,filename_prefix,sheetname):
        table_content=self.get_ExcelContent(filename_prefix,sheetname)
        UserN=self.Get_TotalUserNumber(filename_prefix,sheetname)
        Name_list=[]
        #Name_Dic={}
        if UserN==0:
            print("There is no any record!")
        else:
            for i in range(1,UserN+1):
                #Name_Dic[table_content.row_values(i)[0]]=table_content.row_values(i)[2]
                Name_list.append(table_content.row_values(i)[0])    
        #return Name_Dic
        return Name_list
        
    def Get_HRID(self,filename_prefix,sheetname):
        table_content=self.get_ExcelContent(filename_prefix,sheetname)
        UserN=self.Get_TotalUserNumber(filename_prefix,sheetname)
        #HRID_List=[]
        HRID_Dic={}
        if UserN==0:
            print("There is no any record!")
        else:
            for i in range(1,UserN+1):
                HRID_Dic[table_content.row_values(i)[0]]=table_content.row_values(i)[1]
                #HRID_List.append(table_content.row_values(i)[1])
        return HRID_Dic
        #return HRID_List
        
    def get_ExcelContent(self,filename_prefix,sheetname): 
        G=Get_file()
        MyTeamInfofileaddress=G.Get_downloadfileaddress(self.downloadpath, filename_prefix)
        Cdata=xlrd.open_workbook(MyTeamInfofileaddress)
        table_content = Cdata.sheet_by_name(sheetname)
        return table_content
        '''
        nrows=table.nrows
        for i in range(0,nrows):
            item=table.row_values(i)[0]
            if item == testitem:
                dataneeded=table.row_values(i)[1]
        return dataneeded''' 