import os
import sys
from pathlib import Path
from dateutil import parser
import time
import concurrent.futures
import pickle

import h5py

api_dir = "/home/student.unimelb.edu.au/pushkarnap/Documents/research/xbox_mlbd/project_scripts"

if api_dir not in sys.path:
    sys.path.insert(0, api_dir)

from trend_funcs.timing_funcs import *

if __name__ == "__main__":

    path_l3 = Path("/home/student.unimelb.edu.au/pushkarnap/Documents/research/xbox_mlbd/Data/Xbox3_TD24_bo_L3_HDF/data")
    path_l4 = Path("/home/student.unimelb.edu.au/pushkarnap/Documents/research/xbox_mlbd/Data/Xbox3_TD24_ubo_L4_HDF")

    pulse_delays = []
    trend_lags = []
    label_errs = []

    with concurrent.futures.ProcessPoolExecutor() as executor:
        event_paths = list(path_l4.glob("EventData*.hdf"))
        results = [executor.submit(timestamp_processor, event_path, path_l3, path_l4) for event_path in event_paths]

        for f in concurrent.futures.as_completed(results):
            delay, lag, err = f.result()
            pulse_delays.append(delay)
            trend_lags.append(lag)
            label_errs.append(err)

    with open("timestampB.pickle", "wb") as fhand:
        pickle.dump((pulse_delays, trend_lags, label_errs), fhand)
