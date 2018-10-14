'''
Created on Aug 7, 2017

@author: symbio
'''
from decimal import Decimal
class KPI_method(object):
    '''
    classdocs
    '''


    def get_IndexOfTwovalue_list(self,KPIlist):
        index_Dic={}
        SingleValue_index_list=[]
        TwoValue_index_list=[]
        for a in range(0,len(KPIlist)):
            if type(KPIlist[a])==list:
                if "\n" in KPIlist[a][0]:
                    TwoValue_index_list.append(a) 
                else:
                    SingleValue_index_list.append(a)
            else:
                if "\n" in KPIlist[a]:
                    TwoValue_index_list.append(a) 
                else:
                    SingleValue_index_list.append(a) 
        index_Dic["SingleValue_index_list"]=SingleValue_index_list
        index_Dic["TwoValue_index_list"]=TwoValue_index_list   
        return index_Dic
    
    def DeletDate_Intitle(self,title):
        if len(title)>12:
            #print len(title)
            #print title[-13:]
            if title[-12]=="(" and title[-1]==")":
                title_new=title.replace(title[-13:],"") 
            else:
                title_new=title
        else:
            title_new=title
        return title_new
    
    
    def Decimal_To_Percentage(self,KPI_value):
        Decimal_digits='0.0000'
        if KPI_value=='0.0':
            KPI_Percentage='0.00%'
        elif KPI_value=='':
            KPI_Percentage=KPI_value
        elif KPI_value=='N/A':
            KPI_Percentage=KPI_value
        else:
            KPI_new=self.Change_Decimal_digits(KPI_value,Decimal_digits)
            KPI_Percentage='%.2f%%' % (KPI_new * 100)
        return KPI_Percentage
    
    def Change_Decimal_digits(self,KPI_value,Decimal_digits):
        if KPI_value=='N/A':
            KPI=KPI_value
        elif KPI_value=='':
            KPI=KPI_value
        elif "~" in str(KPI_value):
            KPI=KPI_value
        else:
            KPI=Decimal(KPI_value).quantize(Decimal(Decimal_digits))#2:'0.00',4:'0.0000'
        return KPI
    
    