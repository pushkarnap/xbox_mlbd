#!/usr/bin/env bash
L3PATH="/home/student.unimelb.edu.au/pushkarnap/Documents/research/xbox_mlbd/Data/Xbox3_TD24_bo_L3"
L4PATH="/home/student.unimelb.edu.au/pushkarnap/Documents/research/xbox_mlbd/Data/Xbox3_TD24_ubo_L4/EVENTdata"
CWD=$(pwd)

mapfile -t trendfiles < diffonly_trendcmp.txt

echo "${trendfiles[@]}"

for file in "${trendfiles[@]}"
do
    echo "considering ${file}"
    cmp -l "${L3PATH}/${file}" "${L4PATH}/${file}"
done | tee granular_trenddiff.txt
