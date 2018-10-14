'''
Created on 2017.9.6

@author: yalan.yin
'''
from Tablet_pages.LeadershipAcademyCoachingScoresPage import LeadershipAcademyCoachingScoresPage


class LeadershipDate_Actual(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''  
    
    
    def get_page_teamandsite_Actual(self,lineindex):
        Lpage=LeadershipAcademyCoachingScoresPage()
        warmal=Lpage.get_Leadershippage_Teamandsite_value(lineindex,2)
        uncover=Lpage.get_Leadershippage_Teamandsite_value(lineindex,3)
        personalizee=Lpage.get_Leadershippage_Teamandsite_value(lineindex,4)
        gain=Lpage.get_Leadershippage_Teamandsite_value(lineindex,5)
        thoroughly=Lpage.get_Leadershippage_Teamandsite_value(lineindex,6)
        sincerely=Lpage.get_Leadershippage_Teamandsite_value(lineindex,7)
        total=Lpage.get_Leadershippage_Teamandsite_value(lineindex,8)
        teamandsite_Actual=[warmal,uncover,personalizee,gain,thoroughly,sincerely,total]
        #teamandsite_Actual={'warmal':warmal,'uncover':uncover,'personalizee':personalizee,'gain':gain,'thoroughly':thoroughly,'sincerely':sincerely,'total':total}
        return teamandsite_Actual
    
    def get_page_agent_Actual(self):
        Lpage=LeadershipAcademyCoachingScoresPage()
        warmal=Lpage.get_Leadershippage_agent_value(2)
        uncover=Lpage.get_Leadershippage_agent_value(3)
        personalizee=Lpage.get_Leadershippage_agent_value(4)
        gain=Lpage.get_Leadershippage_agent_value(5)
        thoroughly=Lpage.get_Leadershippage_agent_value(6)
        sincerely=Lpage.get_Leadershippage_agent_value(7)
        total=Lpage.get_Leadershippage_agent_value(8)
        agent_Actual=[warmal,uncover,personalizee,gain,thoroughly,sincerely,total]
        return agent_Actual
    
    def get_page_TL_Actual(self,lineindex):
        Lpage=LeadershipAcademyCoachingScoresPage()
        warmal=Lpage.get_Leadershippage_tl_value(lineindex,2)
        uncover=Lpage.get_Leadershippage_tl_value(lineindex,3)
        personalizee=Lpage.get_Leadershippage_tl_value(lineindex,4)
        gain=Lpage.get_Leadershippage_tl_value(lineindex,5)
        thoroughly=Lpage.get_Leadershippage_tl_value(lineindex,6)
        sincerely=Lpage.get_Leadershippage_tl_value(lineindex,7)
        total=Lpage.get_Leadershippage_tl_value(lineindex,8)
        tl_Actual=[warmal,uncover,personalizee,gain,thoroughly,sincerely,total]
        return tl_Actual
    
    def get_page_TLsagent(self,index1,index2):
        Lpage=LeadershipAcademyCoachingScoresPage()
        warmal=Lpage.get_agentdate(index1, index2, 2)
        uncover=Lpage.get_agentdate(index1, index2, 3)
        personalizee=Lpage.get_agentdate(index1, index2, 4)
        gain=Lpage.get_agentdate(index1, index2, 5)
        thoroughly=Lpage.get_agentdate(index1, index2, 6)
        sincerely=Lpage.get_agentdate(index1, index2, 7)
        total=Lpage.get_agentdate(index1, index2, 8)
        tl_Actual=[warmal,uncover,personalizee,gain,thoroughly,sincerely,total]
        return tl_Actual
    
        
        