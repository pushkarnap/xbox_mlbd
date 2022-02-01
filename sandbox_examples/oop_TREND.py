from datetime import datetime, timezone
from dateutil.relativedelta import relativedelta
import pytz
import numpy as np

LABVIEW_OFFSET = 66 #years

class trendrun:

    "Processing tasks for trend data"

    def __init__(self, rungroup, dateformat):
        self.group = rungroup
        self.DATE_FORMAT = dateformat
        self.true_tstamps_utc = self.labview_to_unix()
        self.time_init = self.calc_time_init()

    def calc_time_init(self):
        run_name = self.group.name
        dt = datetime.strptime(run_name, self.DATE_FORMAT)
        return dt
        #CHANGELOG: have reason to believe that the recorded times are already
        #in UTC, so no time conversion required.
        #local = pytz.timezone("Europe/Zurich")
        #local_dt = local.localize(naive, is_dst = None)
        #utc_dt = local_dt.astimezone(pytz.utc)

    def calc_rel_time(self):
        tstamps_raw = np.array(self.group["Timestamp"])
        tstamps_min = np.amin(tstamps_raw)
        tstamps_init = tstamps_raw[0]

        if tstamps_min == tstamps_init:
            tstamps_rel = tstamps_raw - tstamps_min
            tstamps_rel_posix = tstamps_rel + self.time_init_posix
            tstamps_rel_utc = np.vectorize(datetime.utcfromtimestamp)(tstamps_rel)
            return tstamps_rel, tstamps_rel_posix, tstamps_rel_utc
        else:
            return "Timestamp array out of order!"

    def labview_to_unix(self):
        labview_tstamps = np.array(self.group["Timestamp"])
        labview_dates = np.vectorize(datetime.utcfromtimestamp)(labview_tstamps)
        true_dates = labview_dates - np.vectorize(relativedelta)(years = LABVIEW_OFFSET)
        return true_dates


    """
    def posix_to_utc(self):
        tstamps = list(np.array(self.group['Timestamp']))
        utcs = [datetime.fromtimestamp(tstamp, tz = pytz.utc) for tstamp in tstamps]
        return utcs
    """
