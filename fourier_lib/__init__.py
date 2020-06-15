
from math import sin, cos
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm


def tfd(x, inverse=False):
    """Compute the discrete Fourier Transform of the 1D array x"""

    N = x.shape[0]
    n = np.arange(N)
    k = n.reshape((N, 1))

    multiplier = 1 if inverse else -1
    divider = N if inverse else 1

    # get the base coefficient matrix, (Nx1) x (1xN) -> NxN
    coeff_matrix = k * n 

    # calculate the omega coefficient
    omega_n = np.exp(multiplier * 2j * np.pi / N)

    # create a matrix of omega raised to the power of the base coefficients
    M = np.power(omega_n, coeff_matrix)

    return np.dot(M, x) / divider
    

def tfdi(x):
    return tfd(x, inverse=True)


def tfd2(x, inverse=False):
    callback = tfdi if inverse else tfd
    x = np.apply_along_axis(callback, axis=0, arr=x)
    x = np.apply_along_axis(callback, axis=1, arr=x)
    return x


def tfdi2(x):
    return tfd2(x, inverse=True)


def get_dist_from_center_matrix(spectrum):
    """ 
    Returns distances from the center of the matrix.
    """
    rows, cols = spectrum.shape
    r_center = rows // 2
    c_center = cols // 2

    r = np.power(np.arange(rows) - r_center, 2)
    c = np.power(np.arange(cols).reshape((cols, 1)) - c_center, 2)

    return r + c


def low_pass_filter(spectrum, thresh):
    """ Our "ideal" low pass filter for the Fourier Space. Cutoff frequency if determined by the distance from the center (low frequencies) in the shifted Fourier space.
    * cutoff = dx^2 + dy^2  = (columns * threshold)^2
    * param: spectrum -> the Fourier space onto which we shall apply the lowpass filter.
    * param: thresh -> distance from the center, the degree of compression in function of the cutoff frequency. (closer to center -> lower frequencies)
    * return filtered spectrum -> the Fourier space from which we have removed certain high frequencies, higher than the cutoff
    """
    max_distance_sq = (spectrum.shape[1] * thresh)**2

    shifted = np.fft.fftshift(spectrum)

    distance_matrix = get_dist_from_center_matrix(shifted)

    circle_mask = np.where(distance_matrix > max_distance_sq, 0, 1)

    filtered = shifted * circle_mask.T

    return np.fft.ifftshift(filtered)


def plot_spectrum(spectrum):
    """ Plots the Fourier space (spectrum), by taking the amplitudes of the Fourier Coefficients. """
    plt.imshow(np.abs(spectrum), norm=LogNorm(vmin=5))
    plt.colorbar()


def display_results(spectrum, filtered_spectrum, original, filtered):
    """ 
    displays the result for the two exercices (Denoise and Compression)
    * param: spectrum
    * param: spectrum after lowpass filter
    * param: original grayscale image
    * param: compressed grayscale image
    """
    plt.figure()
    plt.subplot(221)
    plot_spectrum(spectrum)

    plt.subplot(222)
    plot_spectrum(filtered_spectrum)

    plt.subplot(223)
    plt.axis('off')
    plt.imshow(original, cmap='gray')

    plt.subplot(224)
    plt.axis('off')
    plt.imshow(filtered, cmap='gray')

    plt.show()
