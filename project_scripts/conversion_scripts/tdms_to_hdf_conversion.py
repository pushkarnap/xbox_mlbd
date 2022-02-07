import os
import sys
import subprocess as sp
from pathlib import Path
import time

api_dir = "/home/student.unimelb.edu.au/pushkarnap/Documents/research/rfstudies"
tdms_path_L3 = Path("/home/student.unimelb.edu.au/pushkarnap/Documents/research/xbox_mlbd/Data/Xbox3_TD24_bo_L3")
tdms_path_L4 = Path("/home/student.unimelb.edu.au/pushkarnap/Documents/research/xbox_mlbd/Data/Xbox3_TD24_ubo_L4/EVENTdata")
hdf_path_L3 = Path("/home/student.unimelb.edu.au/pushkarnap/Documents/research/xbox_mlbd/Data/Xbox3_TD24_bo_L3_HDF")
hdf_path_L4 = Path("/home/student.unimelb.edu.au/pushkarnap/Documents/research/xbox_mlbd/Data/Xbox3_TD24_ubo_L4_HDF")

if api_dir not in sys.path:
    sys.path.insert(0, api_dir)

from src.transformation import transform
from src.utils.transf_tools.converter import _convert_file

p1 = sp.run(['ls', str(tdms_path_L3)], capture_output = True, text = True)
L3filelist = p1.stdout.split()

for file in L3filelist:
    if not(".tdms_index" in file):
        print(f"converting {file}")
        _convert_file(tdms_path_L3/file, hdf_path_L3)
        print(f"cooldown")
        time.sleep(10)
