

from fourier_lib import *
import cv2 
import numpy as np

import time
import progress_bar

def real_to_int(image):
    """ mapping the real components of the image to the 8-bit number space. """
    image = (image - image.min()) * 255 / (image.max() - image.min())
    return np.uint8(image)


def compression(deg):
    """ 
    Compression exercice for the Mathematics class of O. Malaspinas. 
    The goal is to compress an image using the Fourier Transform by manipulating the resulting Fourier Space 
    by removing the frequencies above a cutoff frequency that the human eye might not perceive.
    The program needs to be flexible to degrees of compression, ranging from 0 to 9, 0 being not compressed at all and 9 "relatively" compressed to max. 
    """
    assert deg in range(0,10)

    fast = True
    
    # file_2_read = "./resources/transmetropolitan.pgm"
    # file_2_write = "./resources/compressed.pgm"

    file_2_read = "./resources/dylan.png"
    file_2_write = "./resources/compressed.png"

    original = cv2.imread(file_2_read, 0)

    original = np.double(original)

    spectrum = np.fft.fft2(original) if fast else tfd2(original)

    thresh = 1.0 - (deg / 10.0)
    compressed_spectrum = low_pass_filter(spectrum, thresh)

    compressed_image = np.fft.ifft2(compressed_spectrum) if fast else tfdi2(compressed_spectrum)
    compressed_image = real_to_int(compressed_image.real)

    cv2.imwrite(file_2_write, compressed_image)

    display_results(spectrum, compressed_spectrum, original, compressed_image)


if __name__ == "__main__":
    compression(deg = 1)