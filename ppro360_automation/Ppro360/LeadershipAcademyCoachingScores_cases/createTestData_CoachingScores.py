'''

@author: yanbin.shu
'''
import unittest
import MySQLdb
from datetime import datetime,timedelta  
import xlrd
import os
from public_method.Get_configration_data import Get_configration_data

class createTestData_CoachingScores(unittest.TestCase):


    def setUp(self):
        self.configrationfilename='configration.xlsx'
        self.caseID='createTestData_CoachingScores'
        self.CASE_LOBSITEsheetname="CASE-LOBSITE"
         
        self.planned='0'
        self.ongoing='3'
        self.completed='1'
        self.acknowledged='4'
        self.cancelled='2'
        self.uffbackID='45'
        
        GetData=Get_configration_data()
        #Get AWS LOBs
        self.AWSLOBs_list=GetData.get_AWSLOBs_list()
        #Get VXI LOBs
        self.VXILOBs_list=GetData.get_VXILOBs_list()
        #Get AWS hostindex
        self.AWS_hostname=GetData.get_StageNodeHost(93)
        #Get VXI hostindex
        self.VXI_hostname=GetData.get_StageNodeHost(92)
       

    def tearDown(self):
        pass


    def testName(self):
        now=datetime.now()
        sixmonthAgotime=now-timedelta(days=190)
        fivemonthAgotime=now-timedelta(days=150)
        threemonthAgotime=now-timedelta(days=90)
        yesterday=now-timedelta(days=1)
        
        self.sixmonthAgo_time=sixmonthAgotime.strftime('%Y-%m-%d %H:%M:%S')
        self.fivemonthAgo_time=fivemonthAgotime.strftime('%Y-%m-%d %H:%M:%S')
        self.threemonthAgo_time=threemonthAgotime.strftime('%Y-%m-%d %H:%M:%S')
        self.yesterday_time=yesterday.strftime('%Y-%m-%d %H:%M:%S')
        self.deadlinetime=now.strftime('%Y-%m-%d %H:%M:%S')
        #print self.sixmonthAgo_time,self.fivemonthAgo_time,self.threemonthAgo_time,self.yesterday_time,self.deadlinetime
        self.testLOBSITE_list=self.get_LOBSITETest(self.caseID)
        for i in range(0,len(self.testLOBSITE_list)):
            Flag=self.get_LOBSITESTATUS(self.testLOBSITE_list[i])
            if Flag==True:
                each_LOBSITE=self.testLOBSITE_list[i].split(":")
                lobname=each_LOBSITE[0]
                
                #Get hostindex: AWS OR VXI
                if lobname in self.AWSLOBs_list:
                    hostname=self.AWS_hostname
                elif lobname in self.VXILOBs_list:
                    hostname=self.VXI_hostname
                #Get hostindex: AWS OR VXI
                
                #Get Site to test
                site_list=each_LOBSITE[1].split("*")
                for n in range(0,len(site_list)):
                    sitename=site_list[n]
                    print "lobname,sitename=",(lobname, sitename)
                    database_name=self.Get_Database_Name(lobname, sitename) 
                    print 'databaseName= ', database_name
                    
                    print hostname
           
                    conn=MySQLdb.connect(host=hostname,user='normal',passwd='A3EDD019E341B5A124986FEAF78F20C7',db=database_name)
                    cur=conn.cursor()
                    self.sql_TL="SELECT rt.hr_id tl_hr_id,rtl.history_id,rtl.firstname tl_first_name,rtl.lastname \
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
                    self.data_list=[]
                    self.TL=[]
                    self.number=cur.execute(self.sql_TL)
                #   print number
                    self.data=cur.fetchall()
                    self.data_list.append(self.number)
                    self.data_list.append(self.data)
                    print "TL list= " , self.data_list
                    
                        
                #   print data_list[0],data_list[1][0][0],data_list[1][1][0]
                    if self.number<3 :
                        print "Must have three TLs, but actually only has :", self.number
                    else:
                        for i in range(0,self.number):
                            self.tlID=self.data_list[1][i][0]
                            self.TL.append(self.tlID)
                        print "get TLs=" ,self.TL
                #       print TL[1]
                        self.historyID=str(self.data_list[1][0][1])
                        print "historyID= ", self.historyID
                        
                    self.sql_agents="select r.* from roster r join upload_history up on r.history_id=up.id where up.active_time=( \
                                    SELECT MAX(active_time)\
                                    FROM upload_history \
                                    WHERE TYPE='2' AND DATE(data_date)<=now()) and r.hr_id not in (select hr_id from roster_teamleaders where history_id=(SELECT id FROM upload_history uh\
                                    WHERE TYPE='2' AND uh.active_time=(\
                                    SELECT MAX(active_time)\
                                    FROM upload_history\
                                    WHERE TYPE='2' AND DATE(data_date)<=now()))) and r.team_id is not null  order by r.firstname,r.lastname asc;"
                    self.agent_list=[]
                    self.Agents=[]
                    self.numberAgent=cur.execute(self.sql_agents)
                    self.dataAgent=cur.fetchall()
                    self.agent_list.append(self.numberAgent)
                    self.agent_list.append(self.dataAgent) 
                    print "Agents list= " , self.agent_list   
                    if self.numberAgent<17:
                        print  "there is no 18 agents, total agents is ", self.numberAgent
                    else:
                        for j in range(0,self.numberAgent):
                            self.agentID=self.agent_list[1][j][0]
                            self.Agents.append(self.agentID)
                             
                        print "get agents= ",self.Agents
                               
                #       insert data of form 'Plan For Success Process Confirmation': 2 acknowledged, 1 planned,1 cancel
                        self.planForm_insert_validRecords(cur)
                        self.planForm_insert_Records6monthsAgo(cur)       
                     
                    conn.autocommit(True)
                    conn.close()
        
    def planForm_insert_validRecords(self,cur):
        # agent[0]:
        pfspcoach_sql1="insert into coach (acknowledge_time,cancel_time,completed_time,created_time,deadline,history_id,hr_id,kpi_json_str,sn,status,type,assign_to_id,classification) values ('"+self.fivemonthAgo_time+"',null,'"+self.fivemonthAgo_time+"','"+self.fivemonthAgo_time+"','"+self.deadlinetime+"','"+self.historyID+"','"+self.Agents[0]+"','{}','Auto-ScriptIinsert_notForManualTest',"+self.acknowledged+","+self.uffbackID+",66776677,0);"
        sql2="select LAST_INSERT_ID();"
        cur.execute(pfspcoach_sql1)
        cur.execute(sql2)
        data=cur.fetchall()
        #print "sql2= ", data
        coachID=str(data[0][0])
        print "unified form acknowledged coachID1= ", coachID
        pfspcoach_sql3="insert into uffcoach (greet,introduce,attitude,points1,understand,listen,ownership,points2,offer,resolution,maintain,points3,reinforce,overcome,confirm,points4,educate,expectation,changes,points5,appreciation,goodbye,points6,totalpoints,coach_id) values (null,1,null,3,null,null,null,0,null,1,null,7,1,1,null,17,null,1,1,13,null,1,3,43,"+ coachID+ ");"
        cur.execute(pfspcoach_sql3)
        
        pfspcoach_sql1="insert into coach (acknowledge_time,cancel_time,completed_time,created_time,deadline,history_id,hr_id,kpi_json_str,sn,status,type,assign_to_id,classification) values (null,null,'"+self.yesterday_time+"','"+self.yesterday_time+"','"+self.deadlinetime+"','"+self.historyID+"','"+self.Agents[0]+"','{}','Auto-ScriptIinsert_notForManualTest',"+self.completed+","+self.uffbackID+",66776677,0);"
        sql2="select LAST_INSERT_ID();"
        cur.execute(pfspcoach_sql1)
        cur.execute(sql2)
        data=cur.fetchall()
        #print "sql2= ", data 
        coachID=str(data[0][0])
        print "unified form completed coachID1= ", coachID
        pfspcoach_sql3="insert into uffcoach (greet,introduce,attitude,points1,understand,listen,ownership,points2,offer,resolution,maintain,points3,reinforce,overcome,confirm,points4,educate,expectation,changes,points5,appreciation,goodbye,points6,totalpoints,coach_id) values (1,null,null,3,1,null,null,7,null,1,null,7,null,null,null,0,null,null,null,0,null,null,0,17,"+ coachID+ ");"
        cur.execute(pfspcoach_sql3)
        
        
        #agent[1]:
        pfspcoach_sql1="insert into coach (acknowledge_time,cancel_time,completed_time,created_time,deadline,history_id,hr_id,kpi_json_str,sn,status,type,assign_to_id,classification) values ('"+self.threemonthAgo_time+"',null,'"+self.threemonthAgo_time+"','"+self.sixmonthAgo_time+"','"+self.deadlinetime+"','"+self.historyID+"','"+self.Agents[1]+"','{}','Auto-ScriptIinsert_notForManualTest',"+self.acknowledged+","+self.uffbackID+",66776677,0);"
        sql2="select LAST_INSERT_ID();"
        cur.execute(pfspcoach_sql1)
        cur.execute(sql2)
        data=cur.fetchall()
        #print "sql2= ", data
        coachID=str(data[0][0])
        print "unified form acknowledged coachID1= ", coachID
        pfspcoach_sql3="insert into uffcoach (greet,introduce,attitude,points1,understand,listen,ownership,points2,offer,resolution,maintain,points3,reinforce,overcome,confirm,points4,educate,expectation,changes,points5,appreciation,goodbye,points6,totalpoints,coach_id) values (1,1,1,10,1,1,null,13,1,null,null,7,1,0,-1,8,null,1,-1,7,0,-1,0,45,"+ coachID+ ");"
        cur.execute(pfspcoach_sql3)
        
        pfspcoach_sql1="insert into coach (acknowledge_time,cancel_time,completed_time,created_time,deadline,history_id,hr_id,kpi_json_str,sn,status,type,assign_to_id,classification) values ('"+self.yesterday_time+"',null,'"+self.yesterday_time+"','"+self.yesterday_time+"','"+self.deadlinetime+"','"+self.historyID+"','"+self.Agents[1]+"','{}','Auto-ScriptIinsert_notForManualTest',"+self.acknowledged+","+self.uffbackID+",66776677,0);"
        sql2="select LAST_INSERT_ID();"
        cur.execute(pfspcoach_sql1)
        cur.execute(sql2)
        data=cur.fetchall()
        #print "sql2= ", data
        coachID=str(data[0][0])
        print "unified form acknowledged coachID1= ", coachID
        pfspcoach_sql3="insert into uffcoach (greet,introduce,attitude,points1,understand,listen,ownership,points2,offer,resolution,maintain,points3,reinforce,overcome,confirm,points4,educate,expectation,changes,points5,appreciation,goodbye,points6,totalpoints,coach_id) values (null,1,null,3,null,null,null,0,null,1,null,7,1,1,null,17,null,1,1,13,null,1,3,43,"+ coachID+ ");"
        cur.execute(pfspcoach_sql3)
        
        #agent[2]
        pfspcoach_sql1="insert into coach (acknowledge_time,cancel_time,completed_time,created_time,deadline,history_id,hr_id,kpi_json_str,sn,status,type,assign_to_id,classification) values ('"+self.threemonthAgo_time+"',null,'"+self.threemonthAgo_time+"','"+self.fivemonthAgo_time+"','"+self.deadlinetime+"','"+self.historyID+"','"+self.Agents[2]+"','{}','Auto-ScriptIinsert_notForManualTest',"+self.acknowledged+","+self.uffbackID+",66776677,0);"
        sql2="select LAST_INSERT_ID();"
        cur.execute(pfspcoach_sql1)
        cur.execute(sql2)
        data=cur.fetchall()
        #print "sql2= ", data
        coachID=str(data[0][0])
        print "unified form acknowledged coachID1= ", coachID
        pfspcoach_sql3="insert into uffcoach (greet,introduce,attitude,points1,understand,listen,ownership,points2,offer,resolution,maintain,points3,reinforce,overcome,confirm,points4,educate,expectation,changes,points5,appreciation,goodbye,points6,totalpoints,coach_id) values (null,1,null,3,null,null,null,0,null,1,null,7,1,1,null,17,null,1,1,13,null,1,3,43,"+ coachID+ ");"
        cur.execute(pfspcoach_sql3)
        
        pfspcoach_sql1="insert into coach (acknowledge_time,cancel_time,completed_time,created_time,deadline,history_id,hr_id,kpi_json_str,sn,status,type,assign_to_id,classification) values ('"+self.fivemonthAgo_time+"',null,'"+self.fivemonthAgo_time+"','"+self.sixmonthAgo_time+"','"+self.deadlinetime+"','"+self.historyID+"','"+self.Agents[2]+"','{}','Auto-ScriptIinsert_notForManualTest',"+self.acknowledged+","+self.uffbackID+",66776677,0);"
        sql2="select LAST_INSERT_ID();"
        cur.execute(pfspcoach_sql1)
        cur.execute(sql2)
        data=cur.fetchall()
        #print "sql2= ", data
        coachID=str(data[0][0])
        print "unified form acknowledged coachID1= ", coachID
        pfspcoach_sql3="insert into uffcoach (greet,introduce,attitude,points1,understand,listen,ownership,points2,offer,resolution,maintain,points3,reinforce,overcome,confirm,points4,educate,expectation,changes,points5,appreciation,goodbye,points6,totalpoints,coach_id) values (1,1,1,10,1,1,null,13,1,null,null,7,1,0,-1,8,null,1,-1,7,0,-1,0,45,"+ coachID+ ");"
        cur.execute(pfspcoach_sql3)
        
        #agent[3]
        pfspcoach_sql1="insert into coach (acknowledge_time,cancel_time,completed_time,created_time,deadline,history_id,hr_id,kpi_json_str,sn,status,type,assign_to_id,classification) values ('"+self.fivemonthAgo_time+"',null,'"+self.fivemonthAgo_time+"','"+self.fivemonthAgo_time+"','"+self.deadlinetime+"','"+self.historyID+"','"+self.Agents[3]+"','{}','Auto-ScriptIinsert_notForManualTest',"+self.acknowledged+","+self.uffbackID+",66776677,0);"
        sql2="select LAST_INSERT_ID();"
        cur.execute(pfspcoach_sql1)
        cur.execute(sql2)
        data=cur.fetchall()
        #print "sql2= ", data
        coachID=str(data[0][0])
        print "unified form acknowledged coachID1= ", coachID
        pfspcoach_sql3="insert into uffcoach (greet,introduce,attitude,points1,understand,listen,ownership,points2,offer,resolution,maintain,points3,reinforce,overcome,confirm,points4,educate,expectation,changes,points5,appreciation,goodbye,points6,totalpoints,coach_id) values (1,null,null,3,1,1,null,13,null,1,1,13,null,null,null,0,null,null,null,0,null,null,0,29,"+ coachID+ ");"
        cur.execute(pfspcoach_sql3)
        
        #agent[11]
        pfspcoach_sql1="insert into coach (acknowledge_time,cancel_time,completed_time,created_time,deadline,history_id,hr_id,kpi_json_str,sn,status,type,assign_to_id,classification) values ('"+self.yesterday_time+"',null,'"+self.yesterday_time+"','"+self.yesterday_time+"','"+self.deadlinetime+"','"+self.historyID+"','"+self.Agents[11]+"','{}','Auto-ScriptIinsert_notForManualTest',"+self.acknowledged+","+self.uffbackID+",66776677,0);"
        sql2="select LAST_INSERT_ID();"
        cur.execute(pfspcoach_sql1)
        cur.execute(sql2)
        data=cur.fetchall()
        #print "sql2= ", data
        coachID=str(data[0][0])
        print "unified form acknowledged coachID1= ", coachID
        pfspcoach_sql3="insert into uffcoach (greet,introduce,attitude,points1,understand,listen,ownership,points2,offer,resolution,maintain,points3,reinforce,overcome,confirm,points4,educate,expectation,changes,points5,appreciation,goodbye,points6,totalpoints,coach_id) values (1,1,1,10,1,1,null,13,1,null,null,7,1,0,-1,8,null,1,-1,7,0,-1,0,45,"+ coachID+ ");"
        cur.execute(pfspcoach_sql3)
        #agent[12]
        pfspcoach_sql1="insert into coach (acknowledge_time,cancel_time,completed_time,created_time,deadline,history_id,hr_id,kpi_json_str,sn,status,type,assign_to_id,classification) values ('"+self.fivemonthAgo_time+"',null,'"+self.fivemonthAgo_time+"','"+self.fivemonthAgo_time+"','"+self.deadlinetime+"','"+self.historyID+"','"+self.Agents[12]+"','{}','Auto-ScriptIinsert_notForManualTest',"+self.acknowledged+","+self.uffbackID+",66776677,0);"
        sql2="select LAST_INSERT_ID();"
        cur.execute(pfspcoach_sql1)
        cur.execute(sql2)
        data=cur.fetchall()
        #print "sql2= ", data
        coachID=str(data[0][0])
        print "unified form acknowledged coachID1= ", coachID
        pfspcoach_sql3="insert into uffcoach (greet,introduce,attitude,points1,understand,listen,ownership,points2,offer,resolution,maintain,points3,reinforce,overcome,confirm,points4,educate,expectation,changes,points5,appreciation,goodbye,points6,totalpoints,coach_id) values (1,1,1,10,null,1,null,7,null,1,1,13,null,null,1,8,1,null,1,13,null,null,0,51,"+ coachID+ ");"
        cur.execute(pfspcoach_sql3)
        
        #agent[15]
        pfspcoach_sql1="insert into coach (acknowledge_time,cancel_time,completed_time,created_time,deadline,history_id,hr_id,kpi_json_str,sn,status,type,assign_to_id,classification) values ('"+self.yesterday_time+"',null,'"+self.threemonthAgo_time+"','"+self.fivemonthAgo_time+"','"+self.deadlinetime+"','"+self.historyID+"','"+self.Agents[15]+"','{}','Auto-ScriptIinsert_notForManualTest',"+self.acknowledged+","+self.uffbackID+",66776677,0);"
        sql2="select LAST_INSERT_ID();"
        cur.execute(pfspcoach_sql1)
        cur.execute(sql2)
        data=cur.fetchall()
        #print "sql2= ", data
        coachID=str(data[0][0])
        print "unified form acknowledged coachID1= ", coachID
        pfspcoach_sql3="insert into uffcoach (greet,introduce,attitude,points1,understand,listen,ownership,points2,offer,resolution,maintain,points3,reinforce,overcome,confirm,points4,educate,expectation,changes,points5,appreciation,goodbye,points6,totalpoints,coach_id) values (1,1,1,10,1,1,null,13,1,null,null,7,1,0,-1,8,null,1,-1,7,0,-1,0,45,"+ coachID+ ");"
        cur.execute(pfspcoach_sql3)
        
        pfspcoach_sql1="insert into coach (acknowledge_time,cancel_time,completed_time,created_time,deadline,history_id,hr_id,kpi_json_str,sn,status,type,assign_to_id,classification) values (null,null,'"+self.threemonthAgo_time+"','"+self.fivemonthAgo_time+"','"+self.deadlinetime+"','"+self.historyID+"','"+self.Agents[15]+"','{}','Auto-ScriptIinsert_notForManualTest',"+self.completed+","+self.uffbackID+",66776677,0);"
        sql2="select LAST_INSERT_ID();"
        cur.execute(pfspcoach_sql1)
        cur.execute(sql2)
        data=cur.fetchall()
        #print "sql2= ", data
        coachID=str(data[0][0])
        print "unified form completed coachID1= ", coachID
        pfspcoach_sql3="insert into uffcoach (greet,introduce,attitude,points1,understand,listen,ownership,points2,offer,resolution,maintain,points3,reinforce,overcome,confirm,points4,educate,expectation,changes,points5,appreciation,goodbye,points6,totalpoints,coach_id) values (1,null,null,3,1,1,null,13,null,1,1,13,null,null,null,0,null,null,null,0,null,null,0,29,"+ coachID+ ");"
        cur.execute(pfspcoach_sql3)
        
        
        
        #agent[7]
        pfspcoach_sql1="insert into coach (acknowledge_time,cancel_time,completed_time,created_time,deadline,history_id,hr_id,kpi_json_str,sn,status,type,assign_to_id,classification) values ('"+self.fivemonthAgo_time+"',null,'"+self.fivemonthAgo_time+"','"+self.threemonthAgo_time+"','"+self.deadlinetime+"','"+self.historyID+"','"+self.Agents[7]+"','{}','Auto-ScriptIinsert_notForManualTest',"+self.acknowledged+","+self.uffbackID+",66776677,0);"
        sql2="select LAST_INSERT_ID();"
        cur.execute(pfspcoach_sql1)
        cur.execute(sql2)
        data=cur.fetchall()
        #print "sql2= ", data
        coachID=str(data[0][0])
        print "unified form acknowledged coachID1= ", coachID
        pfspcoach_sql3="insert into uffcoach (greet,introduce,attitude,points1,understand,listen,ownership,points2,offer,resolution,maintain,points3,reinforce,overcome,confirm,points4,educate,expectation,changes,points5,appreciation,goodbye,points6,totalpoints,coach_id) values (1,1,1,10,1,1,null,13,1,null,null,7,1,0,-1,8,null,1,-1,7,0,-1,0,45,"+ coachID+ ");"
        cur.execute(pfspcoach_sql3)
        
        pfspcoach_sql1="insert into coach (acknowledge_time,cancel_time,completed_time,created_time,deadline,history_id,hr_id,kpi_json_str,sn,status,type,assign_to_id,classification) values ('"+self.threemonthAgo_time+"',null,'"+self.threemonthAgo_time+"','"+self.fivemonthAgo_time+"','"+self.deadlinetime+"','"+self.historyID+"','"+self.Agents[7]+"','{}','Auto-ScriptIinsert_notForManualTest',"+self.acknowledged+","+self.uffbackID+",66776677,0);"
        sql2="select LAST_INSERT_ID();"
        cur.execute(pfspcoach_sql1)
        cur.execute(sql2)
        data=cur.fetchall()
        #print "sql2= ", data
        coachID=str(data[0][0])
        print "unified form acknowledged coachID1= ", coachID
        pfspcoach_sql3="insert into uffcoach (greet,introduce,attitude,points1,understand,listen,ownership,points2,offer,resolution,maintain,points3,reinforce,overcome,confirm,points4,educate,expectation,changes,points5,appreciation,goodbye,points6,totalpoints,coach_id) values (null,1,null,3,null,null,1,7,null,null,null,0,1,1,null,17,1,null,null,7,null,1,3,37,"+ coachID+ ");"
        cur.execute(pfspcoach_sql3)
        
        
    def planForm_insert_Records6monthsAgo(self,cur):
        #agent[0]
        pfspcoach_sql1="insert into coach (acknowledge_time,cancel_time,completed_time,created_time,deadline,history_id,hr_id,kpi_json_str,sn,status,type,assign_to_id,classification) values ('"+self.fivemonthAgo_time+"',null,'"+self.fivemonthAgo_time+"','"+self.sixmonthAgo_time+"','"+self.deadlinetime+"','"+self.historyID+"','"+self.Agents[0]+"','{}','Auto-ScriptIinsert_notForManualTest',"+self.acknowledged+","+self.uffbackID+",66776677,0);"
        sql2="select LAST_INSERT_ID();"
        cur.execute(pfspcoach_sql1)
        cur.execute(sql2)
        data=cur.fetchall()
        #print "sql2= ", data
        coachID=str(data[0][0])
        print "six months ago,unified form acknowledged coachID1= ", coachID
        pfspcoach_sql3="insert into uffcoach (greet,introduce,attitude,points1,understand,listen,ownership,points2,offer,resolution,maintain,points3,reinforce,overcome,confirm,points4,educate,expectation,changes,points5,appreciation,goodbye,points6,totalpoints,coach_id) values (1,1,1,10,null,1,null,7,null,1,1,13,null,null,1,8,1,null,1,13,null,null,0,51,"+ coachID+ ");"
        cur.execute(pfspcoach_sql3)
        
        pfspcoach_sql1="insert into coach (acknowledge_time,cancel_time,completed_time,created_time,deadline,history_id,hr_id,kpi_json_str,sn,status,type,assign_to_id,classification) values ('"+self.sixmonthAgo_time+"',null,'"+self.sixmonthAgo_time+"','"+self.sixmonthAgo_time+"','"+self.deadlinetime+"','"+self.historyID+"','"+self.Agents[0]+"','{}','Auto-ScriptIinsert_notForManualTest',"+self.acknowledged+","+self.uffbackID+",66776677,0);"
        sql2="select LAST_INSERT_ID();"
        cur.execute(pfspcoach_sql1)
        cur.execute(sql2)
        data=cur.fetchall()
        #print "sql2= ", data
        coachID=str(data[0][0])
        print "six months ago,unified form acknowledged coachID1= ", coachID
        pfspcoach_sql3="insert into uffcoach (greet,introduce,attitude,points1,understand,listen,ownership,points2,offer,resolution,maintain,points3,reinforce,overcome,confirm,points4,educate,expectation,changes,points5,appreciation,goodbye,points6,totalpoints,coach_id) values (null,1,null,3,null,null,1,7,null,null,null,0,1,1,null,17,1,null,null,7,null,1,3,37,"+ coachID+ ");"
        cur.execute(pfspcoach_sql3)
        
        pfspcoach_sql1="insert into coach (acknowledge_time,cancel_time,completed_time,created_time,deadline,history_id,hr_id,kpi_json_str,sn,status,type,assign_to_id,classification) values (null,null,'"+self.threemonthAgo_time+"','"+self.sixmonthAgo_time+"','"+self.deadlinetime+"','"+self.historyID+"','"+self.Agents[0]+"','{}','Auto-ScriptIinsert_notForManualTest',"+self.completed+","+self.uffbackID+",66776677,0);"
        sql2="select LAST_INSERT_ID();"
        cur.execute(pfspcoach_sql1)
        cur.execute(sql2)
        data=cur.fetchall()
        #print "sql2= ", data
        coachID=str(data[0][0])
        print "six months ago,unified form completed coachID1= ", coachID
        pfspcoach_sql3="insert into uffcoach (greet,introduce,attitude,points1,understand,listen,ownership,points2,offer,resolution,maintain,points3,reinforce,overcome,confirm,points4,educate,expectation,changes,points5,appreciation,goodbye,points6,totalpoints,coach_id) values (null,null,1,3,null,null,1,7,null,null,1,7,null,null,null,0,1,1,1,20,1,1,5,42,"+ coachID+ ");"
        cur.execute(pfspcoach_sql3)
        
        pfspcoach_sql1="insert into coach (acknowledge_time,cancel_time,completed_time,created_time,deadline,history_id,hr_id,kpi_json_str,sn,status,type,assign_to_id,classification) values (null,null,'"+self.sixmonthAgo_time+"','"+self.sixmonthAgo_time+"','"+self.deadlinetime+"','"+self.historyID+"','"+self.Agents[0]+"','{}','Auto-ScriptIinsert_notForManualTest',"+self.completed+","+self.uffbackID+",66776677,0);"
        sql2="select LAST_INSERT_ID();"
        cur.execute(pfspcoach_sql1)
        cur.execute(sql2)
        data=cur.fetchall()
        #print "sql2= ", data
        coachID=str(data[0][0])
        print "six months ago,unified form completed coachID1= ", coachID
        pfspcoach_sql3="insert into uffcoach (greet,introduce,attitude,points1,understand,listen,ownership,points2,offer,resolution,maintain,points3,reinforce,overcome,confirm,points4,educate,expectation,changes,points5,appreciation,goodbye,points6,totalpoints,coach_id) values (1,1,1,10,null,1,null,7,null,1,1,13,null,null,1,8,1,null,1,13,null,null,0,51,"+ coachID+ ");"
        cur.execute(pfspcoach_sql3)
        
        pfspcoach_sql1="insert into coach (acknowledge_time,cancel_time,completed_time,created_time,deadline,history_id,hr_id,kpi_json_str,sn,status,type,assign_to_id,classification) values (null,null,null,'"+self.fivemonthAgo_time+"','"+self.deadlinetime+"','"+self.historyID+"','"+self.Agents[0]+"','{}','Auto-ScriptIinsert_notForManualTest',"+self.ongoing+","+self.uffbackID+",66776677,0);"
        sql2="select LAST_INSERT_ID();"
        cur.execute(pfspcoach_sql1)
        cur.execute(sql2)
        data=cur.fetchall()
        #print "sql2= ", data
        coachID=str(data[0][0])
        print ",unified form ongoing coachID1= ", coachID
        pfspcoach_sql3="insert into uffcoach (greet,introduce,attitude,points1,understand,listen,ownership,points2,offer,resolution,maintain,points3,reinforce,overcome,confirm,points4,educate,expectation,changes,points5,appreciation,goodbye,points6,totalpoints,coach_id) values (null,null,null,0,1,1,null,13,null,null,1,7,null,null,1,8,null,null,null,0,null,null,0,28,"+ coachID+ ");"
        cur.execute(pfspcoach_sql3)
        
        
   
        
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