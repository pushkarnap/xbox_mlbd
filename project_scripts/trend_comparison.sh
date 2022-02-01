#!/usr/bin/env bash
L3PATH="/home/student.unimelb.edu.au/pushkarnap/Documents/research/xbox_mlbd/Data/Xbox3_TD24_bo_L3"
L4PATH="/home/student.unimelb.edu.au/pushkarnap/Documents/research/xbox_mlbd/Data/Xbox3_TD24_ubo_L4/EVENTdata"
CWD=$(pwd)

echo "Current working directory is:"
echo $CWD

declare -a arrL3files_trend
declare -a arrL4files_trend

cd $L3PATH
for file in $(ls TrendData*.tdms)
do
    arrL3files_trend=("${arrL3files_trend[@]}" "$file")
done

cd $L4PATH
for file in $(ls TrendData*.tdms)
do
    arrL4files_trend=("${arrL4files_trend[@]}" "$file")
done

echo "Counting number of files in each directory"
echo ${#arrL3files_trend[@]}
echo ${#arrL4files_trend[@]}
echo "Done counting"

cd $CWD
for file in "${arrL3files_trend[@]}"
do
    echo $file
done > trendfilesL3.txt

for file in "${arrL4files_trend[@]}"
do
    echo $file
done > trendfilesL4.txt

echo "Comparing TREND files content in both directories"
diff -y trendfilesL3.txt trendfilesL4.txt > trendfile_cmp_general.txt
echo "Done comparing"

echo "1-to-1 file comparison"
for file in "${arrL3files_trend[@]}"
do
  echo "considering ${file}"
  if [[ " ${arrL4files_trend[*]} " =~ " ${file} " ]]; then
    cmp --silent "$L3PATH/$file" "$L4PATH/$file" || echo "files are different, ${file}"
  fi
done | tee trendfile_cmp_1t1.txt
echo "Done 1-to-1"
