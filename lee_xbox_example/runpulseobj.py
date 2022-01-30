from datetime import datetime, timezone
import pytz
import numpy as np

class trendrun:

    "Processing tasks for trend data"

    def __init__(self, rungroup, dateformat):
        self.group = rungroup
        self.DATE_FORMAT = dateformat
        self.time_init_utc = self.calc_time_init()
        self.time_init_posix = self.time_init_utc.timestamp()

    def calc_time_init(self):
        run_name = self.group.name
        naive = datetime.strptime(run_name, self.DATE_FORMAT)
        local = pytz.timezone("Europe/Zurich")
        local_dt = local.localize(naive, is_dst = None)
        utc_dt = local_dt.astimezone(pytz.utc)
        return utc_dt

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

    """
    def posix_to_utc(self):
        tstamps = list(np.array(self.group['Timestamp']))
        utcs = [datetime.fromtimestamp(tstamp, tz = pytz.utc) for tstamp in tstamps]
        return utcs
    """
class pulse:

    "Procssing tasks for pulse data"

    def __init__(self, pulsegroup):
        self.group = pulsegroup
