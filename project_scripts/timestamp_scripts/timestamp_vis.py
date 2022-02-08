import pickle
from dateutil.relativedelta import relativedelta
from datetime import datetime
import numpy as np
import sys
import matplotlib.pyplot as plt
from pathlib import Path

api_dir = "/home/student.unimelb.edu.au/pushkarnap/Documents/research/xbox_mlbd/project_scripts"
out_path = Path("/home/student.unimelb.edu.au/pushkarnap/Documents/research/xbox_mlbd/project_scripts/timestamp_scripts/output")

if api_dir not in sys.path:
    sys.path.insert(0, api_dir)

from trend_funcs.timing_funcs import *

if __name__ == "__main__":
    pulse_delays = []
    trend_lags = []
    label_errs = []

    with open("timestampB.pickle", "rb") as fhand:
        pulse_delays, trend_lags, label_errs = pickle.load(fhand)

    to_histogram(pulse_delays, 20,
                    out_path,
                    "EVENT vs TREND earliest tstamp diff",
                    "event_trend_init_B.png")
    to_histogram(label_errs, 10,
                    out_path,
                    "TREND group label errors",
                    "trend_label_errs_B.png")
