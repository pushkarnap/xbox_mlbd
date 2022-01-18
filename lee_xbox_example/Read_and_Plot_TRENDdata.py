import os
import pathlib
import datetime
from datetime import timedelta
import matplotlib.pyplot as plt
from nptdms import TdmsFile, tdms
from nptdms import tdms
import matplotlib.dates as md

work_dir = os.getcwd()
out_dir = os.path.join(work_dir, "output")
data_dir = os.path.join(work_dir, "Xbox3_TD24_bo_L3")

DATA_START_DATE = {'YEAR' : 2020,
                   'MONTH' : 2,
                   'DAY' : 11}

#Import any functions and useful modules.
######################################################################################################
exec(open("./Functions.py").read())
print('Daterange function imported successfully')

#NOTE: I've used this function all the scripts so I have shoved it in a separate file instead,
# you can paste it here and collapse it if you want.



#Define the Range of Dates we'd like to plot
######################################################################################################
start = datetime.date(year = DATA_START_DATE['YEAR'],
                      month = DATA_START_DATE['MONTH'],
                      day = DATA_START_DATE['DAY'])
end = start

#NOTE: I have set the end date as the start date so that it only reads a single file but you can
#      use the daterange function and a loop like the one below to read many in sequence then
#      concatenate/convert to another format.



#Check if the file exists for each day and plot it if it does
######################################################################################################
for date in daterange(start, end):
    use_date = date.strftime('20%y%m%d')
    file_name = "TrendData_%s.tdms" % use_date
    check_file_path = os.path.join(data_dir, file_name)

    if os.path.isfile(check_file_path):
        tdms_file = TdmsFile(check_file_path)
        print ('TrendData file loaded.')

    else:
        print ('Data for %s does not exist, terminating script.' % use_date)
        raise SystemExit(0)



#Print the channels and grab some data to plot(the ion pump before the structure in this example).
######################################################################################################
    PC1_tempchannels = {'PC1_Left Temp': 'red',
                        'PC1_Right Temp': 'green',
                        'PC1_Hybrid Temp': 'blue'}
    groups = tdms_file.groups()
    group_names = [group.name for group in groups]
    for group_name in group_names:
        fig, ax = plt.subplots()
        ax.set_title(f"PC1 temperature plots (Group: {group_name})")
        ax.set_xlabel("Time [Hour-Minute-Second-ms]")
        ax.set_ylabel("Temperature [Celsius]")
        for temp_chl, chl_colour in PC1_tempchannels.items():
            temp_data = tdms_file[group_name][temp_chl]
            time_data = tdms_file[group_name]["Timestamp"]
            ax.plot(time_data, temp_data, chl_colour, label = temp_chl)
        fig.savefig(f"output/PC1_temp_TREND_{group_name}.png")

'''
    channels = groups[0].channels()
    print("Available Channels:", channels)


    Timestamp_Data = group[0]["Timestamp"]
    IPB4_Data = group[0]["IP before structure"]


#Generate a Plot
######################################################################################################

    plt.xlabel('Time [Hour-Minute-Second-ms]', fontsize=15)
    plt.ylabel('Pressure [mbar]', fontsize=15)
    plt.subplots_adjust(bottom=0.2)
    plt.xticks( rotation=25 )
    plt.yscale('log')
    plt.grid()

    ax=plt.gca()

    xfmt = md.DateFormatter('%H:%M:%S:%f ')
    ax.xaxis.set_major_formatter(xfmt)

    plt.scatter(Timestamp_Data,IPB4_Data,s=5,color='black')
'''
