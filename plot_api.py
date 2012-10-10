#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function

# NOTE: this code doesn't necessarily work, it's almost pseudocode

import numpy as np
import matplotlib.pyplot as plt

import astropy.nddata import NDData
import astropy.table import Table

# The absolute simplest case is a one dimensional NDData object that is really
#   just a simple numpy array
one_d_data = NDData([1,2,3,4,5])
ax = one_d_data.plot() # show the data and return a matplotlib Axes object

fig = plt.figure()
ax = fig.add_subplot(111)
ax = one_d_data.plot(ax=ax) # plot the data to the supplied Axes object

# plot also accepts any kwargs, but just passes them blindly to the plotting command
ax = one_d_data.plot(color="r", linestyle="-", marker="o") 

# The next case is having a two-dimensional dataset, e.g. an image, where the 
#   plot() method is really calling imshow() internally
two_d_data = NDData(np.random.random(size=(100,100)))
ax = two_d_data.plot() # show the data and return a matplotlib AxesImage object

# If we have a high-dimensional object, it's up to the user to slice or project
#   that object down to two dimensions
high_d_data = NDData(np.random.random(size=(100,100,6,31,14)))
high_d_data[:,0,3,1,:].plot()
# or
high_d_data.project((0,2)).plot() # ?
