'''
Created on May 12, 2017

@author: symbio
'''
import xlrd
from public_method.Get_file import Get_file
from public_method.Get_configration_data import Get_configration_data
class Get_CoachContent():
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        #Get default download path
        GetData=Get_configration_data()
        self.downloadpath=GetData.get_DefaultDownloadPath()
        #Get filename_prefix
        #self.filename_prefix=GetData.get_CoachExportfile_prefix()
    
    def Get_TotalCoachNumber(self,filename_prefix,sheetname):
        table_content=self.get_ExcelContent(filename_prefix,sheetname)
        CoachN=0
        nrows=table_content.nrows
        for i in range(1,nrows):
            if table_content.row_values(i)!="":
                if table_content.row_values(i)[0]!="":
                    CoachN=CoachN+1
        return CoachN
    def Get_CoachExcelHeader_Actual(self,filename_prefix,sheetname,header_rows):
        table_content=self.get_ExcelContent(filename_prefix,sheetname)
        headerlist_Actual=[]
        for a in range(0,header_rows):
            source_list=table_content.row_values(a)
            headerlist_Actual=headerlist_Actual+source_list
        return headerlist_Actual
    
    '''
    def Get_CoachExcelHeader(self,filename_prefix,sheetname,header_rows):
        table_content=self.get_ExcelContent(filename_prefix,sheetname)
        
        headerlist=[]
        #null_list=self.get_null_list(source_list)
        if header_rows==1:
        #if null_list==[]:
            source_list=table_content.row_values(0)
            headerlist=source_list
        else:
            for i in range(1,header_rows+1):
                source_list=table_content.row_values(i-1)
                null_list=self.get_null_list(source_list)
                print source_list
                print null_list
                #for a in null_list:
                
                
                a=0
                while source_list[null_list[0]]=="" and a<=len(null_list):
                    print a
                    del source_list[null_list[0]]
                    a=a+1
                
                headerlist=headerlist+source_list
                #second_list=null_list.append(null_list[0])
            
            headerlist.append(table_content.row_values(1)[null_list[0]-1])
            for a in null_list:
                headerlist.append(table_content.row_values(1)[a])  
        return headerlist  
    def get_null_list(self,source_list):
        null_list=[]
        for i in range(0,len(source_list)):
            if source_list[i]=="":
                null_list.append(i)
        return null_list
    def get_subheader(self):
        pass        
    '''      
    
    def Get_EmployeeName(self,filename_prefix,sheetname):
        table_content=self.get_ExcelContent(filename_prefix,sheetname)
        CoachN=self.Get_TotalCoachNumber(filename_prefix,sheetname)
        EmployeeName_Dic={}
        if CoachN==0:
            print "There is no any record!"
        else:
            for i in range(1,CoachN+1):
                EmployeeName_Dic[table_content.row_values(i)[0]]=table_content.row_values(i)[2]
        return EmployeeName_Dic
        
    def Get_CoachingName(self,filename_prefix,sheetname):
        table_content=self.get_ExcelContent(filename_prefix,sheetname)
        CoachN=self.Get_TotalCoachNumber(filename_prefix,sheetname)
        CoachingName_Dic={}
        if CoachN==0:
            print "There is no any record!"
        else:
            for i in range(1,CoachN+1):
                CoachingName_Dic[table_content.row_values(i)[0]]=table_content.row_values(i)[1]
        return CoachingName_Dic
        
    def get_ExcelContent(self,filename_prefix,sheetname): 
        G=Get_file()
        CoachExportfileaddress=G.Get_downloadfileaddress(self.downloadpath, filename_prefix)
        Cdata=xlrd.open_workbook(CoachExportfileaddress)
        table_content = Cdata.sheet_by_name(sheetname)
        return table_content
        '''
        nrows=table.nrows
        for i in range(0,nrows):
            item=table.row_values(i)[0]
            if item == testitem:
                dataneeded=table.row_values(i)[1]
        return dataneeded'''