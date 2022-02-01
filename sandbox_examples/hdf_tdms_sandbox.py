import os
import sys
from pathlib import Path

import h5py
from nptdms import TdmsFile, tdms

import numpy as np
from oop_calc import trendrun
#import pprint as pp

api_dir = "/home/student.unimelb.edu.au/pushkarnap/Documents/research/rfstudies"
tdms_path = Path("/home/student.unimelb.edu.au/pushkarnap/Documents/research/xbox_mlbd/sandbox_examples/Xbox3_TD24_bo_L3")
hdf_path = Path("/home/student.unimelb.edu.au/pushkarnap/Documents/research/xbox_mlbd/sandbox_examples/hdf_data")
hdfdata_path = Path("/home/student.unimelb.edu.au/pushkarnap/Documents/research/xbox_mlbd/sandbox_examples/hdf_data/data")

FIRST_TRANSFORM = 0

if api_dir not in sys.path:
    sys.path.insert(0, api_dir)

from src.transformation import transform

if FIRST_TRANSFORM:
    transform(tdms_dir=tdms_path, hdf_dir=hdf_path)

DATE_FORMAT = "/%Y.%m.%d-%H:%M:%S.%f"
with h5py.File(hdfdata_path/"TrendData_20200211.hdf", "r") as fhand:
    keys = fhand.keys()
    runs = [trendrun(fhand[key], DATE_FORMAT) for key in keys]
    for run in runs:
        print(run.time_init_posix)
        print(np.array(run.group['Timestamp']))

"""
with h5py.File(hdfdata_path/"EventDataA_20200211.hdf", "r") as fhand:
    pulses = [val for val in fhand.values()]
    expuls = pulses[0]
    chls = [val for val in expuls.values()]
    for chl in chls:
        for chl_attr in chl.attrs.__iter__():
            print(chl_attr)

with TdmsFile.open(tdms_path/"TrendData_20200211.tdms") as fhand:
    #pp.pprint(fhand.__dict__)
    runs = fhand.groups()
    exrun = runs[0]
    #pp.pprint(exrun.__dict__)
    channels = exrun.channels()
    exchl = channels[0]
    #pp.pprint(exchl.__dict__)

with TdmsFile.open(tdms_path/"EventDataA_20200211.tdms") as fhand:
    #pp.pprint(fhand.__dict__)
    runs = fhand.groups()
    exrun = runs[0]
    #pp.pprint(exrun.__dict__)
    channels = exrun.channels()
    exchl = channels[0]
    #pp.pprint(exchl.__dict__)

with h5py.File(hdfdata_path/"TrendData_20200211.hdf", "r") as fhand:
    #pp.pprint(fhand.__dict__)
    file_attr_iter = fhand.attrs.__iter__()
    #for file_attr in file_attr_iter:
        #pp.pprint(file_attr)

    runs = [fhand[key] for key in list(fhand.keys())]
    exrun = runs[0]
    #pp.pprint(runs)

    #pp.pprint(exrun.__dict__)
    run_attr_iter = exrun.attrs.__iter__()
    #for run_attr in run_attr_iter:
        #pp.pprint(run_attr)

    channels = [exrun[key] for key in list(exrun.keys())]
    exchl = channels[0]
    #pp.pprint(channels)

    #pp.pprint(exchl.__dict__)
    chl_attr_iter = exchl.attrs.__iter__()
    #for chl_attr in chl_attr_iter:
        #pp.pprint(chl_attr)

with h5py.File(hdfdata_path/"EventDataA_20200211.hdf", "r") as fhand:
    pp.pprint(fhand.__dict__)
    file_attr_iter = fhand.attrs.__iter__()
    for file_attr in file_attr_iter:
        pp.pprint(file_attr)

    pulses = [fhand[key] for key in list(fhand.keys())]
    expuls = pulses[0]
    #pp.pprint(runs)

    pp.pprint(expuls.__dict__)
    puls_attr_iter = expuls.attrs.__iter__()
    for puls_attr in puls_attr_iter:
        pp.pprint(puls_attr)

    channels = [expuls[key] for key in list(expuls.keys())]
    exchl = channels[0]
    #pp.pprint(channels)

    pp.pprint(exchl.__dict__)
    chl_attr_iter = exchl.attrs.__iter__()
    for chl_attr in chl_attr_iter:
        pp.pprint(chl_attr)
"""

"""
date_format = "%Y.%m.%d-%H:%M:%S.%f"
run_labels = [datetime.strptime(run, date_format) for run in runs]
print(run_labels)

DATE_FORMAT = "/%Y.%m.%d-%H:%M:%S.%f"
with h5py.File(hdfdata_path/"TrendData_20200211.hdf", "r") as fhand:
    keys = fhand.keys()
    runs = [trendrun(fhand[key], DATE_FORMAT) for key in keys]
    for run in runs:
        print(run.time_init_posix)
        #print(np.array(run.group['Timestamp']))

with h5py.File(hdfdata_path/"EventDataA_20200211.hdf", "r") as fhand:
    pulses = list(fhand.keys())
    example_pulse = pulses[0]
    print(f"{example_pulse}\n")
    example_e_channels = list(fhand[example_pulse].keys())
    for channel in example_e_channels:
        chl_data = fhand[example_pulse][channel]
        #print(f"{channel}: {chl_data.shape}, {chl_data.size}, {chl_data.ndim}, {chl_data.dtype}, {chl_data.nbytes}")


with h5py.File(hdfdata_path/"TrendData_20200211.hdf", "r") as fhand:
    trend_runs = list(fhand.keys())
    example_run = trend_runs[0]
    print(f"{example_run}\n")
    example_t_channels = list(fhand[example_run].keys())
    tstamp = fhand[example_run]['Timestamp']
    print(np.array(tstamp))
    print(tstamp)


    #for channel in example_t_channels:
        #chl_data = fhand[example_run][channel]
        #print(f"{channel}: {chl_data.shape}, {chl_data.size}, {chl_data.ndim}, {chl_data.dtype}, {chl_data.nbytes}")

print("")

with h5py.File(hdfdata_path/"EventDataA_20200211.hdf", "r") as fhand:
    pulses = list(fhand.keys())
    example_pulse = pulses[0]
    print(f"{example_pulse}\n")
    example_e_channels = list(fhand[example_pulse].keys())
    for channel in example_e_channels:
        chl_data = fhand[example_pulse][channel]
        #print(f"{channel}: {chl_data.shape}, {chl_data.size}, {chl_data.ndim}, {chl_data.dtype}, {chl_data.nbytes}")

#bash scripting attempt

#!/bin/bash
TDMS_PATH=/home/student.unimelb.edu.au/pushkarnap/Documents/research/xbox_mlbd/lee_xbox_example/Xbox3_TD24_bo_L3
HDF_PATH=/home/student.unimelb.edu.au/pushkarnap/Documents/research/xbox_mlbd/lee_xbox_example/hdf_data
TRANSFORM_PATH=/home/student.unimelb.edu.au/pushkarnap/Documents/research/rfstudies/src
cd $TRANSFORM_PATH
python transformation.py $TDMS_PATH $HDF_PATH --verbose |& tee $HDF_PATH/transform_log.txt
"""
