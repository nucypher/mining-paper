#!/usr/bin/env python3

import matplotlib.pyplot as plt
import math
import numpy as np

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
plt.rcParams.update(params)
plt.figure(1)
plt.clf()
a = 0.17
b = 0.21
plt.axes([a, b, 0.96-a, 0.97-b])

my_reward = 1.0
network_reward = (1.0 + 0.5) / 2  # uniform distribution
staked = 0.60
T12 = 365 * 2
I0 = 1.0 / 365  # Initial reward rate
Tavg = T12 / network_reward  # actual halving time


def plot(tmax=5, reward=my_reward, **kw):
    tmax = tmax * 365
    t = np.linspace(0, tmax, 50)
    S = 1.0 + network_reward * I0 * Tavg / np.log(2) * (1.0 - 2 ** (- t / Tavg))
    Smax = 1.0 + network_reward * I0 * Tavg / np.log(2)
    rate = reward * np.log(2) / (staked * S * T12) * (Smax - S)
    plt.plot(t / 365, rate * 100, linewidth=1, **kw)


def label():
    plt.title('Daily reward rate')
    plt.xlabel('Time (years)')
    plt.ylabel('Daily reward rate (%)')


if __name__ == '__main__':
    plot(reward=1.0, color='blue', label='1 year+ staking')
    plot(reward=0.5 * (1 + 1./12), color='red', linestyle='--', label='1 month staking')
    label()
    plt.legend()
    plt.savefig('daily-compensation.pdf')
