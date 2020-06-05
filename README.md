

# Fourier TP
## Authors: Téo Kaltrachian, Sergey Platonov

********

## Setup:
### Noise removal:
please import the Python __colored__ library. For the progress bar.
```bash
cd fourier_kaltrachian_platonov
python3 . -n
```
You can close the matplotlib figures one after one. Ctrl+C to stop.

### Compression:
```bash
cd fourier_kaltrachian_platonov
python3 . -c 2
```
you can replace 2 with any other integer between 0 and 9 (degrees of compression).

### DFT:
```bash
cd fourier_kaltrachian_platonov
python3 . -t
```
Launches unit tests that verify the validity of our DFT implementations.

### Code Organisation:
#### fourier_lib
Contains the functions used in our project.
#### exercices
Contains the exercices...
#### tests . py
Contains the unit tests.
#### resources
Contains all the images used in this project (in both exercices).

For more information, use:
```bash
cd fourier_kaltrachian_platonov
python3 . --help
```
