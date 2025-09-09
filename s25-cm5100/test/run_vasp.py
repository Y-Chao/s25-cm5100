import os
import sys
import subprocess
import numpy as np
from ase.io import read
import ase.calculators.vasp as vasp_calculator
from ase.calculators.vasp import create_input
from ase.data import atomic_masses, atomic_numbers
from ase.io.vasp import _symbol_count_from_symbols

# Generic VASP calculator common for all cases
calc = vasp_calculator.Vasp(
           #Performance
           istart=0,  # 0, start from scratch; 1, start from WAVECAR
           iniwav=1,  # 0, for jellium orbitals; 1, for random number
           icharg=2,  # 0, calculated from WAVECAR; 2, superpositions
           
           ncore=4,  #Parallelization
           kpar=1,    #Parallelization over nodes
           #nsim=1,
           ispin=1,
           #npar=4,
           isym=0,

           #DFT parameters
           encut=450,  #PW cutoff
           gamma=False,
           #kspacing=0.25,  #kpt
           xc='PBE',         #xc for pseudopotential
           #gga='RP',         #actual xc
           ismear=0,         # 0 for gaussian smearing; 2 for MP
           sigma=0.05,       #Fermi temperature
           lreal='false',    # projection operators are evaluated in real-space or reciprocal space           

           #Structure optimization
           ibrion=-1,   #optimization method. 0, for md; 1, for RMM-DIIS; 2, for cg
           #isif=3,
           #potim=0.1,
           #nsw=5000,  # number of time steps

           #CONVERGENCE
           algo = 'all',
           isearch = 1,
           ediffg=-0.05,
           ediff=5e-6,
           prec='Accurate',
           nelmin=4,
           nelm=120,
           #amix=0.2,
           #bmix=0.0001,
            
           #OUTPUT
           lvhar=False,       #write hartree potential
           lwave=False,       #write WAVCAR
           #lcharg=False,       #write CHARGECAR
           laechg=False,

           # OTHER
           ivdw=12,   # DFT-D3. 11, for no damping; 12, fo BJ-damping
           #lasph=True,
           #lorbit=11,
                   )

atom = read("init.vasp")
atom.calc = calc
energy = atom.get_potential_energy()
