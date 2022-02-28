import os
import sys
from pathlib import Path
import concurrent.futures

import h5py
import numpy as np
import pandas as pd
import csv
import time

api_dir = "/home/student.unimelb.edu.au/pushkarnap/Documents/research/xbox_mlbd/project_scripts"

if api_dir not in sys.path:
    sys.path.insert(0, api_dir)

from trend_funcs.timing_funcs import *

def make_dims(channel_list, fhand, key):

    rows = len(channel_list)
    cols = len(fhand[key][channel_list[0]])
    return (rows, cols)

def make_run_matrix(channel_list, fhand, key):

    rows, cols = make_dims(channel_list, fhand, key)
    run_matrix = np.empty((rows, cols))
    for i in range(len(channel_list)):
        channel = np.array(fhand[key][channel_list[i]])
        if len(channel) == cols:
            run_matrix[i] = channel
        else:
            print("ALARM")
    return np.transpose(run_matrix).tolist()

def run_matrix_writer(trend_path, writer):

    with h5py.File(trend_path, "r") as fhand:
        print(f"processing {trend_path.stem}")
        for key in fhand:
            run_matrix = make_run_matrix(channel_list, fhand, key)
            writer.writerows(run_matrix)
        print(f"done processing {trend_path.stem}")

def trend_data_to_csv(trend_paths, csv_name, channel_list):

    with open(csv_name, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(channel_list)
        for trend_path in trend_paths:
            run_matrix_writer(trend_path, writer)

if __name__ == "__main__":
    path_l3 = Path("/home/student.unimelb.edu.au/pushkarnap/Documents/research/xbox_mlbd/Data/Xbox3_TD24_bo_L3_HDF/data")
    path_l4 = Path("/home/student.unimelb.edu.au/pushkarnap/Documents/research/xbox_mlbd/Data/Xbox3_TD24_ubo_L4_HDF")
    out_path = Path("/home/student.unimelb.edu.au/pushkarnap/Documents/research/xbox_mlbd/project_scripts/timestamp_scripts/output")

    # trend_paths_l3 = list(path_l3.glob("TrendData*.hdf"))
    trend_paths = list(path_l4.glob("TrendData*.hdf"))

    test_files = trend_paths
    channel_list = ['1PKIA_amp max','1PKIA_amp pulse width',
                    '1PKIB_amp max','1PKIB_amp pulse width',
                    '2PKIA_amp max','2PKIA_amp pulse width',
                    '2PKIB_amp max','2PKIB_amp pulse width',
                    'Pulse Count 1', 'Pulse Count 2',
                    'Timestamp']

    time_init = time.perf_counter()
    trend_data_to_csv(test_files, "conditioning_data_kly.csv", channel_list)
    time_fin = time.perf_counter()
    print(time_fin - time_init)
