import os
import sys
from pathlib import Path
import concurrent.futures

import h5py

api_dir = "/home/student.unimelb.edu.au/pushkarnap/Documents/research/xbox_mlbd/project_scripts"

if api_dir not in sys.path:
    sys.path.insert(0, api_dir)

from trend_funcs.timing_funcs import *

if __name__ == "__main__":
    path_l3 = Path("/home/student.unimelb.edu.au/pushkarnap/Documents/research/xbox_mlbd/Data/Xbox3_TD24_bo_L3_HDF/data")
    path_l4 = Path("/home/student.unimelb.edu.au/pushkarnap/Documents/research/xbox_mlbd/Data/Xbox3_TD24_ubo_L4_HDF")
    out_path = Path("/home/student.unimelb.edu.au/pushkarnap/Documents/research/xbox_mlbd/project_scripts/timestamp_scripts/output")

    trend_paths = list(path_l3.glob("TrendData*.hdf"))
    event_paths = list(path_l3.glob("EventData*.hdf")) + list(path_l4.glob("EventData*.hdf"))

    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = [executor.submit(event_time_inc_dt, event_path) for event_path in event_paths]

        glob_increm = np.array([])
        for f in concurrent.futures.as_completed(results):
            increm = f.result()
            glob_increm = np.concatenate((glob_increm, increm), axis = 0)

    max = glob_increm < 100
    min = glob_increm > 0
    mask = np.logical_and(max, min)

    print(glob_increm)
    print(np.amax(glob_increm))
    print(np.amin(glob_increm))

    to_histogram(glob_increm, 100, out_path, "Time increment distribution", "glob_increm_dt.png")
    to_histogram(glob_increm[mask], 100, out_path, "Time increment distribution", "glob_increm_dt_shape.png")


    """TREND TIMESTAMP SPACING"""
        # with concurrent.futures.ProcessPoolExecutor() as executor:
        #     results = [executor.submit(trend_time_inc_dt, trend_path) for trend_path in trend_paths]
        #
        #     glob_increm = np.array([])
        #     for f in concurrent.futures.as_completed(results):
        #         increm = f.result()
        #         glob_increm = np.concatenate((glob_increm, increm), axis = 0)
        # max = glob_increm < 5
        # min = glob_increm > 0
        # mask = np.logical_and(max, min)
        # print(mask)
        #
        # print(np.amax(glob_increm))
        # print(np.amax(glob_increm[mask]))
        #
        # to_histogram(glob_increm, 100, out_path, "Time increment distribution", "glob_increm_dt.png")
        # to_histogram(glob_increm[mask], 100, out_path, "Time increment distribution", "glob_increm_shape_dt.png")
