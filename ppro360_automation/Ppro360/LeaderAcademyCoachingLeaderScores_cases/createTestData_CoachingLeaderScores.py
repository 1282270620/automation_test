'''

@author: yanbin.shu
'''
import unittest
import MySQLdb
from datetime import datetime,timedelta  
import xlrd
import os
from public_method.Get_configration_data import Get_configration_data

class createTestData_CoachingLeaderScores(unittest.TestCase):


    def setUp(self):
        self.configrationfilename='configration.xlsx'
        self.caseID='createTestData_CoachingLeaderScores'
        self.CASE_LOBSITEsheetname="CASE-LOBSITE"
         
        self.planned='0'
        self.ongoing='3'
        self.completed='1'
        self.acknowledged='4'
        self.cancelled='2'
        self.hotlapFormID='58'
        self.rapidfireFormID='57'
        self.FlyFormID='56'
        self.MGSLeaderFormID='55'
        self.MGSAgentFormID='54'
        self.planFormID='53'
        self.strategicFormID='15'
        
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
        sixmonthAgotime=now-timedelta(days=186)
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
                                 
                #       insert data of form 'Plan For Success Process Confirmation': 2 acknowledged, 1 planned,1 cancel
                        self.planForm_insert(cur)             
                #       Form 'Strategic Alignment Meeting Process Confirmation' : 1 going record, 1 acknowledged    
                        self.strategicForm_insert(cur)              
                #       Monthly Goal Setting - Agent Process Confirmation: 1 completed, 1 acknowledged, 1 canceled              
                        self.MGSAgentForm_insert(cur)
            #           Monthly Goal Setting - Leader Process Confirmation:1 acknowledged, 1 completed
                        self.MGSLeaderForm_insert(cur)
                 
            #           On the Fly Process Confirmation:1 ongoing, 2 acknowledged,1 canceled (total score>0)
                        self.onTheFlyForm_insert(cur)         
                
            #           Form: Rapid Fire Process Confirmation : 1 planned, 1 ongoing, 2 acknowledged,1 canceled,1 completed
                        self.rapidFireForm_insert(cur)
                       
            #           Form: Hot Lap Process Confirmation:  1 planned, 1 ongoing, 2 acknowledged,1 canceled
                        self.hotlapsForm_insert(cur)    
