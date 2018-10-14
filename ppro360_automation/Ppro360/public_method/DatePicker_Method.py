'''
Created on Jun 26, 2018

@author: Sabrina
'''
from Tablet_pages.LeaderAcademyCoachingLeaderScorespage import LeaderAcademyCoachingLeaderScorespage
from Tablet_pages.RedemptionReport_Page import RedemptionReport_Page

class DatePicker_Method():
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    def get_DateLocation(self,Date_Type,StartEndeindex,Date_need,Month_need):
        #LACLS=LeaderAcademyCoachingLeaderScorespage()
        #The center loc is the follwing
        lineindex1=3
        lineindex2=4
        Dateindex_center=4
        Date1=self.Get_DateText(Date_Type, StartEndeindex, lineindex1, Dateindex_center)
        Date2=self.Get_DateText(Date_Type, StartEndeindex, lineindex2, Dateindex_center)
        
        print "Date1:",Date1
        print "Date2:",Date2
        
        if int(Date_need)>int(Date1):
            print "int(Date_need)>int(Date1):",int(Date_need)>int(Date1)
            if int(Date_need)>int(Date2):
                print "int(Date_need)>int(Date2):",int(Date_need)>int(Date2)
                lineindex_centerOfLastHalfMonth=5
                Dateindex_centerOfLastHalfMonth=6
                Date_CenterOfLastHalfMonth=self.Get_DateText(Date_Type, StartEndeindex, lineindex_centerOfLastHalfMonth, Dateindex_centerOfLastHalfMonth)
                print "Date_CenterOfLastHalfMonth:",Date_CenterOfLastHalfMonth
                if Month_need=="02":
                    Date_max=28
                elif Month_need in ["01","03","05","07","08","10","12"]:
                    Date_max=31
                else:
                    Date_max=30
                if int(Date_need)<int(Date_CenterOfLastHalfMonth)<=int(Date_max) or self.Get_ClassValue(Date_Type, StartEndeindex, lineindex_centerOfLastHalfMonth, Dateindex_centerOfLastHalfMonth)=="day disabled" :
                    list1=[5,6,7]#lineindex=4
                    list2=[1,2,3,4,5]#lineindex=5
                    if self.Get_Dateindex(Date_Type, StartEndeindex, Date_need, 4, list1)=="":
                        lineindex=5
                        Dateindex=self.Get_Dateindex(Date_Type, StartEndeindex, Date_need, lineindex, list2)
                    else:
                        lineindex=4
                        Dateindex=self.Get_Dateindex(Date_Type, StartEndeindex, Date_need, lineindex, list1)
                    
                elif int(Date_need)>int(Date_CenterOfLastHalfMonth)<=int(Date_max):
                    if int(Date_CenterOfLastHalfMonth)>int(Date2):
                        List=[1,2,3,4,5,6,7]
                        if self.Get_Dateindex(Date_Type, StartEndeindex, Date_need, 5, [7])!="":
                            lineindex=5
                            Dateindex=7
                        else:
                            lineindex=6
                            Dateindex=self.Get_Dateindex(Date_Type, StartEndeindex, Date_need, lineindex, List)
                    else:
                        list1=[5,6,7]#lineindex=4
                        list2=[1,2,3,4,5]#lineindex=5
                        if self.Get_Dateindex(Date_Type, StartEndeindex, Date_need, 4, list1)=="":
                            lineindex=5
                            Dateindex=self.Get_Dateindex(Date_Type, StartEndeindex, Date_need, lineindex, list2)
                        else:
                            lineindex=4
                            Dateindex=self.Get_Dateindex(Date_Type, StartEndeindex, Date_need, lineindex, list1)

                elif int(Date_need)==int(Date_CenterOfLastHalfMonth):
                    lineindex=lineindex_centerOfLastHalfMonth
                    Dateindex=Dateindex_centerOfLastHalfMonth
                
            elif int(Date_need)<int(Date2):
                list1=[5,6,7]#lineindex=3
                list2=[1,2,3]#lineindex=4
                if self.Get_Dateindex(Date_Type, StartEndeindex, Date_need, 3, list1)=="":
                    lineindex=4
                    Dateindex=self.Get_Dateindex(Date_Type, StartEndeindex, Date_need, lineindex, list2)
                else:
                    lineindex=3
                    Dateindex=self.Get_Dateindex(Date_Type, StartEndeindex, Date_need, lineindex, list1)
                
            elif int(Date_need)==int(Date2):
                lineindex=lineindex2
                Dateindex=Dateindex_center
        elif int(Date_need)<int(Date1):
            lineindex1_center=2
            Dateindex_center_1=2
            Date_CenterOfFirstHalfMonth=self.Get_DateText(Date_Type, StartEndeindex, lineindex1_center, Dateindex_center_1)
            if int(Date_need)<int(Date_CenterOfFirstHalfMonth):
                if int(Date_need)==int(self.Get_DateText(Date_Type, StartEndeindex, 2, 1)):
                    lineindex=2
                    Dateindex=1
                    print lineindex
                else:
                    lineindex_lookup=1
                    List=[1,2,3,4,5,6,7]
                    for i in List:
                        Dateindex_lookup=i
                        if int(Date_need)==int(self.Get_DateText(Date_Type, StartEndeindex, lineindex_lookup, Dateindex_lookup)):
                            lineindex=lineindex_lookup
                            Dateindex=Dateindex_lookup
                    print lineindex
         
            elif int(Date_need)>int(Date_CenterOfFirstHalfMonth):
                list1=[3,4,5,6,7]#lindex=2
                list2=[1,2,3]#lindex=3
                if self.Get_Dateindex(Date_Type, StartEndeindex, Date_need, 2, list1)=="":
                    lineindex=3
                    Dateindex=self.Get_Dateindex(Date_Type, StartEndeindex, Date_need, lineindex, list2)
                    print lineindex
                else:
                    lineindex=2
                    Dateindex=self.Get_Dateindex(Date_Type, StartEndeindex, Date_need, lineindex, list1)
                    print lineindex
            elif int(Date_need)==int(Date_CenterOfFirstHalfMonth):
                lineindex=lineindex1_center
                Dateindex=Dateindex_center_1
                print lineindex
        elif int(Date_need)==int(Date1):
            lineindex=lineindex1
            Dateindex=Dateindex_center
            print lineindex
        Location_list=[lineindex,Dateindex]
        return Location_list
    
    def get_DateLocatioEarlierThanSpecifiedDate(self,location_list):#One day earlier than SpecifiedDate
        if location_list[1]==1:
            Newlocation_list=[location_list[0]-1,7]
        else:
            Newlocation_list=[location_list[0],location_list[1]-1]
        return Newlocation_list
    def Get_DateText(self,Date_Type,StartEndeindex,lineindex,Dateindex):
        Redemption=RedemptionReport_Page()
        LACLS=LeaderAcademyCoachingLeaderScorespage()
        if Date_Type=="Created_Date":
            Date=LACLS.Get_CreatedDateInDatePicker(StartEndeindex, lineindex,Dateindex)
        elif Date_Type=="Acknowledge_Date":
            Date=LACLS.Get_AcknowledgeDateInDatePicker(StartEndeindex, lineindex,Dateindex)
        elif Date_Type=="Redeem Date":
            Date=Redemption.Get_RedemptionDateInDatePicker(StartEndeindex, lineindex, Dateindex)
        return Date
    
    def Get_ClassValue(self,Date_Type,StartEndeindex,lineindex,dateindex):
        Redemption=RedemptionReport_Page()
        LACLS=LeaderAcademyCoachingLeaderScorespage()
        if Date_Type=="Created_Date":
            Class_value=LACLS.Get_ClassValue_CreatedDateInDatePicker(StartEndeindex, lineindex, dateindex)
        elif Date_Type=="Acknowledge_Date":
            Class_value=LACLS.Get_ClassValue_AcknowledgeDateInDatePicker(StartEndeindex, lineindex, dateindex)
        elif Date_Type=="Redeem Date":
            Class_value=Redemption.Get_ClassValue_RedemptionDateInDatePicker(StartEndeindex, lineindex, dateindex)
        return Class_value
        
        
    def Get_Dateindex(self,Date_Type, StartEndeindex,Date_need,lineindex,List):
        Dateindex=""
        for item in List:
            if int(Date_need)==int(self.Get_DateText(Date_Type, StartEndeindex, lineindex, item)):
                Dateindex=item
        return Dateindex  
        
    