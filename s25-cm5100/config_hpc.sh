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
server=$(check_hpc)
if [ $server == "NSCC" ];then
    module load miniforge3
    # For the first time use conda in a new shell
    eval "$(conda shell.bash hook)"
    condaenv=$(conda env list | grep cm5100)
    if [ ! -n "$condaenv" ]; then
        echo "Conda environment cm5100 does not exist. Creating..."
        conda create -n "cm5100" python=3.12 -y
        conda activate cm5100
        pip install ase
        pip install pymatgen
        pip install mace
    else
        echo "Conda environment cm5100 already exists. Activating..."
        conda activate cm5100
        pip install ase
    fi
elif [ $server == "VANDA" ];then
    module load Miniconda3/24.7.1-0
    # For the first time use conda in a new shell
    eval "$(conda shell.bash hook)"
    condaenv=$(conda env list | grep cm5100)
    if [ ! -n "$condaenv" ]; then
        echo "Conda environment cm5100 does not exist. Creating..."
        conda create -n "cm5100" python=3.12 -y
        conda activate cm5100
        pip install ase
        pip install pymatgen
        pip install mace
    else
        echo "Conda environment cm5100 already exists. Activating..."
        conda activate cm5100
        pip install ase
        pip install pymatgen
        pip install mace
    fi
else
    echo "Wrong server"
    exit 0
fi

# --- Step 2: Modify the ase calculator  ---
echo "[INFO] Patching the ase calculator"
ase_path=$(python -c "import ase; print(ase.__path__[0])")
echo "Finding ase path: $ase_path"
sed -i "/'ibrion',/a\ \ \ \ 'isearch'," $ase_path/calculators/vasp/create_input.py

# --- Step 3: Set environment variables ---
echo "[INFO] Setting environment variables"
read -p "Please input IP address: " ip
if [ -z "$ip" ]; then
    echo "No IP address provided. Exiting."
    exit 1
fi
cd s25-cm5100/data/dft/
echo "Downloading vasp and potential files from ${ip}"
wget "${ip}/vasp_651_intel_mkl_std"
wget "${ip}/potpaw_PBE.64.tar"

mkdir potpaw_PBE
tar -xvf potpaw_PBE.64.tar -C ${PWD}/potpaw_PBE
echo "Finished"

# --- Step 4: Test the installation ---
echo "[INFO] Testing the installation"
cd ~/s25-cm5100/s25-cm5100/test/
qsub sub_vasp.pbs
echo "Job submitted. Please check the job status using 'qstat -u $USER'"
echo "If the job completes successfully, you have configured your environment correctly."
echo "To activate the conda environment in future sessions, use: conda activate cm5100"
echo "Setup complete!"