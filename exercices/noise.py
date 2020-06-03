

from matplotlib.colors import LogNorm
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from fourier import tfd, tfdi, tfd2, tfdi2 
import cv2 
import numpy as np

import time
import progress_bar


def plot_spectrum(spectrum):
    plt.imshow(np.abs(spectrum), norm=LogNorm(vmin=5))
    plt.colorbar()

def apply_spectrual_lowpass(spectrum, thresh):
    r, c = spectrum.shape
    filtered = spectrum.copy()

    start_row = int(r*thresh)
    end_row = int(r*(1-thresh))
    start_col = int(c*thresh)
    end_col = int(c*(1-thresh))

    filtered[start_row : end_row] = 0
    filtered[:, start_col : end_col] = 0

    return filtered

def display_results(spectrum, filtered_spectrum, original, filtered):
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


def noise():

    fft = True

    for i in range(1, 18):
        progress_bar.init()
        start_time = time.time()
        filename = f"./resources/{i}.png"

        original = cv2.imread(filename, 0)

        progress_bar.draw_progress_bar(25, "FT")

        spectrum = np.fft.fft2(original) if fft else tfd2(original)

        thresh_val = 0.1

        progress_bar.draw_progress_bar(50, "Filter")

        spectrum_filtered = apply_spectrual_lowpass(spectrum, thresh_val)

        progress_bar.draw_progress_bar(75, "IFT")

        filtered = np.fft.ifft2(spectrum_filtered) if fft else tfdi2(spectrum_filtered)
        filtered = np.real(filtered)

        progress_bar.draw_progress_bar(99, "Done")

        print(f"duration: {round(time.time() - start_time, 2)}s")

        display_results(spectrum, spectrum_filtered, original, filtered)

        progress_bar.destroy()
        


if __name__ == "__main__":
    noise()
