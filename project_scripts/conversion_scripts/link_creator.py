import os
import sys
from pathlib import Path
import argparse as ap
import time

api_dir = "/home/student.unimelb.edu.au/pushkarnap/Documents/research/rfstudies"

if api_dir not in sys.path:
    sys.path.insert(0, api_dir)

from src.transformation import create_trend_ext_link, create_event_ext_link

HDF_PATH = Path("/home/student.unimelb.edu.au/pushkarnap/Documents/research/xbox_mlbd/Data/Xbox3_TD24_bo_L3_HDF")

print("NOW CREATING TREND DATA LINKS")
trend_init = time.perf_counter()
create_trend_ext_link(HDF_PATH)
trend_fin = time.perf_counter()
print("DONE CREATING TREND DATA LINKS")
print(f"TOOK {trend_fin - trend_init} second(s)")

print("NOW CREATING EVENT DATA LINKS")
event_init = time.perf_counter()
create_event_ext_link(HDF_PATH)
event_fin = time.perf_counter()
print("DONE CREATING EVENT DATA LINKS")
print(f"TOOK {event_fin - event_init} second(s)")
