

from fourier_lib import *
import cv2 
import numpy as np

import time
import progress_bar



def noise():
    """
    Denoising exercice for the Mathematics class of O. Malaspinas. 
    The goal is to remove the noise from the provided images (in resources/) by applying a lowpass filter.
    that removes the frequencies above a cutoff frequency. 
    """
    fft = True

    for i in range(1, 18):
        progress_bar.init()
        start_time = time.time()
        filename = f"./resources/{i}.png"

        original = cv2.imread(filename, 0)

        progress_bar.draw_progress_bar(25, "FT")

        spectrum = np.fft.fft2(original) if fft else tfd2(original)

        thresh_val = 0.08

        progress_bar.draw_progress_bar(50, "Filter")

        spectrum_filtered = low_pass_filter(spectrum, thresh_val)

        progress_bar.draw_progress_bar(75, "IFT")

        filtered = np.fft.ifft2(spectrum_filtered) if fft else tfdi2(spectrum_filtered)
        filtered = np.real(filtered)

        progress_bar.draw_progress_bar(99, "Done")

        print(f"duration: {round(time.time() - start_time, 2)}s")

        display_results(spectrum, spectrum_filtered, original, filtered)

        progress_bar.destroy()
        


if __name__ == "__main__":
    noise()
