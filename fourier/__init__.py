
from math import sin, cos
import numpy as np


def tfd(x, inverse=False):
    """Compute the discrete Fourier Transform of the 1D array x"""
    N = x.shape[0]
    n = np.arange(N)
    k = n.reshape((N, 1))

    multiplier = 1 if inverse else -1
    divider = N if inverse else 1

    M = np.exp(multiplier * 2j * np.pi * k * n / N)

    return np.dot(M, x) / divider

def tfdi(x):
    return tfd(x, inverse=True)


def tfd2(x, inverse=False):
    callback = tfdi if inverse else tfd
    x = np.apply_along_axis(callback, axis=0, arr=x)
    x = np.apply_along_axis(callback, axis=0, arr=x.T)
    return x.T


def tfdi2(x):
    return tfd2(x, inverse=True)
