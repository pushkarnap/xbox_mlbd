import os
import sys
import h5py
from pathlib import Path

api_dir = "/home/student.unimelb.edu.au/pushkarnap/Documents/research/xbox_mlbd/project_scripts"

if api_dir not in sys.path:
    sys.path.insert(0, api_dir)

from trend_funcs.timing_funcs import *

if __name__ == "__main__":
    path_l3 = Path("/home/student.unimelb.edu.au/pushkarnap/Documents/research/xbox_mlbd/Data/Xbox3_TD24_bo_L3_HDF/data")
    path_l4 = Path("/home/student.unimelb.edu.au/pushkarnap/Documents/research/xbox_mlbd/Data/Xbox3_TD24_ubo_L4_HDF")
    out_path = Path("/home/student.unimelb.edu.au/pushkarnap/Documents/research/xbox_mlbd/project_scripts/timestamp_scripts/output")
    TEST_FILE = "TrendData_20200209.hdf"

    plot_trend_from_stitch("Timestamp", "DUT 1 Pressure",
                                path_l3/TEST_FILE, out_path)
