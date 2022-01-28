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
        #self.utc_tstamp = self.posix_to_utc()

    def calc_time_init(self):
        run_name = self.group.name
        naive = datetime.strptime(run_name, self.DATE_FORMAT)
        local = pytz.timezone("Europe/Zurich")
        local_dt = local.localize(naive, is_dst = None)
        utc_dt = local_dt.astimezone(pytz.utc)
        return utc_dt

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
