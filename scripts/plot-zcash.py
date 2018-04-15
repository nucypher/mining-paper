#!/usr/bin/env python3

import pylab
import json
import math
import numpy as np
from datetime import datetime
import matplotlib.dates as mdates

# Configure matplotlib for publication quality
# http://www.scipy.org/Cookbook/Matplotlib/LaTeX_Examples
# thesis: 345
fig_width_pt = 246.0
inches_per_pt = 1.0/72.27               # Convert pt to inches
golden_mean = (math.sqrt(5)-1.0)/2.0         # Aesthetic ratio
fig_width = fig_width_pt * inches_per_pt  # width in inches
fig_height = fig_width * golden_mean       # height in inches
fig_size = [fig_width, fig_height]
params = {
    'backend': 'ps',
    'axes.labelsize': 8,
    'axes.linewidth': 0.35,
    'font.family': 'serif',
    'font.size': 8,
    'legend.fontsize': 8,
    'xtick.labelsize': 6,
    'ytick.labelsize': 6,
    'xtick.major.size': 2,
    'ytick.major.size': 2,
    'text.usetex': False,
    'figure.figsize': fig_size,
    'lines.linewidth': 0.2,
    'lines.markeredgewidth': 0.2,
}
pylab.rcParams.update(params)
pylab.figure(1)
pylab.clf()
a = 0.17
b = 0.21

with open('zcash.json') as f:
    data = json.load(f)

data = np.array(data)
t = np.array([datetime.fromtimestamp(i // 1000) for i in data[:, 0]])
price = data[:, 1]
cond = t < datetime(year=2017, month=8, day=30)
t = t[cond]
price = price[cond]

fmt = mdates.DateFormatter('%m/%y')
ax = pylab.axes([a, b, 0.96-a, 0.97-b])
ax.xaxis.set_major_formatter(fmt)

pylab.semilogy(t, price)
pylab.xlabel('Time')
pylab.ylabel('ZCash price (USD)')
pylab.savefig('zcash-price.pdf')
