import numpy as np


def sine(len=5*np.pi, res=0.1):
    return np.sin(np.arange(0, len, res))


def comb(len=5*np.pi, res=0.1, f2=1.3):
    return list(np.sin(np.arange(0, len, res)) + np.sin(f2*np.arange(0, len, res)))


def two_class_labeled_signals(total=1):
    return [comb(f2=1.3)+['class 1'] * total] + \
        [comb(f2=1.6)+['class 2'] * total]