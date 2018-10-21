'''

@author: yanbin.shu
'''
import unittest
import MySQLdb
from datetime import datetime,timedelta  
import xlrd
import os
from public_method import Gl
from public_method.Get_configration_data import Get_configration_data
from public_method.HandleMySQL import HandleMySQL

class createTestData_CoachingScores(unittest.TestCase):


    def setUp(self):
        self.configrationfilename='configration.xlsx'
        self.caseID='createTestData_CoachingScores'
        self.CASE_LOBSITEsheetname="CASE-LOBSITE"
        self.testLOBSITE_list=self.get_LOBSITETest(self.caseID)
         
        self.planned='0'
        self.ongoing='3'
        self.completed='1'
        self.acknowledged='4'
        self.cancelled='2'
        self.uffbackID='45'
        self.dfmbackID='1'
        
        GetData=Get_configration_data()
        #Get AWS LOBs
        self.AWSLOBs_list=GetData.get_AWSLOBs_list()
        #Get VXI LOBs
        self.VXILOBs_list=GetData.get_VXILOBs_list()
        #Get AWS hostindex
        self.AWS_hostname=GetData.get_StageNodeHost(93)
        #Get VXI hostindex
        self.VXI_hostname=GetData.get_StageNodeHost(92)
        
        self.dbuser=GetData.get_StageDatabaseUser()
        self.dbpassword=GetData.get_StageDatabasePassword()
        
        #datetime
        now=datetime.now()
        sixmonthAgotime=now-timedelta(days=190)
        fivemonthAgotime=now-timedelta(days=1)
        threemonthAgotime=now-timedelta(days=90)
        yesterday=now-timedelta(days=1)
        
        self.sixmonthAgo_time=sixmonthAgotime.strftime('%Y-%m-%d %H:%M:%S')
        self.fivemonthAgo_time=fivemonthAgotime.strftime('%Y-%m-%d %H:%M:%S')
        self.acknowledge_time = 'null'
        self.threemonthAgo_time=threemonthAgotime.strftime('%Y-%m-%d %H:%M:%S')
        self.yesterday_time=yesterday.strftime('%Y-%m-%d %H:%M:%S')
        self.deadlinetime=now.strftime('%Y-%m-%d %H:%M:%S')
        print self.sixmonthAgo_time,self.fivemonthAgo_time,self.threemonthAgo_time,self.yesterday_time,self.deadlinetime
        
        #==============Coaching Data====================
        #records number createdate = 20180925
        #self.recordsNumber_Tl1 = {'Agent 1':1,'Agent 2':3,'Agent 3':0,'Agent 4':2,'Agent 5':2,'Agent 6':1,'Agent 7':2,'Agent 8':1,'Agent 9':1,'Agent 10':2,'Agent 11':1}
        #self.recordsNumber_Tl2 = {'Agent 12':2,'Agent 13':2,'Agent 14':1}
        #self.recordsNumber_Tl3 = {'Agent 15':2,'Agent 16':3,'Agent 17':1}
        #self.recordsNumber_L2 = {'Agent 1':1,'Agent 14':1}
        #self.recordsNumber_L3 = {'Agent 1':1,'Agent 14':1,'Agent 17':1}
        #self.coaching_recordsnumber = [self.recordsNumber_Tl1,self.recordsNumber_Tl2,self.recordsNumber_Tl3,self.recordsNumber_L2,self.recordsNumber_L3]
        
        #records number createdate = 20180926
        self.recordsNumber_Tl1 = {'Agent 1':1,'Agent 2':2,'Agent 3':2,'Agent 4':3,'Agent 5':2,'Agent 6':2,'Agent 7':2,'Agent 8':2,'Agent 9':2,'Agent 10':2,'Agent 11':3}
        self.recordsNumber_Tl2 = {'Agent 12':3,'Agent 13':2,'Agent 14':1}
        self.recordsNumber_Tl3 = {'Agent 15':2,'Agent 16':3,'Agent 17':2}
        self.recordsNumber_L2 = {'Agent 1':1,'Agent 14':1}
        self.recordsNumber_L3 = {'Agent 14':1}
        self.coaching_recordsnumber = [self.recordsNumber_Tl1,self.recordsNumber_Tl2,self.recordsNumber_Tl3,self.recordsNumber_L2,self.recordsNumber_L3]
        
        #==============Traid Coaching Data==============
        self.LCuserid = '88888888'
        self.L3userid = '66776677'
        #records number createdate = 20180925
        #self.recordsNumber_LC = {'Tl1':1,'Tl2':2,'Tl3':1}
        #self.recordsNumber_L3 = {'Tl1':1,'Tl2':3,'Tl3':2}
        
        #records number createdate = 20180926
        self.recordsNumber_LC = {'Tl1':2,'Tl2':1,'Tl3':3}
        self.recordsNumber_L3 = {'Tl1':3,'Tl2':3,'Tl3':3}

    def tearDown(self):
        Gl.driver.quit()
        pass
    
    def test_PrepareTraidCoaching(self):
        GetData=Get_configration_data()        

        for i in range(0,len(self.testLOBSITE_list)):
            Flag=self.get_LOBSITESTATUS(self.testLOBSITE_list[i])
            if Flag==True:
                each_LOBSITE=self.testLOBSITE_list[i].split(":")
                lobname=each_LOBSITE[0]
                hostindex=GetData.get_Test_Hostindex(lobname)
                hostname=GetData.get_StageNodeHost(hostindex)
                
                #Get Site to test
                site_list=each_LOBSITE[1].split("*")
                for n in range(0,len(site_list)):
                    sitename=site_list[n]

                    LobSiteDBName=GetData.get_LobSiteDBName(lobname, sitename)
                    lobname_database=LobSiteDBName.get("lobname_database")
                    sitename_database=LobSiteDBName.get("sitename_database")
                        
                    print "lobname,sitename=",(lobname_database, sitename_database)
                    database_name=self.Get_Database_Name(lobname_database, sitename_database) 
                    print 'databaseName= ', database_name
                    
                    print hostname
           
                    conn=MySQLdb.connect(host=hostname,user='normal',passwd='A3EDD019E341B5A124986FEAF78F20C7',db=database_name)
                    cur=conn.cursor()
                    sql_TL="SELECT rt.hr_id tl_hr_id,rtl.history_id,rtl.firstname tl_first_name,rtl.lastname \
                            tl_last_name,rt.team_id as rt_teamID,r.hr_id as agentHRID,rag.firstname as \
                            agentFirstName,rag.lastname as agentLastName \
                            FROM roster_teamleaders rt \
                            JOIN roster rtl ON rt.history_id = rtl.history_id AND rt.hr_id = rtl.hr_id \
                            LEFT JOIN roster r ON rt.history_id=r.history_id AND rt.team_id=r.team_id \
                            JOIN roster rag ON r.history_id = rag.history_id AND r.hr_id = rag.hr_id \
                            WHERE rt.history_id=(\
                            SELECT id FROM upload_history uh \
                            WHERE TYPE='2' AND uh.active_time=(\
                            SELECT MAX(active_time) \
                            FROM upload_history \
                            WHERE TYPE='2' AND DATE(data_date)<=now())) and rt.hr_id=r.hr_id;"
                    execute_sql=cur.execute(sql_TL)
                    TLListDB=cur.fetchall()
                    print TLListDB
                    TLhistoryID=str(TLListDB[0][1])
                    print "historyID= ", TLhistoryID
                    
                    print self.recordsNumber_LC
                    for tl,num in self.recordsNumber_LC.items():
                        for tllist in TLListDB:
                            if tl in tllist:
                                tluserid = tllist[0]
                                print("insert %s coaching %s into coach table"%(self.LCuserid,tluserid))
                                for i in range(num):
                                    self.planFrom_inster_validRecordsCoachrole_1(cur, TLhistoryID,tluserid, self.LCuserid)
                    for tl,num in self.recordsNumber_L3.items():
                        for tllist in TLListDB:
                            if tl in tllist:
                                tluserid = tllist[0]
                                print("insert %s coaching %s into coach table"%(self.L3userid,tluserid))
                                for i in range(num):
                                    self.planFrom_inster_validRecordsCoachrole_1(cur, TLhistoryID,tluserid, self.L3userid) 
                    conn.autocommit(True)
                    conn.close()
                    
    def test_PrepareCoaching(self):
        GetData=Get_configration_data()
        
        for i in range(0,len(self.testLOBSITE_list)):
            Flag=self.get_LOBSITESTATUS(self.testLOBSITE_list[i])
            if Flag==True:
                each_LOBSITE=self.testLOBSITE_list[i].split(":")
                lobname=each_LOBSITE[0]
                hostindex=GetData.get_Test_Hostindex(lobname)
                hostname=GetData.get_StageNodeHost(hostindex)
                
                #Get Site to test
                site_list=each_LOBSITE[1].split("*")
                for n in range(0,len(site_list)):
                    sitename=site_list[n]

                    LobSiteDBName=GetData.get_LobSiteDBName(lobname, sitename)
                    lobname_database=LobSiteDBName.get("lobname_database")
                    sitename_database=LobSiteDBName.get("sitename_database")
                        
                    print "lobname,sitename=",(lobname_database, sitename_database)
                    database_name=self.Get_Database_Name(lobname_database, sitename_database) 
                    print 'databaseName= ', database_name
                    print hostname
           
                    conn=MySQLdb.connect(host=hostname,user='normal',passwd='A3EDD019E341B5A124986FEAF78F20C7',db=database_name)
                    cur=conn.cursor()

                    sql_relationTLAgent = "select re.hr_id agent_id,concat(re.firstname,' ',re.lastname) agentname,rt.hr_id tl_id,ro.firstname,ro.history_id,ro.team_id,ma.Hr_id L2_id,left(ma.firstname,2) L2name from \
                    (select r.* from roster r join upload_history up on r.history_id=up.id where up.active_time=( \
                    SELECT MAX(active_time) FROM upload_history \
                    WHERE TYPE='2' AND DATE(data_date)<=now()) and r.hr_id not in (select hr_id from roster_teamleaders where history_id=(SELECT id FROM upload_history uh \
                    WHERE TYPE='2' AND uh.active_time=(SELECT MAX(active_time) FROM upload_history \
                    WHERE TYPE='2' AND DATE(data_date)<=now()))) and r.team_id is not null  order by r.firstname,r.lastname asc) re \
                    left join roster_teamleaders rt on re.team_id=rt.team_id and re.history_id=rt.history_id \
                    left join roster ro on ro.hr_id=rt.hr_id and ro.history_id=rt.history_id \
                    left join manager m on ro.hr_id=m.Hr_id and m.history_id=ro.history_id \
                    left join manager ma on m.parent_id=ma.id and m.history_id=ma.history_id;"
                    
                    execute_sql=cur.execute(sql_relationTLAgent)
                    TLAgentListDB=cur.fetchall()
                    #The field of TLAgentListDB is (Agent Hrid, Agent name, TLofAgent Hrid, TLname, history_id, team_id, L2ofTL Hrid, L2name)
                    historyID=str(TLAgentListDB[0][4])
                    print "historyID= ", historyID

                    #   print data_list[0],data_list[1][0][0],data_list[1][1][0]
                    if len(TLAgentListDB)!=17:
                        print "Must have three TLs, but actually only has :", len(TLAgentListDB)
                    else:
                        List_Tl1 = []
                        List_Tl2 = []
                        List_Tl3 = []
                        for TLAgentList in TLAgentListDB:
                            if TLAgentList[3] == 'Tl1':
                                List_Tl1.append(TLAgentList[0])
                            elif TLAgentList[3] == 'Tl2':
                                List_Tl2.append(TLAgentList[0])
                            elif TLAgentList[3] == 'Tl3':
                                List_Tl3.append(TLAgentList[0])
                        print "Tl1 list:%s"%List_Tl1
                        print "Tl2 list:%s"%List_Tl2
                        print "Tl3 list:%s"%List_Tl3
                        
                        for recordsNumber in self.coaching_recordsnumber:
                            print recordsNumber
                            for agent,num in recordsNumber.items():
                                for tlagentlist in TLAgentListDB:
                                    if agent in tlagentlist:
                                        tlagentuserid = tlagentlist[0]
                                        tluserid = tlagentlist[2]
                                        print("insert %s coaching %s into coach table"%(self.LCuserid,tluserid))
                                        for i in range(num):
                                            self.planFrom_inster_validRecordsCoachrole_0(cur, historyID,tlagentuserid, tluserid)
                        conn.autocommit(True)
                        conn.close()
                        
    def planFrom_inster_validRecordsCoachrole_0(self,cur,historyID,employee_id,coacher_id,coachrole=str(0)):
        pfspcoach_sql1="insert into coach (acknowledge_time,cancel_time,completed_time,created_time,deadline,history_id,hr_id,kpi_json_str,sn,status,type,assign_to_id,classification) values (null,null,'"+self.fivemonthAgo_time+"','"+self.fivemonthAgo_time+"','"+self.deadlinetime+"','"+historyID+"','"+employee_id+"','{}','Auto-ScriptIinsert_notForManualTest',"+self.completed+","+self.uffbackID+",'"+coacher_id+"','"+coachrole+"');"
        sql2="select LAST_INSERT_ID();"
        cur.execute(pfspcoach_sql1)
        cur.execute(sql2)
        data=cur.fetchall()
        #print "sql2= ", data
        coachID=str(data[0][0])
        print "unified form acknowledged coachID1= ", coachID
        pfspcoach_sql3="insert into uffcoach (greet,introduce,attitude,points1,understand,listen,ownership,points2,offer,resolution,maintain,points3,reinforce,overcome,confirm,points4,educate,expectation,changes,points5,appreciation,goodbye,points6,totalpoints,coach_id) values (null,1,null,3,null,null,null,0,null,1,null,7,1,1,null,17,null,1,1,13,null,1,3,43,"+ coachID+ ");"
        cur.execute(pfspcoach_sql3)
    def planFrom_inster_validRecordsCoachrole_1(self,cur,historyID, employee_id, coacher_id, coachrole=str(1)):
        pfspcoach_sql1="insert into coach (acknowledge_time,cancel_time,completed_time,created_time,deadline,history_id,hr_id,kpi_json_str,sn,status,type,assign_to_id,classification) values (null,null,'"+self.fivemonthAgo_time+"','"+self.fivemonthAgo_time+"','"+self.deadlinetime+"','"+historyID+"','"+employee_id+"','{}','Auto-ScriptIinsert_notForManualTest',"+self.completed+","+self.dfmbackID+",'"+coacher_id+"','"+coachrole+"');"
        sql2="select LAST_INSERT_ID();"
        cur.execute(pfspcoach_sql1)
        cur.execute(sql2)        
        data=cur.fetchall()
        #print "sql2= ", data
        coachID=str(data[0][0])
        print "DFM= ", coachID
        #pfspcoach_sql3="insert into dfmcoach (greet,introduce,attitude,points1,understand,listen,ownership,points2,offer,resolution,maintain,points3,reinforce,overcome,confirm,points4,educate,expectation,changes,points5,appreciation,goodbye,points6,totalpoints,coach_id) values (null,1,null,3,null,null,null,0,null,1,null,7,1,1,null,17,null,1,1,13,null,1,3,43,"+ coachID+ ");"
        #cur.execute(pfspcoach_sql3)'''
   
        
    def get_LOBSITETest(self,caseID):
        #TestLOBSITE_title=caseID+"_LOBSITE"
        TestLOBSITE_inExcel=caseID
        print "****",
        print TestLOBSITE_inExcel,
        print "****"
        print self.get_data_needed(self.CASE_LOBSITEsheetname, TestLOBSITE_inExcel)
        LOBSITElist=self.get_data_needed(self.CASE_LOBSITEsheetname, TestLOBSITE_inExcel).split(",")
        return LOBSITElist 
    
    def get_LOBSITESTATUS(self,lobsitestring):
        Flag=True
        if lobsitestring=="":#No any configuration for LOB-SITE in LOB-SITE sheet
            print "!!!There is empty for LOBSITE configuration!!!Pleach check out it!!!"
            Flag=False
        elif ":" not in lobsitestring:#The format of LOB-SITE is not correct in LOB-SITE sheet
            print "!!!The format is not correct for LOB-site!!!Pleach check out it!!!"
            Flag=False
        else:
            lobsite_list=lobsitestring.split(":")
            if lobsite_list[0]=="":#No lob is set in LOB-SITE sheet
                print "!!!There is no any lob for test, please check out it!!!"
                Flag=False
            elif lobsite_list[1]=="":#No site is set in LOB-SITE sheet
                print "!!!There is no any site for test, please check out it!!!"
                Flag=False
        return Flag
    def get_data_needed(self,sheetname,testitem):  
      
        Configurationfile=self.Get_projectaddress()+self.configrationfilename
        Cdata=xlrd.open_workbook(Configurationfile)
        table = Cdata.sheet_by_name(sheetname)
        nrows=table.nrows
        for i in range(0,nrows):
            item=table.row_values(i)[0]
            if item == testitem:
                dataneeded1=table.row_values(i)[1]
        return dataneeded1    
    
    def Get_Database_Name(self,lobname,sitename):
        A=lobname.lower().replace(" ","")
        B=sitename.lower().replace("-","").replace(" ","")
        DatabaseName=A+"_"+B
        return DatabaseName  
    
    def Get_projectaddress(self):
        Currentpath= str(os.getcwd())
        Clist=Currentpath.split("\\")
        projectaddress=Currentpath.replace(str(Clist[len(Clist)-1]), '')
        return projectaddress 

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()