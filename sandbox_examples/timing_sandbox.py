import os
import sys
from pathlib import Path

import h5py
import numpy as np
import matplotlib.pyplot as plt

from oop_TREND import trendrun

hdfdata_path = Path("/home/student.unimelb.edu.au/pushkarnap/Documents/research/xbox_mlbd/sandbox_examples/hdf_data/data")
out_path = Path("/home/student.unimelb.edu.au/pushkarnap/Documents/research/xbox_mlbd/sandbox_examples/output")
DATE_FORMAT = "/%Y.%m.%d-%H:%M:%S.%f"

with h5py.File(hdfdata_path/"TrendData_20200211.hdf", "r") as fhand:
    run_names = list(fhand.keys())
    run_groups = [trendrun(fhand[run_name], DATE_FORMAT) for run_name in run_names]

    for run_group in run_groups:
        grp_time = run_group.time_init
        tst amps = run_group.true_tstamps_utc
        print(grp_time)
        print(tstamps)





        """
        tstamps_diff = np.diff(tstamps)
        increment_var = np.var(tstamps_diff)

        n, bins, patches = plt.hist(tstamps_diff, bins = 'auto')

        plt.xlabel("Increment (mystery units)")
        plt.ylabel("Frequency")
        plt.title("Distbt of time increment in Timestamp")
        plt.text(0.9, 200, f"$\sigma = {increment_var:.5f}$")
        plt.savefig(out_path/f"diffhist_{name}.png")
        plt.close()
        """
