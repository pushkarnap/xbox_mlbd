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
    out_path = Path("/home/student.unimelb.edu.au/pushkarnap/Documents/research/xbox_mlbd/project_scripts/timestamp_scripts/output")
    TEST_FILE = "EventDataA_20200211.hdf"

    with h5py.File(path_l3/TEST_FILE, "r") as fhand:
        for pulse_name in fhand.keys():
            pulse = fhand[pulse_name]
            for channel_name in pulse.keys():
                channel = pulse[channel_name]
                plot_wf(channel, "Time (s)", channel.attrs["NI_ChannelName"], out_path)
            break

    # x_axis_chl_name = "Timestamp"
    # y_axis_chl_name = "Timestamp"

    """PLOT GENERATOR"""
    # with concurrent.futures.ProcessPoolExecutor() as executor:
    #     trend_paths = list(path_l3.glob("TrendData*.hdf"))
    #     results = [executor.submit(plot_trend_from_stitch,
    #                                     x_axis_chl_name, y_axis_chl_name,
    #                                     trend_path, out_path) for trend_path in trend_paths]
    #
    #     for f in concurrent.futures.as_completed(results):
    #         gaps = f.result()

    """STITCHING CHECKER"""
    # # print(stitch_check(path_l3/TEST_FILE))
    #
    # all_gaps = np.array([])
    #
    # with concurrent.futures.ProcessPoolExecutor() as executor:
    #     trend_paths = list(path_l3.glob("TrendData*.hdf"))
    #     results = [executor.submit(stitch_check, trend_path) for trend_path in trend_paths]
    #
    #     for f in concurrent.futures.as_completed(results):
    #         gaps = f.result()
    #         all_gaps = np.concatenate((all_gaps, gaps), axis = 0)
    #
    # print(all_gaps)