#                     
                    conn.autocommit(True)
                    conn.close()
        
    def planForm_insert(self,cur):
        pfspcoach_sql1="insert into coach (acknowledge_time,cancel_time,completed_time,created_time,deadline,history_id,hr_id,kpi_json_str,sn,status,type,assign_to_id,classification) values ('"+self.fivemonthAgo_time+"',null,'"+self.fivemonthAgo_time+"','"+self.sixmonthAgo_time+"','"+self.deadlinetime+"','"+self.historyID+"','"+self.TL[0]+"','{}','Auto-ScriptIinsert_notForManualTest',"+self.acknowledged+","+self.planFormID+",66776677,1);"
        sql2="select LAST_INSERT_ID();"
        cur.execute(pfspcoach_sql1)
        cur.execute(sql2)
        data=cur.fetchall()
        #print "sql2= ", data
        coachID=str(data[0][0])
        print "plan form acknowledged coachID1= ", coachID
        pfspcoach_sql3="insert into pfspcoach (action1,action2,action3,action4,action5,action6,overall,coach_id) values (2,3,null,null,null,null,2.5, "+ coachID+ ");"
        cur.execute(pfspcoach_sql3)
        
        pfspcoach_sql1="insert into coach (acknowledge_time,cancel_time,completed_time,created_time,deadline,history_id,hr_id,kpi_json_str,sn,status,type,assign_to_id,classification) values ('"+self.fivemonthAgo_time+"',null,'"+self.fivemonthAgo_time+"','"+self.sixmonthAgo_time+"','"+self.deadlinetime+"','"+self.historyID+"','"+self.TL[0]+"','{}','Auto-ScriptIinsert_notForManualTest',"+self.acknowledged+","+self.planFormID+",66776677,1);"
        sql2="select LAST_INSERT_ID();"
        cur.execute(pfspcoach_sql1)
        cur.execute(sql2)
        data=cur.fetchall()
        #print "sql2= ", data
        coachID=str(data[0][0])
        print "plan form acknowledged coachID2= ", coachID
        pfspcoach_sql3="insert into pfspcoach (action1,action2,action3,action4,action5,action6,overall,coach_id) values (2,3,null,null,3,3,2.75, "+ coachID+ ");"
        cur.execute(pfspcoach_sql3)
        
        pfspcoach_sql1="insert into coach (acknowledge_time,cancel_time,completed_time,created_time,deadline,history_id,hr_id,kpi_json_str,sn,status,type,assign_to_id,classification) values ('"+self.sixmonthAgo_time+"',null,'"+self.sixmonthAgo_time+"','"+self.sixmonthAgo_time+"','"+self.deadlinetime+"','"+self.historyID+"','"+self.TL[0]+"','{}','Auto-ScriptIinsert_notForManualTest',"+self.acknowledged+","+self.planFormID+",66776677,1);"
        sql2="select LAST_INSERT_ID();"
        cur.execute(pfspcoach_sql1)
        cur.execute(sql2)
        data=cur.fetchall()
        #print "sql2= ", data
        coachID=str(data[0][0])
        print "plan form acknowledged coachID2= ", coachID
        pfspcoach_sql3="insert into pfspcoach (action1,action2,action3,action4,action5,action6,overall,coach_id) values (3,3,2,3,3,2,2.67, "+ coachID+ ");"
        cur.execute(pfspcoach_sql3)
        
        
          
        pfspcoach_sql1="insert into coach (acknowledge_time,cancel_time,completed_time,created_time,deadline,history_id,hr_id,kpi_json_str,sn,status,type,assign_to_id,classification) values ('"+self.fivemonthAgo_time+"',null,'"+self.fivemonthAgo_time+"','"+self.fivemonthAgo_time+"','"+self.deadlinetime+"','"+self.historyID+"','"+self.TL[1]+"','{}','Auto-ScriptIinsert_notForManualTest',"+self.acknowledged+","+self.planFormID+",66776677,1);"
        sql2="select LAST_INSERT_ID();"
        cur.execute(pfspcoach_sql1)
        cur.execute(sql2)
        data=cur.fetchall()
        #print "sql2= ", data
        coachID=str(data[0][0])
        print "plan form acknowledged coachID3= ", coachID
        pfspcoach_sql3="insert into pfspcoach (action1,action2,action3,action4,action5,action6,overall,coach_id) values (2,3,null,2,null,null,2.33, "+ coachID+ ");"
        cur.execute(pfspcoach_sql3)
        
        pfspcoach_sql1="insert into coach (acknowledge_time,cancel_time,completed_time,created_time,deadline,history_id,hr_id,kpi_json_str,sn,status,type,assign_to_id,classification) values ('"+self.fivemonthAgo_time+"',null,'"+self.fivemonthAgo_time+"','"+self.fivemonthAgo_time+"','"+self.deadlinetime+"','"+self.historyID+"','"+self.TL[0]+"','{}','Auto-ScriptIinsert_notForManualTest',"+self.acknowledged+","+self.planFormID+",66776677,1);"
        sql2="select LAST_INSERT_ID();"
        cur.execute(pfspcoach_sql1)
        cur.execute(sql2)
        data=cur.fetchall()
        #print "sql2= ",data
        coachID=str(data[0][0])
        print "plan form acknowledged coachID4= ", coachID
        pfspcoach_sql3="insert into pfspcoach (action1,action2,action3,action4,action5,action6,overall,coach_id) values (1,2,2,3,3,2,2.17, "+ coachID+ ");"
        cur.execute(pfspcoach_sql3)
        
        pfspcoach_sql1="insert into coach (acknowledge_time,cancel_time,completed_time,created_time,deadline,history_id,hr_id,kpi_json_str,sn,status,type,assign_to_id,classification) values ('"+self.fivemonthAgo_time+"',null,'"+self.fivemonthAgo_time+"','"+self.fivemonthAgo_time+"','"+self.deadlinetime+"','"+self.historyID+"','"+self.TL[2]+"','{}','Auto-ScriptIinsert_notForManualTest',"+self.acknowledged+","+self.planFormID+",66776677,1);"
        sql2="select LAST_INSERT_ID();"
        cur.execute(pfspcoach_sql1)
        cur.execute(sql2)
        data=cur.fetchall()
        #print "sql2= ",data
        coachID=str(data[0][0])
        print "plan form acknowledged coachID4= ", coachID
        pfspcoach_sql3="insert into pfspcoach (action1,action2,action3,action4,action5,action6,overall,coach_id) values (1,2,2,3,3,2,2.17, "+ coachID+ ");"
        cur.execute(pfspcoach_sql3)
        
            
        pfspcoach_sql6="insert into coach (acknowledge_time,cancel_time,completed_time,created_time,deadline,history_id,hr_id,kpi_json_str,sn,status,type,assign_to_id,classification) values (null,null,null,'"+self.fivemonthAgo_time+"','"+self.deadlinetime+"','"+self.historyID+"','"+self.TL[0]+"','{}','Auto-ScriptIinsert_notForManualTest',"+self.planned+","+self.planFormID+",66776677,1);"
        cur.execute(pfspcoach_sql6)
        sql2="select LAST_INSERT_ID();"
        cur.execute(sql2)
        data=cur.fetchall()
        coachID=str(data[0][0])
        print "plan form planned coachID5= ", coachID
        
        pfspcoach_sql8="insert into coach (acknowledge_time,cancel_time,completed_time,created_time,deadline,history_id,hr_id,kpi_json_str,sn,status,type,assign_to_id,classification) values (null,'"+self.fivemonthAgo_time+"',null,'"+self.fivemonthAgo_time+"','"+self.deadlinetime+"','"+self.historyID+"','"+self.TL[0]+"','{}','Auto-ScriptIinsert_notForManualTest',"+self.cancelled+","+self.planFormID+",66776677,1);"
        sql2="select LAST_INSERT_ID();"
        cur.execute(pfspcoach_sql8)
        cur.execute(sql2)
        data=cur.fetchall()
        coachID=str(data[0][0])
        print "plan form canceled coachID6= ", coachID
        pfspcoach_sql9="insert into pfspcoach (action1,action2,action3,action4,action5,action6,overall,coach_id) values (1,null,null,3,3,null,2.33, "+ coachID+ ");"
        cur.execute(pfspcoach_sql9) 
    #   print "Plan For Success Process Confirmation form:created."
    
        
        
    def strategicForm_insert(self,cur):
        strategic_sql1="insert into coach (acknowledge_time,cancel_time,completed_time,created_time,deadline,history_id,hr_id,kpi_json_str,sn,status,type,assign_to_id,classification) values (null,null,null,'"+self.fivemonthAgo_time+"','"+self.deadlinetime+"','"+self.historyID+"','"+self.TL[0]+"','{}','Auto-ScriptIinsert_notForManualTest',"+self.ongoing+","+self.strategicFormID+",66776677,1);"
        sql2="select LAST_INSERT_ID();"
        cur.execute(strategic_sql1)
        cur.execute(sql2)
        data=cur.fetchall()
        #print "sql2= ", data
        coachID=str(data[0][0])
        print "strategic_ongoing coachID= ", coachID
        strategic_sql3="insert into strategic_alignment_meeting (score1,score2,score3,score4,score5,score6,score7,overall_score,coach_id) values (null,null,null,3,2,2,null,2.33, "+ coachID+ ");"
        cur.execute(strategic_sql3)
           
        strategic_sql1="insert into coach (acknowledge_time,cancel_time,completed_time,created_time,deadline,history_id,hr_id,kpi_json_str,sn,status,type,assign_to_id,classification) values ('"+self.fivemonthAgo_time+"',null,'"+self.fivemonthAgo_time+"','"+self.fivemonthAgo_time+"','"+self.deadlinetime+"','"+self.historyID+"','"+self.TL[0]+"','{}','Auto-ScriptIinsert_notForManualTest',"+self.acknowledged+","+self.strategicFormID+",66776677,1);"
        sql2="select LAST_INSERT_ID();"
        cur.execute(strategic_sql1)
        cur.execute(sql2)
        data=cur.fetchall()
        #print "sql2= ", data
        coachID=str(data[0][0])
        print "strategic_acknowledged coachID= ", coachID
        strategic_sql3="insert into strategic_alignment_meeting (score1,score2,score3,score4,score5,score6,score7,overall_score,coach_id) values (1,2,3,3,2,1,3,2.14, "+ coachID+ ");"
        cur.execute(strategic_sql3)
        
        strategic_sql1="insert into coach (acknowledge_time,cancel_time,completed_time,created_time,deadline,history_id,hr_id,kpi_json_str,sn,status,type,assign_to_id,classification) values ('"+self.yesterday_time+"',null,'"+self.threemonthAgo_time+"','"+self.fivemonthAgo_time+"','"+self.deadlinetime+"','"+self.historyID+"','"+self.TL[0]+"','{}','Auto-ScriptIinsert_notForManualTest',"+self.acknowledged+","+self.strategicFormID+",66776677,1);"
        sql2="select LAST_INSERT_ID();"
        cur.execute(strategic_sql1)
        cur.execute(sql2)
        data=cur.fetchall()
        #print "sql2= ", data
        coachID=str(data[0][0])
        print "strategic_acknowledged coachID= ", coachID
        strategic_sql3="insert into strategic_alignment_meeting (score1,score2,score3,score4,score5,score6,score7,overall_score,coach_id) values (1,1,3,3,null,1,2,1.83, "+ coachID+ ");"
        cur.execute(strategic_sql3)
        
        
        strategic_sql1="insert into coach (acknowledge_time,cancel_time,completed_time,created_time,deadline,history_id,hr_id,kpi_json_str,sn,status,type,assign_to_id,classification) values ('"+self.fivemonthAgo_time+"',null,'"+self.fivemonthAgo_time+"','"+self.fivemonthAgo_time+"','"+self.deadlinetime+"','"+self.historyID+"','"+self.TL[2]+"','{}','Auto-ScriptIinsert_notForManualTest',"+self.acknowledged+","+self.strategicFormID+",66776677,1);"
        sql2="select LAST_INSERT_ID();"
        cur.execute(strategic_sql1)
        cur.execute(sql2)
        data=cur.fetchall()
        #print "sql2= ", data
        coachID=str(data[0][0])
        print "strategic_acknowledged coachID= ", coachID
        strategic_sql3="insert into strategic_alignment_meeting (score1,score2,score3,score4,score5,score6,score7,overall_score,coach_id) values (1,2,3,3,2,1,3,2.14, "+ coachID+ ");"
        cur.execute(strategic_sql3)
        
        
    def MGSAgentForm_insert(self,cur):
        mgsccoach_sql1="insert into coach (acknowledge_time,cancel_time,completed_time,created_time,deadline,history_id,hr_id,kpi_json_str,sn,status,type,assign_to_id,classification) values ('"+self.yesterday_time+"',null,'"+self.fivemonthAgo_time+"','"+self.fivemonthAgo_time+"','"+self.deadlinetime+"','"+self.historyID+"','"+self.TL[0]+"','{}','Auto-ScriptIinsert_notForManualTest',"+self.acknowledged+","+self.MGSAgentFormID+",66776677,1);"
        sql2="select LAST_INSERT_ID();"
        cur.execute(mgsccoach_sql1)
        cur.execute(sql2)
        data=cur.fetchall()
        coachID=str(data[0][0])
        print "MGS_agent_acknowledged coachID= ", coachID
        mgsccoach_sql3="insert into mgsccoach (accountability_conversation,mgs_goals_reviewed_score,performance_commitments_score,skill_transfer_conducted_score,what_actions_taken_score,what_current_mgs_goals_score,what_examples_shared_score,what_specific_behaviors_score,overall_score,coach_id) values (2,1,2,1,1,3,1,2,1.63, "+ coachID+ ");"
        cur.execute(mgsccoach_sql3)
        
        mgsccoach_sql1="insert into coach (acknowledge_time,cancel_time,completed_time,created_time,deadline,history_id,hr_id,kpi_json_str,sn,status,type,assign_to_id,classification) values ('"+self.fivemonthAgo_time+"',null,'"+self.fivemonthAgo_time+"','"+self.fivemonthAgo_time+"','"+self.deadlinetime+"','"+self.historyID+"','"+self.TL[0]+"','{}','Auto-ScriptIinsert_notForManualTest',"+self.acknowledged+","+self.MGSAgentFormID+",66776677,1);"
        sql2="select LAST_INSERT_ID();"
        cur.execute(mgsccoach_sql1)
        cur.execute(sql2)
        data=cur.fetchall()
        coachID=str(data[0][0])
        print "MGS_agent_acknowledged coachID= ", coachID
        mgsccoach_sql3="insert into mgsccoach (accountability_conversation,mgs_goals_reviewed_score,performance_commitments_score,skill_transfer_conducted_score,what_actions_taken_score,what_current_mgs_goals_score,what_examples_shared_score,what_specific_behaviors_score,overall_score,coach_id) values (3,3,1,2,2,null,3,2,2.29, "+ coachID+ ");"
        cur.execute(mgsccoach_sql3)
        
        
          
        mgsccoach_sql1="insert into coach (acknowledge_time,cancel_time,completed_time,created_time,deadline,history_id,hr_id,kpi_json_str,sn,status,type,assign_to_id,classification) values ('"+self.yesterday_time+"',null,'"+self.fivemonthAgo_time+"','"+self.fivemonthAgo_time+"','"+self.deadlinetime+"','"+self.historyID+"','"+self.TL[1]+"','{}','Auto-ScriptIinsert_notForManualTest',"+self.acknowledged+","+self.MGSAgentFormID+",66776677,1);"
        sql2="select LAST_INSERT_ID();"
        cur.execute(mgsccoach_sql1)
        cur.execute(sql2)
        data=cur.fetchall()
        coachID=str(data[0][0])
        print "MGS_agent_acknowledged coachID= ", coachID
        mgsccoach_sql3="insert into mgsccoach (accountability_conversation,mgs_goals_reviewed_score,performance_commitments_score,skill_transfer_conducted_score,what_actions_taken_score,what_current_mgs_goals_score,what_examples_shared_score,what_specific_behaviors_score,overall_score,coach_id) values (2,1,2,1,1,3,1,2,1.63, "+ coachID+ ");"
        cur.execute(mgsccoach_sql3)
        
        mgsccoach_sql1="insert into coach (acknowledge_time,cancel_time,completed_time,created_time,deadline,history_id,hr_id,kpi_json_str,sn,status,type,assign_to_id,classification) values (null,null,'"+self.fivemonthAgo_time+"','"+self.fivemonthAgo_time+"','"+self.deadlinetime+"','"+self.historyID+"','"+self.TL[0]+"','{}','Auto-ScriptIinsert_notForManualTest',"+self.completed+","+self.MGSAgentFormID+",66776677,1);"
        sql2="select LAST_INSERT_ID();"
        cur.execute(mgsccoach_sql1)
        cur.execute(sql2)
        data=cur.fetchall()
        coachID=str(data[0][0])
        print "MGS_agent_completed coachID= ", coachID
        mgsccoach_sql3="insert into mgsccoach (accountability_conversation,mgs_goals_reviewed_score,performance_commitments_score,skill_transfer_conducted_score,what_actions_taken_score,what_current_mgs_goals_score,what_examples_shared_score,what_specific_behaviors_score,overall_score,coach_id) values (2,1,2,null,null,null,null,null,1.67, "+ coachID+ ");"
        cur.execute(mgsccoach_sql3)
          
        mgsccoach_sql1="insert into coach (acknowledge_time,cancel_time,completed_time,created_time,deadline,history_id,hr_id,kpi_json_str,sn,status,type,assign_to_id,classification) values (null,'"+self.fivemonthAgo_time+"',null,'"+self.fivemonthAgo_time+"','"+self.deadlinetime+"','"+self.historyID+"','"+self.TL[0]+"','{}','Auto-ScriptIinsert_notForManualTest',"+self.cancelled+","+self.MGSAgentFormID+",66776677,1);"
        sql2="select LAST_INSERT_ID();"
        cur.execute(mgsccoach_sql1)
        cur.execute(sql2)
        data=cur.fetchall()
        coachID=str(data[0][0])
        print "MGS_agent_canceled coachID= ", coachID
        mgsccoach_sql3="insert into mgsccoach (accountability_conversation,mgs_goals_reviewed_score,performance_commitments_score,skill_transfer_conducted_score,what_actions_taken_score,what_current_mgs_goals_score,what_examples_shared_score,what_specific_behaviors_score,overall_score,coach_id) values (2,1,null,null,null,null,null,null,1.5, "+ coachID+ ");"
        cur.execute(mgsccoach_sql3)
        

    def MGSLeaderForm_insert(self,cur):
        
        mgslcoach_sql1="insert into coach (acknowledge_time,cancel_time,completed_time,created_time,deadline,history_id,hr_id,kpi_json_str,sn,status,type,assign_to_id,classification) values ('"+self.yesterday_time+"',null,'"+self.threemonthAgo_time+"','"+self.fivemonthAgo_time+"','"+self.deadlinetime+"','"+self.historyID+"','"+self.TL[0]+"','{}','Auto-ScriptIinsert_notForManualTest',"+self.acknowledged+","+self.MGSLeaderFormID+",66776677,1);"
        sql2="select LAST_INSERT_ID();"
        cur.execute(mgslcoach_sql1)
        cur.execute(sql2)
        data=cur.fetchall()
        coachID=str(data[0][0])
        print "MGS_leder acknowledged coachID= ", coachID
        mgslcoach_sql3="insert into mgslcoach (accountability_conversation_score,action_plan_score,discuss_current_sam_goals_score,sam_goals_reviewed_score,specific_behaviors_identified_score,what_actions_taken_score,overall_score,coach_id) values (3,3,1,null,null,null,2.33, "+ coachID+ ");"
        cur.execute(mgslcoach_sql3)
        
        mgslcoach_sql1="insert into coach (acknowledge_time,cancel_time,completed_time,created_time,deadline,history_id,hr_id,kpi_json_str,sn,status,type,assign_to_id,classification) values ('"+self.sixmonthAgo_time+"',null,'"+self.sixmonthAgo_time+"','"+self.sixmonthAgo_time+"','"+self.deadlinetime+"','"+self.historyID+"','"+self.TL[0]+"','{}','Auto-ScriptIinsert_notForManualTest',"+self.acknowledged+","+self.MGSLeaderFormID+",66776677,1);"
        sql2="select LAST_INSERT_ID();"
        cur.execute(mgslcoach_sql1)
        cur.execute(sql2)
        data=cur.fetchall()
        coachID=str(data[0][0])
        print "MGS_leder acknowledged coachID= ", coachID
        mgslcoach_sql3="insert into mgslcoach (accountability_conversation_score,action_plan_score,discuss_current_sam_goals_score,sam_goals_reviewed_score,specific_behaviors_identified_score,what_actions_taken_score,overall_score,coach_id) values (2,3,null,null,3,3,2.75, "+ coachID+ ");"
        cur.execute(mgslcoach_sql3)
        
        mgslcoach_sql1="insert into coach (acknowledge_time,cancel_time,completed_time,created_time,deadline,history_id,hr_id,kpi_json_str,sn,status,type,assign_to_id,classification) values ('"+self.yesterday_time+"',null,'"+self.threemonthAgo_time+"','"+self.fivemonthAgo_time+"','"+self.deadlinetime+"','"+self.historyID+"','"+self.TL[1]+"','{}','Auto-ScriptIinsert_notForManualTest',"+self.acknowledged+","+self.MGSLeaderFormID+",66776677,1);"
        sql2="select LAST_INSERT_ID();"
        cur.execute(mgslcoach_sql1)
        cur.execute(sql2)
        data=cur.fetchall()
        coachID=str(data[0][0])
        print "MGS_leder acknowledged coachID= ", coachID
        mgslcoach_sql3="insert into mgslcoach (accountability_conversation_score,action_plan_score,discuss_current_sam_goals_score,sam_goals_reviewed_score,specific_behaviors_identified_score,what_actions_taken_score,overall_score,coach_id) values (1,2,2,3,1,2,1.83, "+ coachID+ ");"
        cur.execute(mgslcoach_sql3)
        
        mgslcoach_sql1="insert into coach (acknowledge_time,cancel_time,completed_time,created_time,deadline,history_id,hr_id,kpi_json_str,sn,status,type,assign_to_id,classification) values (null,null,'"+self.threemonthAgo_time+"','"+self.fivemonthAgo_time+"','"+self.deadlinetime+"','"+self.historyID+"','"+self.TL[1]+"','{}','Auto-ScriptIinsert_notForManualTest',"+self.completed+","+self.MGSLeaderFormID+",66776677,1);"
        sql2="select LAST_INSERT_ID();"
        cur.execute(mgslcoach_sql1)
        cur.execute(sql2)
        data=cur.fetchall()
        coachID=str(data[0][0])
        print "MGS_leder completed coachID= ", coachID
        mgslcoach_sql3="insert into mgslcoach (accountability_conversation_score,action_plan_score,discuss_current_sam_goals_score,sam_goals_reviewed_score,specific_behaviors_identified_score,what_actions_taken_score,overall_score,coach_id) values (null,2,2,null,1,2,1.75, "+ coachID+ ");"
        cur.execute(mgslcoach_sql3)
    
    
        mgslcoach_sql1="insert into coach (acknowledge_time,cancel_time,completed_time,created_time,deadline,history_id,hr_id,kpi_json_str,sn,status,type,assign_to_id,classification) values ('"+self.yesterday_time+"',null,'"+self.threemonthAgo_time+"','"+self.fivemonthAgo_time+"','"+self.deadlinetime+"','"+self.historyID+"','"+self.TL[2]+"','{}','Auto-ScriptIinsert_notForManualTest',"+self.acknowledged+","+self.MGSLeaderFormID+",66776677,1);"
        sql2="select LAST_INSERT_ID();"
        cur.execute(mgslcoach_sql1)
        cur.execute(sql2)
        data=cur.fetchall()
        coachID=str(data[0][0])
        print "MGS_leder acknowledged coachID= ", coachID
        mgslcoach_sql3="insert into mgslcoach (accountability_conversation_score,action_plan_score,discuss_current_sam_goals_score,sam_goals_reviewed_score,specific_behaviors_identified_score,what_actions_taken_score,overall_score,coach_id) values (1,2,2,3,1,2,1.83, "+ coachID+ ");"
        cur.execute(mgslcoach_sql3)
        
        mgslcoach_sql1="insert into coach (acknowledge_time,cancel_time,completed_time,created_time,deadline,history_id,hr_id,kpi_json_str,sn,status,type,assign_to_id,classification) values ('"+self.yesterday_time+"',null,'"+self.threemonthAgo_time+"','"+self.fivemonthAgo_time+"','"+self.deadlinetime+"','"+self.historyID+"','"+self.TL[2]+"','{}','Auto-ScriptIinsert_notForManualTest',"+self.acknowledged+","+self.MGSLeaderFormID+",66776677,1);"
        sql2="select LAST_INSERT_ID();"
        cur.execute(mgslcoach_sql1)
        cur.execute(sql2)
        data=cur.fetchall()
        coachID=str(data[0][0])
        print "MGS_leder acknowledged coachID= ", coachID
        mgslcoach_sql3="insert into mgslcoach (accountability_conversation_score,action_plan_score,discuss_current_sam_goals_score,sam_goals_reviewed_score,specific_behaviors_identified_score,what_actions_taken_score,overall_score,coach_id) values (1,2,null,3,3,null,2.25, "+ coachID+ ");"
        cur.execute(mgslcoach_sql3)
        
        
           
        
        
    def onTheFlyForm_insert(self,cur):
        ofpccoach_sql1="insert into coach (acknowledge_time,cancel_time,completed_time,created_time,deadline,history_id,hr_id,kpi_json_str,sn,status,type,assign_to_id,classification) values ('"+self.threemonthAgo_time+"',null,'"+self.fivemonthAgo_time+"','"+self.fivemonthAgo_time+"','"+self.deadlinetime+"','"+self.historyID+"','"+self.TL[0]+"','{}','Auto-ScriptIinsert_notForManualTest',"+self.acknowledged+","+self.FlyFormID+",66776677,1);"
        sql2="select LAST_INSERT_ID();"
        cur.execute(ofpccoach_sql1)
        cur.execute(sql2)
        data=cur.fetchall()
        coachID=str(data[0][0])
        print "on the fly_ acknowledged coachID= ", coachID
        ofpccoach_sql3="insert into ofpccoach (actions1rating,actions2rating,actions3rating,actions4rating,actions5rating,actions6rating,actions7rating,results,coach_id) values (2,2,3,3,2,1,3,2.29, "+ coachID+ ");"
        cur.execute(ofpccoach_sql3)
        
        ofpccoach_sql1="insert into coach (acknowledge_time,cancel_time,completed_time,created_time,deadline,history_id,hr_id,kpi_json_str,sn,status,type,assign_to_id,classification) values (null,null,'"+self.yesterday_time+"','"+self.yesterday_time+"','"+self.deadlinetime+"','"+self.historyID+"','"+self.TL[0]+"','{}','Auto-ScriptIinsert_notForManualTest',"+self.completed+","+self.FlyFormID+",66776677,1);"
        sql2="select LAST_INSERT_ID();"
        cur.execute(ofpccoach_sql1)
        cur.execute(sql2)
        data=cur.fetchall()
        coachID=str(data[0][0])
        print "on the fly_ comoleted coachID= ", coachID
        ofpccoach_sql3="insert into ofpccoach (actions1rating,actions2rating,actions3rating,actions4rating,actions5rating,actions6rating,actions7rating,results,coach_id) values (3,2,1,2,null,null,1,1.8, "+ coachID+ ");"
        cur.execute(ofpccoach_sql3)
        
        
        ofpccoach_sql1="insert into coach (acknowledge_time,cancel_time,completed_time,created_time,deadline,history_id,hr_id,kpi_json_str,sn,status,type,assign_to_id,classification) values ('"+self.threemonthAgo_time+"',null,'"+self.fivemonthAgo_time+"','"+self.fivemonthAgo_time+"','"+self.deadlinetime+"','"+self.historyID+"','"+self.TL[1]+"','{}','Auto-ScriptIinsert_notForManualTest',"+self.acknowledged+","+self.FlyFormID+",66776677,1);"
        sql2="select LAST_INSERT_ID();"
        cur.execute(ofpccoach_sql1)
        cur.execute(sql2)
        data=cur.fetchall()
        coachID=str(data[0][0])
        print "on the fly_ acknowledged coachID= ", coachID
        ofpccoach_sql3="insert into ofpccoach (actions1rating,actions2rating,actions3rating,actions4rating,actions5rating,actions6rating,actions7rating,results,coach_id) values (1,2,3,3,1,1,1,1.71, "+ coachID+ ");"
        cur.execute(ofpccoach_sql3)
         
        ofpccoach_sql1="insert into coach (acknowledge_time,cancel_time,completed_time,created_time,deadline,history_id,hr_id,kpi_json_str,sn,status,type,assign_to_id,classification) values ('"+self.threemonthAgo_time+"',null,'"+self.fivemonthAgo_time+"','"+self.fivemonthAgo_time+"','"+self.deadlinetime+"','"+self.historyID+"','"+self.TL[1]+"','{}','Auto-ScriptIinsert_notForManualTest',"+self.acknowledged+","+self.FlyFormID+",66776677,1);"
        sql2="select LAST_INSERT_ID();"
        cur.execute(ofpccoach_sql1)
        cur.execute(sql2)
        data=cur.fetchall()
        coachID=str(data[0][0])
        print "on the fly_ acknowledged coachID= ", coachID
        ofpccoach_sql3="insert into ofpccoach (actions1rating,actions2rating,actions3rating,actions4rating,actions5rating,actions6rating,actions7rating,results,coach_id) values (1,null,3,3,1,null,1,1.8, "+ coachID+ ");"
        cur.execute(ofpccoach_sql3)
        
        ofpccoach_sql1="insert into coach (acknowledge_time,cancel_time,completed_time,created_time,deadline,history_id,hr_id,kpi_json_str,sn,status,type,assign_to_id,classification) values ('"+self.threemonthAgo_time+"',null,'"+self.fivemonthAgo_time+"','"+self.fivemonthAgo_time+"','"+self.deadlinetime+"','"+self.historyID+"','"+self.TL[2]+"','{}','Auto-ScriptIinsert_notForManualTest',"+self.acknowledged+","+self.FlyFormID+",66776677,1);"
        sql2="select LAST_INSERT_ID();"
        cur.execute(ofpccoach_sql1)
        cur.execute(sql2)
        data=cur.fetchall()
        coachID=str(data[0][0])
        print "on the fly_ acknowledged coachID= ", coachID
        ofpccoach_sql3="insert into ofpccoach (actions1rating,actions2rating,actions3rating,actions4rating,actions5rating,actions6rating,actions7rating,results,coach_id) values (1,null,3,3,1,null,1,1.8, "+ coachID+ ");"
        cur.execute(ofpccoach_sql3)
        
            
        ofpccoach_sql1="insert into coach (acknowledge_time,cancel_time,completed_time,created_time,deadline,history_id,hr_id,kpi_json_str,sn,status,type,assign_to_id,classification) values (null,null,null,'"+self.fivemonthAgo_time+"','"+self.deadlinetime+"','"+self.historyID+"','"+self.TL[1]+"','{}','Auto-ScriptIinsert_notForManualTest',"+self.ongoing+","+self.FlyFormID+",66776677,1);"
        sql2="select LAST_INSERT_ID();"
        cur.execute(ofpccoach_sql1)
        cur.execute(sql2)
        data=cur.fetchall()
        coachID=str(data[0][0])
        print "on the fly_ ongoing coachID= ", coachID
        ofpccoach_sql3="insert into ofpccoach (actions1rating,actions2rating,actions3rating,actions4rating,actions5rating,actions6rating,actions7rating,results,coach_id) values (1,null,3,3,1,2,1,1.83, "+ coachID+ ");"
        cur.execute(ofpccoach_sql3)
           
        ofpccoach_sql1="insert into coach (acknowledge_time,cancel_time,completed_time,created_time,deadline,history_id,hr_id,kpi_json_str,sn,status,type,assign_to_id,classification) values (null,'"+self.fivemonthAgo_time+"',null,'"+self.fivemonthAgo_time+"','"+self.deadlinetime+"','"+self.historyID+"','"+self.TL[1]+"','{}','Auto-ScriptIinsert_notForManualTest',"+self.cancelled+","+self.FlyFormID+",66776677,1);"
        sql2="select LAST_INSERT_ID();"
        cur.execute(ofpccoach_sql1)
        cur.execute(sql2)
        data=cur.fetchall()
        coachID=str(data[0][0])
        print "on the fly_ canceled coachID= ", coachID
        ofpccoach_sql3="insert into ofpccoach (actions1rating,actions2rating,actions3rating,actions4rating,actions5rating,actions6rating,actions7rating,results,coach_id) values (1,null,3,3,null,null,null,2.33, "+ coachID+ ");"
        cur.execute(ofpccoach_sql3)      
        
        
    def rapidFireForm_insert(self,cur):
        rfpccoach_sql1="insert into coach (acknowledge_time,cancel_time,completed_time,created_time,deadline,history_id,hr_id,kpi_json_str,sn,status,type,assign_to_id,classification) values ('"+self.yesterday_time+"',null,'"+self.threemonthAgo_time+"','"+self.fivemonthAgo_time+"','"+self.deadlinetime+"','"+self.historyID+"','"+self.TL[0]+"','{}','Auto-ScriptIinsert_notForManualTest',"+self.acknowledged+","+self.rapidfireFormID+",66776677,1);"
        sql2="select LAST_INSERT_ID();"
        cur.execute(rfpccoach_sql1)
        cur.execute(sql2)
        data=cur.fetchall()
        coachID=str(data[0][0])
        print "rapid form_ acknowledged coachID= ", coachID
        rfpccoach_sql3="insert into rfpccoach (actions1rating,actions2rating,actions3rating,actions4rating,actions5rating,actions6rating,actions7rating,actions8rating,results,coach_id) values (1,null,3,3,1,2,1,null,1.83, "+ coachID+ ");"
        cur.execute(rfpccoach_sql3)
        
        rfpccoach_sql1="insert into coach (acknowledge_time,cancel_time,completed_time,created_time,deadline,history_id,hr_id,kpi_json_str,sn,status,type,assign_to_id,classification) values ('"+self.yesterday_time+"',null,'"+self.yesterday_time+"','"+self.yesterday_time+"','"+self.deadlinetime+"','"+self.historyID+"','"+self.TL[0]+"','{}','Auto-ScriptIinsert_notForManualTest',"+self.acknowledged+","+self.rapidfireFormID+",66776677,1);"
        sql2="select LAST_INSERT_ID();"
        cur.execute(rfpccoach_sql1)
        cur.execute(sql2)
        data=cur.fetchall()
        coachID=str(data[0][0])
        print "rapid form_ acknowledged coachID= ", coachID
        rfpccoach_sql3="insert into rfpccoach (actions1rating,actions2rating,actions3rating,actions4rating,actions5rating,actions6rating,actions7rating,actions8rating,results,coach_id) values (3,2,1,3,2,2,3,3,2.38, "+ coachID+ ");"
        cur.execute(rfpccoach_sql3)
        
        rfpccoach_sql1="insert into coach (acknowledge_time,cancel_time,completed_time,created_time,deadline,history_id,hr_id,kpi_json_str,sn,status,type,assign_to_id,classification) values ('"+self.yesterday_time+"',null,'"+self.threemonthAgo_time+"','"+self.fivemonthAgo_time+"','"+self.deadlinetime+"','"+self.historyID+"','"+self.TL[1]+"','{}','Auto-ScriptIinsert_notForManualTest',"+self.acknowledged+","+self.rapidfireFormID+",66776677,1);"
        sql2="select LAST_INSERT_ID();"
        cur.execute(rfpccoach_sql1)
        cur.execute(sql2)
        data=cur.fetchall()
        coachID=str(data[0][0])
        print "rapid form_ acknowledged coachID= ", coachID
        rfpccoach_sql3="insert into rfpccoach (actions1rating,actions2rating,actions3rating,actions4rating,actions5rating,actions6rating,actions7rating,actions8rating,results,coach_id) values (1,2,3,2,2,2,3,3,2.25, "+ coachID+ ");"
        cur.execute(rfpccoach_sql3)
         
        rfpccoach_sql1="insert into coach (acknowledge_time,cancel_time,completed_time,created_time,deadline,history_id,hr_id,kpi_json_str,sn,status,type,assign_to_id,classification) values ('"+self.yesterday_time+"',null,'"+self.yesterday_time+"','"+self.yesterday_time+"','"+self.deadlinetime+"','"+self.historyID+"','"+self.TL[1]+"','{}','Auto-ScriptIinsert_notForManualTest',"+self.acknowledged+","+self.rapidfireFormID+",66776677,1);"
        sql2="select LAST_INSERT_ID();"
        cur.execute(rfpccoach_sql1)
        cur.execute(sql2)
        data=cur.fetchall()
        coachID=str(data[0][0])
        print "rapid form_ acknowledged coachID= ", coachID
        rfpccoach_sql3="insert into rfpccoach (actions1rating,actions2rating,actions3rating,actions4rating,actions5rating,actions6rating,actions7rating,actions8rating,results,coach_id) values (1,2,3,2,2,null,null,3,2.17, "+ coachID+ ");"
        cur.execute(rfpccoach_sql3)
        
        rfpccoach_sql1="insert into coach (acknowledge_time,cancel_time,completed_time,created_time,deadline,history_id,hr_id,kpi_json_str,sn,status,type,assign_to_id,classification) values ('"+self.yesterday_time+"',null,'"+self.yesterday_time+"','"+self.yesterday_time+"','"+self.deadlinetime+"','"+self.historyID+"','"+self.TL[2]+"','{}','Auto-ScriptIinsert_notForManualTest',"+self.acknowledged+","+self.rapidfireFormID+",66776677,1);"
        sql2="select LAST_INSERT_ID();"
        cur.execute(rfpccoach_sql1)
        cur.execute(sql2)
        data=cur.fetchall()
        coachID=str(data[0][0])
        print "rapid form_ acknowledged coachID= ", coachID
        rfpccoach_sql3="insert into rfpccoach (actions1rating,actions2rating,actions3rating,actions4rating,actions5rating,actions6rating,actions7rating,actions8rating,results,coach_id) values (1,2,3,2,2,null,null,3,2.17, "+ coachID+ ");"
        cur.execute(rfpccoach_sql3)
        
         
        rfpccoach_sql1="insert into coach (acknowledge_time,cancel_time,completed_time,created_time,deadline,history_id,hr_id,kpi_json_str,sn,status,type,assign_to_id,classification) values (null,null,'"+self.yesterday_time+"','"+self.yesterday_time+"','"+self.deadlinetime+"','"+self.historyID+"','"+self.TL[1]+"','{}','Auto-ScriptIinsert_notForManualTest',"+self.completed+","+self.rapidfireFormID+",66776677,1);"
        sql2="select LAST_INSERT_ID();"
        cur.execute(rfpccoach_sql1)
        cur.execute(sql2)
        data=cur.fetchall()
        coachID=str(data[0][0])
        print "rapid form_ completed coachID= ", coachID
        rfpccoach_sql3="insert into rfpccoach (actions1rating,actions2rating,actions3rating,actions4rating,actions5rating,actions6rating,actions7rating,actions8rating,results,coach_id) values (1,2,3,null,null,null,null,3,2.25, "+ coachID+ ");"
        cur.execute(rfpccoach_sql3)
         
        rfpccoach_sql1="insert into coach (acknowledge_time,cancel_time,completed_time,created_time,deadline,history_id,hr_id,kpi_json_str,sn,status,type,assign_to_id,classification) values (null,null,null,'"+self.yesterday_time+"','"+self.deadlinetime+"','"+self.historyID+"','"+self.TL[1]+"','{}','Auto-ScriptIinsert_notForManualTest',"+self.planned+","+self.rapidfireFormID+",66776677,1);"
        sql2="select LAST_INSERT_ID();"
        cur.execute(rfpccoach_sql1)
        cur.execute(sql2)
        data=cur.fetchall()
        coachID=str(data[0][0])
        print "rapid form_ planned coachID= ", coachID
         
        rfpccoach_sql1="insert into coach (acknowledge_time,cancel_time,completed_time,created_time,deadline,history_id,hr_id,kpi_json_str,sn,status,type,assign_to_id,classification) values (null,null,null,'"+self.yesterday_time+"','"+self.deadlinetime+"','"+self.historyID+"','"+self.TL[1]+"','{}','Auto-ScriptIinsert_notForManualTest',"+self.ongoing+","+self.rapidfireFormID+",66776677,1);"
        sql2="select LAST_INSERT_ID();"
        cur.execute(rfpccoach_sql1)
        cur.execute(sql2)
        data=cur.fetchall()
        coachID=str(data[0][0])
        print "rapid form_ ongoing coachID= ", coachID
        rfpccoach_sql3="insert into rfpccoach (actions1rating,actions2rating,actions3rating,actions4rating,actions5rating,actions6rating,actions7rating,actions8rating,results,coach_id) values (1,2,3,null,2,null,null,3,2.2, "+ coachID+ ");"
        cur.execute(rfpccoach_sql3)
        
        
        rfpccoach_sql1="insert into coach (acknowledge_time,cancel_time,completed_time,created_time,deadline,history_id,hr_id,kpi_json_str,sn,status,type,assign_to_id,classification) values (null,'"+self.threemonthAgo_time+"',null,'"+self.yesterday_time+"','"+self.deadlinetime+"','"+self.historyID+"','"+self.TL[1]+"','{}','Auto-ScriptIinsert_notForManualTest',"+self.cancelled+","+self.rapidfireFormID+",66776677,1);"
        sql2="select LAST_INSERT_ID();"
        cur.execute(rfpccoach_sql1)
        cur.execute(sql2)
        data=cur.fetchall()
        coachID=str(data[0][0])
        print "rapid form_ cancelled coachID= ", coachID
        rfpccoach_sql3="insert into rfpccoach (actions1rating,actions2rating,actions3rating,actions4rating,actions5rating,actions6rating,actions7rating,actions8rating,results,coach_id) values (1,2,3,null,2,1,null,3,2, "+ coachID+ ");"
        cur.execute(rfpccoach_sql3)    
         
    def hotlapsForm_insert(self,cur):
        hlpccoach_sql1="insert into coach (acknowledge_time,cancel_time,completed_time,created_time,deadline,history_id,hr_id,kpi_json_str,sn,status,type,assign_to_id,classification) values ('"+self.yesterday_time+"',null,'"+self.threemonthAgo_time+"','"+self.fivemonthAgo_time+"','"+self.deadlinetime+"','"+self.historyID+"','"+self.TL[1]+"','{}','Auto-ScriptIinsert_notForManualTest',"+self.acknowledged+","+self.hotlapFormID+",66776677,1);"
        sql2="select LAST_INSERT_ID();"
        cur.execute(hlpccoach_sql1)
        cur.execute(sql2)
        data=cur.fetchall()
        coachID=str(data[0][0])
        print "hot laps form_ acknowledged coachID= ", coachID
        hlpccoach_sql3="insert into hlpccoach (actions1rating,actions2rating,actions3rating,actions4rating,actions5rating,actions6rating,results,coach_id) values (1,2,2,3,3,3,2.33, "+ coachID+ ");"
        cur.execute(hlpccoach_sql3)
        
        hlpccoach_sql1="insert into coach (acknowledge_time,cancel_time,completed_time,created_time,deadline,history_id,hr_id,kpi_json_str,sn,status,type,assign_to_id,classification) values ('"+self.yesterday_time+"',null,'"+self.threemonthAgo_time+"','"+self.fivemonthAgo_time+"','"+self.deadlinetime+"','"+self.historyID+"','"+self.TL[1]+"','{}','Auto-ScriptIinsert_notForManualTest',"+self.acknowledged+","+self.hotlapFormID+",66776677,1);"
        sql2="select LAST_INSERT_ID();"
        cur.execute(hlpccoach_sql1)
        cur.execute(sql2)
        data=cur.fetchall()
        coachID=str(data[0][0])
        print "hot laps form_ acknowledged coachID= ", coachID
        hlpccoach_sql3="insert into hlpccoach (actions1rating,actions2rating,actions3rating,actions4rating,actions5rating,actions6rating,results,coach_id) values (1,2,2,3,3,3,2.33, "+ coachID+ ");"
        cur.execute(hlpccoach_sql3)
         
        hlpccoach_sql1="insert into coach (acknowledge_time,cancel_time,completed_time,created_time,deadline,history_id,hr_id,kpi_json_str,sn,status,type,assign_to_id,classification) values ('"+self.yesterday_time+"',null,'"+self.threemonthAgo_time+"','"+self.fivemonthAgo_time+"','"+self.deadlinetime+"','"+self.historyID+"','"+self.TL[1]+"','{}','Auto-ScriptIinsert_notForManualTest',"+self.acknowledged+","+self.hotlapFormID+",66776677,1);"
        sql2="select LAST_INSERT_ID();"
        cur.execute(hlpccoach_sql1)
        cur.execute(sql2)
        data=cur.fetchall()
        coachID=str(data[0][0])
        print "hot laps form_ acknowledged coachID= ", coachID
        hlpccoach_sql3="insert into hlpccoach (actions1rating,actions2rating,actions3rating,actions4rating,actions5rating,actions6rating,results,coach_id) values (null,2,2,3,3,3,2.6, "+ coachID+ ");"
        cur.execute(hlpccoach_sql3)
        
        hlpccoach_sql1="insert into coach (acknowledge_time,cancel_time,completed_time,created_time,deadline,history_id,hr_id,kpi_json_str,sn,status,type,assign_to_id,classification) values ('"+self.yesterday_time+"',null,'"+self.threemonthAgo_time+"','"+self.fivemonthAgo_time+"','"+self.deadlinetime+"','"+self.historyID+"','"+self.TL[0]+"','{}','Auto-ScriptIinsert_notForManualTest',"+self.acknowledged+","+self.hotlapFormID+",66776677,1);"
        sql2="select LAST_INSERT_ID();"
        cur.execute(hlpccoach_sql1)
        cur.execute(sql2)
        data=cur.fetchall()
        coachID=str(data[0][0])
        print "hot laps form_ acknowledged coachID= ", coachID
        hlpccoach_sql3="insert into hlpccoach (actions1rating,actions2rating,actions3rating,actions4rating,actions5rating,actions6rating,results,coach_id) values (null,2,2,3,3,3,2.6, "+ coachID+ ");"
        cur.execute(hlpccoach_sql3)
        
        hlpccoach_sql1="insert into coach (acknowledge_time,cancel_time,completed_time,created_time,deadline,history_id,hr_id,kpi_json_str,sn,status,type,assign_to_id,classification) values ('"+self.yesterday_time+"',null,'"+self.threemonthAgo_time+"','"+self.fivemonthAgo_time+"','"+self.deadlinetime+"','"+self.historyID+"','"+self.TL[0]+"','{}','Auto-ScriptIinsert_notForManualTest',"+self.acknowledged+","+self.hotlapFormID+",66776677,1);"
        sql2="select LAST_INSERT_ID();"
        cur.execute(hlpccoach_sql1)
        cur.execute(sql2)
        data=cur.fetchall()
        coachID=str(data[0][0])
        print "hot laps form_ acknowledged coachID= ", coachID
        hlpccoach_sql3="insert into hlpccoach (actions1rating,actions2rating,actions3rating,actions4rating,actions5rating,actions6rating,results,coach_id) values (null,2,2,3,3,3,2.6, "+ coachID+ ");"
        cur.execute(hlpccoach_sql3)
        
        hlpccoach_sql1="insert into coach (acknowledge_time,cancel_time,completed_time,created_time,deadline,history_id,hr_id,kpi_json_str,sn,status,type,assign_to_id,classification) values ('"+self.yesterday_time+"',null,'"+self.threemonthAgo_time+"','"+self.fivemonthAgo_time+"','"+self.deadlinetime+"','"+self.historyID+"','"+self.TL[2]+"','{}','Auto-ScriptIinsert_notForManualTest',"+self.acknowledged+","+self.hotlapFormID+",66776677,1);"
        sql2="select LAST_INSERT_ID();"
        cur.execute(hlpccoach_sql1)
        cur.execute(sql2)
        data=cur.fetchall()
        coachID=str(data[0][0])
        print "hot laps form_ acknowledged coachID= ", coachID
        hlpccoach_sql3="insert into hlpccoach (actions1rating,actions2rating,actions3rating,actions4rating,actions5rating,actions6rating,results,coach_id) values (null,2,2,3,3,3,2.6, "+ coachID+ ");"
        cur.execute(hlpccoach_sql3)
        
          
        hlpccoach_sql1="insert into coach (acknowledge_time,cancel_time,completed_time,created_time,deadline,history_id,hr_id,kpi_json_str,sn,status,type,assign_to_id,classification) values (null,null,'"+self.threemonthAgo_time+"','"+self.threemonthAgo_time+"','"+self.deadlinetime+"','"+self.historyID+"','"+self.TL[1]+"','{}','Auto-ScriptIinsert_notForManualTest',"+self.completed+",'"+self.hotlapFormID+"',66776677,1);"
        sql2="select LAST_INSERT_ID();"
        cur.execute(hlpccoach_sql1)
        cur.execute(sql2)
        data=cur.fetchall()
        coachID=str(data[0][0])
        print "hot laps form_ completed coachID= ", coachID
        hlpccoach_sql3="insert into hlpccoach (actions1rating,actions2rating,actions3rating,actions4rating,actions5rating,actions6rating,results,coach_id) values (null,null,2,3,3,3,2.75, "+ coachID+ ");"
        cur.execute(hlpccoach_sql3)
        
       
        
          
        hlpccoach_sql1="insert into coach (acknowledge_time,cancel_time,completed_time,created_time,deadline,history_id,hr_id,kpi_json_str,sn,status,type,assign_to_id,classification) values (null,null,null,'"+self.threemonthAgo_time+"','"+self.deadlinetime+"','"+self.historyID+"','"+self.TL[0]+"','{}','Auto-ScriptIinsert_notForManualTest',"+self.ongoing+","+self.hotlapFormID+",66776677,1);"
        sql2="select LAST_INSERT_ID();"
        cur.execute(hlpccoach_sql1)
        cur.execute(sql2)
        data=cur.fetchall()
        coachID=str(data[0][0])
        print "hot laps form_ ongoing coachID= ", coachID
        hlpccoach_sql3="insert into hlpccoach (actions1rating,actions2rating,actions3rating,actions4rating,actions5rating,actions6rating,results,coach_id) values (null,null,null,2,3,3,2.67, "+ coachID+ ");"
        cur.execute(hlpccoach_sql3)
          
       
          
          
        hlpccoach_sql1="insert into coach (acknowledge_time,cancel_time,completed_time,created_time,deadline,history_id,hr_id,kpi_json_str,sn,status,type,assign_to_id,classification) values (null,'"+self.threemonthAgo_time+"',null,'"+self.threemonthAgo_time+"','"+self.deadlinetime+"','"+self.historyID+"','"+self.TL[1]+"','{}','Auto-ScriptIinsert_notForManualTest',"+self.cancelled+","+self.hotlapFormID+",66776677,1);"
        sql2="select LAST_INSERT_ID();"
        cur.execute(hlpccoach_sql1)
        cur.execute(sql2)
        data=cur.fetchall()
        coachID=str(data[0][0])
        print "hot laps form_ canceled coachID= ", coachID
        hlpccoach_sql3="insert into hlpccoach (actions1rating,actions2rating,actions3rating,actions4rating,actions5rating,actions6rating,results,coach_id) values (null,null,null,2,null,3,2.5, "+ coachID+ ");"
        cur.execute(hlpccoach_sql3)
        
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