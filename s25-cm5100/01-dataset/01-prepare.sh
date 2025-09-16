#!/bin/bash

# ==========================================
# Submit your batch jobs on NSCC server
# Written by Chao Yang
# Version 1.0
# ==========================================

echo "[INFO] Update your sm25-cm5100 repository"
git fetch origin
git reset --hard origin/main

echo "[INFO] Download your dataset to your scratch folder"
cd ~/scratch
read -p "Please input IP address: " ip
if [ -z "$ip" ]; then
    echo "No IP address provided. Exiting."
    exit 1
fi
read -p "Please input your file name: " file
if [ -z "$file" ]; then
    echo "No file name provided. Exiting."
    exit 1
fi
wget "${ip}/${file}" -O dataset.xyz

echo "[INFO] Preparing your dataset"
python ~/s25-cm5100/s25-cm5100/data/dft/uncompress_xyz.py dataset.xyz

echo "[INFO] Submitting your DFT jobs"
cp ~/s25-cm5100/s25-cm5100/data/dft/sub_vasp.pbs .
nohup python ~/s25-cm5100/s25-cm5100/data/dft/dpdispatch.py q >log 2>&1 &
echo "[INFO] Your jobs has been submited!"
echo "[INFO] Use 'qstat -t' to check the job status."
echo "[INFO] Use 'tail log' to check the log file."