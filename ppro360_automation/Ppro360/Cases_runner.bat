SET PYTHONPATH=%cd%
cd Coaching_cases
python	OMCheckCoachingFormList.py
timeout /t 1
python	TLCheckCoachingFormList.py
timeout /t 1
python	CoachingFilterFunction_Agent.py
timeout /t 1
python	LCCheckCoachingFormList.py
cd ..




goto start


cd Performance_Cases_GREEN
python GREEN_Performance_OM.py
python GREEN_Performance_LC.py
python GREEN_Performance_TL.py
python GREEN_Performance_Agent.py
python GREEN_Outlier_TL.py
cd ..

cd Performance_Cases_UBIZICM
python UBIZICM_Performance_OM.py
python UBIZICM_Performance_LC.py
python UBIZICM_Performance_TL.py
python UBIZICM_Performance_Agent.py
python UBIZICM_Outlier_TL.py
cd ..
cd Performance_Cases_DTVRCX
python DTVRCX_Performance_OM.py
python DTVRCX_Performance_LC.py
python DTVRCX_Performance_TL.py
python DTVRCX_Performance_Agent.py
python DTVRCX_Outlier_TL.py
cd ..


cd LoginHomePage_cases
python	LoginPage.py
timeout /t 1
python	ChangePassword_LC.py
timeout /t 1
python	ChangeToInvalidPassword_LC.py
timeout /t 1
python	ChangePassword_OM.py
timeout /t 1
python	ChangeToInvalidPassword_OM.py
timeout /t 1
python	ChangePassword_TL.py
timeout /t 1
python	ChangeToInvalidPassword_TL.py
timeout /t 1
python	ChangePassword_Agent.py
timeout /t 1
python	ChangeToInvalidPassword_Agent.py
timeout /t 1
cd ..




cd AdminSystem_cases 
python	AddOMAccount.py
timeout /t 1
python	AddOMAccount_Abnormal.py
timeout /t 1
python	EditAdminAccount_Normal.py
timeout /t 1
python	EditAccount_SpecialName.py
timeout /t 1
python	ResetOMPassword.py
timeout /t 1
python	AdminEditLCAccountName.py
timeout /t 1
python	ResetLCPassword.py
timeout /t 1
cd ..

cd Triadcoaching_cases
python OMCheckTriadCoachingFormList.py
timeout /t 1
python LCCheckTriadCoachingFormList.py
timeout /t 1
python TriadCoachingTypeDropDown_TL.py
cd ..





cd Performance_Cases_UBIZICM
python UBIZICM__Performance_OM.py
python UBIZICM__Performance_LC.py
python UBIZICM__Performance_TL.py
python UBIZICM_Performance_Agent.py
python UBIZICM_Outlier_TL.py
cd ..



cd Performance_Cases_DTVDS
python DTVDS_Performance_LC.py
python DTVDS_Performance_TL.py
python DTVDS_Performance_OM.py
cd ..

cd Performance_Cases_LCBB
python LCBB_Outlier_TL.py
cd ..
cd CoachingWorkFollow_Case
python SettingExpectations_OngoingToCanceled.py
cd ..

cd Coaching_cases
python	OMCheckCoachingFormList.py
timeout /t 1
python	TLCheckCoachingFormList.py
timeout /t 1
python	CoachingFilterFunction_Agent.py
timeout /t 1
python	LCCheckCoachingFormList.py
python	HRIDOnSpecificCoachingRecord_Bug.py
timeout /t 1
python	Timezonecheck_Bug.py
timeout /t 1
cd ..



cd Validation_cases
python PerformanceFile_EarlierThanToday.py
python PerformanceFile_TodayOrLaterThanToday.py
python Performance_NumberOfSheet.py
python Performance_REPcolumn.py
cd ..



cd Performance_Cases_LCBB
python LCBB_Performance_OM.py
timeout /t 1
python LCBB_Performance_LC.py
timeout /t 1
python LCBB_Performance_Agent.py
timeout /t 1
python LCBB_Performance_TL.py
timeout /t 1
python LCBB_Outlier_TL.py




cd CoachingWorkFollow_Case
python	Commendation_PlanedToAcknowledged.py
python	Commendation_AddFromOtherPage.py
python	Commendation_PlannedToCanceled.py
python	Commendation_OngoingToCanceled.py
cd ..

cd TriadCoachingWorkFollow_Cases
python	Commendation_PlannedToCompleted.py
cd ..

cd CoachingExport_cases
python OMLCCheckTypeDropDown_ExportModule.py
cd ..

cd Other_Scripts
python CompareDataFromThreeDB.py
cd ..


:start


