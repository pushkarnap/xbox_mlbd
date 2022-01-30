import os
import sys
from pathlib import Path

import h5py
import numpy as np
import matplotlib.pyplot as plt

from runpulseobj import trendrun

hdfdata_path = Path("/home/student.unimelb.edu.au/pushkarnap/Documents/research/xbox_mlbd/lee_xbox_example/hdf_data/data")
out_path = Path("/home/student.unimelb.edu.au/pushkarnap/Documents/research/xbox_mlbd/lee_xbox_example/output")
DATE_FORMAT = "/%Y.%m.%d-%H:%M:%S.%f"

with h5py.File(hdfdata_path/"TrendData_20200211.hdf", "r") as fhand:
    run_names = list(fhand.keys())
    run_groups = [trendrun(fhand[run_name], DATE_FORMAT) for run_name in run_names]

    for run_group in run_groups:
        name = run_group.group.name[1:]
        name_utc = run_group.time_init_utc
        tstamps = np.array(run_group.group["Timestamp"])
        tstamps_diff = np.diff(tstamps)

        n, bins, patches = plt.hist(tstamps_diff, bins = 'auto')

        plt.xlabel("Increment (mystery units)")
        plt.ylabel("Frequency")
        plt.title("Distbt of time increment in Timestamp")
        plt.savefig(out_path/f"diffhist_{name}.png")
        plt.close()
