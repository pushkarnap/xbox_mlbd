import os
import sys
from pathlib import Path

api_dir = "/home/student.unimelb.edu.au/pushkarnap/Documents/research/rfstudies"
tdms_path = Path("/home/student.unimelb.edu.au/pushkarnap/Documents/research/xbox_mlbd/lee_xbox_example/Xbox3_TD24_bo_L3")
hdf_path = Path("/home/student.unimelb.edu.au/pushkarnap/Documents/research/xbox_mlbd/lee_xbox_example/hdf_data")

if api_dir not in sys.path:
    sys.path.insert(0, api_dir)

from src.transformation import transform
transform(tdms_dir=tdms_path, hdf_dir=hdf_path)














#bash scripting attempt
"""
#!/bin/bash
TDMS_PATH=/home/student.unimelb.edu.au/pushkarnap/Documents/research/xbox_mlbd/lee_xbox_example/Xbox3_TD24_bo_L3
HDF_PATH=/home/student.unimelb.edu.au/pushkarnap/Documents/research/xbox_mlbd/lee_xbox_example/hdf_data
TRANSFORM_PATH=/home/student.unimelb.edu.au/pushkarnap/Documents/research/rfstudies/src
cd $TRANSFORM_PATH
python transformation.py $TDMS_PATH $HDF_PATH --verbose |& tee $HDF_PATH/transform_log.txt
"""
