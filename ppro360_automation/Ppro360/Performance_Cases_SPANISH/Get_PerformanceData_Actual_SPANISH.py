'''
Created on Apr 7, 2017

@author: symbio
'''
from Tablet_pages.PerformancPage import PerformancePage
class Get_PerformanceData_Actual_SPANISH():
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    def get_SPANISH_Goal_Actual(self):
        Ppage=PerformancePage()
        Goal_lsit=Ppage.get_AllKPIsofGoal_list(13)
        for i in range(0,len(Goal_lsit)):
            if '\n' in Goal_lsit[i]:
                Goal_lsit[i]=Goal_lsit[i].split('\n')
        
        a=Goal_lsit[1][0].replace("$","")
        b=Goal_lsit[1][1].replace("$","")
        NetRevenue_Actual=[a,b]
        NetRevenue_Attain=Goal_lsit[2]

        HSIAIPDSL_Actual=Goal_lsit[3]
        HSIAIPDSL_Attain=Goal_lsit[4]
        
        CRFT_Actual=Goal_lsit[5]
        CRFT_Attain=Goal_lsit[6]
        
        OpsAht=Goal_lsit[7]
        
        VOIP_Actual=Goal_lsit[8]
        VOIP_Attain=Goal_lsit[9]
        
        WLS_Actual=Goal_lsit[10]
        WLS_Attain=Goal_lsit[11]
        
        Achiev=Goal_lsit[12]
        
        Goal_KPI={"NetRevenue_Actual":NetRevenue_Actual,"NetRevenue_Attain":NetRevenue_Attain,"HSIAIPDSL_Actual":HSIAIPDSL_Actual,
                  "HSIAIPDSL_Attain":HSIAIPDSL_Attain,"CRFT_Actual":CRFT_Actual,"CRFT_Attain":CRFT_Attain,
                  "OpsAht":OpsAht,"VOIP_Actual":VOIP_Actual,"VOIP_Attain":VOIP_Attain,"WLS_Actual":WLS_Actual,"WLS_Attain":WLS_Attain,
                  "Achiev":Achiev}
        return Goal_KPI
    def get_SPANISH_SITE_Data_(self):#site:lineindex=2
        Ppage=PerformancePage()
        a=Ppage.get_anyKPIValueOfTotal(2,2)[0].replace("$","")
        b=Ppage.get_anyKPIValueOfTotal(2,2)[1].replace("$","")
        NetRevenue_Actual=[a,b]
        NetRevenue_Attain=Ppage.get_anyKPIValueOfTotal(2,3)
        HSIAIPDSL_Actual=Ppage.get_anyKPIValueOfTotal(2,4)
        HSIAIPDSL_Attain=Ppage.get_anyKPIValueOfTotal(2,5)
        CRFT_Actual=Ppage.get_anyKPIValueOfTotal(2,6)
        CRFT_Attain=Ppage.get_anyKPIValueOfTotal(2,7)
        OpsAht=Ppage.get_anyKPIValueOfTotal(2,8)
        VOIP_Actual=Ppage.get_anyKPIValueOfTotal(2,9)
        VOIP_Attain=Ppage.get_anyKPIValueOfTotal(2,10)
        WLS_Actual=Ppage.get_anyKPIValueOfTotal(2,11)
        WLS_Attain=Ppage.get_anyKPIValueOfTotal(2,12)
        Achiev=Ppage.get_anyKPIValueOfTotal(2,13)
        SITE_KPI={"NetRevenue_Actual":NetRevenue_Actual,"NetRevenue_Attain":NetRevenue_Attain,"HSIAIPDSL_Actual":HSIAIPDSL_Actual,
                  "HSIAIPDSL_Attain":HSIAIPDSL_Attain,"CRFT_Actual":CRFT_Actual,"CRFT_Attain":CRFT_Attain,
                  "OpsAht":OpsAht,"VOIP_Actual":VOIP_Actual,"VOIP_Attain":VOIP_Attain,"WLS_Actual":WLS_Actual,"WLS_Attain":WLS_Attain,
                  "Achiev":Achiev}
        return SITE_KPI
    def get_SPANISH_TEAM_Data_(self):#TEAM:lineindex=3
        Ppage=PerformancePage()
        a=Ppage.get_anyKPIValueOfTotal_doubleKPI(3,2)[0].replace("$","")
        b=Ppage.get_anyKPIValueOfTotal_doubleKPI(3,2)[1].replace("$","")
        NetRevenue_Actual=[a,b]
        NetRevenue_Attain=Ppage.get_anyKPIValueOfTotal(3,3)
        HSIAIPDSL_Actual=Ppage.get_anyKPIValueOfTotal_doubleKPI(3,4)
        HSIAIPDSL_Attain=Ppage.get_anyKPIValueOfTotal(3,5)
        CRFT_Actual=Ppage.get_anyKPIValueOfTotal(3,6)
        CRFT_Attain=Ppage.get_anyKPIValueOfTotal(3,7)
        OpsAht=Ppage.get_anyKPIValueOfTotal(3,8)
        VOIP_Actual=Ppage.get_anyKPIValueOfTotal_doubleKPI(3,9)
        VOIP_Attain=Ppage.get_anyKPIValueOfTotal(3,10)
        WLS_Actual=Ppage.get_anyKPIValueOfTotal_doubleKPI(3,11)
        WLS_Attain=Ppage.get_anyKPIValueOfTotal(3,12)
        Achiev=Ppage.get_anyKPIValueOfTotal(3,13)
        TEAM_KPI={"NetRevenue_Actual":NetRevenue_Actual,"NetRevenue_Attain":NetRevenue_Attain,"HSIAIPDSL_Actual":HSIAIPDSL_Actual,
                  "HSIAIPDSL_Attain":HSIAIPDSL_Attain,"CRFT_Actual":CRFT_Actual,"CRFT_Attain":CRFT_Attain,
                  "OpsAht":OpsAht,"VOIP_Actual":VOIP_Actual,"VOIP_Attain":VOIP_Attain,"WLS_Actual":WLS_Actual,"WLS_Attain":WLS_Attain,
                  "Achiev":Achiev}
        for key in TEAM_KPI:
            if '\n' in TEAM_KPI[key][0]:
                TEAM_KPI[key][0]=TEAM_KPI[key][0].split('\n')
                TEAM_KPI[key][0][1]=TEAM_KPI[key][0][1].replace('(','').replace(')','')
        return TEAM_KPI
    
    
    def get_Achievement_Data(self,lineindex):
        Ppage=PerformancePage()
        Achievement_Data=Ppage.get_anyKPIValueOfTotal(lineindex, 13)
        return Achievement_Data
    
    def get_SPANISH_Agent_KPI_Actual(self,TLindex,Agentindex):
        Ppage=PerformancePage()
        a=Ppage.get_anyKPIofAgent_OM_doubleKPI(TLindex, Agentindex,2)[0].replace("$","")
        b=Ppage.get_anyKPIofAgent_OM_doubleKPI(TLindex, Agentindex,2)[1].replace("$","")
        NetRevenue_Actual=[a,b]
        NetRevenue_Attain=Ppage.get_anyKPIofAgent_OM(TLindex, Agentindex,3)
        HSIAIPDSL_Actual=Ppage.get_anyKPIofAgent_OM_doubleKPI(TLindex, Agentindex,4)
        HSIAIPDSL_Attain=Ppage.get_anyKPIofAgent_OM(TLindex, Agentindex,5)
        CRFT_Actual=Ppage.get_anyKPIofAgent_OM(TLindex, Agentindex,6)
        CRFT_Attain=Ppage.get_anyKPIofAgent_OM(TLindex, Agentindex,7)
        OpsAht=Ppage.get_anyKPIofAgent_OM(TLindex, Agentindex,8)
        VOIP_Actual=Ppage.get_anyKPIofAgent_OM_doubleKPI(TLindex, Agentindex,9)
        VOIP_Attain=Ppage.get_anyKPIofAgent_OM(TLindex, Agentindex,10)
        WLS_Actual=Ppage.get_anyKPIofAgent_OM_doubleKPI(TLindex, Agentindex,11)
        WLS_Attain=Ppage.get_anyKPIofAgent_OM(TLindex, Agentindex,12)
        Achiev=Ppage.get_anyKPIofAgent_OM(TLindex, Agentindex,13)

        Agent_KPI={"NetRevenue_Actual":NetRevenue_Actual,"NetRevenue_Attain":NetRevenue_Attain,"HSIAIPDSL_Actual":HSIAIPDSL_Actual,
                  "HSIAIPDSL_Attain":HSIAIPDSL_Attain,"CRFT_Actual":CRFT_Actual,"CRFT_Attain":CRFT_Attain,
                  "OpsAht":OpsAht,"VOIP_Actual":VOIP_Actual,"VOIP_Attain":VOIP_Attain,"WLS_Actual":WLS_Actual,"WLS_Attain":WLS_Attain,
                  "Achiev":Achiev}
        for key in Agent_KPI:
            if '\n' in Agent_KPI[key][0]:
                Agent_KPI[key][0]=Agent_KPI[key][0].split('\n')
                Agent_KPI[key][0][1]=Agent_KPI[key][0][1].replace('(','').replace(')','')
        return Agent_KPI
    
    def get_SPANISH_TL_KPI_Actual(self,TLindex):
        Ppage=PerformancePage()
        a=Ppage.get_anyKPIofTL_doubleKPI(TLindex,2)[0].replace("$","")
        b=Ppage.get_anyKPIofTL_doubleKPI(TLindex,2)[1].replace("$","")
        NetRevenue_Actual=[a,b]
        NetRevenue_Attain=Ppage.get_anyKPIofTL(TLindex,3)
        HSIAIPDSL_Actual=Ppage.get_anyKPIofTL_doubleKPI(TLindex,4)
        HSIAIPDSL_Attain=Ppage.get_anyKPIofTL(TLindex,5)
        CRFT_Actual=Ppage.get_anyKPIofTL(TLindex,6)
        CRFT_Attain=Ppage.get_anyKPIofTL(TLindex,7)
        OpsAht=Ppage.get_anyKPIofTL(TLindex,8)
        VOIP_Actual=Ppage.get_anyKPIofTL_doubleKPI(TLindex,9)
        VOIP_Attain=Ppage.get_anyKPIofTL(TLindex,10)
        WLS_Actual=Ppage.get_anyKPIofTL_doubleKPI(TLindex,11)
        WLS_Attain=Ppage.get_anyKPIofTL(TLindex,12)
        Achiev=Ppage.get_anyKPIofTL(TLindex,13)
        
        Agent_KPI={"NetRevenue_Actual":NetRevenue_Actual,"NetRevenue_Attain":NetRevenue_Attain,"HSIAIPDSL_Actual":HSIAIPDSL_Actual,
                  "HSIAIPDSL_Attain":HSIAIPDSL_Attain,"CRFT_Actual":CRFT_Actual,"CRFT_Attain":CRFT_Attain,
                  "OpsAht":OpsAht,"VOIP_Actual":VOIP_Actual,"VOIP_Attain":VOIP_Attain,"WLS_Actual":WLS_Actual,"WLS_Attain":WLS_Attain,
                  "Achiev":Achiev}
        
        for key in Agent_KPI:
            if '\n' in Agent_KPI[key][0]:
                Agent_KPI[key][0]=Agent_KPI[key][0].split('\n')
                Agent_KPI[key][0][1]=Agent_KPI[key][0][1].replace('(','').replace(')','')
        #value=Agent_KPI["NetRevenue_Actual"][0][0]
        #Agent_KPI["NetRevenue_Actual"][0][0]=self.float_convert(value)
        
        return Agent_KPI
    
        
        
        
    
    
    def get_SPANISH_AgentKPI_Agent_Actual(self):
        Ppage=PerformancePage()
        a=Ppage.get_anyKPIofAgent_Agent(2)[0].replace("$","")
        b=Ppage.get_anyKPIofAgent_Agent(2)[1].replace("$","")
        NetRevenue_Actual=[a,b]
        NetRevenue_Attain=Ppage.get_anyKPIofAgent_Agent(3)
        HSIAIPDSL_Actual=Ppage.get_anyKPIofAgent_Agent(4)
        HSIAIPDSL_Attain=Ppage.get_anyKPIofAgent_Agent(5)
        CRFT_Actual=Ppage.get_anyKPIofAgent_Agent(6)
        CRFT_Attain=Ppage.get_anyKPIofAgent_Agent(7)
        OpsAht=Ppage.get_anyKPIofAgent_Agent(8)
        VOIP_Actual=Ppage.get_anyKPIofAgent_Agent(9)
        VOIP_Attain=Ppage.get_anyKPIofAgent_Agent(10)
        WLS_Actual=Ppage.get_anyKPIofAgent_Agent(11)
        WLS_Attain=Ppage.get_anyKPIofAgent_Agent(12)
        Achiev=Ppage.get_anyKPIofAgent_Agent(13)
        
        Agent_KPI={"NetRevenue_Actual":NetRevenue_Actual,"NetRevenue_Attain":NetRevenue_Attain,"HSIAIPDSL_Actual":HSIAIPDSL_Actual,
                  "HSIAIPDSL_Attain":HSIAIPDSL_Attain,"CRFT_Actual":CRFT_Actual,"CRFT_Attain":CRFT_Attain,
                  "OpsAht":OpsAht,"VOIP_Actual":VOIP_Actual,"VOIP_Attain":VOIP_Attain,"WLS_Actual":WLS_Actual,"WLS_Attain":WLS_Attain,
                  "Achiev":Achiev}
        for key in Agent_KPI:
            if '\n' in Agent_KPI[key][0]:
                Agent_KPI[key][0]=Agent_KPI[key][0].split('\n')
                Agent_KPI[key][0][1]=Agent_KPI[key][0][1].replace('(','').replace(')','')
        return Agent_KPI
    
    def get_SPANISH_AgentKPI_TL_Actual(self,Agentindex):
        Ppage=PerformancePage()
        a=Ppage.get_anyKPIofAgent_TL_doubleKPI(Agentindex, 2)[0].replace("$","")
        b=Ppage.get_anyKPIofAgent_TL_doubleKPI(Agentindex, 2)[1].replace("$","")
        NetRevenue_Actual=[a,b]
        NetRevenue_Attain=Ppage.get_anyKPIofAgent_TL(Agentindex, 3)
        HSIAIPDSL_Actual=Ppage.get_anyKPIofAgent_TL_doubleKPI(Agentindex, 4)
        HSIAIPDSL_Attain=Ppage.get_anyKPIofAgent_TL(Agentindex, 5)
        CRFT_Actual=Ppage.get_anyKPIofAgent_TL(Agentindex, 6)
        CRFT_Attain=Ppage.get_anyKPIofAgent_TL(Agentindex, 7)
        OpsAht=Ppage.get_anyKPIofAgent_TL(Agentindex, 8)
        VOIP_Actual=Ppage.get_anyKPIofAgent_TL_doubleKPI(Agentindex, 9)
        VOIP_Attain=Ppage.get_anyKPIofAgent_TL(Agentindex, 10)
        WLS_Actual=Ppage.get_anyKPIofAgent_TL_doubleKPI(Agentindex, 11)
        WLS_Attain=Ppage.get_anyKPIofAgent_TL(Agentindex, 12)
        Achiev=Ppage.get_anyKPIofAgent_TL(Agentindex, 13)

        Agent_KPI={"NetRevenue_Actual":NetRevenue_Actual,"NetRevenue_Attain":NetRevenue_Attain,"HSIAIPDSL_Actual":HSIAIPDSL_Actual,
                  "HSIAIPDSL_Attain":HSIAIPDSL_Attain,"CRFT_Actual":CRFT_Actual,"CRFT_Attain":CRFT_Attain,
                  "OpsAht":OpsAht,"VOIP_Actual":VOIP_Actual,"VOIP_Attain":VOIP_Attain,"WLS_Actual":WLS_Actual,"WLS_Attain":WLS_Attain,
                  "Achiev":Achiev}
        for key in Agent_KPI:
            if '\n' in Agent_KPI[key][0]:
                Agent_KPI[key][0]=Agent_KPI[key][0].split('\n')
                Agent_KPI[key][0][1]=Agent_KPI[key][0][1].replace('(','').replace(')','')
        return Agent_KPI
    '''
    def float_convert(self,value):
        if len(value.split(".")[1])==3 and value[len(value)-1]=='5':
            if value[len(value)-2]=='9' and value[len(value)-3]=='9':
                convert_value=str(int(value.split(".")[0])+1)
            elif value[len(value)-2]=='9' and value[len(value)-3]!='9':
                value[len(value)-3]=str(int(value[len(value)-3])+1)
                convert_value=value.split(".")[0]+'.'+value[len(value)-2]+value[len(value)-3]
            elif value[len(value)-2]!='9' and value[len(value)-3]=='9':
                value[len(value)-2]=str(int(value[len(value)-2])+1)
                convert_value=value.split(".")[0]+'.'+value[len(value)-2]
        else:
            a=float(value)
            b=round(a,2)
            c=str(b)
            d=c.split(".")
            if len(d[1])==1 and d[1]=='0':
                convert_value=d[0]
            else:
                convert_value=c
        return convert_value'''
        