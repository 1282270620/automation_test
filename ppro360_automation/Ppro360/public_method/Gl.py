'''
Created on Dec 22, 2016

@author: Sabrina Guo
'''
from selenium import webdriver

driver = webdriver.Chrome()
waittime=1

role_list=["L3","LC","L1","AGENT"]

#performancefor3time_lob=("ICM","UBIZ","AOL","DTVDS","LCBB","DTVSS","DTVRCX","DBS")
#performancefor1time_lob=("BLUE","SPANISH","ISM","GREEN")


performancefor_MultiTimeTab_lob=("ICM","UBIZ","DTVDS","LCBB","DTVSS","DTVRCX","DBS","ISM SERVICE","ISM","BGI DTV","BGI LITE","ISM CLG","ISM HFC","IP","ATT BLUE","VXI IP","PAYPAL","CENTURYLINK","CLG","MOVERS","UBER TRANSPORT VOICE")

performancefor_3TimeTab_lob=("BLUE","SPANISH","GREEN")
performancefor_OldTimeTab_lob=("AOL")
DoubleKPIname_lob=("BLUE","SPANISH","ISM","ISM SERVICE")#,"ISM"
DoubleKPIValue_lob=("BLUE","SPANISH")

Multi_timetab=["Month-to-Date"]#"LastTwoMonth","LastMonth","Yesterday","Week-to-Date",
Less_timetab=["LastTwoMonth","LastMonth","Month-to-Date"]#
Old_timetab=["Yesterday","Week-to-Date","Month-to-Date"]#



SevralFilefor_lob=("DBS","ISM","LCBB")

#Excel file Info
configrationfilename='configration.xlsx'
#DataBase configuration
DatabaseConfigfilename='DataBase_Config.xlsx'

#Performance Data file Info
PerformanceDatafilename='PerformanceaCalculation.xlsx'

#Performance file directory
# PerformanceFile_Directory="D:\FileToBeTest\CorrectSheetNumber"
# PerformanceFlie_Visible_MoreSheetNumber_Directory="D:\FileToBeTest\Visible_MoreSheetNumber"
# PerformanceFlie_Hiden_MoreSheetNumber_Directory="D:\FileToBeTest\Hiden_MoreSheetNumber"
# PerformanceFile_NocommaInREPForISM_Directory="D:\FileToBeTest\NocommaInREP_ForISM"
# LCCBFile_Directory="D:\FileToBeTest\LCBBTestFiles"

#Mysql user and password
Mysql_host='172.18.42.92'
Mysql_user='root'
Mysql_password='A3EDD019E341B5A124986FEAF78F20C7'
Mysql_port=3306


