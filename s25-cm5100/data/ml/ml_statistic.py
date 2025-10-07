#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from __future__ import annotations

__author__ = "Chao Yang"
__version__ = "1.0"


"""
Get the statistics of the dataset
"""
from collections import defaultdict

import numpy as np


def get_histogram(data, bin_size=10, range=None, density=False):

    bins = int(data.max() - data.min() / bin_size)
    hist, bin_edges = np.histogram(data, bins=bins, range=range, density=density)
    return hist, bin_edges


def grid_dataset(data, grid_size):
    """
    Grid the dataset into a fixed size grid
    """
    data_grid = (data / grid_size).astype(int)
    grid_dict = defaultdict(list)
    for i, j in enumerate(data_grid):
        grid_dict[f"{j[0]}_{j[1]}"].append(i)
    data_grid = (
        np.array([ikey.split("_") for ikey in grid_dict.keys()], int) * grid_size
    )
    num = np.array([len(grid_dict[ikey]) for ikey in grid_dict.keys()])

    #  select = np.array([grid_dict[key][0] for key in grid_dict.keys()], int)
    return data_grid, num
