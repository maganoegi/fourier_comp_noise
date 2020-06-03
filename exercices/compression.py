

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from fourier import tfd, tfdi, tfd2, tfdi2 
import cv2 
import numpy as np

import time
import progress_bar



def plot_spectrum(spectrum):
    plt.imshow(np.abs(spectrum), norm=LogNorm(vmin=5))
    plt.colorbar()


def display_results(spectrum, sp_compr, original, compressed):
    plt.figure()
    plt.subplot(221)
    plot_spectrum(spectrum)

    plt.subplot(222)
    plot_spectrum(sp_compr)

    plt.subplot(223)
    plt.axis('off')
    plt.imshow(original, cmap='gray')

    plt.subplot(224)
    plt.axis('off')
    plt.imshow(compressed, cmap='gray')

    plt.show()


def pixel_averaging(spectrum, deg):
    rows, cols = spectrum.shape
    step = deg + 1
    compressed_spectrum = []

    for r in range(0, rows, step):
        row = []
        for c in range(0, cols, step):
            val = 0
            for h in range(c, c + step):
                for v in range(r, r + step):
                    val += spectrum[r][c]
            
            val /= step**2
            row.append(val)
        compressed_spectrum.append(row)
    compressed_spectrum = np.array(compressed_spectrum)
    print(f"before: {spectrum.shape}\tafter: {compressed_spectrum.shape}")
    return compressed_spectrum

def pixel_restoring(spectrum, deg):
    rows, cols = spectrum.shape
    step = deg + 1

    new_rows = rows * step
    new_cols = cols * step

    new_spectrum = np.empty((new_rows, new_cols)).astype(np.complex64)
    print(f"before: {spectrum.shape}\tafter: {new_spectrum.shape}")
    for r in range(0, rows):
        for c in range(0, cols):

            val = spectrum[r][c]
            big_r = r * step
            big_c = c * step

            new_spectrum[big_r : big_r + step , big_c : big_c + step] = val


    new_spectrum = np.array(new_spectrum)

    return new_spectrum

def frequency_thresholding(spectrum, deg):
    multiplier = deg / 10000

    MM = np.abs(spectrum)
    
    max_magnitude = MM.max()
    
    threshold = multiplier * max_magnitude

    high_pass_cond = MM < threshold

    thresh = spectrum.copy()
    thresh[high_pass_cond] = 0


    print(f"zeros original spectrum vs thresh spectrum:\t{np.count_nonzero(spectrum==0)} -> {np.count_nonzero(thresh==0)}")

    # Re = np.real(thresh) * 255 / np.real(thresh).max()
    # Im = np.imag(thresh) * 255 / np.imag(thresh).max()

    Re = np.real(thresh)
    Im = np.imag(thresh)

    concatenated = np.concatenate((Re, Im))

    return concatenated


def reconstruct_spectrum(compressed_spectrum):
    middle = int(len(compressed_spectrum) / 2)
    return compressed_spectrum[:middle] + 1j * compressed_spectrum[middle:]


def compression(deg):
    assert deg in range(0,10)

    fft = True
    
    file_2_read = "./resources/transmetropolitan.pgm"
    compressed_file = "./resources/compressed.pgm"
    file_2_write = "./resources/decompressed.pgm"

    original = cv2.imread(file_2_read, 0).astype(np.double)

    # COMPRESSION
    spectrum = np.fft.fft2(original) if fft else tfd2(original)

    compressed_spectrum = frequency_thresholding(spectrum, deg).astype(int)
    
    # cv2.imwrite(compressed_file, compressed_spectrum)

    # # DECOMPRESSION
    # compressed_spectrum = cv2.imread(compressed_file).astype(np.double)

    reconstructed_spectrum = reconstruct_spectrum(compressed_spectrum)

    compressed_image = np.fft.ifft2(reconstructed_spectrum) if fft else tfdi2(reconstructed_spectrum)
    compressed_image = np.real(compressed_image)

    cv2.imwrite(file_2_write, compressed_image)

    # display_results(spectrum, compressed_spectrum, original, compressed_image)
    display_results(spectrum, reconstructed_spectrum, original, compressed_image)




    # fft = True
    # deg = 2
    
    # filename = "./resources/transmetropolitan.pgm"

    # original = cv2.imread(filename, 0).astype(np.double)

    # # COMPRESSION
    # spectrum = np.fft.fft2(original) if fft else tfd2(original)

    # compressed_spectrum = pixel_averaging(spectrum, deg)

    # compressed = np.fft.ifft2(compressed_spectrum) if fft else tfdi2(compressed_spectrum)
    # compressed = np.real(compressed)

    # display_results(spectrum, compressed_spectrum, original, compressed)
    # # compressed = compressed.astype(np.int8)

    # # DECOMPRESSION
    # compressed = compressed.astype(np.double)

    # spectrum = np.fft.fft2(compressed) if fft else tfd2(compressed)

    # decompressed_spectrum = pixel_restoring(spectrum, deg)

    # decompressed = np.fft.ifft2(decompressed_spectrum) if fft else tfdi2(decompressed_spectrum)
    # decompressed = np.real(decompressed)

    # display_results(spectrum, decompressed_spectrum, compressed, decompressed)
    # decompressed = decompressed.astype(np.int8)






    



# ''' Compress img using FFT and IFFT
# '
# '   Arguments: img - 2d numpy array
# '   Return: 2d numpy array
# '''
# # Do 2D FFT
# img = np.apply_along_axis(FFT, 1, img)
# img = np.apply_along_axis(FFT, 0, img)

# # # Drop some values
# img[img < np.mean(img) - 13 * np.std(img)] = 0

# # # Do 2D IFFT
# img = np.apply_along_axis(IFFT, 1, img)
# img = np.apply_along_axis(IFFT, 0, img)

# # Return real values of img
# return np.real(img)


# def save_image(path, img):
# ''' Save image
# '
# '   Arguments: path - string, img - 2d numpy array
# '   Return: None
# '''
# # Get the file name
# f_name = path.split('/')[1]
# # Get the name of the file without extension
# name = f_name.split('.')[0]

# # Map the image to grayscale format and save it in format `nameCompressed.ext`
# mpimg.imsave(f'{out_folder}/{name}Compressed.{ext}',
#                 img,
#                 format='TIFF',
#                 cmap='gray')


# if __name__ == "__main__":
# # Get filenames from input/ with *.tif extension
# f_names = glob(f'{in_folder}/*.{ext}')
# # Read all files as images
# imgs = [mpimg.imread(f) for f in f_names]

# # Compress images using FFT
# compressed_imgs = list(map(compress, imgs))

# # Create folder for output images
# if not path.exists(out_folder) or path.isfile(out_folder):
#     mkdir(out_folder)

# # Save images
# [save_image(path, img) for path, img in zip(f_names, compressed_imgs)]


# if __name__ == "__main__":
#     compression()