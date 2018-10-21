from configparser import ConfigParser
import os 
from public_method.Get_configration_data import Get_configration_data

ini = 'ACE_SITEL'
excel = 'ACE_SITEL'
print(list(ini))
print(list(excel))
print(ini.replace('\x1f_', '_') ==r'ACE_SITEL')