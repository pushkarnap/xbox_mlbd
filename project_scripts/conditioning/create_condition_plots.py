import os
import sys
from pathlib import Path
import concurrent.futures

import h5py
import numpy as np
import pandas as pd
import time

import matplotlib.pyplot as plt

api_dir = "/home/student.unimelb.edu.au/pushkarnap/Documents/research/xbox_mlbd/project_scripts"

if api_dir not in sys.path:
    sys.path.insert(0, api_dir)

from trend_funcs.timing_funcs import *

def norm_tstamp(tstamps, div):
    return (tstamps - np.amin(tstamps))/div

def create_condition_plot(xpts1, xpts2, ypts1, ypts2, labels):

    fig, ax = plt.subplots()
    ax2 = ax.twinx()
    plt.title(labels["title"])

    ax.plot(xpts1, ypts1, marker = ",", linewidth = 0,
            color = labels["color1"], alpha = labels["alpha"])

    ax2.plot(xpts2, ypts2, marker = ",", linewidth = 0,
            color = labels["color2"])

    ax.set_xlabel(labels["xlabel"])
    ax.set_ylabel(labels["ylabel1"])
    ax2.set_ylabel(labels["ylabel2"])
    fig.savefig(labels['savename'])

    return

if __name__ == "__main__":
    df_data = pd.read_csv("conditioning_data.csv").dropna()

    NOISE_THRESH = 650000 #650kW noise threshhold set by Lee Millar
    ALPHA = 0.002
    line1_noise_cond = np.array(df_data["1PSI_amp max"]) > NOISE_THRESH
    line2_noise_cond = np.array(df_data["2PSI_amp max"]) > NOISE_THRESH
    noise_red_cond = np.logical_and(line1_noise_cond, line2_noise_cond)
    df_noise_red = df_data.loc[noise_red_cond, :]

    #remove zeros from pulse width data and put in new frames
    zero_cond_pw1 = np.array(df_noise_red["1PSI_amp pulse width"]).astype("bool")
    zero_cond_pw2 = np.array(df_noise_red["2PSI_amp pulse width"]).astype("bool")
    df_zero_rm1 = df_noise_red.loc[zero_cond_pw1, ["1PSI_amp pulse width", "Pulse Count 1", "Timestamp"]]
    df_zero_rm2 = df_noise_red.loc[zero_cond_pw2, ["2PSI_amp pulse width", "Pulse Count 2", "Timestamp"]]

    HOUR = 3600

    label_dict = {
    "title": "Conditioning plot for Line 1 in XBOX3 data",
    "color1": "blue",
    "color2": "green",
    "alpha": ALPHA,
    "xlabel": "Timestamp [hrs]",
    "ylabel1": "Max input power to structure [MW] (blue)",
    "ylabel2": r"Structure input power pulse width [$\mu s$] (green)",
    "savename": "output/condition1_t.png"
    }
    tstamps1 = norm_tstamp(df_noise_red["Timestamp"], HOUR)
    psi1 = df_noise_red["1PSI_amp max"]/1e6
    tstamps2 = norm_tstamp(df_zero_rm1["Timestamp"], HOUR)
    pw1 = df_zero_rm1["1PSI_amp pulse width"]*1e6
    create_condition_plot(tstamps1, tstamps2, psi1, pw1, label_dict)

    label_dict = {
    "title": "Conditioning plot for Line 1 in XBOX3 data",
    "color1": "blue",
    "color2": "green",
    "alpha": ALPHA,
    "xlabel": "Pulse Count [Millions]",
    "ylabel1": "Max input power to structure [MW] (blue)",
    "ylabel2": r"Structure input power pulse width [$\mu s$] (green)",
    "savename": "output/condition1_p.png"
    }
    pc1 = df_noise_red["Pulse Count 1"]/1e6
    psi1 = df_noise_red["1PSI_amp max"]/1e6
    pc1ax2 = df_zero_rm1["Pulse Count 1"]/1e6
    pw1 = df_zero_rm1["1PSI_amp pulse width"]*1e6
    create_condition_plot(pc1, pc1ax2, psi1, pw1, label_dict)

    label_dict = {
    "title": "Conditioning plot for Line 2 in XBOX3 data",
    "color1": "blue",
    "color2": "green",
    "alpha": ALPHA,
    "xlabel": "Timestamp [hrs]",
    "ylabel1": "Max input power to structure [MW] (blue)",
    "ylabel2": r"Structure input power pulse width [$\mu s$] (green)",
    "savename": "output/condition2_t.png"
    }
    tstamps1 = norm_tstamp(df_noise_red["Timestamp"], HOUR)
    psi2 = df_noise_red["2PSI_amp max"]/1e6
    tstamps2 = norm_tstamp(df_zero_rm2["Timestamp"], HOUR)
    pw2 = df_zero_rm2["2PSI_amp pulse width"]*1e6
    create_condition_plot(tstamps1, tstamps2, psi1, pw1, label_dict)

    label_dict = {
    "title": "Conditioning plot for Line 2 in XBOX3 data",
    "color1": "blue",
    "color2": "green",
    "alpha": ALPHA,
    "xlabel": "Pulse Count [Millions]",
    "ylabel1": "Max input power to structure [MW] (blue)",
    "ylabel2": r"Structure input power pulse width [$\mu s$] (green)",
    "savename": "output/condition2_p.png"
    }
    pc2 = df_noise_red["Pulse Count 2"]/1e6
    psi2 = df_noise_red["2PSI_amp max"]/1e6
    pc2ax2 = df_zero_rm2["Pulse Count 2"]/1e6
    pw2 = df_zero_rm2["2PSI_amp pulse width"]*1e6
    create_condition_plot(pc2, pc2ax2, psi2, pw2, label_dict)
