#Double for loop for accessing groups and channels in TREND data
print("Groups:")
groups = tdms_file.groups()
for grp_idx in range(len(groups)):
    grp_name = groups[grp_idx].name
    print(grp_name)
    print(f"Channels for {grp_name}")
    channels = tdms_file[grp_name].channels()
    for chl_idx in range(len(channels)):
        chl_name = channels[chl_idx].name
        chl_path = channels[chl_idx].path
        print(chl_name)

#more elegant way of doing above
groups = tdms_file.groups()
group_names = [group.name for group in groups]
for group_name in group_names:
    channels = tdms_file[group_name].channels()
    channel_names = [channel.name for channel in channels]
    for channel_name in in channel_names:
        print(group_name, channel_name)

#get file 'properties'
file_props = tdms_file.properties
print(file_props)

#list comprehension for group datagroups = tdms_file.groups()
groups = tdms_file.groups()
group_names = [group.name for group in groups]

#WARNING! Doing a full TdmsFile(FILE_PATH) can be slow for large files 
