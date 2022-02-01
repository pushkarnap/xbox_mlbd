import os
import sys
from pathlib import Path

import h5py
import numpy as np
import matplotlib.pyplot as plt

hdfdata_path = Path("/home/student.unimelb.edu.au/pushkarnap/Documents/research/xbox_mlbd/sandbox_examples/hdf_data/data")
out_path = Path("/home/student.unimelb.edu.au/pushkarnap/Documents/research/xbox_mlbd/sandbox_examples/output")

pulse_container = []
with h5py.File(hdfdata_path/"EventDataA_20200211.hdf", "r") as fhandA:
    with h5py.File(hdfdata_path/"EventDataB_20200211.hdf", "r") as fhandB:

        Apulse = list(fhandA.values())
        Bpulse = list(fhandB.values())

        all_pulse = Apulse + Bpulse
