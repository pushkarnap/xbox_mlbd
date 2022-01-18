import numpy as np
import matplotlib.pyplot as plt
import datetime
import os
import operator
from nptdms import TdmsFile
from nptdms import tdms
import pathlib
from pprint import pprint as pp
import pandas as pd

work_dir = os.getcwd()
out_dir = os.path.join(work_dir, "output")
data_dir = os.path.join(work_dir, "Xbox3_TD24_bo_L3")

CHOSEN_DATA_DATE = {'YEAR' : 2020,
                    'MONTH' : 2,
                    'DAY' : 11}

#Enter the date for the file you want to read below.
######################################################################################################
chosen_date = datetime.date(year = CHOSEN_DATA_DATE['YEAR'],
                            month = CHOSEN_DATA_DATE['MONTH'],
                            day = CHOSEN_DATA_DATE['DAY'])

use_date = chosen_date.strftime('20%y%m%d')
print(use_date)
file_name_A = "EventDataA_%s.tdms" % use_date
file_name_B = "EventDataB_%s.tdms" % use_date
file_path_A = os.path.join(data_dir, file_name_A)
file_path_B = os.path.join(data_dir, file_name_B)

if os.path.isfile(file_path_A) and os.path.isfile(file_path_B):
    file_A = TdmsFile.open(file_path_A)
    file_B = TdmsFile.open(file_path_B)
    print('EVENTDataA files loaded')
    print('EVENTDataB files loaded')

else:
    print ('File(s) %s do not exist, terminating script.' % use_date)
    raise SystemExit(0)


# Print the groups and some other interesting properties
######################################################################################################

# prints the groups i.e. different RF pulses
groups_A = file_A.groups()
groups_B = file_B.groups()
group_names_A = [group.name for group in groups_A]
group_names_B = [group.name for group in groups_B]

# prints the properties associated with the first group
tgrp = groups_A[0]
pp(tgrp.__dict__)
#pp(vars(tgrp))
#pp(dir(tgrp))
tgrpprp = tgrp.properties
tgrpchls = tgrp.channels()
tgrpnm = tgrp.name
tgrppt = tgrp.path
tgrpdf = tgrp.as_dataframe()

tchl = tgrpchls[0]
pp(dir(tchl))
tchldf = tchl.as_dataframe()
tchltt = tchl.time_track()
pp(len(tchltt))
#pp(tgrpprp)
#pp(tgrpchls)
#print(tgrpnm)
#print(tgrppt)
#pp(tgrpdf)

"""
for group_name in group_names_A:
    group_prop = file_A[group_name].properties
    pp(vars(group_name))
"""


'''
# prints the channels i.e. the waveforms we log on each pulse
channels= group[0].channels()
print (channels)

# prints the properties associated with the PSI channel on the first group
PSI_Properties = group[0]['PSI Amplitude'].properties
print (PSI_Properties)



# Print the breakdown pulses
######################################################################################################
for x in range (len(group)):
    if 'Breakdown' in str(group[x]):
        print (group[x], x)



# Ask the user to choose a breakdown pulse
######################################################################################################
BDN = input("Please enter a breakdown number (the final digits on the entries above):")
BDN = int(BDN)



# Grab some RF waveforms from that pulse and creat an accompanying time axis
######################################################################################################
PSIBD_data = group[BDN]['PSI Amplitude'].data
PEIBD_data = group[BDN]['PEI Amplitude'].data
PSRBD_data = group[BDN]['PSR Amplitude'].data

PSI_data = group[BDN-1]['PSI Amplitude'].data
PSR_data = group[BDN-1]['PSR Amplitude'].data
PEI_data = group[BDN-1]['PEI Amplitude'].data
time_axis = np.linspace(0, 2, len(PSI_data))



# Plot some data
######################################################################################################

#subplot 1
###########################################
plt.subplot(3, 1, 1)

PSRBD, = plt.plot(time_axis , PSRBD_data, label ='PSRBD', linewidth=2)
PSR, = plt.plot(time_axis , PSR_data, label ='PSR', linewidth=2)

plt.legend(handles=[PSRBD, PSR])

plt.xlabel('Time [\u03bcs]', fontsize=10)
plt.ylabel('Amplitude [Arb. Units]', fontsize=10)
plt.title('PSI2 Plot %s_%s'% (chosen_date.strftime('20%y%m%d'),group[BDN]), fontsize=10)

#subplot 2
###########################################
plt.subplot(3, 1, 2)

PSIBD, = plt.plot(time_axis , PSIBD_data, label ='PSIBD', linewidth=2)
PSI, = plt.plot(time_axis , PSI_data, label ='PSI', linewidth=2)

plt.legend(handles=[PSIBD, PSI])

plt.xlabel('Time [\u03bcs]', fontsize=10)
plt.ylabel('Amplitude [Arb. Units]', fontsize=10)

#subplot 3
###########################################
plt.subplot(3, 1, 3)

PEIBD, = plt.plot(time_axis , PEIBD_data, label ='PEIBD', linewidth=2)
PEI, = plt.plot(time_axis , PEI_data, label ='PEI', linewidth=2)

plt.legend(handles=[PEIBD, PEI])

plt.xlabel('Time [\u03bcs]', fontsize=10)
plt.ylabel('Amplitude [Arb. Units]', fontsize=10)
'''
