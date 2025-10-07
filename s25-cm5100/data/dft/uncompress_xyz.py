import os
import sys
from glob import glob

import numpy as np
from ase.io import read, write
from tqdm import tqdm

atoms = read(sys.argv[1], index=":")

if os.path.exists("joblist.dat"):
    os.remove("joblist.dat")

print(f"The length of your sturcture is {len(atoms)}")
for i, atom in tqdm(enumerate(atoms), total=len(atoms), desc="Distributing structures"):
    directory = f"{i:05d}"
    if not os.path.exists(directory):
        os.makedirs(directory)
    write(f"{directory}/init.vasp", atom)
    cell = atom.cell.cellpar()[:3]
    if np.all(cell > 16):
        with open(f"{directory}/type.dat", "w") as f:
            f.write("cluster")
    elif np.sum(cell > 16) == 1:
        with open(f"{directory}/type.dat", "w") as f:
            f.write("surface")
    else:
        with open(f"{directory}/type.dat", "w") as f:
            f.write("bulk")

all_jobs = glob("*/init.vasp")
jobs_info = [f"{i:05d}" for i in range(len(all_jobs))]
jobs_info = "\n".join(jobs_info)
with open("joblist.dat", "w") as fd:
    fd.write(jobs_info)
