#!/bin/bash

# ==========================================
# Configure your environment on NSCC server
# Written by Chao Yang
# Version 1.0
# ==========================================

check_hpc() {
    server_name=$(hostname)
    if [[ ${server_name} == asp2a* ]];then
        echo "NSCC"
    elif [[ ${server_name} == stdct* ]];then
        echo "VANDA"
    else
        echo
    fi
}

# --- Step 1: Create conda environment ---
echo "[INFO] Creating conda environment: cm5100"
server=check_hpc()
if [ server == "NSCC" ];then
    module load miniforge3
    conda create -n "cm5100" python=3.12 -y
    pip install pymatgen
    pip install mace
elif [ server == "VANDA" ];then
    module load Miniconda3/24.7.1-0
    conda create -n "cm5100" python=3.12 -y
    pip install pymatgen
    pip install mace
else
    echo "Wrong server"
    exit 0

# --- Step 2: Download prerequisite files ---
echo "[INFO] Download needed files to current directory"

# --- Step 3: Set environment variables ---
echo "[INFO] Setting environment variables"