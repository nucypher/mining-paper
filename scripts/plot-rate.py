#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np


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
    plt.plot(t / 365, rate * 100, linewidth=2, **kw)


def label():
    plt.title('Daily reward rate')
    plt.xlabel('Time (years)')
    plt.ylabel('Daily reward rate (%)')


if __name__ == '__main__':
    plot(reward=1.0, color='blue', label='1 year+ staking')
    plot(reward=0.5 * (1 + 1./12), color='red', linestyle='--', label='1 month staking')
    label()
    plt.legend()
    plt.show()
