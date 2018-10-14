'''
Created on 20180115

@author: luming.zhao
'''
from public_method.Get_file import Get_file

class LOBlistConfigration(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.LOBlist_Sheetiname="BASE-CONFIGURATION"
        
    def get_LOBlistConfigration(self,lineindex): 
        '''
        Can get all data of LOBs or Sites name
        The range of Linenumber_ALL_LOBs: line~5
        The range of Linenumber_Sites:line~6-26
        '''
        Getfile=Get_file()
        table=Getfile.Get_LOBlist_sheet_Info(self.LOBlist_Sheetiname)
        
        ALLLOBs_name=table.row_values(lineindex)[1]
        ALLLOBs=[ALLLOBs_name]
        
        ICMsites_name=table.row_values(lineindex)[1]
        ICMsites=[ICMsites_name]
        UBIZsites_name=table.row_values(lineindex)[1]
        ISMsites_name=table.row_values(lineindex)[1]
        ISMServicesites_name=table.row_values(lineindex)[1]
        ISMHFCsites_name=table.row_values(lineindex)[1]
        BGILITEsites_name=table.row_values(lineindex)[1]
        BGIDTVsites_name=table.row_values(lineindex)[1]
        ISMCLGsites_name=table.row_values(lineindex)[1]
        SPANISHsites_name=table.row_values(lineindex)[1]
        ATTBLUEsites_name=table.row_values(lineindex)[1]
        BLUEsites_name=table.row_values(lineindex)[1]
        DTVDSsites_name=table.row_values(lineindex)[1]
        LCBBsites_name=table.row_values(lineindex)[1]
        DTVSSsites_name=table.row_values(lineindex)[1]
        DTVRCXsites_name=table.row_values(lineindex)[1]
        DBSsites_name=table.row_values(lineindex)[1]
        GREENsites_name=table.row_values(lineindex)[1]
        PAYPALsites_name=table.row_values(lineindex)[1]
        IPsites_name=table.row_values(lineindex)[1]
        VXIIPsites_name=table.row_values(lineindex)[1]
        
        
        