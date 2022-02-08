from datetime import datetime, timezone
from dateutil.relativedelta import relativedelta
from dateutil import parser
import matplotlib.pyplot as plt
import pytz
import numpy as np
import h5py

LABVIEW_OFFSET = 66 #years

def trend_event_checker(event_path, *trend_paths):
    """
    Given a complete file path for an EVENT file,
    Given directories which store TREND files,
    If TREND corresponding to provided EVENT is found,
        Returns the full file path for TREND file
    If TREND correspondingto provided EVENT is not found
        Returns None.
    """

    event_name = event_path.stem
    date = event_name.split("_")[1]

    FOUND = 0
    selected_trend_path = trend_paths[0]

    for trend_path in trend_paths:
        trend_cand = trend_path/f"TrendData_{date}.hdf"
        if trend_cand.is_file():
            selected_trend_path = trend_cand
            FOUND = 1
            break

    if FOUND:
        return selected_trend_path
    else:
        return None

def extract_event_tstamps(event_path):
    """
    Retrieve the timestamps of each pulse in an EVENT file, and return as np
    array of datetime objects
    """
    tstamps_event = []
    with h5py.File(event_path, "r") as fhand:
        for key in fhand.keys():
            pulse = fhand[key]
            tstamp = pulse.attrs["Timestamp"]
            tstamp = tstamp.decode('utf-8')
            tstamps_event.append(parser.parse(tstamp, ignoretz = True))
    return np.array(tstamps_event)

def extract_trend_tstamps(trend_path):
    """
    Retrieve timestamps from each group in a TREND file. Return as type dict.
    """
    tstamps_trend = {}
    with h5py.File(trend_path, "r") as fhand:
        for run_name in fhand.keys():
            run = fhand[run_name]
            run_tstamp = parser.parse(run_name)
            tstamps = np.array(run["Timestamp"])
            tstamps = labview_to_dt(tstamps)
            tstamps_trend[run_tstamp] = tstamps
    return tstamps_trend

def labview_to_dt(labview_tstamps):
    """
    Convert timestamps from absolute epoch (1904) to utc datetime format
    """
    labview_dates = np.vectorize(datetime.utcfromtimestamp)(labview_tstamps)
    true_dates = labview_dates - np.vectorize(relativedelta)(years = LABVIEW_OFFSET)
    return true_dates

def calculate_time_metrics(tstamps_event, tstamps_trend, file_date):

    sorted_trend_grps = sorted(list(tstamps_trend.keys()))

    earliest_event = tstamps_event[0]
    last_event = tstamps_event[-1]
    earliest_trend_grp = sorted_trend_grps[0]
    earliest_trend_tstamp = tstamps_trend[earliest_trend_grp][0]
    last_trend_tstamp = tstamps_trend[sorted_trend_grps[-1]][-1]

    print(file_date)
    print(earliest_event, last_event)
    for trend_grp in sorted_trend_grps:
        earliest_trend_tstamp = tstamps_trend[trend_grp][0]
        last_trend_tstamp = tstamps_trend[trend_grp][-1]
        print(trend_grp, earliest_trend_tstamp, last_trend_tstamp)

    pulsing_delay = earliest_event - earliest_trend_tstamp
    logging_lag = last_trend_tstamp - last_event
    labelling = earliest_trend_grp - earliest_trend_tstamp

    return (pulsing_delay, logging_lag, labelling)

def timestamp_processor(event_path, *trend_paths):

    file_date = parser.parse(event_path.stem.split("_")[1])
    trend_path = trend_event_checker(event_path, *trend_paths)
    tstamps_event = extract_event_tstamps(event_path)

    tstamps_trend = {}
    if trend_path:
        tstamps_trend = extract_trend_tstamps(trend_path)
        return calculate_time_metrics(tstamps_event, tstamps_trend, file_date)
    else:
        return ("", "", "")

def timedelta_to_seconds(delta):
    if delta:
        return delta.total_seconds()
    else:
        return None

def to_histogram(val_arr, bin_num, out_path, title, savename):
    val_arr = np.vectorize(timedelta_to_seconds)(np.array(val_arr))/3600
    val_arr = val_arr[~np.isnan(val_arr)]

    n, bins, patches = plt.hist(val_arr, bins = bin_num)

    plt.xlabel("Time difference (Hrs)")
    plt.ylabel("Frequency")
    plt.title(title)
    plt.savefig(out_path/savename)
    plt.close()
    return





# class trendrun:
#
#     "Processing tasks for trend data"
#
#     def __init__(self, rungroup, dateformat):
#         self.group = rungroup
#         self.DATE_FORMAT = dateformat
#         self.true_tstamps_utc = self.labview_to_unix()
#         self.time_init = self.calc_time_init()
#
#     def calc_time_init(self):
#         run_name = self.group.name
#         dt = datetime.strptime(run_name, self.DATE_FORMAT)
#         return dt
#         #CHANGELOG: have reason to believe that the recorded times are already
#         #in UTC, so no time conversion required.
#         #local = pytz.timezone("Europe/Zurich")
#         #local_dt = local.localize(naive, is_dst = None)
#         #utc_dt = local_dt.astimezone(pytz.utc)
#
#     def calc_rel_time(self):
#         tstamps_raw = np.array(self.group["Timestamp"])
#         tstamps_min = np.amin(tstamps_raw)
#         tstamps_init = tstamps_raw[0]
#
#         if tstamps_min == tstamps_init:
#             tstamps_rel = tstamps_raw - tstamps_min
#             tstamps_rel_posix = tstamps_rel + self.time_init_posix
#             tstamps_rel_utc = np.vectorize(datetime.utcfromtimestamp)(tstamps_rel)
#             return tstamps_rel, tstamps_rel_posix, tstamps_rel_utc
#         else:
#             return "Timestamp array out of order!"
#
#     def labview_to_unix(self):
#         labview_tstamps = np.array(self.group["Timestamp"])
#         labview_dates = np.vectorize(datetime.utcfromtimestamp)(labview_tstamps)
#         true_dates = labview_dates - np.vectorize(relativedelta)(years = LABVIEW_OFFSET)
#         return true_dates
#
#
#     """
#     def posix_to_utc(self):
#         tstamps = list(np.array(self.group['Timestamp']))
#         utcs = [datetime.fromtimestamp(tstamp, tz = pytz.utc) for tstamp in tstamps]
#         return utcs
#     """
