#!/usr/bin/env bash
INPATH="/home/student.unimelb.edu.au/pushkarnap/Documents/research/xbox_mlbd/Data/Xbox3_TD24_ubo_L4/EVENTdata"
DESTPATH="/home/student.unimelb.edu.au/pushkarnap/Documents/research/xbox_mlbd/Data/Xbox3_TD24_ubo_L4_HDF"

CWD=$(pwd)
echo "Current working directory is:"
echo $CWD

declare -a infiles

cd $INPATH
for file in $(ls *.tdms)
do
    infiles=("${infiles[@]}" "$file")
done

cd $CWD
for file in "${infiles[@]}"
do
    echo "NOW CONVERTING: ${file}"
    python3 singlefile_converter.py "${INPATH}/${file}" "${DESTPATH}"
done | tee conversion_log_ubo_3.txt
