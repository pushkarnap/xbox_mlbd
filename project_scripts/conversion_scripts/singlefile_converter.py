import os
import sys
from pathlib import Path
import argparse as ap

api_dir = "/home/student.unimelb.edu.au/pushkarnap/Documents/research/rfstudies"

if api_dir not in sys.path:
    sys.path.insert(0, api_dir)

from src.utils.transf_tools.converter import _convert_file

parser = ap.ArgumentParser(description = 'Single shot tdms to hdf file conversion')
parser.add_argument('input', help = 'full TDMS file path')
parser.add_argument('output', help = 'destination path for HDF5 files')
args = parser.parse_args()

_convert_file(Path(args.input), Path(args.output))
